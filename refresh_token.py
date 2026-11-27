#!/usr/bin/env python3
"""Renew a long-lived Instagram user token for another 60 days.

Prints only the new token on stdout, so a workflow can capture it. Instagram
renews tokens that are at least 24 hours old and not yet expired.
"""
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

token = os.environ.get("IG_ACCESS_TOKEN", "").strip()
if not token:
    sys.exit("Missing environment variable IG_ACCESS_TOKEN")
url = "https://graph.instagram.com/refresh_access_token?" + urllib.parse.urlencode(
    {"grant_type": "ig_refresh_token", "access_token": token})
try:
    with urllib.request.urlopen(url, timeout=60) as resp:
        data = json.loads(resp.read().decode())
except urllib.error.HTTPError as e:
    sys.exit(f"Token renewal failed with HTTP {e.code}: {e.read().decode(errors='replace')}")
new_token = data.get("access_token")
if not new_token:
    sys.exit("Token renewal returned no token")
print(new_token)
print(f"Renewed; expires in {int(data.get('expires_in', 0)) // 86400} days", file=sys.stderr)
