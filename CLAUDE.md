# Pearl of Restoration — CLAUDE.md

## Project
- Brand: **Pearl of Restoration** / Жемчужина Возрождения
- Company: ООО ТД «Ренессанс-Контракт», Director: Андрей Барановский
- Repo: https://github.com/polyalpha-hq/pearl-of-restoration (GitHub Pages)
- Primary file: `index.html` — **81 KB** after Phase 1 extraction (was ~8.9MB; 14 images now in `media/`)
- Backup: `/tmp/backup-v5.html` (v5), git tag `pre-extraction-baseline` (8.5MB state)

---

## CRITICAL RULE
Never mention Russia, Russian origin, Russian standards, or Russian companies in any international materials.
- Patents → use only: "Patented technology, WIPO registered"
- No GOST references
- No Russian product names (СОЖ 2000 → Metalworking Fluid Concentrate)
- Russia is NOT a target market

---

## Page Structure (v6.1 — post Phase 1)
- 4 content blocks + tab buttons (max-width: 1060px) → full-width gallery
- **Block I** — Industrial Oil Regeneration System: 7 external photos in `media/` + 2 videos
- **Block II** — MWF video: `media/mwf-video-1.mp4`
- **Block III** — Activated Carbon (sorbent): 2 external photos in `media/`
- **Block IV** — Waste-to-Energy Complex (KDK): 1 external photo in `media/`
- Each block has a **Read More** button → full-width panel below
- QR modal: crypto donate working
- CO2 counter formula: $1 = 100L = 320kg CO2

## Media Files (all external after Phase 1)
**Images extracted from base64:**
- `media/hero-bg.jpg` — hero section CSS background
- `media/iceland-bg.jpg` — iceland section CSS background
- `media/cosmos-bg.jpg` — cosmos/roadmap section CSS background
- `media/about-director.png` — director portrait (contains JPEG data despite .png extension — pre-existing mismatch)
- `media/block1-photo-{1..7}.jpg` — Block I (Oil Regeneration) gallery, 7 photos
- `media/block3-photo-{1,2}.jpg` — Block III (Activated Carbon) gallery, 2 photos
- `media/block4-photo-1.jpg` — Block IV (KDK/Waste-to-Energy) gallery, 1 photo

**Videos (were already external):**
- `media/mwf-video-1.mp4` — MWF block video
- `media/station-video-1.mp4` — station video
- `media/station-video-2.mp4` — station video

## Crypto Donate
- USDT TRC-20: `THt3iokn8NELPyaeWHWd8n7xBNECVxwyND`
- BTC: `bc1q04azu8yus2ynku0fdf2decvjm6javynnx8e0kr`
- TON (owner wallet): `UQACdIf-AKuiV5_mQMiMX_OVJtfV1aABXBZIaWS8Gn8nbcyV`

---

## TODO (open as of 2026-05-05)
- [x] Remove small circle buttons from hero section — done v6.1
- [x] Add manifesto text to hero (EB Garamond italic, gold) — done v6.1
- [x] Move stats cards from hero to impact section — done v6.1

---

## Terminology
| Russian | International |
|---|---|
| Станция / МСРМ | Industrial Oil Regeneration System |
| СОЖ 2000 | Metalworking Fluid Concentrate / Bio-based MWF |
| Меласса → сорбент | Activated Carbon from Organic Waste |
| КДК | Waste-to-Energy Complex |
| Замкнутый цикл | Closed-Loop Resource Recovery |

---

## Ecosystem — Four Components
1. **Industrial Oil Regeneration System** ✅ AVAILABLE NOW — 3 units exist, 500 L/hr, ROI < 12 months, WIPO patent
2. **Metalworking Fluid Concentrate (Bio-based MWF)** 🔄 IN SALES — analog: Blasocut 2000 Universal
3. **Activated Carbon from Organic Waste** 🔄 IN DEVELOPMENT — Voronezh, CAPEX ~$7M, offtake signed 300t @ ~$3.5/kg
4. **Waste-to-Energy Complex** 📋 CONCEPT STAGE — no operating facility yet, position carefully

## Key Numbers
- Client savings: up to 70% on oil costs
- Throughput: 4,000,000 liters/year
- ROI: < 12 months
- Processing cost: < $0.01/liter

## DO NOT
- Mention Russia or Russian origin in any output
- Mention molasses, sugar plants, or specific feedstock sources
- Promise operating Waste-to-Energy facilities (none exist)
- Position Pearl token as investment instrument
- Use `python3 -m http.server` for local testing — it breaks video playback (no Range request support); use `npx serve` instead

---

