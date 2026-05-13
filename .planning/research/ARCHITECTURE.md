# Architecture Patterns

**Domain:** Single-file static investment/marketing landing page with multilingual support, referral link generation, and live facility feed — deployed on GitHub Pages
**Researched:** 2026-05-13
**Confidence:** HIGH (architecture is grounded in existing code inspection + verified patterns)

---

## Current Architecture (Baseline)

```
index.html (8.5MB)
├── <head>      — meta, CDN links (Google Fonts, Font Awesome)
├── <style>     — ~280 lines of inline CSS
├── <body>      — Nav, Hero, iceland-bg (product blocks), cosmos-bg (impact/roadmap), Contact, Footer
│   ├── #hero
│   ├── #iceland-bg
│   │   ├── #about
│   │   ├── #how        — 4 content blocks + Read More panels + Gallery panels
│   │   ├── #impact     — CO2 slider calculator
│   │   └── #donate
│   ├── #cosmos-bg
│   │   └── #roadmap
│   ├── #contact
│   ├── footer
│   └── Modals: #modal-usdt, #modal-btc
├── <script>    — inline JS block 1: reveal + CO2 calculator + donate modal
├── <script>    — inline JS block 2: switchReadmore / switchGallery / lightbox
├── <script>    — inline JS block 3: i18n object (EN/ES/PT, ~600 lines) + setLang()
└── <script>    — inline JS block 4: setLang(currentLang) call + calc() call

media/
├── station-1.jpg
├── station-7.jpg
└── mwf-video-1.mp4

qrcode.min.js   — local copy, required for modal QR generation
```

**Key observation:** The i18n system is already built and functional. It uses a flat `data-i18n` attribute pattern on every translated element, a single `i18n` object with language sub-objects, `setLang()` that calls `querySelectorAll('[data-i18n]')` and swaps `innerHTML`, and `localStorage` persistence under key `pearl_lang`. EN, ES, PT are complete. HI is absent. No language button for HI exists in the nav yet.

---

## Recommended Target Architecture

The site stays single-file. No build pipeline is introduced. File size target is met by extracting base64 blobs to `media/` before adding new content. All new sections are vanilla JS inline blocks following the existing pattern.

```
index.html (~80-120KB after extraction)
├── <head>        — same CDN links; add <link rel="preconnect"> for media CDN if used
├── <style>       — existing CSS + new section styles appended
├── <body>
│   ├── Nav       — add HI lang button; add #token nav anchor
│   ├── #hero
│   ├── #iceland-bg
│   │   ├── #about
│   │   ├── #how
│   │   ├── #token          — NEW: PEARL token section (TOKEN-01..03)
│   │   ├── #impact
│   │   └── #donate
│   ├── #cosmos-bg
│   │   └── #roadmap
│   ├── #pearl-calc         — NEW: investment calculator (CALC-01..02)
│   ├── #facility-feed      — NEW: live facility photo (CAM-01..02)
│   ├── #referral           — NEW: referral section (REF-01..03)
│   ├── #contact
│   ├── footer
│   └── Modals: existing + no new modals needed for referral
├── <script> blocks — existing preserved
├── <script>      — NEW: investment calculator logic
├── <script>      — NEW: facility feed polling logic
├── <script>      — NEW: referral link generator logic
├── <script>      — EXTENDED i18n object: add HI + new keys for all new sections
└── <script>      — existing setLang() init call (unchanged)

media/
├── (all base64 images extracted here — ~14 files)
├── station-1.jpg, station-7.jpg (already here)
├── mwf-video-1.mp4 (already here)
└── facility-latest.jpg   — (camera feed placeholder; overwritten by camera system)
```

---

## Component Boundaries

