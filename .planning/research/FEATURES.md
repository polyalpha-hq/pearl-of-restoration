# Feature Landscape — PEARL Token Investment Platform

**Domain:** Crypto token sale / RWA revenue-sharing investment site
**Researched:** 2026-05-13
**Confidence:** MEDIUM-HIGH (cross-verified across multiple sources)

---

## Context

PEARL is a utility token on TON blockchain. Token holders receive 15% of annual activated carbon production revenue, distributed proportionally. All purchases and referral tracking flow through an existing Telegram bot — the website is a pure acquisition funnel. Static site on GitHub Pages; no backend.

This feature landscape covers what the platform section of the site needs to add on top of the existing marketing content.

---

## Table Stakes

Features investors expect. Missing = product feels incomplete or untrustworthy.

| Feature | Why Expected | Complexity | Notes |
|---------|--------------|------------|-------|
| Token price + supply display | Investors need to evaluate entry cost and dilution immediately | Low | Static values or manually updated; no live oracle needed at v1 |
| Fundraising progress indicator | Shows traction, creates urgency, proves legitimacy | Low | Visual thermometer/bar with raised amount vs target ($24.75M). Can be manually updated or hardcoded at launch |
| "Buy token" CTA with clear path | Every visitor needs an unambiguous next action | Low | Single button → Telegram bot link (`t.me/BOTNAME`). Already scoped (TOKEN-02) |
| Token utility explanation | Investors must understand what the token does before buying | Low | The 15% revenue share model needs one clear, scannable explanation block |
| Tokenomics breakdown | Supply allocation, vesting, distribution logic | Medium | Pie chart or table: total supply, team %, sale %, reserve % |
| Investment calculator | "If I put in $X, I get Y tokens and Z USDT/year" | Medium | Already scoped (CALC-01/02). This is the highest-converting feature for revenue-share models |
| Risk/legal disclaimer | Required to avoid securities framing; protects project | Low | Footer disclaimer positioning PEARL as utility token, not investment. Non-negotiable per PROJECT.md constraints |
| Mobile-responsive token section | Over 70% of crypto traffic is mobile (Telegram-first audience especially) | Low | Already constraint in existing site; must extend to new sections |
| Multilingual content | EN/ES/PT-BR/HI markets are target; non-English investors distrust English-only sites | Medium | Already scoped (I18N-01 through I18N-03). All new token content must be translatable |
| Social/community links | Investors verify legitimacy via Telegram, X/Twitter presence | Low | Telegram group link + channel at minimum |
| Referral program explanation | Two-level USDT payout is a major acquisition multiplier; visitors need to understand it | Low | Already scoped (REF-01). Clear explanation of Level 1 and Level 2 structure with USDT amounts |

---

## Differentiators

Features that set PEARL apart from generic crypto token sales. Not universally expected, but high trust/conversion value for this specific project.

| Feature | Value Proposition | Complexity | Notes |
|---------|-------------------|------------|-------|
| Live facility photo feed | Proves the physical asset exists. Uniquely powerful for RWA tokens — almost no competitors do this | Low-Medium | Static image refresh approach already scoped (CAM-01/02). Refresh every 15-60 min via CDN URL. Display with timestamp. This is a major trust differentiator |
| Personal referral link generator | Turns every token buyer into a distributor; viral growth flywheel for Telegram-native audience | Low-Medium | Already scoped (REF-02/REF-03). Generates `t.me/BOTNAME?start=REFCODE`. Display code + copy button |
| Revenue distribution timeline | Shows when investors receive their first payout (monthly? quarterly? annual?) | Low | Clear timeline graphic or text block removes the #1 investor anxiety: "when do I get paid?" |
| Environmental impact counter | CO2 avoided per activated carbon production tonne → connects sustainability to investment | Low | Existing CO2 counter can extend to token sale section; reinforces the "green" RWA framing |
| Production progress milestone tracker | Shows construction completion % or milestones (site prep, equipment, commissioning) | Medium | Updates needed manually or via periodic CMS-style edit. Builds ongoing engagement reason to revisit site |
| Payout model explainer (visual) | Revenue share with proportional distribution is unfamiliar to retail crypto investors | Medium | Animated or static diagram showing: total production revenue → 15% → token pool → individual holder. Resolves confusion before it blocks purchase |
| Language auto-detect on first visit | Reduces friction for non-English visitors; feel welcomed immediately | Low | Browser `navigator.language` → auto-select locale, then persist to localStorage |

---

## Anti-Features

Features to explicitly NOT build in v1.

