# US accept-payments — полный каталог найденного

Собрано **2026-08-30** из всех раундов (`/tmp/payfac-wide`, `/tmp/payfac-2024`, `/tmp/payfac-2026`).  
Не выдумано: бренд есть здесь только если был first-party ToS/help, press процессора или «powered by».

**Критерии (финальные):** US; signup / SaaS-триал / вертикальный софт → in-app apply; первая payments-SKU **2021–2026**; PayFac / ISO / PSP / gateway / embedded SaaS / PFaaS frontend / MoR.  
**Жёсткий запрет в «главном» списке:** Stripe / Stripe Connect как единственный карточный рельс. Dual Stripe+X оставлен, помечен.  
Sales-only без in-product apply — в NEAR или не включали как IN.

`sales` = да, если SaaS/продукт только через демо; apply платежей после аккаунта всё равно может быть in-app.

---

## 1. Открытый SMB (любой US business, другой софт не обязателен)

| Бренд | Год | Тип | Процессор / банк | Signup | Sales |
|---|---|---|---|---|---|
| Venmo Business Profiles | 2021-02 | PSP | PayPal / Venmo | venmo.com | нет |
| GoDaddy Payments | 2021-06 | PayFac | Elavon / Adyen / Nuvei · U.S. Bank | godaddy.com | нет |
| PayPal Zettle US (PayPal POS) | 2021-06 | PayFac / POS | PayPal | paypal.com/us/business/pos-system | нет |
| Paddle | 2022 self-serve | MoR | Paddle (не Stripe) | login.paddle.com/signup | нет |
| Airwallex Payments US | 2024-04 | PSP | Airwallex / Paymentech · JPM | airwallex.com/us/signup | нет |
| Frame Payments | ~2024 | PSP / acquiring | Commercial Bank of California (front processor unnamed) | app.framepayments.com/register | нет |
| Dodo Payments | 2024 | MoR | собственные MoR rails (BYOP Stripe/Adyen optional) | app.dodopayments.com/signup | нет |
| Easy (itseasy.co) | 2025-01 | PFaaS frontend | **Finix** · Pathward / Fifth Third | app.itseasy.co/signup | нет |
| Trailing Paper | 2026-04 | PFaaS frontend | **Finix** | trailingpaper.com/register | нет |
| MannyPay | 2026-07 | PayFac / ISO | **Adyen** via iMerchant; dedicated MID unnamed | mannypay.io/merchant-sign-up | нет |
| Coastal Pay SignUp Link | 2026-04 UX (ISO 2013) | ISO boarding | Wells Fargo + Axiom; Fiserv / TSYS / Elavon | signuplink.ai/register | нет |

**Рядом, не полный PayFac:** STRYD (2025-11) — ACH / Pay-by-Bank, settlement **Paya (Nuvei)**, карты не доказаны.  
**Finix Direct SMB** — сам PayFac, live через sales / $250 min. Не frontend.

**Вне окна (инкумбенты):** Square, Helcim, QuickBooks Payments, Wave Payments (сейчас Adyen + Worldpay + Stripe), Authorize.net.

---

## 2. Finix (Pathward processor · Fifth Third PayFac)

### Подтверждено — accept cards