## PEARL Token — Spec v5.0 (finalized 2026-05-20)

| Parameter | Value |
|-----------|-------|
| Price (3 rounds) | **Round 1 — $1.00 · Round 2 — $1.50 · Round 3 — $2.00** |
| Total emission | **31,051,657 PEARL** — **frozen forever**, additional issuance technically impossible |
| Blockchain | **TON** |
| Yield | **~49% annual** (Scenario A) |
| Gross profit per line | **$14,201,086 / year** |
| DEX listing | STON.fi / DeDust — **after Line II completion** (third holder income stream) |
| Personal dashboard | **Telegram bot only**, NOT on the website |
| Legal framing | Utility token (revenue participation) — NOT investment instrument |

### Sale Rounds
| Round | Price |
|-------|-------|
| Round 1 | **$1.00** |
| Round 2 | **$1.50** |
| Round 3 | **$2.00** |

### Holder Income Streams
1. **Revenue-share dividends** — share of operating-line turnover
2. **Buyback** — token repurchase
3. **DEX secondary market** — STON.fi / DeDust, **after Line II completion**

### v5 Invariants (spec)
- **Molasses mentioned nowhere** — only "organic feedstock"
- **Geographic names removed** — only **Line I / Line II / Line III**, no cities or countries
- **Emission frozen forever** — 31,051,657 tokens, no additional issuance possible
- **Transparency Report** — **Phase 2** (after the first dividend payout), not at launch

## Telegram Bot

- Accepts: **USDT TRC-20**, **TON**, **Toncoin**
- Languages: **EN / HI / PT-BR / ID / RU** — all equal
- Built-in referral system; `/mycode` command returns user's referral code
- **Personal dashboard — bot only**, not on the website
- All token purchases and referral actions flow through the bot only

## Referral Program — v5 (3 levels + statuses)

### Levels (multi-level)
| Level | Reward |
|-------|--------|
| Level 1 (direct referral) | **5%** |
| Level 2 | **2%** |
| Level 3 | **1%** |

### Statuses (BOTH conditions met simultaneously)
| Status | Referrals | Volume |
|--------|-----------|--------|
| **Pearl Starter** | 25 people | $5,000 |
| **Pearl Builder** | 100 people | $30,000 |
| **Pearl Ambassador** | 500 people | $150,000 |

- Crypto-only payouts
- Status granted only when **both** thresholds (referral count **AND** volume) are reached at once

## Financial Model — v5 (recalculated 2026-05-20)

### Per-Line Economics
| Item | Value |
|------|-------|
| **Gross profit per line** | **$14,201,086 / year** |
| **Yield (Scenario A)** | **~49% annual** |

### CRF — two scenarios
- **Base scenario** — **no CRF** (Carbon Recovery Fee excluded from the public model)
- **Scenario B** — with CRF, **internal use only**; never shown in public materials

> **v3 model is obsolete.** "30% of full turnover" (pool $6,991,370/yr, yield 22.5% / 67.5%,
> CRF $4,369,565, full turnover $23,304,565) — **replaced by v5**. Do not use v3 figures in new materials.

## Public Positioning Formula

> "Agricultural biomass waste → premium activated carbon"

Never mention: Russia, molasses, sugar plants, GOST, МСРМ, СОЖ, КДК.

## Pitch Deck (5 languages) — delivered 2026-05-19

### Files (repo root)
| Lang | File | Size | Audience |
|------|------|------|----------|
| EN | `presentation-en.html` | 55 KB | International base |
| ES | `presentation-es.html` | 57 KB | Latin American Spanish (Chile / Argentina / Colombia / Mexico) |
| PT-BR | `presentation-pt-br.html` | 57 KB | Brazilian Portuguese (São Paulo / Rio formal investor tone) |
| HI | `presentation-hi.html` | 75 KB | Hindi (Devanagari) + English finance terms (Mumbai / Delhi / Bangalore) |
| RU | `presentation-ru.html` | 68 KB | International Russian (diaspora — EU / Israel / Dubai / Kazakhstan), **NOT** RF domestic |

### Structure (15 slides — same across all locales)
- **Part I — Problem & Opportunity** (slides 1–3): title, problem, market drivers
- **Part II — Product** (slides 4–8): intro, 7-parameter QC table, applications, competitive edge, production tech
- **Part III — Economics** (slides 9–13): unit economics, 3-line expansion, revenue streams, PEARL token, ROI / payback
- **Part IV — Closing** (slides 14–15): credentials, single-channel CTA

