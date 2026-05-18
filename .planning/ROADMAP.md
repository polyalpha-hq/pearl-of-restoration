# Roadmap — Pearl of Restoration Investment Platform

**Project:** PEARL
**Milestone:** v1
**Defined:** 2026-05-13
**Updated:** 2026-05-18 — restructured Phases 3-9 (added trust-through-transparency tier: Phases 7-9)
**Granularity:** coarse (9 phases)
**Mode:** yolo

---

## Phases

- [x] **Phase 1: Image Extraction & Baseline** — Extract all base64 images to `media/` folder, bringing `index.html` from 8.5MB to ~50KB (completed 2026-05-13)
- [x] **Phase 2: Hindi Locale** — Add HI to the existing EN/ES/PT-BR i18n engine with full translations (completed 2026-05-14)
- [ ] **Phase 3: Token Sale Section** — Ship PEARL token section with price, supply, progress bar, Buy CTA, and tokenomics page
- [ ] **Phase 4: Revenue Participation Estimator** — Integrate dashboard HTML as investment calculator with scoped CSS
- [ ] **Phase 5: Facility Photo Feed** — Construction feed loading latest photo from CDN URL with 5-minute refresh
- [ ] **Phase 6: Referral Section** — 2-level referral payout explainer and personal link generator
- [ ] **Phase 7: Proof-of-Processing** — On-chain production telemetry from line sensors, live-verifiable on the site
- [ ] **Phase 8: Object Map** — Interactive map of operating facilities with live load % per node (anonymized geography)
- [ ] **Phase 9: Transparency Report** — Each dividend payout linked on-chain to the sorbent batches that produced its revenue

---

## Phase Details

### Phase 1: Image Extraction & Baseline
**Goal:** Extract all base64-encoded images from `index.html` to the `media/` folder, reducing file size from ~8.5MB to under 50KB so all subsequent editing work is safe and fast.
**Mode:** mvp
**Requirements:** PERF-01, PERF-02
**Success Criteria** (what must be TRUE):
  1. Visitor's browser begins rendering the page within 2 seconds on a 10 Mbps connection (HTML under 200KB served from GitHub Pages)
  2. All four product blocks display their photos correctly — no broken images, no missing content
  3. A developer can open and edit `index.html` in a standard text editor without risk of corrupting base64 blobs
**Depends on:** Nothing
**Plans:** 2/2 complete
  - [x] 01-01-PLAN.md — Build extraction tooling and safety net
  - [x] 01-02-PLAN.md — Run extraction, swap index.html, verify visually

### Phase 2: Hindi Locale
**Goal:** Add HI (Hindi) as the fourth language in the existing i18n engine so all current and future content is authored once and published in all four locales simultaneously.
**Mode:** mvp
**Requirements:** I18N-01, I18N-02, I18N-03
**Success Criteria** (what must be TRUE):
  1. A visitor can click the HI button in the nav and the entire page renders in Hindi without a page reload
  2. Switching between EN, ES, PT-BR, and HI produces complete translations with no untranslated English strings visible in any locale
  3. After selecting Hindi and refreshing, the page reloads in Hindi (localStorage persistence confirmed)
**Depends on:** Phase 1
**Plans:** 2/2 complete
  - [x] 02-01-PLAN.md — Insert hi:{} translation block (122 keys, Devanagari)
  - [x] 02-02-PLAN.md — Add HI button to nav and verify visually

### Phase 3: Token Sale Section
**Goal:** Publish the PEARL token sale section — token explainer, price per token, total supply, fundraising progress bar, Buy CTA routing to Telegram bot, and a tokenomics page framing the 30% revenue participation model as a compliant utility token.
**Mode:** mvp
**Requirements:** TOKEN-01, TOKEN-02, TOKEN-03
**Success Criteria** (what must be TRUE):
  1. A visitor scrolling the page sees the PEARL token section displaying: token name, price per token (`$1.00`), total emission (`31,051,657 PEARL`), and a visual fundraising progress bar against the `$24,749,074` construction target (after 5% referral pool)
  2. Clicking "Buy PEARL" opens the Telegram bot purchase link (`t.me/BOTNAME?start=buy`) — no on-site transaction occurs
  3. The tokenomics page explains the **30% pool of full line turnover** (sorbent revenue + Carbon Recovery Fee) using "utility token" and "revenue participation" language exclusively — the phrases "investment return", "profit", and "guaranteed" appear nowhere in any locale
  4. All token section text is translated and renders correctly in all five locales (EN, ES, PT-BR, HI, RU)
**Depends on:** Phase 2
**Blocked on:** TOKEN-03 tokenomics content must pass legal review before publish
**Plans:** TBD
**UI hint:** yes

