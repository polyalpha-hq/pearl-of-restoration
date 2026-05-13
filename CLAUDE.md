# Pearl of Restoration — CLAUDE.md

## Project
- Brand: **Pearl of Restoration** / Жемчужина Возрождения
- Company: ООО ТД «Ренессанс-Контракт», Director: Андрей Барановский
- Repo: https://github.com/polyalpha-hq/pearl-of-restoration (GitHub Pages)
- Primary file: `index.html` (built from `pearl-of-restoration-v6.html`, ~8.9MB)
- Backup: `/tmp/backup-v5.html` (v5), `~/Desktop/pearl-of-restoration-v5.html`

---

## CRITICAL RULE
Never mention Russia, Russian origin, Russian standards, or Russian companies in any international materials.
- Patents → use only: "Patented technology, WIPO registered"
- No GOST references
- No Russian product names (СОЖ 2000 → Metalworking Fluid Concentrate)
- Russia is NOT a target market

---

## Page Structure (v6)
- 4 content blocks + tab buttons (max-width: 1060px) → full-width gallery
- **Block I** — Industrial Oil Regeneration System: 7 photos (base64) + 2 videos (`media/`)
- **Block II** — MWF video: `media/mwf-video-1.mp4`
- **Block III** — Activated Carbon (sorbent): 2 photos (base64)
- **Block IV** — Waste-to-Energy Complex (KDK): 1 photo (base64)
- Each block has a **Read More** button → full-width panel below
- QR modal: crypto donate working
- CO2 counter formula: $1 = 100L = 320kg CO2

## Media Files
- `media/station-1.jpg` — station photo
- `media/station-7.jpg` — station photo
- `media/mwf-video-1.mp4` — MWF block video

## Crypto Donate
- USDT TRC-20: `THt3iokn8NELPyaeWHWd8n7xBNECVxwyND`
- BTC: `bc1q04azu8yus2ynku0fdf2decvjm6javynnx8e0kr`

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
- Promise operating Waste-to-Energy facilities (none exist)
- Position Pearl token as investment instrument

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
- **Images**: Base64-encoded inline (~14 instances, responsible for ~8.4MB of file size)
- **Videos**: External files in `media/` folder (`station-1.jpg`, `station-7.jpg`, `mwf-video-1.mp4`)
- **Fonts/Icons**: CDN-loaded at runtime
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
