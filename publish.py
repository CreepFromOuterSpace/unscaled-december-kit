#!/usr/bin/env python3
"""Publish the posts in schedule.csv whose time has come, using Instagram's
official API (Instagram API with Instagram Login, host graph.instagram.com).

Run it every few minutes; the included GitHub Action runs it every 15. Each run
publishes posts whose publish_at has passed and that aren't recorded in
posted.json, then records them there.

Required environment variables
  IG_ACCESS_TOKEN   long-lived Instagram user token (lasts 60 days; see refresh_token.py)
  IMAGE_BASE_URL    public URL serving this folder, e.g. https://you.github.io/your-repo

Optional
  IG_USER_ID        your Instagram account's user ID (looked up from the token if unset)
  IG_API_VERSION    default v26.0
  SCHEDULE_FILE     default schedule.csv
  STATE_FILE        default posted.json
  MAX_PER_RUN       default 1, so a backlog never posts all at once
  GRACE_HOURS       default 6; posts more overdue than this are skipped, not posted late
  DRY_RUN=1         print what would happen without calling Instagram
  NOW               pretend it's this time (ISO 8601), for testing with DRY_RUN

Usage
  python publish.py           publish anything due
  python publish.py --check   test the token and image hosting; posts nothing
  python publish.py --list    show every post and its status
"""
import csv
import datetime as dt
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

API = "https://graph.instagram.com/" + os.environ.get("IG_API_VERSION", "v26.0")
SCHEDULE = os.environ.get("SCHEDULE_FILE", "schedule.csv")
STATE = os.environ.get("STATE_FILE", "posted.json")
DRY = os.environ.get("DRY_RUN", "") == "1"
MAX_PER_RUN = int(os.environ.get("MAX_PER_RUN", "1"))
GRACE = dt.timedelta(hours=float(os.environ.get("GRACE_HOURS", "6")))
MAX_ATTEMPTS = 3      # a failing post is retried on the next runs, then marked failed
MAX_CAROUSEL = 10     # Instagram's carousel limit


def need(name):
    value = os.environ.get(name, "").strip()
    if not value and not DRY:
        sys.exit(f"Missing environment variable {name}")
    return value


def call(method, path, params=None):
    """Call the Instagram API and return the decoded JSON response."""
    url = f"{API}/{path.lstrip('/')}"
    headers = {"Authorization": f"Bearer {need('IG_ACCESS_TOKEN')}"}
    data = None
    if method == "GET":
        if params:
            url += "?" + urllib.parse.urlencode(params)
    else:
        data = json.dumps(params or {}).encode()
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        raise RuntimeError(f"{method} {path} failed with HTTP {e.code}: {body}") from None


_user_id = None
def user_id():
    """IG_USER_ID if set, otherwise the account the token belongs to."""
    global _user_id
    if not _user_id:
        _user_id = os.environ.get("IG_USER_ID", "").strip()
        if not _user_id and not DRY:
            _user_id = str(call("GET", "me", {"fields": "user_id"})["user_id"])
    return _user_id or "<your user ID>"


def wait_until_ready(container_id):
    """Meta recommends checking a container once a minute for no more than 5 minutes."""
    for attempt in range(6):
        status = call("GET", container_id, {"fields": "status_code"}).get("status_code")
        if status in ("FINISHED", "PUBLISHED"):
            return
        if status in ("ERROR", "EXPIRED"):
            raise RuntimeError(f"container {container_id} has status {status}")
        if attempt < 5:
            time.sleep(60)
    raise RuntimeError(f"container {container_id} still not ready after 5 minutes")


def image_urls(row, base_url):
    paths = [p.strip() for p in row["images"].split(";") if p.strip()]
    return [f"{base_url}/{urllib.parse.quote(p)}" for p in paths]


def publish(row, base_url):
    urls = image_urls(row, base_url)
    if not urls:
        raise RuntimeError("no images listed")
    if len(urls) > MAX_CAROUSEL:
        raise RuntimeError(f"{len(urls)} images; carousels allow at most {MAX_CAROUSEL}")
    caption = row["caption"]

    if DRY:
        more = f" (+{len(urls) - 1} more)" if len(urls) > 1 else ""
        print(f"    dry run: would post {len(urls)} image(s): {urls[0]}{more}")
        return None

    uid = user_id()
    if len(urls) == 1:
        params = {"image_url": urls[0], "caption": caption}
        if row.get("alt_text"):
            params["alt_text"] = row["alt_text"]
        container = call("POST", f"{uid}/media", params)["id"]
    else:
        children = [call("POST", f"{uid}/media", {"image_url": u, "is_carousel_item": True})["id"] for u in urls]
        for child in children:
            wait_until_ready(child)
        container = call("POST", f"{uid}/media",
                         {"media_type": "CAROUSEL", "children": ",".join(children), "caption": caption})["id"]
    wait_until_ready(container)
    return call("POST", f"{uid}/media_publish", {"creation_id": container})["id"]