### Source materials (preserved in `.planning/`)
- `.planning/source-pitch-deck-ru.html` (45 KB) — original RU investor deck (13 slides)
- `.planning/source-product-deck-ru.pdf` (1.5 MB) — original RU product/sorbent deck (9 slides)

### Anonymization invariants (0 grep hits per locale)
- No Russia / РФ / russian / russo / Россия (any spelling, any script)
- No molasses / меласса / sugar beet / sugar cane / melaza / melaço / गुड़ / गन्ना
- No Voronezh / Krasnodar / Nizhny / any RF city
- No Uzbekistan / Asia-only framing — keep "global industrial market"
- No ГОСТ / GOST — replaced with "international quality standards" / "independent lab validation"
- No rubles / ₽ / РУБ — USD only (converted at 92 RUB/$)
- No Telegram / wallet / email / USDT / Bitcoin on CTA — single channel only
- **WIPO patent №2820244 retained** as international IP credential

### Slide 14 credentials (no names, no photos)
1. 20+ years industrial chemistry experience
2. Active oil-regeneration deployments since 2018
3. WIPO patent holder · №2820244
4. Independent laboratory validation

### Slide 15 CTA
- Single channel: `https://eco-pearl.com/#contact`
- Anchor verified against `index.html:643` (`<section id="contact">`)

### Site integration — DONE (2026-05-20)
The pitch-deck funnel is wired into `index.html`. Any visitor with investment intent has a path to the locale-matched deck.

- **Hero CTA button** — "Open the investor deck →" (gold-bordered Cinzel), in hero after the manifesto
- **Nav item "Invest"** (`nav_invest`) — last nav entry before the language switcher
- **Language-aware routing** — `openInvestorDeck()` reads `currentLang` and opens the matching file: `en→en, es→es, pt→pt-br, hi→hi, ru→ru` (note: locale code `pt`, file `pt-br`). `window.open(url,'_blank','noopener')`
- **Soft secondary CTA** in donate section — `donate_deck_cta` ("Read the full investor deck →")

**3-card block replaced (revised funnel):** the old "How do you want to help?" 3-card grid (Buy / Invest / Donate) is replaced with one focused investor CTA in the site's poetic register:
- Eyebrow (`paths_orn`): "Ready to invest?" / "Готовы инвестировать?"
- Header (`paths_header`, `.s-h2`): "A pearl grows from a single grain" / "Жемчужина растёт из зерна"
- Subheader (`paths_sub`, `.hero-manifesto` italic): "Invest in the first facility. Earn a share of global scaling."
- Primary CTA (`hero_invest`, `.hero-invest-cta`): "Open the investor deck →"
- Soft link (`paths_donate_alt`): "or support construction with a donation" → scrolls to `#donate`
- Transparent background (no overlay), existing classes only, no new CSS rules
- `hero_invest` unified between hero button and section CTA

**i18n changes:** new keys `paths_header` / `paths_sub` / `paths_donate_alt` (×5 locales); updated `paths_orn` / `hero_invest`; removed `path1_*` / `path2_*` / `path3_*` (24 strings × 5 locales); `chain1-5` preserved (used in manifesto).

**Dead CSS (deliberately untouched, separate cleanup):** `.path-card*` / `.path-icon*` / `.path-btn*` (~9 rules) now unused; left in place to avoid perturbing the minified style block.

### Commit chain (11 unpushed as of 2026-05-20, oldest → newest)
```
2d5ec73  fix(i18n): remove СОЖ from RU locale for international consistency
b667ea1  feat(pitch): EN base — anonymized, international, $24.7M raise
ed641b0  feat(pitch): merge product content — 15-slide unified deck
dd36c01  feat(pitch): finalize slides 14-15 — credentials + contact CTA
0583fd2  feat(pitch): ES variant — Latin American Spanish
996afde  feat(pitch): PT-BR variant — Brazilian Portuguese
98a27bf  feat(pitch): HI variant — Indian Hindi
911b431  feat(pitch): RU variant — international Russian
97e221e  docs: sync memory files with pitch deck delivery (5 locales)
4af9ddd  feat(funnel): add Invest CTA + language-aware pitch deck routing
8cb7286  refactor(funnel): replace 3-card block with focused investor CTA
```

### Pending (after push)
1. Visual verification at `localhost:3000` (6-point checklist: hero CTA, nav, routing EN→RU, soft link, lightbox, mobile)
2. Push to `origin/main` → Vercel auto-deploys `eco-pearl.com`
3. Investment calculator integration — `pearl_dashboard_ru6.html` exists, needs funnel integration
4. Telegram bot for PEARL token purchase
5. Phases 7-9: Proof-of-Processing, Object Map, Transparency Report