| Бренд | Продукт | Год | Vertical | Signup | Sales | Заметки |
|---|---|---|---|---|---|---|
| Easy | Easy | 2025-01 | любой SMB | app.itseasy.co/signup | нет | ToS: Finix, Inc. |
| Trailing Paper | Trailing Paper | 2026-04 | invoicing / accounting | trailingpaper.com/register | нет | sub-merchant Finix |
| Lunchbox | Lunchbox Payments / Lunchmoney | 2023-10 | restaurants | lunchbox.io/essential | частично | help: Finix onboarding |
| SpiceApp POS Lite | Flat rate Powered by Finix | 2022 | restaurant POS | myspiceapp.com | нет | Worldpay IC+ optional |
| Contractor+ Pay | Contractor+ Pay | 2024 | field service | contractorplus.app | нет | in-app apply 24–48h |
| Candid Pay | Candid Pay | 2024 | dental wholesale | app.candidwholesale.com/…/finix | нет* | *нужен Candid; US с Stripe |
| Meadow Pay | Meadow Pay | 2024–25 | higher ed | meadowfi.com/pay | да | колледжи |
| Archy | Archy payments | in-window | dental PMS | archy.com | да | MSA: Finix Payments, Inc. |
| X-CD Payments | X-CD Payments Powered by Finix | 2026-01 | associations / events | x-cd.com/payments-3 | EOI | только клиенты X-CD |
| Ticketbud Payments | Ticketbud Payments | 2024-10 | events | ticketbud.com/users/sign_up | нет | white-label Finix |
| TherapyAppointment | Integrated Payment Processing | 2025-11 / 2026-06 | mental-health EMR | therapyappointment.com/sign-up | нет | 30-day trial; 2.9%+$0.30; внешний процессор можно |
| Omella | Pages / POS / Tap-to-Pay | ToS 2026-06 | K-12 / PTA / nonprofit / SMB | omella.com/signup | нет | **dual Stripe + Finix**; рельс выбирает Omella |
| Shopmonkey | Shopmonkey Payments | unpinned | auto repair | shopmonkey.io | нет | **dual Stripe + Finix**; Instant Payout = Stripe |
| CharityStack | checkout / donations | Finix с ~2023 | nonprofit | charitystack.com | нет | **dual**; privacy 2026-02 ведёт Stripe; `finix-onboarding.charitystack.com` живой |
| Vroom Delivery | Pay360 | 2024-04 | c-store ecommerce | vroomdelivery.tech/demo | да | Finix press + blog |
| T2 Systems | Control Center card processor | Finix fields 2023-03 | parking / campus | t2systems.com | да | Finix или Authorize.Net |
| foreUP | Payments 2.0 | SKU 2022-11; Finix help 2026-08 | golf PMS | foreupgolf.com/get-a-demo | да | Zendesk: Finix Dashboard, eChecks |
| Clubessential | CE Payments | pre-2024 | clubs | sales | да | Finix press; first-party legal = «Processor» |
| Cargas | Cargas Pay | 2022-08 | fuel / HVAC | sales | да | Finix press; Cargas зовёт себя PayFac |
| Passport | parking PayFac | с 2019 | cities / parking | sales | да | Finix case; ToS Finix не найден |
| AgVend | embedded ACH/cards | 2022–23 | ag retail | sales | да | Finix case 2023 |
| Beyond Pricing | Tally | 2023-08 | STR / vacation rental | sales | да | Finix case |

### Finix — не accept cards / не frontend

| Бренд | Почему не в главном |
|---|---|
| Change | 2026-07 — **payouts** на nonprofits, не эквайринг |
| Finix for WooCommerce | 2025-07 — продукт самого Finix, live MID через sales |
| Pay Theory | case 2022; сейчас **Fiserv** PayFac |
| Wave / Lightspeed | исторический Finix; ушли |
| Kabbage Gift Certificates | 2020, продукт мёртв |
| Sublime / Enwoven | цитата на finix.com / press, продукта-мерчанта нет |

**Публичный каталог Finix `/customers`:** Change, Contractor+, Meadow, AgVend, Beyond, Pay Theory, Passport. Остальные имена — help/ToS/press, не логостенка.

---

## 3. Payrix / Worldpay for Platforms