| Anti-Feature | Why Avoid | What to Do Instead |
|--------------|-----------|-------------------|
| KYC/AML gate on website | Telegram bot handles purchase; website has no backend to store identity data. Adding a KYC form creates false compliance theater and drives away buyers | Let bot handle compliance; website is top-of-funnel only |
| On-chain wallet connect (TonConnect/MetaMask) | Increases tech complexity, adds attack surface, confuses non-crypto users. All purchases go through bot. Already out of scope per PROJECT.md | Single "Buy via Telegram" CTA only |
| Live token price feed / oracle | No trading market yet (presale). Showing a live price ticker for a token with no liquidity misleads investors and requires API integration | Display fixed presale price as static text |
| Chat widget / live support | Adds cost, creates support expectations you can't fulfill at this stage. TON/Telegram community does this natively | Link to Telegram community group instead |
| Whitelist registration form | Adds backend requirement. All buyer qualification happens in the Telegram bot | Bot handles whitelist; website just explains eligibility |
| Countdown timer to "close" | Without genuine deadline enforcement, counterfeit urgency is a known scam signal that damages trust with savvy investors | Use raised-amount progress bar instead for real social proof |
| Staking/DeFi dashboard | No DeFi mechanics exist for PEARL. Building UI for non-existent features is misleading | Token utility is revenue share only; document that clearly |
| NFT drops / gamification | Off-brand for industrial RWA token. Would confuse the investor demographic (emerging markets, institutional-leaning) | Keep brand serious and industrial |
| User account / login system | No backend, no session management on GitHub Pages. Impossible without server | All personalization via Telegram bot |
| Exchange listing tracking widget | No exchange listing yet. Showing empty or pending exchange slots signals weakness | Omit until listing is confirmed |

---

## Feature Dependencies

```
Token utility explanation
  → Investment calculator (needs price + supply to calculate)
    → Referral link generator (investor is motivated after calculating ROI)
      → Facility photo feed (confirms physical asset behind the ROI)

Multilingual content
  → All above features must exist in EN/ES/PT-BR/HI

Fundraising progress bar
  → Requires manually maintained raised-amount value (or bot-provided endpoint if available)
```

---

## Regulatory / Compliance Considerations

| Feature | Consideration | Mitigation |
|---------|--------------|------------|
| Revenue share framing | Revenue share = hallmarks of a security under Howey test in US law | Frame consistently as "utility token with production participation rights"; never use "investment returns", "dividends", or "profit sharing" language |
| Calculator output | Showing projected USDT payouts could be construed as guaranteeing returns | Add "estimated based on production targets, not guaranteed" disclaimer below all calculator outputs |
| Fundraising progress bar | Displaying total raised could trigger securities registration requirements in some jurisdictions | Pair with clear utility token disclaimer; avoid "investor" language |
| KYC/geo-blocking | US and some EU jurisdictions restrict token sales without registration | Recommended: add geo-aware disclaimer noting unsupported jurisdictions; do not hard-block (bot can handle at purchase) |
| Referral program | Two-level USDT payout referral programs can be classified as MLM in some jurisdictions | Frame as "community introduction rewards", clearly disclose the flat payout structure, not a percentage chain |
| Team identity | Anonymous team is a scam red flag; named team builds trust but adds personal risk | Include director name (Andrey Baranovsky) and role without Russian company attribution |

---

## MVP Recommendation

Prioritize for this milestone (adds to existing marketing site):

1. **Token sale section** — price, supply, fundraising progress bar, buy CTA (TOKEN-01/02)
2. **Investment calculator** — highest single-feature conversion driver for revenue-share model (CALC-01/02)
3. **Tokenomics + utility explanation** — blocks purchase if missing
4. **Facility photo feed** — unique trust differentiator, technically simple (CAM-01/02)
5. **Referral section + link generator** — turns buyers into marketers (REF-01/02/03)
6. **Multilingual coverage of all above** — required for target markets (I18N-01/02/03)

Defer:

- Production milestone tracker: Needs content authoring process; add in a later milestone
- Revenue distribution timeline: Can be in tokenomics section initially as plain text, formalize later
- Language auto-detect: Nice-to-have; manual switcher (I18N-01) ships first
- Environmental impact expansion into token section: CO2 counter already exists, cross-link rather than rebuild

---

## Sources

- TokenMinds — Crypto presale best practices: https://tokenminds.co/blog/token-sales/presale-token
- ilink.dev — Building ICO/IEO investor trust: https://ilink.dev/blog/building-a-successful-ico-or-ieo-how-to-launch-your-token-and-attract-investors
- ICOGEMHUNTERS — Red flags and scam signals: https://www.icogemhunters.com/blog/ico-scam-red-flags
- BlockShark — No-code presale widgets feature list: https://blockshark.com/no-code-presale-widgets
- PresaleWidget.com — Presale widget UX patterns: https://presalewidget.com/
- Coinbase — Utility vs security token distinctions: https://www.coinbase.com/learn/crypto-basics/utility-tokens-vs-security-tokens-what-are-the-differences
- LegalNodes — Token type legal status: https://www.legalnodes.com/article/token-types-legal-status
- TokenMinds — Asset-backed token guide: https://tokenminds.co/blog/crypto-consulting/asset-backed-tokens
- Chainlink — RWA education: https://chain.link/education-hub/real-world-assets-rwas-explained
- AA Media Studios — Crypto website trust signals: https://blog.aamediastudios.com/building-trust-designing-crypto-website-signals-that-work/
- The Defiant — Legitimate presale checklist: https://thedefiant.io/education/markets/crypto-presales
