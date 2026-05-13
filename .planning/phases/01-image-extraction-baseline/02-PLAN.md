---
id: "01-02"
title: "Run extraction, swap index.html, verify visually"
phase: 1
plan: 2
type: execute
wave: 2
depends_on:
  - "01-01"
files_modified:
  - index.html
  - media/hero-bg.jpg
  - media/iceland-bg.jpg
  - media/cosmos-bg.jpg
  - media/about-director.png
  - media/block1-photo-1.jpg
  - media/block1-photo-2.jpg
  - media/block1-photo-3.jpg
  - media/block1-photo-4.jpg
  - media/block1-photo-5.jpg
  - media/block1-photo-6.jpg
  - media/block1-photo-7.jpg
  - media/block3-photo-1.jpg
  - media/block3-photo-2.jpg
  - media/block4-photo-1.jpg
  - scripts/extraction-report.json
autonomous: false
requirements:
  - PERF-01
  - PERF-02
must_haves:
  truths:
    - "index.html is under 200KB after the swap"
    - "index.html contains zero remaining `data:image` occurrences (PERF-01)"
    - "media/ contains exactly 14 newly extracted image files matching the agreed naming scheme"
    - "Each extracted image file passes magic-byte verification (JPEG starts with FF D8 FF; PNG starts with 89 50 4E 47 0D 0A 1A 0A)"
    - "A fresh browser load of the served page renders all 4 product blocks, the about director photo, and the three section backgrounds correctly — no broken image icons (PERF-02)"
    - "The 3 video references already in media/ remain reachable and untouched"
  artifacts:
    - path: "index.html"
      provides: "Rewritten landing page with media/ references replacing base64 blobs"
      contains: "src=\"media/block1-photo-1.jpg\""
    - path: "media/hero-bg.jpg"
      provides: "Extracted hero background (was line 45 CSS bg)"
    - path: "media/iceland-bg.jpg"
      provides: "Extracted iceland section background (was line 70 CSS bg)"
    - path: "media/cosmos-bg.jpg"
      provides: "Extracted cosmos section background (was line 76 CSS bg)"
    - path: "media/about-director.png"
      provides: "Director portrait — only PNG (was line 406)"
    - path: "media/block1-photo-1.jpg"
      provides: "Block I (Oil Regeneration) gallery photo 1 of 7"
    - path: "media/block1-photo-7.jpg"
      provides: "Block I (Oil Regeneration) gallery photo 7 of 7"
    - path: "media/block3-photo-1.jpg"
      provides: "Block III (Activated Carbon) gallery photo 1 of 2"
    - path: "media/block3-photo-2.jpg"
      provides: "Block III (Activated Carbon) gallery photo 2 of 2"
    - path: "media/block4-photo-1.jpg"
      provides: "Block IV (KDK / Waste-to-Energy) gallery photo 1 of 1"
    - path: "scripts/extraction-report.json"
      provides: "Per-file integrity record: filename, byte count, sha256, original line"
  key_links:
    - from: "index.html"
      to: "media/hero-bg.jpg"
      via: "CSS rule on #hero-img: background-image:url('media/hero-bg.jpg')"
      pattern: "background-image:url\\('media/hero-bg\\.jpg'\\)"
    - from: "index.html"
      to: "media/about-director.png"
      via: "<img src=\"media/about-director.png\"> inside .about-img"
      pattern: "src=\"media/about-director\\.png\""
    - from: "index.html"
      to: "media/block1-photo-{1..7}.jpg"
      via: "7 <img src=\"media/block1-photo-N.jpg\"> tags inside #gallery-block1"
      pattern: "src=\"media/block1-photo-[1-7]\\.jpg\""
    - from: "index.html"
      to: "media/block3-photo-{1,2}.jpg"
      via: "2 <img src=\"media/block3-photo-N.jpg\"> tags inside #gallery-block3"
      pattern: "src=\"media/block3-photo-[12]\\.jpg\""
    - from: "index.html"
      to: "media/block4-photo-1.jpg"
      via: "1 <img src=\"media/block4-photo-1.jpg\"> tag inside #gallery-block4"
      pattern: "src=\"media/block4-photo-1\\.jpg\""