Официальный индекс: [platforms.worldpay.com/customers](https://platforms.worldpay.com/customers/) — **22 слага**. Плюс имена вне индекса.

| Бренд | Продукт | Рельс | Signup / sales | Заметки |
|---|---|---|---|---|
| Printavo (Inktavo) | Printavo Payments | Payrix | sign_up, не sales | self-serve shops |
| JobNimbus | JobNimbus Payments | Payrix | trial-signup | in-app Get started |
| Xoda | embedded | Payrix (+ Ezypay/Stripe listed) | create-account | AU-founded, US claimed |
| GymMaster | billing provider | Payrix | gym software trial | не в индексе |
| Caterease / HPay | HPay | Payrix | sales + migration form | Horizon Cloud |
| Horizon Cloud | embedded + WC | Payrix PFaaS | sales | отдельный case |
| Storable | Storable Payments | Payrix | sales | in-app Activate |
| FieldRoutes | FieldRoutes Payments | Payrix | sales | |
| Neon One | Neon Pay | Payrix | demo | не neonpay.com |
| Kangarootime | embedded | Payrix | sales | с ~2020 |
| Eyefinity | integrated | WP **referral** | sales | не PFaaS |
| Runit Systems | payments | WP referral | sales | luxury retail POS |
| CryptoPay | CryptoTap unattended | WP referral | sales | laundry / car wash OEM |
| Boost Payment Solutions | Boost 100 | PayFac® + WPG | sales | B2B AP |
| PIREL | embedded | Payrix PFaaS | sales | docs / AP-AR |
| 2TouchPOS (Xenios) | embedded + WC | PFaaS | sales | restaurant POS, с 2005 |
| New West Technologies | POS | WP referral | sales | Portland retail |
| Reynolds and Reynolds | ReyPAY | WP referral | sales | dealer DMS |
| SimplySwim | Direct Debit | WP AU | sales | AU |
| SimpleRent | Payment Engine | WP AU | sales | AU |
| HubHello | embedded | WP AU | sales | AU childcare |
| Perfect Gym | payments | WP AU | sales | gym; IntegraPay lineage |
| iClassPro | Payment Services | WP wholesale PF + Payrix AU | sales | не в индексе |
| Docket (DocketPay) | DocketPay | Payrix (+ Fiserv dual) | sales | waste / dumpster; «powered by Payrix» |
| Splynx | Payrix add-on | BYO Payrix credentials | sales | ISP billing |
| fitDEGREE | studio pay | **был Payrix**; live 2026 **Payabli** | sales | dual privacy |
| FieldPulse | FieldPulse Payments | **был Payrix → Rainforest** | sales | 1 200+ MID |
| Infinite Campus | Campus Payments | **был Payrix → Stripe** | sales | K-12 |

Не подтверждено как Payrix: Real Green, Resman, AutoLeap (first-party = Global Payments).

---

## 4. Rainforest Pay

Публично названы **19** из заявленных ~100. Остальные не опубликованы. Не выдумывать.

| Бренд | Продукт | Vertical | Sales | Signup |
|---|---|---|---|---|
| Hint | Hint Payments | chiro / DPC / cash-pay | да | hint.com/get-started |
| PayGround | patient pay | healthcare | да | payground.com |
| RoadSync | RoadSync Checkout | trucking | да | roadsync.com |
| QuoteMachine | QM Payments | retail / design quotes | да | quotemachine.com |
| D-Tools | D-Tools Payments | AV / low-voltage | **нет** | d-tools.com/cloud-free-trial |
| ProLine | ProLine Payments | roofing / home-imp | **нет** | new.proline.app |
| Duesy | embedded dues | associations | да | meetduesy.com |
| Materio | MaterioPay | construction materials | **нет** | materio.co/signup |
| FieldPulse | FieldPulse Payments | field service | да | fieldpulse.com |
| Decoda Health | branded payments | healthcare SaaS | да | decodahealth.com |
| Crystal PM | Crystal Payments | dental/chiro PM | да | crystalpm.com/payments |
| Keap | Keap Pay | CRM / SMB | **нет** | keap.com/free-trial |
| Handoff | Handoff Finance | construction | да | handoff.ai/trials |
| CivicPlus | CivicPlus Payments | gov / civic | да | civicplus.com |
| Newton | Newton Processing | ? | да | joinnewton.com/book-a-demo |
| Rose Rocket | implementation | freight TMS | да | roserocket.com |
| Curae | CURAEPay | patient finance | да | curae.com |
| Albiware | Albi Pay | restoration | да | albiware.com/albipay |
| SalesThumb | payment processing | sales | **нет** | salesthumb.com |

**Не Rainforest** (часто путали с Payrix): Caterease, Storable, FieldRoutes, Neon Pay, Xoda, GymMaster.  
Подкаст ≠ клиент: Mindbody, Jane, Tithe.ly.

---

## 5. Payabli (Centavo, Inc.)

Заявлено 60→70→95–100 платформ. Публично названы ниже. Остальные не раскрыты.

### Pay-in CONFIRMED

| Бренд | Продукт | Vertical | Sales | Заметки |
|---|---|---|---|---|
| Roofr | Roofr Payments | roofing | **нет** | единственный явный self-serve → Payabli apply |
| BuildOps | Payments+ by Payabli | construction | да | |
| Builder Prime | Builder Prime Payments | construction | да | Payabli с 2021 |
| CurbWaste | ACH/CC | waste | да | Payabli **или** PayEngine |
| fitDEGREE | studio MID | fitness | да | live 2026 Payabli; был Payrix |
| Cubby | operator/tenant | self-storage | да | **dual Stripe + Payabli** |
| ExactEstate | resident / PM | property | да | 2024-11 |
| Sunbound | RCM collections | healthcare? | да | ушли со Stripe+JPM ACH |
| ID Tenant (ID Plans) | ID Tenant payments | CRE / tenant | да | 2026-07 «powered by Payabli» |
| Fyxt | Rent Pay + Vendor Pay | CRE | да | pay-in + pay-out |

### Pay-out only

Edstruments (AP / schools); Smartwebs Payment Distribution (HOA AP).

### LIKELY / не live Payabli pay-in

| Бренд | Статус |
|---|---|
| PayHOA | назван в Series A; first-party help = **Stripe** |
| The Event Community (TEC) | партнёрство анонсировано; payments «Soon» |
| Huntington Bank | embed в online banking, не SaaS |

UNCONFIRMED (FeaturedCustomers only): BDR, BxB Media.

---

## 6. JustiFi · Tilled · Launchpay · Payops (Infinicept)

Каталогов клиентов нет. Только те, кто сами написали процессор.

| Бренд | Процессор | Vertical | Sales | Signup / apply |
|---|---|---|---|---|
| Leap (LeapPay) | JustiFi | roofing / remodel CRM | да (Pay на Team) | leaptodigital.com |
| LASSO Payments | JustiFi | live events | да | lasso.io |
| Projul | JustiFi | construction | да | projul.com; ToS §17 |
| ResortCleaning | Tilled (+ Propelr/Stripe) | vacation cleaning | да | tilled case с 2022-01 |
| LaunchPad | Tilled | youth / after-school | ? | golaunchpad.com (сайт флапал) |
| Bambi (HiBambi) | Tilled | NEMT | да | Settings → Connect Tilled |
| Drake Pay | Launchpay | tax prep | нет* | *нужен Drake; in-product apply |
| TaxAct Professional Integrated Payments | Launchpay | tax pros | нет* | «powered by Drake Pay» / Infinicept |
| TapGoods Payments | Launchpay (US); Till (CA) | event rental | да | merchantapp.io invite |
| WorkWave Payments | Payops | field service | да | backoffice.infinicept.com/wwpayments-… |

Исторические Payops: Fivestars Pay (→ SumUp 2021); RunSignUp (первый клиент Infinicept, 2014); Squire (теперь Stripe).  
PatientPal = Tilled не подтверждён в 2026 first-party.

---

## 7. Adyen for Platforms / Adyen rails

| Бренд | Год | Vertical | Sales | Заметки |
|---|---|---|---|---|
| TicketSpice | Adyen year unpinned | event tickets | нет | Webconnex Payments powered by Adyen |
| GivingFuel | same | nonprofit | нет | ACH 1% |
| RegFox | same | event registration | нет | |
| RedPodium | same | race registration | нет | |
| GroupRev | same | group fundraising | нет | disclaimer ещё WePay |
| Epos Now Payments US | privacy 2023 | retail / hospitality POS | да | Facilitating Bank = Adyen |
| Olo Pay **card-present** | 2023-04/07 | restaurants | да | CNP 2022 был **Stripe** — не мешать |
| Jackrabbit Pay | 2023 | youth class software | да | Capital on Adyen 2025 |
| RMS Pay US/CA | NA **2025-08-18** | hospitality PMS | да | in-app KYC после CS password |
| Oracle Payments | US **2022-06** | restaurant / hotel | да | 2 550 орг / 16 200 venues (2025) |
| Tessitura Merchant Services | NA **2022-03** | arts CRM / ticketing | да | только members |
| ITX Payments (Intellitix) | 2024 | live events cashless | да | San Diego Comic-Con named |
| Konnect Payments (Connect&GO) | GTV 2022–23 | parks / attractions | да | US users named |
| Klipboard Money | embedded 2024; бренд **2026-02** NA | vertical ERP | да | Adyen пишет Adyen; Klipboard press — нет |
| Mews Payments | US transition; multicurrency **2026-07** | hotel PMS | да | часть отелей ещё Stripe |
| 8am LawPay | Adyen addenda **2025-12** | legal / IOLTA | нет | продукт 2007 |
| 8am CPACharge | same addenda | accounting | нет | продукт 2016 |
| 8am ClientPay | acquired 2021-02 | professional services | нет | |
| 8am AffiniPay Associations | addenda | associations | нет | |
| MyCase → LawPay | 2025 migration | legal PMS | нет | не first accept |
| MannyPay | 2026-07 | open SMB | нет | см. §1 |
| Slice | in-window | pizza / QSR | да | hardware path |

**До окна 2021:** Fresha, ROLLER, Zenoti Payments, modmed Pay (все ~2020).  
Lightspeed US с 2020 = Stripe Connect, не Adyen.

---

## 8. Stax · NMI · CardPointe · Paysafe · Moov · прочее

| Бренд | Процессор | Год | Vertical | Sales | Заметки |
|---|---|---|---|---|---|
| TetherPay (ClientTether) | **Stax** | 2022-01 | franchise CRM | нет | Settings → Start enrollment; единственный Stax IN |
| ChiroSpring Pay | Stax | surcharge 2025; Pay year unpinned | chiro PMS | да | |
| Sera Payments | Stax | unpinned | field service | да | ~48h UW |
| Fishbowl Payments | Stax | ~2023 | manufacturing inventory | да | site не печатает Stax |
| Everyware | NMI (+ PNC на одном SKU) | unpinned | healthcare text-to-pay | да | |
| Vori Payments | CardPointe; **+Paysafe с 2025-04** | 2024-01 | grocery POS | да | «Sign My Application» |
| Gingr | CardConnect | unpinned | pet daycare | soft | новый бренд = **Stripe** |
| iDonate | CardPointe (ACH BlueChex) | unpinned | nonprofit | да | |
| Building Stack | Paysafe | case 2025-05 | property PMS | да | CA-founded; US claimed historically |
| Tap2Local | **Moov** via Jack Henry Banno | 2025-08 | bank/CU tap-to-pay | FI-gated | не публичный SaaS |
| Revolv3 | Nuvei **один из** (ещё WP/Adyen/TSYS) | unpinned | subscription orchestration | да | не exclusive |
| CosmoLexPay | LexCharge / ProfitSolv | 2021 | legal | нет | trial → in-app; LawPay тоже option |
| Cal Payments (Cal.com) | **Whop** | 2026 | booking | нет | MoR checkout |
| AutoLeap Payments | Global Payments | unpinned | auto shop | да | не Payrix |
| Club Caddie | CardConnect + Clover Go HW | unpinned | golf club | да | **не Finix, не Clover platform acquiring** |

Stax говорит «150+ partners» — пятого публичного ISV нет.  
NMI FACe — ISO (Canyon, Coastal, ISVPay), не вертикальный SaaS.  
Checkout.com / Elavon TaaS / Priority MX — нового named US SaaS white-label не нашли.

---

## 9. Square / Helcim внутри SaaS (BYO MID, не white-label PayFac)

Мерчант открывает **свой** Square или Helcim.

| Бренд | Рельс | Год (публичный) | Sales |
|---|---|---|---|
| Towbook | Square | 2021-02 | нет (30-day trial) |
| Whoosh | Square | 2024 | да (golf) |
| TicketSocket | Square | unpinned | да (BYO) |
| Trafft | Square | marketplace **2024-09** | нет |
| ARI | Square Terminal **2026-02**; Helcim **2026-05** | нет | auto repair |
| sBizzl | Square cards+ACH | unpinned | нет (30-day) |
| Setmore, Occasion, Appointy, Acuity, Checkfront, Bookeo, vCita | Square | 2017–2021 marketplace | нет |
| Rentrax | Square (+ Stripe/Windcave/Cardknox) | 2021-09 | mixed |
| 360Winery | Square (site также Clover/Global) | 2023-01 | да |
| 3C Connect | Square | unpinned | да (HVAC) |
| SimplyBook.me | Helcim register-in-SBPay; Worldpay BYO credentials | unpinned | нет |
| Booky | Helcim | unpinned | да |
| ZenMaid | Stripe **или** Square BYO | — | нет |

---

## 10. Stripe-only (нашли, но в главный список не клали)

Lemon Squeezy (2021), Fourthwall (2021), Stan Store (2021), Whop (2021, сам платформа), Wix POS (2021), WooPayments (2021), Clio Payments (2021), Skool, Luma, Beacons, GiveLink, Numu POS, Baselane, Squarespace Payments (2023), Kajabi Payments (2023), Practice Better (2023), Polar (2024), Creem (2024), Fungies (2023), FreshBooks Payments (2024), Mercury Invoicing (2024), Calendly Payments (2024), Zoho Payments (2025, ToS Stripe **и** Adyen), Gumroad MoR (2025), Pixieset Payments (2025-04), Stripe Managed Payments (2026), PushPress, Mangomint Pay (2021), TenantCloud / Hemlane / Avail, PayHOA (live Stripe), Lillio Payments (2022), QuoteIQ, Teach 'n Go, TutorCruncher, Mindbody Payments, ChowNow, Digitail, Shepherd Pay (reported), Checkfront Payments (primary Stripe), Gingr Payments (новый бренд), Squire, Infinite Campus (миграция).

---

## 11. Ушли / не клиенты / ловушки

| Имя | Факт |
|---|---|
| Wave | был Finix PayFac infra; US ToS сейчас Adyen + Worldpay + Stripe |
| Lightspeed US | Finix-era 2019 → Stripe Connect 2020-01 |
| Pay Theory | Finix Flex 2022 → Fiserv |
| FieldPulse | Payrix → Rainforest |
| Infinite Campus | Payrix → Stripe |
| fitDEGREE | Payrix case ещё жив; ops 2026 = Payabli |
| PayHOA | в списке Payabli Series A; help = Stripe |
| Club Caddie | Fiserv / CardConnect, не Finix |
| neonpay.com | gaming MoR, не Neon One |
| `*.payments-dashboard.com` | wildcard Finix, **не** доказательство клиента |
| WePay standalone | свёрнут в J.P. Morgan Payments ~2025 |

---

## 12. Исследовали, не подтвердили (не изобретать)

Sublime, Enwoven, Revvable, Abre, Fexco payUnite, Real Green, Resman, PatientPal-as-Tilled, CCStorage (гипотеза в блоге Tilled), Straata (advisor), Fullsteam portfolio ISVs, Checkout.com named US SaaS white-label, Priority/MX named ISV, Elavon Converge new SaaS brand, NMI vertical SaaS frontend, пятый Stax Connect ISV, Finix cannabis EFI slot (без имени), Dutchie/Flowhub/BLAZE на Finix.

---

## 13. Что обычному бизнесу реально открыть без sales

1. Easy, Trailing Paper, Frame, MannyPay, Airwallex, GoDaddy, Paddle, Dodo, Venmo Business, PayPal POS, Coastal SignUp Link  
2. TherapyAppointment → Finix; Omella → Stripe/Finix; Ticketbud → Finix; SpiceApp → Finix  
3. Printavo / JobNimbus → Payrix  
4. Keap / D-Tools / ProLine / Materio / SalesThumb → Rainforest  
5. Roofr → Payabli  
6. ClientTether → Stax  
7. Webconnex (TicketSpice family) → Adyen  
8. Drake / TaxAct Pro → Launchpay  
9. ARI / Trafft / Towbook / SimplyBook → свой Square или Helcim  

---

## 14. Дыры (честно)

| Стек | Публичных имён | Заявлено вендором |
|---|---|---|
| Rainforest | 19 | ~100 |
| Payabli | 12 pay-in | 60–100 |
| Finix | ~23 named (не все в /customers) | «billions» / логостенка короткая |
| Payrix | 22 index + ~6 extra | «40+ platforms» в 2021 PR, большинство без имён |
| JustiFi / Tilled | 3 + 3 | каталога нет |
| Stax Connect | 4 | «150+» |
| Adyen AfP | много кейсов, нет единого каталога SaaS | — |

---

## Источники (сырые отчёты)

`/tmp/payfac-wide/` — FINAL.md, ROUND2-NEW.md, ROUND3-OTHER-PROCESSORS.md, w1–w9, finix-frontends (2024), finix-more.md, finix-deep.md, payrix-clients.md, rainforest-clients.md, payabli-clients.md, tilled-justifi-clients.md, other-processors.md, adyen-stax-nmi-more.md, square-fiserv-more.md  
`/tmp/payfac-2024/` — finix-frontends.md  
`/tmp/payfac-2026/` — FINAL.md (строгий 2025–26 PayFac)

Копия этого файла: `/workspace/.planning/research/payfac-all-findings.md`
