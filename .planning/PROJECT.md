# Pearl of Restoration — Investment Platform

## What This Is

A global investment website for the PEARL token on the TON blockchain, enabling investors worldwide to participate in an activated-carbon production facility. The site markets the technology, explains the 15% revenue-share token model, and routes all purchases and referrals through a Telegram bot. No Russian geography or company branding is exposed — international technology positioning only.

## Core Value

A prospective investor can understand the PEARL token opportunity and take action (buy tokens, refer friends) in under 60 seconds in their own language.

## Requirements

### Validated

- ✓ Marketing landing page with 4 product sections (Oil Regeneration, MWF, Activated Carbon, KDK) — existing
- ✓ Crypto donate modal with USDT TRC-20 + BTC QR codes — existing
- ✓ Contact form via Formspree — existing
- ✓ Tab-based gallery and Read More panels — existing
- ✓ CO2 impact counter — existing
- ✓ Mobile-responsive layout with gold/cream brand palette — existing
- ✓ GitHub Pages deployment — existing

### Validated

- ✓ **PERF-01** — Extract base64 images to `media/` folder — Validated in Phase 1: `index.html` reduced from 8.5 MB to 81 KB, 14 images in `media/`
- ✓ **PERF-02** — All product block content fully intact after extraction — Validated in Phase 1: human-verified in browser, no broken images

### Active
- [ ] **I18N-01** — Language switcher with 4 locales: EN, ES, PT-BR, HI
- [ ] **I18N-02** — All visible text translated per locale; default is EN
- [ ] **I18N-03** — Language selection persists across page reloads (localStorage)
- [ ] **TOKEN-01** — Token sale section: PEARL token explainer, price, supply, fundraising progress
- [ ] **TOKEN-02** — "Buy PEARL" CTA that opens Telegram bot link
- [ ] **TOKEN-03** — Token economics page showing 15% annual revenue distribution model
- [ ] **CALC-01** — Investment calculator: input $ amount → show token count + estimated annual USDT payout
- [ ] **CALC-02** — Calculator integrated from existing separate HTML dashboard file
- [ ] **CAM-01** — Construction feed section showing latest facility photo (refreshed periodically)
- [ ] **CAM-02** — Photo hosted on external server/CDN, loaded by URL (no base64)
- [ ] **REF-01** — Referral section explaining the 2-level USDT payout program
- [ ] **REF-02** — Personal referral link generator producing `t.me/BOTNAME?start=REF_CODE`
- [ ] **REF-03** — Referral code input/display (user enters their Telegram ID or bot-generated code)

### Out of Scope

- Live RTSP/HLS camera stream — no relay server; using static photo refresh instead
- TonConnect SDK / on-chain DApp — both buy paths redirect to Telegram bot; no wallet signing in browser
- Custom backend/database — Telegram bot handles all purchase tracking, referral attribution, and USDT payouts
- Russian geography, GOST references, or Russian company names — international positioning only
- Pearl token as investment instrument framing — regulatory positioning: utility token

## Context

**Codebase state:** Single-file static site (`index.html`, now 81 KB after Phase 1 extraction). 14 images in `media/`. Deployed to GitHub Pages from `polyalpha-hq/pearl-of-restoration`. No build pipeline — edit HTML, commit, deploy.

**Blockchain:** PEARL token deployed on TON blockchain. Smart contract exists. Purchases handled via Telegram bot (both TonKeeper and credit-card-style flows redirect to bot). Total raise target: $24,749,074.

**Token model:** Token holders receive 15% of annual production revenue, distributed proportionally. Three production lines of activated carbon from agricultural biomass waste.

**Telegram bot:** Already exists and handles: token purchases, referral tracking, 2-level USDT payouts. Website is the acquisition funnel — bot is the backend.

**Camera:** IP camera (RTSP) at production facility. For v1, static approach: camera uploads latest frame to a CDN/server URL at intervals; website loads that URL.

**Existing dashboard:** Investment calculator built as separate HTML file. To be provided and integrated — exact UI/logic to be preserved.

**Languages:** EN (primary), ES (Spanish), PT-BR (Brazilian Portuguese), HI (Hindi). Targets Latin America, South Asia, and global crypto audiences.

## Constraints

- **Deployment**: GitHub Pages — static files only, no server-side execution
- **Telegram bot**: All purchase/referral actions MUST flow through Telegram bot — no website backend
- **Content rules**: Never mention Russia, Russian origin, GOST, or Russian company names in any user-visible text
- **Token positioning**: Position PEARL as utility token (revenue-share), NOT investment instrument — regulatory caution
- **File size**: `index.html` must stay under 200KB after image extraction (currently 8.5MB)
- **Single-file constraint**: Prefer single-file approach until image extraction proves feasible with GitHub Pages

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Telegram bot as only purchase backend | Avoids need for custom server, leverages existing infrastructure | — Pending |
| Static photo refresh instead of live stream | No relay server available; static approach works within GitHub Pages constraints | — Pending |
| No TonConnect SDK for v1 | Simplifies tech stack; bot handles all on-chain logic | — Pending |
| Keep GitHub Pages deployment | Zero infrastructure cost; appropriate for static marketing funnel | — Pending |
| EN/ES/PT-BR/HI language support | Primary crypto investor markets outside Russia | — Pending |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `/gsd-transition`):
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update if drifted

**After each milestone** (via `/gsd-complete-milestone`):
1. Full review of all sections
2. Core Value check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-05-13 — Phase 1 complete (image extraction baseline)*