### Known issue — claude-mem worker
- `npx claude-mem status` fails: `Cannot find module 'zod/v3'`
- Hook chain still captures observations; only the on-demand status query is broken
- Fix: `cd ~/.claude/plugins/marketplaces/thedotmack/plugin && npm install`

### Tech context (snapshot)
- Pearl design system: bg `#04080f`, gold `#c9a84c`, cream `#f0e8d0`
- Fonts: Cinzel Decorative (h1), Cinzel (h2/h3), EB Garamond (body)
- 5 active languages: EN / ES / PT-BR / HI / RU
- Vercel auto-deploys from GitHub `origin/main`
- Site live at https://www.eco-pearl.com
- Repo path: `/Users/votykvot/Desktop/pearl-of-restoration`

## Known Bugs (non-blocking — fix in future phase)

| Bug | Location | Impact |
|-----|----------|--------|
| Lightbox JS crash | `index.html:832-839` — `openLightbox()` calls `#lightbox` which doesn't exist | Gallery image clicks throw `TypeError` |
| Backslash in footer | `index.html:704` — `\&nbsp;\&middot;\&nbsp;` renders as `\ · \` | Two visible stray backslashes |
| extraction-report.json not gitignored | `.gitignore` missing this entry | Unexpected diffs on script re-runs |

<!-- GSD:project-start source:PROJECT.md -->
## Project

**Pearl of Restoration — Investment Platform**

A global investment website for the PEARL token on the TON blockchain, enabling investors worldwide to participate in an activated-carbon production facility. The site markets the technology, explains the 15% revenue-share token model, and routes all purchases and referrals through a Telegram bot. No Russian geography or company branding is exposed — international technology positioning only.

**Core Value:** A prospective investor can understand the PEARL token opportunity and take action (buy tokens, refer friends) in under 60 seconds in their own language.

### Constraints

- **Deployment**: GitHub Pages — static files only, no server-side execution
- **Telegram bot**: All purchase/referral actions MUST flow through Telegram bot — no website backend
- **Content rules**: Never mention Russia, Russian origin, GOST, or Russian company names in any user-visible text
- **Token positioning**: Position PEARL as utility token (revenue-share), NOT investment instrument — regulatory caution
- **File size**: `index.html` must stay under 200KB after image extraction (currently 8.5MB)
- **Single-file constraint**: Prefer single-file approach until image extraction proves feasible with GitHub Pages
<!-- GSD:project-end -->

<!-- GSD:stack-start source:codebase/STACK.md -->
## Technology Stack

## Core Technologies
| Layer | Technology | Version/Notes |
|-------|-----------|---------------|
| Markup | HTML5 | Single file (`index.html`, ~8.5MB) |
| Styling | CSS3 (inline `<style>`) | No preprocessor, no framework |
| Scripting | Vanilla JavaScript (inline `<script>`) | No bundler, no transpiler |
| Fonts | Google Fonts CDN | Cinzel, Cinzel Decorative, EB Garamond |
| Icons | Font Awesome 6.5.0 | CDN, crossorigin + SRI integrity hash |
| QR Codes | qrcode.min.js | Local file (crypto donate modal) |
| Contact Form | @formspree/ajax 1.1.1 | CDN, deferred |
## Runtime Environment
- **Deployment**: GitHub Pages (static hosting)
- **No server-side logic** — fully client-rendered
- **No build step** — edit `index.html`, commit, push = deploy
- **No package.json / node_modules** — zero dependencies to install
## Asset Approach
- **Images**: External files in `media/` folder (extracted in Phase 1 — no longer base64 inline)
- **Videos**: External files in `media/` folder (`mwf-video-1.mp4`, `station-video-1.mp4`, `station-video-2.mp4`)
- **Fonts/Icons**: CDN-loaded at runtime
- **Local verification**: use `npx serve` (NOT `python3 -m http.server` — lacks Range request support for video)
## Browser Targets
- CSS custom properties (`:root` vars)
- `backdrop-filter: blur()` (webkit-prefixed fallback included)
- Intersection Observer API (implied by scroll animations)
- Modern Flexbox/Grid layout
<!-- GSD:stack-end -->

<!-- GSD:conventions-start source:CONVENTIONS.md -->
## Conventions

## CSS Conventions
- **CSS variables** defined in `:root` for the gold/cream color palette:
- **Minified style block** — no whitespace, rules concatenated for smaller file size
- **Dark background baseline**: `body { background:#04080f; }` (near-black)
- **Responsive typography**: `clamp()` used for font sizes across breakpoints
- **Webkit prefix** included for `backdrop-filter` alongside standard property
## HTML Conventions
- **IDs for sections**: `#hero`, `#iceland-bg`, `#cosmos-bg`, `#contact` — used as nav targets
- **Panel toggle pattern**: `style="display:none;"` on panels; JS sets `display:block`
- **Base64 images inline**: `<img src="data:image/jpeg;base64,…">` — no lazy loading
- **Semantic elements**: `<section>`, `<nav>`, `<footer>`, `<h1>`-`<h3>` used appropriately
- **max-width: 1060px** container for content blocks, full-width for gallery panels
## JavaScript Conventions
- **Vanilla JS only** — no jQuery, no framework
- **DOM queries**: `document.getElementById()` and `querySelector()` patterns
- **Event listeners** attached directly in `<script>` blocks after DOM elements they reference
- **Panel show/hide**: functions like `hideAllPanels()` followed by targeted `show()`
- **Scripts split into 4 blocks** by concern (tabs, scroll, QR modal, counter)
## Naming Conventions
- IDs: `kebab-case` (`#hero-content`, `#readmore-block1`, `#gallery-block2`)
- CSS classes: `kebab-case` (`.nav-logo`, `.gallery-panel`, `.tab-btn`)
- Block numbering: numeric suffix 1-4 matching product ecosystem order
## Content Conventions (from CLAUDE.md)
| Do | Don't |
|----|-------|
| "WIPO registered" / "Patented technology" | Russia / Russian origin / GOST |
| "Industrial Oil Regeneration System" | Станция / МСРМ |
| "Metalworking Fluid Concentrate" | СОЖ 2000 |
| "Activated Carbon from Organic Waste" | Меласса → сорбент |
| "Waste-to-Energy Complex" | КДК |
| "Closed-Loop Resource Recovery" | Замкнутый цикл |
## Version Management
- No semver — version noted in CLAUDE.md (`v6.1` current)
- Breaking changes → backup current file before editing
- Single-commit deploys to GitHub Pages (`main` branch)
<!-- GSD:conventions-end -->

<!-- GSD:architecture-start source:ARCHITECTURE.md -->
## Architecture

## Overview
## Page Layout
```
```
## Tab/Gallery System
- **Tab buttons** toggle `display:none/block` on `#gallery-block{N}` and `#readmore-block{N}` panels
- Panels are hidden by default; JavaScript shows/hides on button click
- No routing, no URL hash changes — pure DOM toggle
## Interaction Model
```
```
## Crypto Donate Modal
```
```
## CO2 Counter
- Formula: `$1 → 100L processed → 320kg CO2 avoided`
- Counter rendered in hero stats cards (moved from hero to impact section in v6.1)
- Animated counter increment via `requestAnimationFrame` or `setInterval`
## Versioning
- Current live version: **v6.1** (in `index.html`)
- Previous: v5 backup at `/tmp/backup-v5.html`
- No semantic versioning enforced — version tracked in CLAUDE.md comments
<!-- GSD:architecture-end -->

<!-- GSD:skills-start source:skills/ -->
## Project Skills

No project skills found. Add skills to any of: `.claude/skills/`, `.agents/skills/`, `.cursor/skills/`, `.github/skills/`, or `.codex/skills/` with a `SKILL.md` index file.
<!-- GSD:skills-end -->

<!-- GSD:workflow-start source:GSD defaults -->
## GSD Workflow Enforcement

Before using Edit, Write, or other file-changing tools, start work through a GSD command so planning artifacts and execution context stay in sync.

Use these entry points:
- `/gsd-quick` for small fixes, doc updates, and ad-hoc tasks
- `/gsd-debug` for investigation and bug fixing
- `/gsd-execute-phase` for planned phase work

Do not make direct repo edits outside a GSD workflow unless the user explicitly asks to bypass it.
<!-- GSD:workflow-end -->

<!-- GSD:profile-start -->
## Developer Profile

> Profile not yet configured. Run `/gsd-profile-user` to generate your developer profile.
> This section is managed by `generate-claude-profile` -- do not edit manually.
<!-- GSD:profile-end -->

---

## Auto-save rule

After every completed phase or significant decision, automatically update `Memory.md`, `CLAUDE.md`, and `SKILL_pearl-of-restoration.md` without waiting for a user reminder. Commit with message:

```
docs: auto-update memory after [phase/decision name]
```

What triggers an auto-update:
- Phase execution completes (`/gsd-execute-phase`)
- New token/financial numbers confirmed by user
- New addresses or bot parameters added
- Architecture decision finalized
- Known bugs discovered or fixed