### Phase 4: Revenue Participation Estimator
**Goal:** Integrate the existing dashboard HTML as an investment calculator embedded in the site, with CSS scoped under `.pearl-calc` to prevent style collision, and a mandatory "estimated, not guaranteed" disclaimer always visible.
**Mode:** mvp
**Requirements:** CALC-01, CALC-02
**Success Criteria** (what must be TRUE):
  1. A visitor enters a USD amount and immediately sees: number of PEARL tokens purchased, resulting share of the 30% annual pool, and estimated annual USDT payout at the 3-line target (`$20,974,109 / 31,051,657 ≈ 67.5%` yield on cost at full ramp)
  2. The disclaimer "Estimated, not guaranteed. Past revenue does not predict future distributions." (or locale equivalent) is visible at all times — cannot be dismissed or scrolled past without being read
  3. The calculator's visual style matches the existing dashboard design exactly — no layout breakage from style collision with parent page
**Depends on:** Phase 3 (token tier numbers must already be on-site)
**Blocked on:** Dashboard HTML file must be provided by project owner before implementation begins
**Plans:** TBD
**UI hint:** yes

### Phase 5: Facility Photo Feed
**Goal:** Add a construction feed section displaying the latest photo from the production site, loaded from an external HTTPS CDN URL and automatically refreshed every 5 minutes with a cache-busting query string.
**Mode:** mvp
**Requirements:** CAM-01, CAM-02
**Success Criteria** (what must be TRUE):
  1. A visitor sees a facility feed section with a photo of the production site — on first visit, either a real photo or a labeled placeholder is shown (never a broken image icon)
  2. The photo is loaded via `<img src="https://...">` pointing to an external HTTPS URL — no base64 data embedded in `index.html` for this image
  3. If a visitor leaves the page open for 5 minutes, the photo refreshes automatically (cache-busting query string confirmed in network tab)
**Depends on:** Phase 1
**Blocked on:** CDN/server endpoint must be set up by the camera operator before a live URL replaces the placeholder
**Plans:** TBD
**UI hint:** yes

### Phase 6: Referral Section
**Goal:** Add a referral program section explaining the 2-level USDT payout structure, allowing a visitor to enter their bot-assigned referral code and instantly generate and copy their personal `t.me/BOTNAME?start=REF_{CODE}` link.
**Mode:** mvp
**Requirements:** REF-01, REF-02, REF-03
**Success Criteria** (what must be TRUE):
  1. A visitor can read the referral section and understand the 2-level payout structure (5% / 2% / 1% by transaction type) from a visual diagram without opening the Telegram bot
  2. A visitor enters their referral code and sees their personal `t.me/BOTNAME?start=REF_{CODE}` link generated instantly in the browser — no server request
  3. A visitor clicks the copy button and the link is copied to clipboard; a visible confirmation ("Copied!") appears for at least 2 seconds
  4. Referral section text and diagram labels are translated and display correctly in all five locales (EN, ES, PT-BR, HI, RU)
**Depends on:** Phase 2
**Blocked on:** Telegram bot owner must confirm `/mycode` command exists and referral codes are assigned per-user before link format is finalized
**Plans:** TBD
**UI hint:** yes

### Phase 7: Proof-of-Processing
**Goal:** Push raw production telemetry from the first operating line to the TON blockchain on a fixed cadence, and render a live dashboard on the site that reads the same chain — so a visitor can verify "the line is running" without trusting us.
**Mode:** mvp
**Requirements:** PROOF-01, PROOF-02, PROOF-03
**Success Criteria** (what must be TRUE):
  1. A visitor opens the Proof-of-Processing section and sees the most recent N hours of telemetry (raw material throughput, sorbent output rate, line temperature) as a time-series chart, with each data point traceable to a specific TON transaction hash
  2. The data on the page is read directly from the TON blockchain (no proxy backend) — a visitor with a TON explorer can independently query the same contract address and see identical raw values
  3. Telemetry packets are signed by the on-site edge device's private key, so a third party can verify the readings originated from the registered facility and were not forged in transit
  4. If the edge device stops publishing for more than 2× the expected cadence, the dashboard shows a "stale data — last update X minutes ago" warning rather than silently displaying old values
**Depends on:** Phase 5 (visual proof of construction) + first line physically operational
**Blocked on:** First activated-carbon line must be operational; edge gateway hardware + TON smart contract for telemetry intake must be deployed
**Plans:** TBD
**UI hint:** yes

### Phase 8: Object Map
**Goal:** Surface live load % per operating facility, fed by Phase 7's on-chain telemetry — so a visitor can see "here are N nodes running right now" instead of reading marketing claims. The **specific visualization (geographic map, abstract globe, region tiles, plain list) is deliberately unresolved** and decided at plan-phase time, after Phase 7 is live and the real number of facilities is known.
**Mode:** mvp
**Requirements:** MAP-01, MAP-02, MAP-03
**Success Criteria** (what must be TRUE):
  1. A visitor sees a section listing each operating facility with its current load % computed from the most recent Phase 7 telemetry packet, updated without a page reload as new telemetry arrives (polling cadence at minimum once per minute)
  2. **No city-level geography is exposed publicly.** Real facility locations (recorded internally in `Memory.md`) MUST NOT appear by name, by pin on a map, or by precise coordinate. The public visualization format is **TBD — deferred to `/gsd-plan-phase 8`** when the number of live facilities and the brand's stance on geographic disclosure are both settled. Acceptable forms include: region/continent labels only, abstract globe with non-geographic markers, country-level tiles, or a plain list with facility IDs. Hard-coded forbidden: any UI that lets a visitor identify a specific Russian city as a facility location
  3. Tapping a facility opens a detail panel with: facility ID, line capacity, current load %, link to that node's Phase 7 telemetry on-chain