---

<objective>
Execute the extraction script built in Plan 01, swap the rewritten HTML in atomically, and verify that the page still renders correctly. After this plan, PERF-01 and PERF-02 are both satisfied: `index.html` is under 200KB, all 14 images live in `media/`, and a real browser render confirms no visual regression.

Purpose: This is the only plan in Phase 1 that modifies `index.html`. It is gated by a human-verify checkpoint because Pitfall #2 documents that base64 corruption produces broken images with no console error — only a human looking at the rendered page can confirm "the 7 Block I photos look right and match the v6.1 baseline."

Output: Rewritten `index.html` (<200KB), 14 image files in `media/`, `scripts/extraction-report.json`, and a verified-by-human snapshot of the rendered page.
</objective>

<execution_context>
@$HOME/.claude/get-shit-done/workflows/execute-plan.md
@$HOME/.claude/get-shit-done/templates/summary.md
</execution_context>

<context>
@.planning/STATE.md
@.planning/research/ARCHITECTURE.md
@.planning/research/PITFALLS.md
@.planning/codebase/CONCERNS.md
@.planning/phases/01-image-extraction-baseline/01-PLAN.md
@.planning/phases/01-image-extraction-baseline/01-01-SUMMARY.md
@CLAUDE.md

<facts>
- Plan 01 has produced `scripts/extract_base64_images.py` with a verified dry-run that emits the expected 14-filename mapping.
- `pre-extraction-baseline` git tag points to the pre-extraction commit, so `git checkout pre-extraction-baseline -- index.html` restores the 8.5MB file on demand.
- `.gitignore` already excludes `.DS_Store` and `index.html.new`.
- `index.html` size at the start of this plan is 8940016 bytes with 14 `data:image` occurrences.
- The 3 video files already in `media/` (mwf-video-1.mp4, station-video-1.mp4, station-video-2.mp4) are referenced by `index.html` at lines 497, 498, 503 — these must remain unchanged.
- Working directory: /Users/votykvot/Desktop/pearl-of-restoration/
- Python 3.9.6 is the local interpreter.
- `python3 -m http.server` is the standard way to serve the file locally for the visual check (per ARCHITECTURE.md Step 1: file:// blocks cross-origin image loads, so a real HTTP server is required for the verification).
</facts>
</context>

<tasks>

<task type="auto">
  <name>Task 1: Run extractor, decode images, swap index.html</name>
  <files>index.html, media/hero-bg.jpg, media/iceland-bg.jpg, media/cosmos-bg.jpg, media/about-director.png, media/block1-photo-1.jpg, media/block1-photo-2.jpg, media/block1-photo-3.jpg, media/block1-photo-4.jpg, media/block1-photo-5.jpg, media/block1-photo-6.jpg, media/block1-photo-7.jpg, media/block3-photo-1.jpg, media/block3-photo-2.jpg, media/block4-photo-1.jpg, scripts/extraction-report.json</files>
  <read_first>
    - /Users/votykvot/Desktop/pearl-of-restoration/scripts/extract_base64_images.py (the script to be executed — read to confirm its CLI flags before invoking)
    - /Users/votykvot/Desktop/pearl-of-restoration/.planning/phases/01-image-extraction-baseline/01-01-SUMMARY.md (confirms Plan 01 finished, contains dry-run report to compare against)
    - /Users/votykvot/Desktop/pearl-of-restoration/.planning/research/PITFALLS.md (Pitfall #2 — extraction methodology and post-extraction integrity check)
  </read_first>
  <action>
    Execute the full extraction in this exact sequence — abort on any failure rather than continuing:

    1. Confirm the rollback anchor is intact: `git rev-parse pre-extraction-baseline` must succeed. If it does not, stop and ask the user.
    2. Run a fresh dry-run for safety: `python3 scripts/extract_base64_images.py --dry-run index.html` — exit code must be 0 and the 14-filename mapping must match Plan 01's saved report. If the script reports a different blob count or filename order, stop — something has shifted in `index.html` and the script is no longer authoritative.
    3. Run the real extraction: `python3 scripts/extract_base64_images.py index.html`. This produces:
       - 14 files under `media/` (3 CSS backgrounds, 1 PNG, 10 JPEGs as listed in the file mapping)
       - `index.html.new` at repo root with all 14 base64 blobs replaced by `media/<name>` references
       - `scripts/extraction-report.json` containing per-file integrity records
    4. Post-extraction integrity checks (each must pass before the swap):
       - The `file` command on each extracted image returns a description containing `JPEG` (for .jpg files) or `PNG` (for the .png file). Run `file media/*.jpg media/*.png`.
       - Each JPEG starts with bytes `FF D8 FF` and each PNG with `89 50 4E 47 0D 0A 1A 0A`. Spot-check the first JPEG and the PNG: `xxd -l 8 media/hero-bg.jpg | head -1` shows `ffd8ff...` and `xxd -l 8 media/about-director.png | head -1` shows `8950 4e47 0d0a 1a0a`.
       - `wc -c index.html.new` reports a size under 204800 bytes (200 KB). Per ARCHITECTURE.md the realistic post-extraction size is 80–120 KB; budget is 200 KB.
       - `grep -c 'data:image' index.html.new` returns `0`.
       - The 3 existing `<source src="media/...mp4">` references at lines 497, 498, 503 of the original are still present in `index.html.new` exactly as before: `grep -c 'src="media/mwf-video-1.mp4"' index.html.new`, `grep -c 'src="media/station-video-1.mp4"' index.html.new`, and `grep -c 'src="media/station-video-2.mp4"' index.html.new` each return `1`. Per CLAUDE.md these are baseline functionality and must not regress.
    5. Atomic swap: `mv index.html.new index.html`. After the swap, immediately re-run `wc -c index.html` and `grep -c 'data:image' index.html` and assert the new state.
    6. Do NOT commit yet. The commit happens after the human verifies the visual render in Task 2's checkpoint.

    Constraint reminders:
    - All paths in `index.html` after rewrite must be RELATIVE (`media/...`, no leading slash, no `https://`). GitHub Pages serves from a subpath when the repo is project-page-style, so absolute paths would 404.
    - Do not modify CSS rules, JavaScript, content text, i18n keys, or any element attribute other than the 14 `data:image` source values being replaced. This is pure extraction (per planning_context constraint).
    - Do not touch the existing video files in `media/`.
  </action>
  <verify>
    <automated>test $(wc -c < index.html) -lt 204800 && [ $(grep -c 'data:image' index.html) -eq 0 ] && [ -f media/hero-bg.jpg ] && [ -f media/iceland-bg.jpg ] && [ -f media/cosmos-bg.jpg ] && [ -f media/about-director.png ] && [ -f media/block1-photo-1.jpg ] && [ -f media/block1-photo-7.jpg ] && [ -f media/block3-photo-1.jpg ] && [ -f media/block3-photo-2.jpg ] && [ -f media/block4-photo-1.jpg ] && [ -f media/mwf-video-1.mp4 ] && [ -f media/station-video-1.mp4 ] && [ -f media/station-video-2.mp4 ] && file media/hero-bg.jpg | grep -q JPEG && file media/about-director.png | grep -q PNG && [ $(grep -c 'src="media/block1-photo-[1-7]\.jpg"' index.html) -eq 7 ] && [ $(grep -c 'src="media/block3-photo-[12]\.jpg"' index.html) -eq 2 ] && [ $(grep -c 'src="media/block4-photo-1\.jpg"' index.html) -eq 1 ] && [ -f scripts/extraction-report.json ]</automated>
  </verify>
  <acceptance_criteria>
    - `wc -c index.html` reports a value less than 204800 (200KB) AND greater than 30000 (sanity floor — must not be empty or truncated).
    - `grep -c 'data:image' index.html` returns exactly `0`.
    - All 14 expected files exist in `media/` (3 backgrounds, 1 PNG portrait, 7 block1 photos, 2 block3 photos, 1 block4 photo).
    - All 3 existing video files in `media/` are still present (`mwf-video-1.mp4`, `station-video-1.mp4`, `station-video-2.mp4`).
    - Magic-byte check: `xxd -l 3 media/hero-bg.jpg | head -1` contains `ffd8ff`. `xxd -l 8 media/about-director.png | head -1` contains `8950 4e47 0d0a 1a0a`.
    - `file` command identifies all .jpg files as JPEG and the .png file as PNG.
    - `grep -c 'src="media/block1-photo-[1-7]\.jpg"' index.html` returns exactly `7`.
    - `grep -c 'src="media/block3-photo-[12]\.jpg"' index.html` returns exactly `2`.
    - `grep -c 'src="media/block4-photo-1\.jpg"' index.html` returns exactly `1`.
    - `grep -c 'background-image:url(.media/hero-bg\.jpg.)' index.html` returns at least `1`.
    - `grep -c 'background-image:url(.media/iceland-bg\.jpg.)' index.html` returns at least `1`.
    - `grep -c 'background-image:url(.media/cosmos-bg\.jpg.)' index.html` returns at least `1`.
    - `grep -c 'src="media/about-director\.png"' index.html` returns exactly `1`.
    - `grep -c 'src="media/[a-z]*-video-[12]\.mp4"' index.html` returns exactly `3` (videos unchanged).
    - `grep -cE 'src="https?://[^"]*\.(jpg|jpeg|png)"' index.html` returns `0` — no absolute image URLs leaked in.
    - `scripts/extraction-report.json` exists and parses as JSON containing 14 entries (`python3 -c "import json; assert len(json.load(open('scripts/extraction-report.json')))==14"`).
    - `index.html.new` does NOT exist in repo root (was renamed to `index.html` by the atomic swap).
  </acceptance_criteria>
  <done>The file swap is complete: `index.html` is under 200KB with all 14 base64 blobs replaced by `media/...` references, all 14 image files exist in `media/` with valid magic bytes, the 3 existing videos are untouched, and the integrity report is on disk. Nothing has been committed yet — Task 2 checkpoint must pass first.</done>
</task>

<task type="checkpoint:human-verify" gate="blocking">
  <name>Task 2: Visual verification in browser, then commit</name>
  <files>(no file edits — human verification + git commit)</files>
  <read_first>
    - /Users/votykvot/Desktop/pearl-of-restoration/.planning/research/PITFALLS.md (Pitfall #2 detection: "open the page in an incognito browser window (no cache) and visually check every image in all four product blocks and the Read More panels")
    - /Users/votykvot/Desktop/pearl-of-restoration/CLAUDE.md (Page Structure section: confirms which blocks have which photos — Block I 7 photos, Block III 2 photos, Block IV 1 photo)
  </read_first>
  <what-built>
    Task 1 has just rewritten `index.html` from ~8.5MB to under 200KB by extracting all 14 base64 image blobs to files under `media/`. The atomic swap is done on disk but the change is NOT committed to git yet. The rollback anchor `pre-extraction-baseline` is in place — if anything looks wrong, one command restores the prior state: `git checkout pre-extraction-baseline -- index.html && rm media/{hero-bg,iceland-bg,cosmos-bg,about-director,block1-photo-{1..7},block3-photo-{1,2},block4-photo-1}.{jpg,png}`.

    What the human is verifying: that the rendered page after the swap is visually identical to v6.1 (the pre-extraction state). Per Pitfall #2, base64 corruption is silent — no console error — so the only reliable check is human eyes on a real browser.
  </what-built>
  <how-to-verify>
    1. Start a local HTTP server in the repo root (file:// cannot load cross-origin images, per ARCHITECTURE.md): `python3 -m http.server 8080` from /Users/votykvot/Desktop/pearl-of-restoration/. Leave it running.
    2. Open a fresh INCOGNITO browser window (so no cache hides a broken result) and navigate to `http://localhost:8080/`.
    3. Walk the page top-to-bottom and confirm each of the following renders correctly:
       a. Hero section: the background image is visible (this is the `hero-bg.jpg` extraction). The manifesto text appears over it.
       b. iceland-bg section: background image renders. The 4 product blocks are visible.
       c. About / About-grid area: the director portrait (the only PNG, `about-director.png`) renders inside the `.about-img` block — not a broken-image icon.
       d. Block I "Read More" / gallery panel: click the gallery toggle. The 7 photos for the Industrial Oil Regeneration System all load.
       e. Block III gallery: open it. The 2 Activated Carbon photos load.
       f. Block IV gallery: open it. The 1 KDK / Waste-to-Energy photo loads.
       g. cosmos-bg section (roadmap area): background image renders.
       h. Videos: confirm the 3 existing videos in Block I / Block II areas (mwf-video, station-video-1, station-video-2) still play when clicked — they were not part of extraction but must not have regressed.
    4. Open browser DevTools → Network tab → reload with Disable Cache enabled. Confirm:
       - Every `media/*.jpg` and `media/*.png` request returns HTTP 200, not 404.
       - No request shows status 0 / failed.
       - No CORS or mixed-content red errors in the Console tab.
    5. Confirm `index.html` itself transferred small (Network tab shows index.html under 200KB).
    6. Stop the local server (Ctrl-C the python3 -m http.server process).

    If anything in steps 3–5 shows a broken image, missing video, 404, or console error:
    - Type `rollback` and describe what failed.
    - The executor will run `git checkout pre-extraction-baseline -- index.html` and clean up `media/` per the rollback recipe in <what-built>.

    If everything renders correctly:
    - Type `approved` (or "approved + any notes").
    - The executor then commits with this message (substituting Co-Authored-By per project policy):
      `feat(01): extract base64 images to media/, reduce index.html to <200KB (PERF-01, PERF-02)`
      Staged files: `index.html`, `media/hero-bg.jpg`, `media/iceland-bg.jpg`, `media/cosmos-bg.jpg`, `media/about-director.png`, `media/block1-photo-1.jpg` through `media/block1-photo-7.jpg`, `media/block3-photo-1.jpg`, `media/block3-photo-2.jpg`, `media/block4-photo-1.jpg`, `scripts/extraction-report.json`. Do NOT stage `.DS_Store` (it must already be ignored by Plan 01's `.gitignore`).
    - After commit, the executor pushes to origin (`git push origin main`) so the change is live on GitHub Pages.
  </how-to-verify>
  <acceptance_criteria>
    - User has responded with `approved` (or `approved` + notes) OR `rollback` + description.
    - If approved: the commit `feat(01): extract base64 images...` exists in git log (`git log --oneline -1 | grep -q "extract base64 images"`).
    - If approved: `git status --porcelain` is clean (no uncommitted changes to the extracted files).
    - If approved: `git push` has succeeded (`git rev-parse @{u}` matches `git rev-parse HEAD`).
    - If rollback: `index.html` is byte-identical to the `pre-extraction-baseline` tag (`git diff pre-extraction-baseline -- index.html` produces no output) and the extracted `media/*.jpg`/`*.png` files have been deleted.
  </acceptance_criteria>
  <resume-signal>Type `approved` to commit + push, or `rollback` + describe what failed.</resume-signal>
</task>

</tasks>

<threat_model>
## Trust Boundaries

| Boundary | Description |
|----------|-------------|
| disk → browser | Extracted images are loaded over HTTP by a public-facing GitHub Pages site; any tampered file would be visible to all visitors |
| working tree → origin/main | `git push` propagates the change to the live site within ~1–10 minutes (Fastly CDN cache window) |
| local HTTP server → human eyes | The verification depends on the human actually loading the page in a real browser, not just trusting greps |

## STRIDE Threat Register

| Threat ID | Category | Component | Disposition | Mitigation Plan |
|-----------|----------|-----------|-------------|-----------------|
| T-01-08 | Tampering | Corrupted extracted image silently shipped to production | mitigate | Three-layer check: magic-byte verification in the script (Plan 01 T-01-02), `file` command output check in Task 1, and human visual verification in Task 2 before commit. The non-autonomous checkpoint is the final gate. |
| T-01-09 | Tampering | Stray edit to JS, CSS, or content text leaked into the rewrite | mitigate | Task 1 grep checks confirm only the 14 `data:image` values changed: video src patterns, the i18n script block presence (`grep -c "const i18n\\|var i18n\\|i18n = {"`), and overall structure (the script never modifies anything outside the matched `data:image/...` regex). Visual diff in Task 2 catches anything the greps miss. |
| T-01-10 | Denial of Service | Page fails to render because GitHub Pages CDN caches the old 8.5MB version after deploy | accept-with-monitoring | Per Pitfall #7 (Fastly ~10-minute cache). Mitigation: the local HTTP server check in Task 2 validates the actual file content before push; user can re-verify the live URL ~10 minutes after push. No automated mitigation in Phase 1 — Cloudflare proxy is out of scope. |
| T-01-11 | Information Disclosure | Extracted JPEG/PNG files contain EXIF metadata (camera GPS, device serial) | accept | The images are marketing photos of industrial equipment; EXIF leakage on already-public content is low risk. Re-evaluate if any photo is later confirmed to be a private/identifying image. Note in summary so a future phase can strip EXIF if needed. |
| T-01-12 | Repudiation | Push to GitHub goes through but extraction is later found broken | mitigate | `pre-extraction-baseline` tag remains in place after this plan; `git revert HEAD` restores the prior state cleanly. Commit message explicitly names PERF-01/PERF-02 for traceability. |
| T-01-13 | Tampering | `.DS_Store` slipping into the `media/` commit | mitigate | `.gitignore` from Plan 01 excludes `**/.DS_Store`. Task 2 commit list is explicit (names each file rather than `git add .`) so DS_Store cannot be accidentally staged. |
| T-01-14 | Elevation of Privilege | Local HTTP server bound to 0.0.0.0 exposes the dev machine on LAN during verification | accept | `python3 -m http.server 8080` binds to all interfaces by default. Short-lived (closes immediately after verification). Single-developer machine in a controlled environment. Note in summary; future phases can use `--bind 127.0.0.1` if a remote-pair-programming scenario emerges. |
</threat_model>

<verification>
After this plan completes, all of the following hold:

1. `wc -c index.html` reports < 204800 bytes (PERF-01 satisfied: <200KB).
2. `grep -c 'data:image' index.html` returns `0`.
3. `ls media/*.jpg media/*.png | wc -l` returns at least `14`.
4. `git log --oneline -1` shows the extraction commit naming PERF-01 and PERF-02.
5. The user has personally confirmed via incognito browser that the rendered page shows all original visual content (PERF-02 satisfied).
6. The `pre-extraction-baseline` git tag still exists, so any future regression can be diff-traced.
</verification>

<success_criteria>
- `index.html` is under 200KB on disk (PERF-01).
- All 14 previously-base64 images are external files in `media/` and load correctly in a fresh browser (PERF-02).
- The 3 existing video files in `media/` and their HTML references are unchanged.
- A clean commit captures the change; the live GitHub Pages site has been redeployed.
- No regression to any existing functionality: 4 product blocks visible, Read More panels still toggle, gallery panels still open, QR donate modal still works, CO2 counter still animates, contact form unchanged. (Task 2 visual checkpoint confirms.)
</success_criteria>

<output>
After completion, create `.planning/phases/01-image-extraction-baseline/01-02-SUMMARY.md` documenting:
- Pre-extraction size: 8940016 bytes (8.5MB)
- Post-extraction size of index.html in bytes (must be <204800)
- The 14 extracted filenames with their byte counts and sha256 hashes (from scripts/extraction-report.json)
- The commit SHA of the extraction commit
- The human checkpoint outcome (`approved` with any notes, or `rollback` with reason)
- Confirmation that PERF-01 and PERF-02 are now satisfied
- A note for Phase 5 (Facility Photo Feed) that the relative `media/` path pattern is the established convention
- Any EXIF / metadata observations worth noting for a future hygiene pass (per T-01-11)
</output>
</content>
</invoke>