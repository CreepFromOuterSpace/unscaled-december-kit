# unscaled.co: December Instagram kit

24 researched posts for Nov 30 to Dec 26, 2026, with the unscaled.co mark and handle on every slide, ready to schedule.

| Path | What it is |
|---|---|
| `posts/<post id>/01.jpg …` | 108 slides, 1080×1350 JPEG, numbered in slide order |
| `schedule.csv` | One row per post: publish time, caption, image paths, alt text, sources, notes |
| `captions.md` | The same captions, laid out for copying by hand |
| `brand/` | Logo files, the Instagram profile photo, and the “Our logo never ends” post |
| `publish.py` | Posts anything that’s due through Instagram’s official API (no dependencies) |
| `refresh_token.py` | Renews your Instagram token before its 60 days run out |
| `.github/workflows/` | Runs the publisher every 15 minutes and renews the token twice a month |
| `generator/` | The script that made the slides: edit `content.py` and re-run to regenerate |

All times are US Eastern; `publish_at` stores the full timestamp with its `-05:00` offset. The first post is Mon Nov 30 at 8:30 a.m.

**Before each hiring post goes out**, re-check the job link. The salary ranges come from postings that were live on Nov 27, 2026, and roles close.

## Fully automated publishing with GitHub (free)

1. **Professional account.** In Instagram, go to Settings and activity › Account type and tools › Switch to professional account, and pick Creator or Business. Keep the account public.
2. **Meta app.** At developers.facebook.com, open All Apps › Create App. Name it, choose the use case **Manage messaging & content on Instagram**, and choose “I don’t want to connect a business portfolio yet.”
3. **Access token.** In the app, open Use cases › Customize › API setup with Instagram login. Under Generate access tokens, click **Add account**, log in as your page, then click **Generate token** and copy it. It lasts 60 days. If Meta sends a tester invite, accept it in Instagram under Settings › Apps and websites › Tester invites.
4. **Repository.** Create a public GitHub repository, for example `unscaled-posts`. Publish this folder to it with GitHub Desktop (File › Add local repository, choose this folder, create a repository when asked, then Publish repository with “Keep this code private” unticked), or from a terminal in this folder:
   ```
   git init && git add . && git commit -m "December posts"
   git branch -M main
   git remote add origin https://github.com/YOURNAME/unscaled-posts.git
   git push -u origin main
   ```
   Don’t drag files into the browser uploader: it can leave out the hidden `.github` folder that holds the automation.
5. **Image hosting.** In the repository: Settings › Pages › Deploy from a branch › `main`, `/ (root)`, Save. After a minute or two, this should show the first slide: `https://YOURNAME.github.io/unscaled-posts/posts/2026-11-30-ipo-wait/01.jpg`
6. **Secrets.** Settings › Secrets and variables › Actions. Add the secret `IG_ACCESS_TOKEN` (your token) and, on the Variables tab, the variable `IMAGE_BASE_URL` = `https://YOURNAME.github.io/unscaled-posts`. Your Instagram user ID is looked up from the token, so `IG_USER_ID` is optional.
7. **Check.** Actions › Publish scheduled Instagram posts › Run workflow, with mode **check**. The log should confirm the token works for your account and that the images are public, and show the next post. Run mode **dry-run** to see exactly what would go out.
8. **Token renewal.** On GitHub, open your profile › Settings › Developer settings › Personal access tokens › Fine-grained tokens › Generate new token. Give it access to this repository only, set Repository permissions › Secrets to **Read and write**, and save it in the repository as the secret `GH_PAT`. The renewal workflow then refreshes your Instagram token on the 1st and 15th.

From then on, every 15 minutes the workflow posts anything due and records it in `posted.json`. Run `python publish.py --list` to see where every post stands.

### Good to know

- GitHub can start scheduled runs several minutes late when it’s busy, so a post may go out a little after its slot.
- `MAX_PER_RUN` (default 1) keeps a backlog from posting all at once. `GRACE_HOURS` (default 6) skips posts that are far overdue, which matters for date-specific history posts. If you start late, edit the dates in `schedule.csv` and push the change.
- To pause everything: Actions › Publish scheduled Instagram posts › ⋯ › Disable workflow.
- In a public repository, upcoming posts are visible to anyone. To keep them private, use a private repository and host the images in a public bucket (Cloudflare R2 or Amazon S3), then point `IMAGE_BASE_URL` there.
- Instagram accepts only JPEG images through the API and fetches each one from its URL, so the images must be reachable when a post publishes. Carousels are capped at 10 images; every post here fits.
- Alt text is sent for single-image posts. For carousels, add it in the Instagram app after publishing if you want it.
- Mark sponsored posts with Instagram’s paid partnership label.

## Other ways to schedule

- **By hand (free, about an hour):** Instagram’s built-in scheduler or Meta Business Suite. Work down `captions.md`: upload each post’s images in order, paste the caption, set the time.
- **Bulk import:** Metricool, Publer and Hootsuite import CSVs with times, captions and image URLs. Host the images first (steps 4 and 5), then each image URL is `IMAGE_BASE_URL/` plus a path from the `images` column.

## Regenerating the slides

```
pip install playwright pillow
playwright install chromium
python generator/render.py --out .
```
Edit `generator/content.py` first (`BRAND_HANDLE`, slide text, captions). The slides use Crimson Text, Anton and Inter, all free on Google Fonts; set `FONT_DIR` to a folder with their font files to render offline.