**Depends on:** Phase 7 (no live data without it)
**Blocked on:** At least 2 facilities on-chain in Phase 7 + visualization-format decision made at plan-phase time
**Plans:** TBD
**UI hint:** yes — but format is unresolved; do not pre-commit to a map-style UI before plan-phase

### Phase 9: Transparency Report
**Goal:** Make each quarterly dividend payout end-to-end auditable on-chain by linking the payout transaction to the specific sorbent batch IDs whose revenue funded it, closing the loop from physical production (Phase 7) to investor return.
**Mode:** mvp
**Requirements:** TXN-01, TXN-02, TXN-03
**Success Criteria** (what must be TRUE):
  1. When a dividend payout occurs, the payout smart contract emits a transparency packet containing: payout amount, batch IDs that generated the underlying revenue, sale prices per batch, and the revenue → pool → payout breakdown
  2. The site's Transparency Report section renders the most recent payout's full chain: Phase 7 telemetry → batches → revenue → pool (30% of full line turnover) → per-token payout
  3. A visitor can click any batch ID in the report and jump to its source telemetry packets on-chain (i.e. a payout in Q3 traces back to the specific sensor readings that produced those batches)
  4. The report includes a prior-quarters archive — at least the last 4 payouts must be readable without scrolling off
**Depends on:** Phase 7 (batch-level telemetry must exist) + dividend payout contract live
**Blocked on:** First dividend payout cycle must have occurred; payout contract must publish the transparency packet format
**Plans:** TBD
**UI hint:** yes

---

## Tier Logic

The roadmap layers into three tiers of escalating commitment:

- **Tier 1 (Phases 1-2): Foundation** — performance, multi-language. Done.
- **Tier 2 (Phases 3-6): Sales surface** — token, calculator, photo, referral. The conversion funnel.
- **Tier 3 (Phases 7-9): Trust through transparency** — the "intrigues" that turn marketing into auditable on-chain proof. Each tier-3 phase requires real-world production to exist before it can ship — these are not pre-launch features.

Tier 3 dependency chain: `Phase 7 → Phase 8`, `Phase 7 → Phase 9`. Phases 8 and 9 are independent of each other after Phase 7 is live.

---

## Progress

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Image Extraction & Baseline | 2/2 | Complete | 2026-05-13 |
| 2. Hindi Locale | 2/2 | Complete | 2026-05-14 |
| 3. Token Sale Section | 0/? | Not started | — |
| 4. Revenue Participation Estimator | 0/? | Not started | — |
| 5. Facility Photo Feed | 0/? | Not started | — |
| 6. Referral Section | 0/? | Not started | — |
| 7. Proof-of-Processing | 0/? | Concept | — |
| 8. Object Map | 0/? | Concept | — |
| 9. Transparency Report | 0/? | Concept | — |

---

## Requirement Coverage

| Requirement | Phase | Status |
|-------------|-------|--------|
| PERF-01 | Phase 1 | Complete |
| PERF-02 | Phase 1 | Complete |
| I18N-01 | Phase 2 | Complete |
| I18N-02 | Phase 2 | Complete |
| I18N-03 | Phase 2 | Complete |
| TOKEN-01 | Phase 3 | Pending |
| TOKEN-02 | Phase 3 | Pending |
| TOKEN-03 | Phase 3 | Pending |
| CALC-01 | Phase 4 | Pending |
| CALC-02 | Phase 4 | Pending |
| CAM-01 | Phase 5 | Pending |
| CAM-02 | Phase 5 | Pending |
| REF-01 | Phase 6 | Pending |
| REF-02 | Phase 6 | Pending |
| REF-03 | Phase 6 | Pending |
| PROOF-01 | Phase 7 | Pending |
| PROOF-02 | Phase 7 | Pending |
| PROOF-03 | Phase 7 | Pending |
| MAP-01 | Phase 8 | Pending |
| MAP-02 | Phase 8 | Pending |
| MAP-03 | Phase 8 | Pending |
| TXN-01 | Phase 9 | Pending |
| TXN-02 | Phase 9 | Pending |
| TXN-03 | Phase 9 | Pending |

**Coverage:** 24 requirements mapped across 9 phases. New requirements (PROOF-*, MAP-*, TXN-*) for Phases 7-9 still need to be added to `.planning/REQUIREMENTS.md` before plan-phase work begins on Tier 3.

---

*Roadmap defined: 2026-05-13 — restructured 2026-05-18 (added Tier 3 intrigues)*