def load_state():
    try:
        with open(STATE, encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError:
        return {}


def save_state(state):
    with open(STATE, "w", encoding="utf-8") as fh:
        json.dump(state, fh, indent=2, sort_keys=True)
        fh.write("\n")


def now_utc():
    forced = os.environ.get("NOW", "").strip()
    if forced:
        t = dt.datetime.fromisoformat(forced.replace("Z", "+00:00"))
        return t if t.tzinfo else t.replace(tzinfo=dt.timezone.utc)
    return dt.datetime.now(dt.timezone.utc)


def check(rows, state):
    """Confirm the token works and the images are public. Posts nothing."""
    ok = True
    if not os.environ.get("IG_ACCESS_TOKEN", "").strip():
        print("  FIX  IG_ACCESS_TOKEN is not set (add it as a repository secret)")
        ok = False
    else:
        try:
            me = call("GET", "me", {"fields": "user_id,username"})
            print(f"  OK   the token works for @{me.get('username')} (user ID {me.get('user_id')})")
            env_id = os.environ.get("IG_USER_ID", "").strip()
            if env_id and env_id != str(me.get("user_id")):
                print(f"  FIX  IG_USER_ID is {env_id}, but the token belongs to {me.get('user_id')}; correct it or delete that secret")
                ok = False
        except Exception as e:
            print(f"  FIX  the token didn't work: {e}")
            ok = False
    base = os.environ.get("IMAGE_BASE_URL", "").strip().rstrip("/")
    if not base:
        print("  FIX  IMAGE_BASE_URL is not set (add it as a repository variable)")
        ok = False
    else:
        url = image_urls(rows[0], base)[0]
        try:
            with urllib.request.urlopen(urllib.request.Request(url, method="HEAD"), timeout=30) as resp:
                ctype = resp.headers.get("Content-Type", "")
            if "jpeg" in ctype:
                print(f"  OK   images are public, e.g. {url}")
            else:
                print(f"  FIX  {url} answered with {ctype or 'no content type'}, not a JPEG")
                ok = False
        except Exception as e:
            print(f"  FIX  couldn't load {url}: {e}")
            ok = False
    now = now_utc()
    queued = [r for r in rows if state.get(r["post_id"], {}).get("status") not in ("published", "skipped", "failed")]
    upcoming = [r for r in queued if dt.datetime.fromisoformat(r["publish_at"]) > now]
    if upcoming:
        print(f"  next post: {upcoming[0]['post_id']} at {upcoming[0]['publish_at']} ({len(upcoming)} queued)")
    print("  All checks passed." if ok else "  Fix the items marked FIX, then run the check again.")
    return 0 if ok else 1


def main():
    with open(SCHEDULE, newline="", encoding="utf-8") as fh:
        rows = sorted(csv.DictReader(fh), key=lambda r: dt.datetime.fromisoformat(r["publish_at"]))
    state = load_state()

    if "--list" in sys.argv:
        for r in rows:
            status = state.get(r["post_id"], {}).get("status", "queued")
            print(f"{r['publish_at']}  {status:<10} {r['post_id']}")
        return 0
    if "--check" in sys.argv:
        return check(rows, state)

    base_url = need("IMAGE_BASE_URL").rstrip("/")
    now = now_utc()
    posted, errors = 0, 0

    for r in rows:
        pid = r["post_id"]
        record = state.get(pid, {})
        if record.get("status") in ("published", "skipped", "failed"):
            continue
        due = dt.datetime.fromisoformat(r["publish_at"])
        if due > now:
            continue
        if now - due > GRACE:
            print(f"  skipped {pid}: due {r['publish_at']}, more than {GRACE} ago")
            state[pid] = {"status": "skipped", "reason": "overdue", "at": now.isoformat()}
            continue
        if posted >= MAX_PER_RUN:
            print(f"  {pid} is due; leaving it for the next run (MAX_PER_RUN={MAX_PER_RUN})")
            break
        print(f"  publishing {pid} (due {r['publish_at']})")
        try:
            media_id = publish(r, base_url)
            if not DRY:
                state[pid] = {"status": "published", "media_id": media_id, "at": now.isoformat()}
                print(f"    published as media {media_id}")
            posted += 1
        except Exception as e:  # keep going; record the failure for a retry
            errors += 1
            attempts = record.get("attempts", 0) + 1
            print(f"    error: {e}")
            state[pid] = {"status": "failed" if attempts >= MAX_ATTEMPTS else "retry",
                          "attempts": attempts, "error": str(e)[:500], "at": now.isoformat()}

    if DRY:
        print("  dry run: posted.json left unchanged")
    else:
        save_state(state)
    if not posted and not errors:
        print("  nothing due")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