| Component | Location in File | Responsibility | Communicates With |
|-----------|-----------------|----------------|-------------------|
| Nav lang switcher | `<nav>` block | Locale switching; persists to localStorage | `setLang()` function |
| i18n engine | Script block 3 | Holds all translation strings; drives all visible text on `setLang` call | Every `data-i18n` element |
| Token section (#token) | After `#how`, inside `#iceland-bg` | Markets PEARL token; surfaces price/supply/raise progress; opens Telegram bot link | i18n, Telegram bot URL |
| Investment calculator (#pearl-calc) | After `#cosmos-bg` or inside `#impact` | User inputs $ → shows token count + estimated annual payout | i18n, TOKEN constants |
| Facility feed (#facility-feed) | Before `#referral` | Displays latest facility photo from CDN URL, refreshes on interval | External CDN URL via `fetch` / `<img>` src swap |
| Referral generator (#referral) | Before `#contact` | User enters Telegram ID or bot code → generates `t.me/BOT?start=CODE` link; copy-to-clipboard | Telegram bot URL constant, clipboard API |
| Modal system | Bottom of `<body>` | QR code display for donations | `qrcode.min.js` |
| Contact form | `#contact` | Lead generation via Formspree | Formspree CDN |

---

## Data Flow

### Multilingual Content Load

```
Page load
  → read localStorage('pearl_lang')  [key: 'pearl_lang']
  → resolve to 'en' | 'es' | 'pt' | 'hi' (default: 'en')
  → setLang(lang) called immediately on DOMContentLoaded
      → querySelectorAll('[data-i18n]')
      → for each element: el.innerHTML = i18n[lang][el.dataset.i18n]
  → lang buttons: active class toggled to match current lang

Lang switch by user
  → setLang(newLang)
  → localStorage.setItem('pearl_lang', newLang)
  → same DOM update loop
  → calc() called to re-render calculator output in new locale
  → Read More buttons re-rendered with locale read_more string
```

**Decision: keep i18n inline, not split to JSON files.**
The existing pattern works perfectly. Loading 4 JSON files via `fetch()` adds async complexity, potential load-order bugs, and a CORS consideration if ever the file is opened from `file://` locally. The inline object is already ~600 lines for 3 languages; adding HI brings it to ~800 lines. At ~50KB gzipped this is negligible vs the 8.5MB baseline. Split to external JSON only if the file grows beyond 300KB total — which it will not.

### Investment Calculator Data Flow

```
User adjusts $ input slider or text field
  → JS reads: investAmount (USD)
  → constants (defined once at top of calc script):
      PEARL_PRICE_USD = [from token section; hardcoded]
      ANNUAL_REVENUE_SHARE_PCT = 0.15
      TOTAL_TOKENS = [total supply from token parameters]
  → outputs:
      tokenCount = investAmount / PEARL_PRICE_USD
      estimatedAnnualPayout = tokenCount * (ANNUAL_REVENUE_SHARE_PCT * ANNUAL_REVENUE_USD) / TOTAL_TOKENS
  → display rendered via DOM update
  → all label strings sourced from i18n[currentLang]
```

**Calculator integration note (CALC-02):** The existing dashboard HTML file will be provided. The correct approach is to extract only the JS calculation logic and CSS from that file, not copy its full DOM structure. The calculator section in index.html will use its own HTML layout (matching the site's visual language) while the underlying math function is preserved from the dashboard. This avoids iframe complexity and style conflicts.

### Facility Feed Data Flow

```
Section rendered with <img id="facility-img" src="media/facility-latest.jpg">
  → on DOMContentLoaded: schedulePhotoRefresh()
  → function schedulePhotoRefresh():
      fetch(FACILITY_PHOTO_URL + '?t=' + Date.now())  // cache-bust
        .then(response → create object URL or just update img.src)
        .catch(err → leave current image, log quietly)
      setTimeout(schedulePhotoRefresh, REFRESH_INTERVAL_MS)  // 5 min default
```

**Pattern choice: setTimeout over setInterval.**
setTimeout-based polling ensures only one request is ever in-flight. setInterval would queue requests if the network is slow. For a ~30-60 second photo (or configurable 5-minute interval), this difference is material on slow mobile connections — the primary audience in India and Latin America.

**Photo URL strategy:** `FACILITY_PHOTO_URL` is a constant defined at the top of the script block. A simple external server (even an S3 bucket with public read, or a Cloudflare R2 bucket) uploads the latest frame. The website only reads that URL. No API, no auth. If the URL returns 404 or error, the last loaded image persists silently.

### Referral Link Generation Data Flow

```
User arrives at #referral section
  → sees explanation of 2-level payout program (i18n'd)
  → input field: "Enter your Telegram ID or referral code"
  → JS on input/button click:
      rawInput = input.value.trim()
      code = sanitize(rawInput)  // alphanumeric + underscore only, max 32 chars
      refLink = 'https://t.me/' + BOT_USERNAME + '?start=' + code
      display refLink in a read-only text field
      copy-to-clipboard button (same pattern as existing modal copy button)
  → no server call required; generation is pure client-side string concatenation
```

**User identifier decision (REF-02, REF-03):**
The referral code = the user's Telegram ID (a numeric string) OR a code already assigned to them by the bot (the bot sends the user their code via `/myref` command). The website does not generate codes — it assembles links from codes the user already has. This is the correct model: the Telegram bot is the authority on referral attribution; the website is only a link-assembly UI. Instructions in the referral section should tell users: "Open the bot and use /myref to get your code. Paste it here."

This eliminates the "what user identifier to use" problem entirely — no fingerprinting, no hashing, no login required on the website side.

---

## Single-File vs Multi-File Decision

**Recommendation: keep single-file (index.html) for all content.**

Rationale:
- GitHub Pages serves a single origin with no server-side routing. Multi-file splits work (e.g., `/token.html`, `/calculator.html`) but break the smooth-scroll nav pattern and require duplicating nav/footer/CSS/JS across files — maintenance multiplier.
- This is an acquisition funnel. Every navigation step is a conversion leak. Single-page keeps the user in the flow from "learn about PEARL" to "buy PEARL" without page reloads.
- All new sections (token, calculator, referral, camera feed) are logically part of the same funnel, not separate destinations.
- After image extraction, index.html will be ~80-120KB. Adding all new sections (token, calculator, referral, camera, HI locale) will bring it to ~150-180KB — comfortably under the 200KB target.
- The only valid reason to split files is if a section needs its own URL for sharing/SEO (e.g., `/invest` landing page for paid ads). That is out of scope for this milestone.

**Exception: if a dedicated token sale page is needed for paid ad campaigns** (separate from the main funnel), that becomes `token.html` as a standalone file, not a split of index.html. Decision deferred — not in current milestone requirements.

---

## Build Order (Suggested Phase Sequence)

The dependencies chain strictly. Later steps break without earlier steps done correctly.

### Step 1 — Image Extraction (PERF-01, PERF-02) — MUST BE FIRST

Rationale: index.html is 8.5MB because of base64 blobs. Any attempt to add new sections (TOKEN, CALC, REF, CAM) to the existing 8.5MB file risks:
- Corrupting a base64 blob with a stray character during edit
- Editor timeouts or truncation on file save
- Exceeding GitHub's 100MB per-file soft limit (not an issue at 8.5MB, but growing worse)
- Diff sizes making PR review unusable

Extract images first. Verify content integrity. Then proceed.

**How:** `grep -n "data:image"` to locate all base64 blobs. For each: extract the data URI value, decode with `base64 -d` to a file in `media/`, replace the `src="data:image/..."` with `src="media/filename.jpg"`. Test locally with a simple HTTP server (`python3 -m http.server 8080`) — `file://` will block cross-origin image loads.

### Step 2 — Add Hindi Locale (I18N-01, I18N-02, I18N-03)

Rationale: HI is missing from the i18n object. Adding it now, before new sections are added, means the HI translations of new sections can be written in one pass when those sections are built. Retrofitting HI translations after all sections exist requires two passes.

Also: add the HI lang button to the nav at this step.

All existing `data-i18n` keys already cover the existing content. The `setLang()` function already handles unknown keys gracefully (falls back to EN). No structural changes to the i18n engine needed.

### Step 3 — Token Section (TOKEN-01, TOKEN-02, TOKEN-03)

This is a new `<div class="sec" id="token">` inserted after `#how` inside `#iceland-bg`. It introduces new i18n keys (prefixed `tok_`). Translations for all 4 languages added to the i18n object in the same commit.

The "Buy PEARL" CTA is an `<a href="https://t.me/BOTNAME">` link. No JS required. `BOTNAME` is a constant defined once at the top of the script block.

### Step 4 — Investment Calculator (CALC-01, CALC-02)

After the existing dashboard file is provided, extract its calculation function (input → output math). Build the calculator HTML section using the site's visual language (gold/cream palette, Cinzel headers, EB Garamond body). Wire the JS. Add i18n keys for all calculator labels.

Insert as `<div class="sec" id="pearl-calc">` — either within `#cosmos-bg` or as a new background section after it, whichever fits visual flow.

### Step 5 — Facility Feed (CAM-01, CAM-02)

Short section: `<div class="sec" id="facility-feed">`. One `<img>` tag plus a caption. The polling script is ~15 lines. Insert `FACILITY_PHOTO_URL` constant. Add i18n keys.

This step requires the external photo endpoint to exist. If the endpoint is not ready, the section renders a static placeholder image from `media/facility-latest.jpg` and the polling script is a no-op until the URL is configured.

### Step 6 — Referral Section (REF-01, REF-02, REF-03)

`<div class="sec" id="referral">`. HTML: explanation text (i18n'd), input field, assembled link display, copy button. JS: ~20 lines. Uses the same copy-to-clipboard pattern as the existing modal (`navigator.clipboard.writeText()`).

Add `BOT_USERNAME` constant at top of script block (same place as `FACILITY_PHOTO_URL` and `PEARL_PRICE_USD`).

---

## Constants Block Pattern

All configuration values that may change (bot username, token price, photo URL, raise target) should be defined at the top of a single `<script>` block as named constants — not scattered through the HTML or buried in event handlers.

```javascript
// ---- SITE CONFIGURATION — edit these when values change ----
const BOT_USERNAME       = 'PearlRestorationBot';   // Telegram bot @handle
const PEARL_PRICE_USD    = 0.10;                    // current token price
const TOTAL_TOKEN_SUPPLY = 247490740;               // total PEARL supply
const ANNUAL_REVENUE_USD = 5000000;                 // projected annual revenue (update quarterly)
const REVENUE_SHARE_PCT  = 0.15;                    // 15% to token holders
const FACILITY_PHOTO_URL = 'https://cdn.example.com/facility/latest.jpg';
const PHOTO_REFRESH_MS   = 5 * 60 * 1000;          // 5 minutes
// ---------------------------------------------------------------
```

This makes the file maintainable without reading all 1100+ lines to find what to change.

---

## Patterns to Follow

### Pattern 1: data-i18n Attribute (existing, proven)

Every user-visible string in HTML gets `data-i18n="key"` with its EN default inline. `setLang()` replaces `innerHTML` for all matching elements. For new sections, follow the existing key naming prefix pattern:

| Section | Key prefix |
|---------|-----------|
| Token | `tok_` |
| Calculator | `pcalc_` |
| Facility feed | `cam_` |
| Referral | `ref_` |

### Pattern 2: Section Insertion Order

New sections are inserted as `<div class="sec" id="...">` matching the existing section structure. CSS for each new section is appended to the existing `<style>` block with a comment delimiter: `/* ---- TOKEN SECTION ---- */`.

### Pattern 3: Graceful Degradation

All JS-dependent features (facility feed, referral link, calculator) must render a meaningful static state without JS. The facility image falls back to `media/facility-latest.jpg`. The calculator shows its input form (just no live calculation until JS loads). The referral section shows an explanation paragraph and an empty input.

### Pattern 4: No External JS Libraries for New Features

The existing site uses `qrcode.min.js` (local copy) and `formspree` CDN. Do not introduce new CDN dependencies for the investment calculator, referral generator, or facility feed. All new logic is plain vanilla JS compatible with all modern browsers.

---

## Anti-Patterns to Avoid

### Anti-Pattern 1: Editing the 8.5MB File Before Image Extraction

**What goes wrong:** A single misplaced character in a base64 blob corrupts the image. The diff is unreadable. Finding the corruption requires binary inspection.
**Instead:** Extract images first. Keep base64 blobs out of the HTML permanently.

### Anti-Pattern 2: Per-Language HTML Files

**What goes wrong:** `/en/index.html`, `/es/index.html` etc. creates 4x maintenance burden. Every content change must be made in 4 files. Nav links break unless carefully constructed.
**Instead:** Single HTML + JS-driven i18n. Already implemented and working.

### Anti-Pattern 3: Fetch-Loading JSON Locale Files

**What goes wrong:** Requires async load, introduces timing bugs where `setLang` runs before the JSON arrives. Breaks on `file://` protocol. Adds 4 extra HTTP requests at page load.
**Instead:** Keep translations inline in the `i18n` JS object. Total size is manageable (~30-40KB of text across 4 languages).

### Anti-Pattern 4: Storing Referral Codes in URL Fragments or Query Params

**What goes wrong:** Someone bookmarks or shares `https://site.com/#ref=12345`, which spreads with hardcoded referral codes and breaks when the bot's attribution system doesn't match.
**Instead:** The referral code is user-entered, assembled into the Telegram bot deep link (`t.me/BOT?start=CODE`). The user shares the bot link, not the website URL. The website is the link assembly tool.

### Anti-Pattern 5: Embedding the Calculator as an iframe

**What goes wrong:** iframes create isolation that breaks the gold/cream visual theme. i18n can't reach inside an iframe. Mobile scroll is notoriously broken inside iframes.
**Instead:** Extract calculation logic from the dashboard HTML file into a standalone function. Rebuild the UI in the site's native markup.

---

## GitHub Pages Constraints Summary

| Constraint | Limit | Impact on This Project |
|------------|-------|----------------------|
| Repository size | 1 GB recommended max | Not a concern (media/ will be ~5-10MB) |
| Published site size | 1 GB | Not a concern |
| Individual file size warning | 50 MB (hard limit 100 MB) | Current 8.5MB is below limit, but too large practically — extract images |
| Bandwidth | 100 GB/month soft | At risk if campaign drives heavy traffic; mitigate with Cloudflare proxy |
| No server-side execution | Static files only | All backend logic must stay in Telegram bot |
| HTTPS | Automatic (GitHub enforced) | Clipboard API (`navigator.clipboard`) requires HTTPS — satisfied |
| Custom domain | Supported | CNAME file in repo root if needed |

---

## Scalability Considerations

| Concern | Current State | After Milestone | If Traffic Scales |
|---------|--------------|-----------------|-------------------|
| Page load time | ~7s (8.5MB) | ~0.3s (80-120KB) | Add Cloudflare proxy for CDN edge |
| i18n maintenance | 3 languages, inline | 4 languages, inline (~800 lines) | At 6+ languages, extract to separate JS file loaded async |
| Token price updates | N/A | 1 constant to change, redeploy | Consider a small JSON endpoint if price changes frequently |
| Photo feed | N/A | 1 URL constant, 5-min poll | Rate-limiting is on the CDN side, not the site |
| Referral link generation | N/A | Pure client-side | No scaling concern — pure string concat |

---

## Sources

- Codebase inspection: `/Users/votykvot/Desktop/pearl-of-restoration/index.html` (lines 843-1101 — existing i18n engine, setLang, localStorage pattern)
- GitHub Pages limits: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
- Telegram start parameter referral pattern: https://core.telegram.org/api/bots/referrals
- vanilla-i18n data-i18n pattern: https://andreasremdt.com/blog/building-a-super-small-and-simple-i18n-script-in-javascript/
- setTimeout polling vs setInterval: https://btholt.github.io/complete-intro-to-realtime/settimeout/
- Single-page vs multi-page SEO: https://ahrefs.com/blog/single-page-website/
- LazyLoad (not used, referenced for completeness): https://github.com/verlok/vanilla-lazyload
