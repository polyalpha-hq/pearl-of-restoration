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

## PEARL Token

| Parameter | Value |
|-----------|-------|
| Price | **$1.00** |
| Supply | **20,000,000 PEARL** |
| Blockchain | **TON** |
| Yield model | **15% of annual activated carbon revenue** |
| Legal framing | Utility token (revenue participation) — NOT investment instrument |

## Telegram Bot

- Accepts: **USDT TRC-20**, **TON**, **Toncoin**
- Languages: **HI** (Hindi), **PT** (Portuguese), **ID** (Indonesian), **EN** (English)
- Built-in referral system; `/mycode` command returns user's referral code

## Referral Program

| Transaction type | Referrer reward |
|-----------------|-----------------|
| Token purchase / donate | **5%** |
| Equipment sale | **2%** |
| Investment | **1%** |

- Crypto-only payouts
- 2-level structure (referrer + referrer's referrer)

## Revenue Numbers

| Scenario | Revenue/year | Token pool (15%)/year |
|----------|--------------|-----------------------|
| 1 production line | $18.9M | $2.84M |
| 3 production lines (target) | $56.8M | $8.5M |

Sustainability fee (3 lines): ~$15.95M/year — shown as a separate operational stream, not part of token pool.

## Public Positioning Formula

> "Agricultural biomass waste → premium activated carbon"

Never mention: Russia, molasses, sugar plants, GOST, МСРМ, СОЖ, КДК.

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

After every completed phase or significant decision, automatically update `Memory.md` and `CLAUDE.md` without waiting for a user reminder. Commit with message:

```
docs: auto-update memory after [phase/decision name]
```

What triggers an auto-update:
- Phase execution completes (`/gsd-execute-phase`)
- New token/financial numbers confirmed by user
- New addresses or bot parameters added
- Architecture decision finalized
- Known bugs discovered or fixed
