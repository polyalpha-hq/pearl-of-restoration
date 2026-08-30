# US accept-payments — каталог

2026-08-30. Есть ToS / help / press / «powered by». Dual = два процессора.  
Ссылка на бренде — signup, если путь открытый; иначе сайт / демо.

**Критерии (с раунда 12)**

- US-мерчант может принять карты и/или ACH.
- Первый payments SKU **2020–2026**. Год не доказан — можно, если стек/Pay SKU живой. `*` = продукт старше 2020, путь всё равно открытый.
- Процессор из ToS / help / press / sponsoring bank. **`неизвестен` можно**, если first-party не Stripe (свой Pay SKU, «our processing», ISO of bank X, help отделяет от Stripe). Stripe-only — не класть. Dual Stripe+X — класть, если X назван.
- Путь: публичный signup, SaaS-триал, **или sales/демо + любая заявка** (письмо, Gravity/Elavon partner URL, boarding slug). Не обязательно кнопка внутри продукта.

**Что такое «in-app apply»** — это не отдельный тег пути. Это уточнение: заявка на мерчант-аккаунт открывается **из самого продукта** (Settings → Payments → форма KYB). Раньше без такой кнопки бренд выкидывали, даже если сейлз присылал заявку после демо. **Теперь демо + заявка тоже кладём** (тег **демо**). In-app apply — частный случай тегов **заявка** / **триал→заявка**.

**Путь**

| тег | что это |
|---|---|
| **моментально** | открыл аккаунт сам, без демо и без «мы перезвоним» |
| **заявка** | публичная форма KYB / merchant apply, ждут андеррайтинг (на сайте или по ссылке от партнёра) |
| **триал→заявка** | сам завёл SaaS (триал), платежи — отдельная заявка **в продукте** (это и есть in-app apply) |
| **демо** | Book a demo / sales, потом заявка — in-app, email-ссылка или partner apply URL |
| **BYO** | подключает свой Square / Helcim |

**Keyed ACH:** плательщик сам вбивает routing + account. Не Plaid и не депозитный счёт мерчанта. Не staff-keyed в кабинете.  
`да` = есть цитата в help. `?` = ACH есть, форму не описали. `нет` = online ACH не живой / только staff или Plaid. `—` = не проверяли.

---

## Всё в одной таблице

| Бренд | Процессор | Год | Вертикаль | Путь | Keyed ACH |
|---|---|---|---|---|---|
| [Easy](https://app.itseasy.co/signup) | Finix | 2025-01 | любой SMB | **моментально** | — |
| [Trailing Paper](https://trailingpaper.com/register) | Finix | 2026-04 | invoicing | **моментально** | — |
| [Venmo Business](https://venmo.com) | PayPal | 2021-02 | любой SMB | **моментально** | — |
| [GoDaddy Payments](https://www.godaddy.com/payments) | Elavon / Adyen / Nuvei | 2021-06 | любой SMB | **моментально** | — |
| [PayPal Zettle / POS](https://www.paypal.com/us/business/pos-system) | PayPal | 2021-06 | любой SMB | **моментально** | — |
| [Paddle](https://login.paddle.com/signup) | Paddle | 2022 | софт | **моментально** | — |
| [Dodo Payments](https://app.dodopayments.com/signup) | own MoR | 2024 | софт | **моментально** | — |
| [Airwallex US](https://www.airwallex.com/us/signup) | Airwallex / JPM | 2024-04 | любой SMB | **моментально** | — |
| [Coastal SignUp Link](https://www.signuplink.ai/register) | Fiserv / TSYS / Elavon | 2026-04 | любой SMB | **моментально** | — |
| [Omella](https://omella.com/signup) | Finix + Stripe | 2026-06 | K-12 / PTA / SMB | **моментально** | — |
| [CharityStack](https://charitystack.com/) | Finix + Stripe | ~2023 | nonprofit | **моментально** | — |
| [TicketSpice](https://signup.ticketspice.com/) | Adyen | — | event tickets | **моментально** | — |
| [GivingFuel](https://signup.givingfuel.com/) | Adyen | — | nonprofit | **моментально** | — |
| [RegFox](https://www.regfox.com/) | Adyen | — | event registration | **моментально** | — |
| [RedPodium](https://www.redpodium.com/) | Adyen | — | race registration | **моментально** | — |
| [GroupRev](https://grouprev.com/) | Adyen | — | fundraising | **моментально** | — |
| [Innago](https://auth.innago.com/signup) | Payload | — | rent / landlords | **моментально** | ? |
| [Cal Payments](https://app.cal.com/signup) | Whop | 2026 | booking | **моментально** | — |
| [8am LawPay](https://www.lawpay.com/) | Adyen | 2007* | legal | **моментально** | — |
| [8am CPACharge](https://www.cpacharge.com/sign-up/) | Adyen | 2016* | accounting | **моментально** | — |
| [8am ClientPay](https://www.clientpay.com/) | Adyen / 8am | 2021-02 | pro services | **моментально** | — |
| [Frame](https://app.framepayments.com/register) | CBC (front unnamed) | ~2024 | любой SMB | **заявка** | — |
| [MannyPay](https://www.mannypay.io/merchant-sign-up) | Adyen / iMerchant | 2026-07 | любой SMB | **заявка** | — |
| [Relay](https://app.relayfi.com/register) | Adyen (карты); ACH = Plaid | 2025-06 | SMB banking / invoices | **заявка** | нет |
| [TherapyAppointment](https://www.therapyappointment.com/sign-up) | Finix | 2025-11 | mental-health EMR | **триал→заявка** | — |
| [Ticketbud Payments](https://ticketbud.com/users/sign_up) | Finix | 2024-10 | events | **триал→заявка** | — |
| [SpiceApp POS Lite](https://myspiceapp.com/products/pos-lite/) | Finix | 2022 | restaurant POS | **триал→заявка** | — |
| [Contractor+ Pay](https://contractorplus.app/) | Finix | 2024 | field service | **триал→заявка** | ? |
| [Candid Pay](https://www.candidwholesale.com/) | Finix | 2024 | dental wholesale | **триал→заявка** | — |
| [Lunchbox Payments](https://lunchbox.io/essential) | Finix | 2023-10 | restaurants | **триал→заявка** | ? |
| [Shopmonkey](https://www.shopmonkey.io/) | Finix + Stripe | — | auto repair | **триал→заявка** | — |
| [Printavo](https://www.printavo.com/users/sign_up) | Payrix | 2022 | print shops | **триал→заявка** | — |
| [JobNimbus Payments](https://www.jobnimbus.com/trial-signup/) | Payrix | — | contractors | **триал→заявка** | — |
| [Xoda](https://xoda.com/create-account) | Payrix | — | fitness | **триал→заявка** | — |
| [GymMaster](https://www.gymmaster.com/us/gym-software/) | Payrix | — | gym | **триал→заявка** | — |
| [D-Tools Payments](https://www.d-tools.com/cloud-free-trial) | Rainforest | 2024-08 | AV | **триал→заявка** | ? |
| [ProLine Payments](https://new.proline.app) | Rainforest | 2023–24 | roofing | **триал→заявка** | ? |
| [MaterioPay](https://www.materio.co/signup) | Rainforest | 2024 | materials | **триал→заявка** | **да** |
| [Keap Pay](https://keap.com/free-trial) | Rainforest | 2024-04 | CRM | **триал→заявка** | ? |
| [SalesThumb](https://salesthumb.com) | Rainforest | — | sales | **триал→заявка** | нет |
| [Roofr Payments](https://app.roofr.com/register) | Payabli | 2024-01 | roofing | **триал→заявка** | — |
| [TetherPay / ClientTether](https://clienttether.com/) | Stax | 2022-01 | franchise CRM | **триал→заявка** | — |
| [CosmoLexPay](https://www.cosmolex.com/) | LexCharge | 2021 | legal | **триал→заявка** | — |
| [Drake Pay](https://www.drakesoftware.com/products/drake-pay/) | Launchpay | 2024-01 | tax | **триал→заявка** | — |
| [TaxAct Pro Payments](https://www.taxact.com/professional/integrated-payments) | Launchpay | — | tax | **триал→заявка** | — |
| [Workiz Pay](https://www.workiz.com/signup/join-workiz/) | Adyen + Stripe | ~2025 US Adyen | field service | **триал→заявка** | ? |
| [Act! Payments](https://www.act.com/products/accept-payments/) | Propelr | 2026-04 | CRM | **триал→заявка** | ? |
| [Encyro Invoicing](https://www.encyro.com/invoicing) | Helcim | 2025-11 | invoicing | **триал→заявка** | ? |
| [InvoiceSherpa](https://www.invoicesherpa.com/pricing) | Propelr (preferred) + BYO | 2026-04 | invoicing / AR | **триал→заявка** | ? |
| [StarPay / StarChapter](https://www.starchapter.com/StarPay) | Fullsteam | 2020-10 | associations | **триал→заявка** | нет |
| [TimeSolv + LexCharge](https://www.timesolv.com/timesolvpay) | LexCharge | 2020-11 | legal | **триал→заявка** | ? |
| [PantherPayments / PracticePanther](https://www.practicepanther.com/pantherpayments) | неизвестен (не Stripe; Headnote 2020) | 2020-09 | legal | **триал→заявка** | ? |
| [Fresha Payments](https://www.fresha.com/) | Adyen | ~2020 | beauty / salon | **триал→заявка** | — |
| [ThryvPay](https://www.thryv.com/) | неизвестен (не Stripe; help отделяет от Stripe/Square/PayPal) | 2020-10 | SMB services | **триал→заявка** | ? |
| [EnrollwarePay](https://www.enrollwaresolutions.com/enrollwarepay) | Fullsteam | * | training / class | **триал→заявка** | — |
| [Tabs3Pay](https://support.tabs3.com/main/r11871.htm) | Stax | 2021 | legal | **триал→заявка** | нет |
| [Vagaro Merchant Services](https://www.vagaro.com/pro/card-processing) | неизвестен (ISO of PNC; не Stripe) | * | salon / spa | **триал→заявка** | — |
| [shopVOX Pay](https://shopvox.com/) | Fullsteam | 2025 | print / sign / apparel | **триал→заявка** | ? |
| [BILL Receivables](https://www.bill.com/signup) | Adyen | 2024-02 | invoicing / AR | **триал→заявка** | **да** |
| [Haulvana](https://www.haulvana.com/pricing) | Xplor Pay | 2025-11 | waste | **триал→заявка** | ? |
| [MyKidReports](https://app.mykidreports.com/signup) | Deluxe + Stripe | 2025-07 | childcare | **триал→заявка** | ? |
| [Recur360Pay](https://www.recur360.com/payment-processing/) | Fullsteam | 2023-06 | invoicing / AR | **триал→заявка** | ? |
| [Automaid Pay](https://www.launch27.com/) | Fullsteam | 2025 | cleaning / maid | **триал→заявка** | ? |
| [Brokerage Engine](https://www.brokerageengine.com/) | Payload | 2023-06 | real estate back-office | **заявка** | ? |
| [SkySlope Keybox](https://www.skyslope.com/) | Payload | 2022 | real estate / EMD | **заявка** | ? |
| [Towbook](https://towbook.com/) | Square | 2021-02 | towing | **BYO** | — |
| [Trafft](https://trafft.com/) | Square | 2024-09 | booking | **BYO** | — |
| [ARI](https://ari.app/) | Square / Helcim | 2026 | auto repair | **BYO** | — |
| [sBizzl](https://sbizzl.com/) | Square | — | booking | **BYO** | — |
| [SimplyBook.me](https://simplybook.me/) | Helcim | — | booking | **BYO** | — |
| [Knowify](https://knowify.com/construction-payment-processing/) | Square / QBO Payments | — | contractors | **BYO** | ? |
| [GorillaDesk](https://gorilladesk.com/features/credit-card-processing/) | Square + Stripe | — | pest / lawn | **BYO** | нет |
| [Meadow Pay](https://www.meadowfi.com/pay) | Finix | 2024–25 | higher ed | **демо** | — |
| [Archy](https://archy.com) | Finix | — | dental PMS | **демо** | — |
| [X-CD Payments](https://www.x-cd.com/payments-3/) | Finix | 2026-01 | associations | **демо** | — |
| [Vroom Pay360](https://www.vroomdelivery.tech/demo) | Finix | 2024-04 | c-store | **демо** | — |
| [T2 Systems](https://www.t2systems.com/) | Finix / Auth.net | 2023-03 | parking | **демо** | — |
| [foreUP Payments 2.0](https://foreupgolf.com/get-a-demo/) | Finix | 2022-11 | golf | **демо** | — |
| [Clubessential](https://www.clubessential.com/) | Finix (press) | pre-2024 | clubs | **демо** | — |
| [Cargas Pay](https://www.cargas.com/) | Finix (press) | 2022-08 | fuel / HVAC | **демо** | — |
| [Passport](https://www.passportinc.com/) | Finix (case) | 2019* | parking | **демо** | — |
| [AgVend](https://www.agvend.com/) | Finix (case) | 2022–23 | ag retail | **демо** | — |
| [Beyond / Tally](https://beyondpricing.com/) | Finix (case) | 2023-08 | STR | **демо** | — |
| [Caterease HPay](https://www.caterease.com/) | Payrix | — | catering | **демо** | — |
| [Horizon Cloud](https://www.horizoncloud.com/) | Payrix | — | hospitality | **демо** | — |
| [Storable](https://www.storable.com/) | Payrix | — | self-storage | **демо** | — |
| [FieldRoutes](https://www.fieldroutes.com/) | Payrix | — | field service | **демо** | — |
| [Neon Pay](https://neonone.com/solutions/neon-pay/) | Payrix | — | nonprofit CRM | **демо** | — |
| [Kangarootime](https://www.kangarootime.com/) | Payrix | ~2020 | childcare | **демо** | — |
| [Eyefinity](https://www.eyefinity.com/) | WP referral | — | optometry | **демо** | — |
| [Runit](https://www.runit.com/) | WP referral | — | luxury POS | **демо** | — |
| [CryptoPay](https://www.getcryptopay.com/) | WP referral | — | laundry OEM | **демо** | — |
| [Boost](https://www.boostb2b.com/) | WP PayFac | — | B2B AP | **демо** | — |
| [PIREL](https://www.pirel.com/) | Payrix | — | docs / AP-AR | **демо** | — |
| [2TouchPOS](https://www.2touchpos.com/) | Payrix | с 2005 | restaurant POS | **демо** | — |
| [New West](https://www.newestech.com/) | WP referral | — | retail POS | **демо** | — |
| [ReyPAY](https://www.reyrey.com/) | WP referral | ~2020 | dealers | **демо** | — |
| [SimplySwim](https://www.simplyswim.com.au/) | Payrix AU | — | swim | **демо** | — |
| [SimpleRent](https://go.simplerent.com.au/) | Payrix AU | — | property | **демо** | — |
| [HubHello](https://www.hubhello.com.au/) | Payrix AU | — | childcare | **демо** | — |
| [Perfect Gym](https://www.perfectgym.com/) | Payrix AU | — | gym | **демо** | — |
| [iClassPro](https://www.iclasspro.com/payment-services) | Worldpay + Payrix | 2015* | youth class | **демо** | — |
| [DocketPay](https://www.yourdocket.com/) | Payrix | — | waste | **демо** | — |
| [Splynx](https://splynx.com/) | BYO Payrix | — | ISP | **демо** | — |
| [Hint Payments](https://www.hint.com/get-started) | Rainforest | — | chiro / DPC | **демо** | **да** |
| [PayGround](https://www.payground.com/) | Rainforest | — | patient pay | **демо** | **да** |
| [RoadSync Checkout](https://www.roadsync.com/) | Rainforest | — | trucking | **демо** | ? |
| [QuoteMachine](https://www.quotemachine.com/) | Rainforest | — | quotes | **демо** | ? |
| [Duesy](https://www.meetduesy.com/) | Rainforest | — | associations | **демо** | ? |
| [FieldPulse](https://www.fieldpulse.com/) | Rainforest (был Payrix) | ~2025 | field service | **демо** | ? |
| [Decoda Health](https://www.decodahealth.com/) | Rainforest | 2024-10 | healthcare | **демо** | **да** |
| [Crystal PM](https://www.crystalpm.com/payments/) | Rainforest | — | dental / chiro | **демо** | ? |
| [Handoff](https://www.handoff.ai/trials) | Rainforest | — | construction | **демо** | ? |
| [CivicPlus](https://www.civicplus.com/) | Rainforest | — | gov | **демо** | **да** |
| [Newton](https://joinnewton.com/book-a-demo) | Rainforest | — | — | **демо** | ? |
| [Rose Rocket](https://www.roserocket.com/) | Rainforest | — | freight | **демо** | ? |
| [Curae](https://curae.com/) | Rainforest | — | patient finance | **демо** | ? |
| [Albiware](https://albiware.com/albipay/) | Rainforest | — | restoration | **демо** | **да** |
| [BuildOps](https://buildops.com/) | Payabli | — | construction | **демо** | — |
| [Builder Prime](https://www.builderprime.com/payments) | Payabli | 2021 | construction | **демо** | — |
| [CurbWaste](https://www.curbwaste.com/) | Payabli / PayEngine | — | waste | **демо** | — |
| [fitDEGREE](https://www.fitdegree.com/) | Payabli (был Payrix) | — | fitness | **демо** | — |
| [Cubby](https://www.cubbystorage.com/) | Payabli + Stripe | — | self-storage | **демо** | — |
| [ExactEstate](https://www.exactestate.com/) | Payabli | 2024-11 | property | **демо** | — |
| [Sunbound](https://www.sunbound.ai/) | Payabli | — | collections | **демо** | — |
| [ID Tenant](https://www.idplans.com/idtenant/) | Payabli | 2026-07 | CRE | **демо** | — |
| [Fyxt](https://fyxt.com/try/) | Payabli | 2025 | CRE | **демо** | — |
| [Leap / LeapPay](https://leaptodigital.com/) | JustiFi | 2024 | roofing CRM | **демо** | — |
| [LASSO Payments](https://www.lasso.io/) | JustiFi | 2025 | events | **демо** | — |
| [Projul](https://projul.com/) | JustiFi | — | construction | **демо** | — |
| [ResortCleaning](https://www.resortcleaning.com/) | Tilled | 2022-01 | vacation cleaning | **демо** | — |
| [LaunchPad](https://golaunchpad.com/) | Tilled | — | youth | **демо** | — |
| [Bambi](https://www.hibambi.com/) | Tilled | — | NEMT | **демо** | — |
| [TapGoods](https://www.tapgoods.com/pro/payment-processing/) | Launchpay | 2023 | event rental | **демо** | — |
| [WorkWave Payments](https://www.workwave.com/fintech) | Payops | — | field service | **демо** | — |
| [Epos Now US](https://www.eposnow.com/) | Adyen | 2023 | retail POS | **демо** | — |
| [Olo Pay CP](https://www.olo.com/) | Adyen | 2023 | restaurants | **демо** | — |
| [Jackrabbit Pay](https://www.jackrabbitpay.com/) | Adyen | 2023 | youth class | **демо** | — |
| [RMS Pay US/CA](https://www.rmscloud.com/features/hospitality-payment-solutions) | Adyen | 2025-08 | hotel PMS | **демо** | — |
| [Oracle Payments](https://www.oracle.com/payments/) | Adyen | 2022-06 | restaurant / hotel | **демо** | — |
| [Tessitura MS](https://www.tessitura.com/Features/Payment-Processing) | Adyen | 2022-03 | arts | **демо** | — |
| [ITX Payments](https://www.intellitix.com/) | Adyen | 2024 | live events | **демо** | — |
| [Konnect Payments](https://www.connectngo.com/) | Adyen | 2022–23 | parks | **демо** | — |
| [Klipboard Money](https://www.klipboard.com/en-us/solutions/payment/klipboard-money) | Adyen? | 2026-02 | ERP | **демо** | — |
| [Mews Payments](https://www.mews.com/) | Adyen (+ Stripe) | 2026-07 | hotel PMS | **демо** | — |
| [Slice](https://www.slicelife.com/) | Adyen | — | pizza | **демо** | — |
| [ChiroSpring Pay](https://www.chirospring.com/) | Stax | — | chiro | **демо** | — |
| [Sera Payments](https://sera.tech/) | Stax | — | field service | **демо** | — |
| [Fishbowl Payments](https://www.fishbowlinventory.com/) | Stax | ~2023 | manufacturing | **демо** | — |
| [Everyware](https://www.everyware.com/) | NMI | — | healthcare SMS | **демо** | — |
| [Vori Payments](https://www.vori.com/) | CardPointe + Paysafe | 2024-01 | grocery | **демо** | — |
| [Gingr](https://www.gingrapp.com/) | CardConnect → Stripe | — | pet daycare | **демо** | — |
| [iDonate](https://www.idonate.com/) | CardPointe | — | nonprofit | **демо** | — |
| [Building Stack](https://www.buildingstack.com/) | Paysafe | — | property | **демо** | — |
| [Tap2Local](https://www.jackhenry.com/press-release/jack-henry-launches-tap2local-seamless-digital-payments) | Moov / Jack Henry | 2025-08 | банк / КУ | **демо** | — |
| [Revolv3](https://www.revolv3.com/) | Nuvei + others | — | subscriptions | **демо** | — |
| [AutoLeap](https://autoleap.com/) | Global Payments | — | auto shop | **демо** | — |
| [Club Caddie](https://clubcaddie.com/) | CardConnect | — | golf club | **демо** | — |
| [Whoosh](https://www.whoosh.io/public-golf-operations) | Square | 2024 | golf | **демо** + BYO | — |
| [TicketSocket](https://www.ticketsocket.com/) | Square | — | box office | **демо** + BYO | — |
| [360Winery](https://www.360winery.com/) | Square | 2023-01 | winery | **демо** + BYO | — |
| [3C Connect](https://3cconnect.com/book-demo/) | Square | — | HVAC | **демо** + BYO | — |
| [Booky](https://www.booky.ca/) | Helcim | — | booking | **демо** + BYO | — |
| [MyCase](https://www.mycase.com/) | LawPay / Adyen | 2025 | legal | **демо** | — |
| [Buildertrend Payments](https://buildertrend.com/financial-tools/payments/) | Adyen | 2023-02 | construction | **демо** | ? |
| [ServiceTitan Payments](https://www.servicetitan.com/) | Adyen (+ NMI/TSYS; ACH ProfitStars) | — | field service | **демо** | ? |
| [SingleOps Payments](https://www.singleops.com/) | ProPay / Global Payments | — | landscape | **демо** | ? |
| [Confido Legal](https://confidolegal.com/) | Gravity Payments | 2023-12* | legal / IOLTA | **демо** | ? |
| [BillingPlatform BP Pay](https://billingplatform.com/solutions/portal/payments/bp-pay) | Adyen | 2025-03 | enterprise billing | **демо** | ? |
| [improveit 360 Payments](https://www.improveit360.com/features/) | PaySimple | — | remodeling CRM | **демо** | ? |
| [Successware Payments](https://www.successware.com/features/the-new-successware-platform/successware-payments/) | Stax | 2022-01 | HVAC | **демо** | ? |
| [FieldEdge Payments](https://fieldedge.com/fe-payments/) | Xplor Pay | 2022-02 | HVAC | **демо** | нет |
| [Service Autopilot Payments](https://www.serviceautopilot.com/credit-card-processing/) | Xplor Pay | — | pest / lawn / cleaning | **демо** | **да** |
| [Flex Payments](https://www.flexrentalsolutions.com/flex-payments/) | PayEngine | 2024-11 | event rental | **демо** | ? |
| [improviPay](https://improvifi.com/technology/) | Xplor Pay | 2026-05 | home improvement | **демо** | ? |
| [Dental Intelligence Payments](https://www.dentalintel.com/) | Xplor Pay | 2023-07 | dental | **демо** | нет |
| [SmartMoving](https://www.smartmoving.com/) | Remedy | — | moving | **демо** | **да** |
| [Prophet Pay](https://www.clubprophet.com/products/prophetpay) | Fullsteam | — | golf POS | **демо** | нет |
| [SC Pay](https://www.storagecommander.com/merchant-processing) | Fullsteam | — | self-storage | **демо** | нет |
| [Roc Services](https://payroc.com/solutions/roc-services/) | Payroc | 2024-07 | field invoicing | **демо** | ? |
| [DrivePay](https://driveshops.com/) | Propelr + FreedomPay | 2026-03 | auto shop ERP | **демо** | ? |
| [Cerbo](https://cer.bo/) | Propelr / CardPointe | — | cash-pay clinic | **демо** | ? |
| [WebRezPay](https://webrezpro.com/payments/) | Fullsteam | — | lodging PMS | **демо** | нет |
| [FieldServio](https://fieldservio.com/) | Payroc | 2024 | field service ERP | **демо** | ? |
| [Visual Matrix Fortis Pay](https://visualmatrix.com/fortis/) | Fortis | 2023-08 | hotel PMS | **демо** | нет |
| [CareStack CS Pay](https://carestack.com/dental-software/cspay) | Adyen | — | dental | **демо** | ? |
| [Lever360](https://www.lever360.com/) | Propelr + Stripe | 2026-04 | restoration | **демо** | ? |
| [vinSUITE](https://www.vinsuite.com/) | Propelr | 2026-07 | winery DTC | **демо** | ? |
| [Atrium Campus](https://atriumcampus.com/) | Propelr | 2026-07 | campus card | **демо** | ? |
| [Commerce7 Fullsteam Payments](https://www.commerce7.com/c7-payments/) | Fullsteam (+ Stripe wallets) | 2021-09 | winery | **демо** | ? |
| [RICS Pay](https://www.ricssoftware.com/rics-pay/) | Fullsteam | 2021-01 | footwear / apparel POS | **демо** | нет |
| [Silverware Pay](https://www.silverwarepos.com/silverware-pay) | Fullsteam | 2024-06 | hospitality POS | **демо** | нет |
| [MezzoPay](https://www.maestropms.com/) | Fullsteam | 2024-04 | hotel PMS | **демо** | нет |
| [UrPay](https://urable.com/urpay/) | Fullsteam (Worldpay / Fifth Third) | 2025 | detailing / PPF | **демо** | ? |
| [GROUND PAY](https://fasttrakcloud.com/groundpay/) | Fullsteam | 2026 | limo / ground | **демо** | нет |
| [Winworks Pay](https://winworks.com/pay/) | Fullsteam | 2021 | auto shop | **демо** | нет |
| [Limo Anywhere Pay](https://www.limoanywhere.com/pay/) | Fullsteam | 2022 | limo / black car | **демо** | **да** |
| [Arryved Pay](https://arryved.com/products/arryved-pay/) | Fullsteam | 2024-06 | brewery / taproom POS | **демо** | нет |
| [Canopy Payments](https://www.getcanopy.com/) | Adyen | 2022-01 | tax / accounting PMS | **демо** | ? |
| [Stayntouch Pay](https://www.stayntouch.com/stayntouch-pay/) | Adyen | 2022-10 | hotel PMS | **демо** | ? |
| [Print Reach Pay](https://printreach.com/how-print-reach-pay-can-transform-your-print-shop/) | Fullsteam | 2021-03 | print / mail MIS | **демо** | ? |
| [RaccoonPay / RoomRaccoon](https://roomraccoon.com/) | Adyen | 2023-03 | hotel HMS | **демо** | ? |
| [EZClaimPay](https://ezclaim.com/ezclaimpay/) | Fullsteam | 2020-08 | medical billing | **демо** | — |
| [Flybook Pay](https://info.theflybook.com/flybook-pay-powered-by-fullsteam) | Fullsteam | 2020-01 | marina / yacht | **демо** | ? |
| [ROLLER Payments](https://www.roller.software/) | Adyen | 2020 | attractions | **демо** | — |
| [Zenoti Payments](https://www.zenoti.com/) | Adyen | ~2020 | spa / salon | **демо** | — |
| [Provet Pay](https://www.provet.com/product/provet-pay) | Adyen | — | vet | **демо** | — |
| [DockMaster Payments / ValPay](https://portal.dockmaster.com/docs/category/dockmaster-payments/) | Adyen (ValPay) | — | marina | **демо** | — |
| [Pushpay Giving](https://pushpay.com/) | Fiserv / First Data + CheckCommerce (Nuvei) | * | church / giving | **демо** | ? |
| [BridalLive Pay](https://www.bridallive.com/merchant-services-for-us-residents) | Fullsteam | — | bridal retail | **демо** | — |
| [ConsignCloud](https://consigncloud.com/integrations/gravity-payments) | Gravity Payments | — | consignment | **демо** | — |
| [FROG + Gravity](https://gravitypayments.com/partner/frog/) | Gravity Payments | 2022-12 | furniture retail | **демо** | — |
| [Lizzy + Gravity](https://gravitypayments.com/lp/lizzy/) | Gravity Payments | — | auto dealers | **демо** | — |
| [Smart Storage Software](https://smartstoragesoftware.com/features/integrations) | Fortis | * | self-storage | **демо** | ? |
| [Supermove Payments](https://www.supermove.com/) | PayEngine | * | moving | **демо** | нет |
| [SylogistPay](https://www.nuvei.com/posts/sylogist-selects-nuvei-to-upgrade-its-payments-solution) | Nuvei / Paya | 2023-06 | nonprofit / gov / edu | **демо** | — |
| [UPay360](https://360s2g.com/upay360-elavon-partnership-revolutionizes-payments/) | Elavon | — | utility / gov | **демо** | ? |
| [Vetspire Pay](https://www.vetspire.com/) | CardConnect + Stripe + Square + Worldpay | * | vet | **демо** | — |
| [Bay-Master BM Pay](https://www.bay-master.com/bay-master-plus-features/) | неизвестен (Fullsteam-owned; first-party rail не назван) | * | auto / marine service | **демо** | — |

`*` продукт payments старше 2020, путь всё равно открытый.

**Keyed ACH да** (плательщик вводит routing+account): Hint, PayGround, MaterioPay, Decoda Health, CivicPlus, Albi Pay, Service Autopilot, SmartMoving, Limo Anywhere Pay, BILL Receivables.  
**нет:** SalesThumb; Relay (Plaid); FieldEdge / Dental Intel / Prophet Pay / SC Pay / WebRezPay / Fortis Pay / RICS Pay / Silverware Pay / MezzoPay / GROUND PAY / Winworks Pay / Arryved Pay (нет payer ACH формы); Tabs3Pay (staff вбивает client bank, не payer); StarPay (карты); Supermove (ACH только record).  
**?:** ACH в тарифах есть, форму не разобрали. Lunchbox (help = eChecks); Contractor+ (сайт = Card & ACH; форму payer не разобрали).

**Раунд 5 (2026-08-30):** Successware, FieldEdge, Service Autopilot, Flex, improviPay, Dental Intel, SmartMoving, Prophet Pay, SC Pay, Roc Services, Act!, Encyro, DrivePay, Cerbo, WebRezPay, FieldServio, Visual Matrix Fortis Pay, CareStack CS Pay.  
Не клали: MarketSharp / Profit Rhino / MSI (PaySimple ~2018), Spot (Xplor, CC с 1996), ezyVet+PayJunction (2017), Goose (Adyen Capital).

**Раунд 6 (2026-08-30):** InvoiceSherpa, Lever360, vinSUITE, Atrium Campus, Commerce7 Fullsteam, RICS Pay.  
Не клали: Field2Base (sales callback), KORONA (agnostic referral), Party Center / ERS / RoomKey Pay (2019), LW Pay (expense/payouts), Jobber / Housecall Pro (Stripe-only), Toast+Adyen US (не новый merchant SKU).

**Раунд 7 (2026-08-30):** shopVOX Pay, Silverware Pay, MezzoPay, UrPay, GROUND PAY.  
Не клали: Maxanet / Pluss / ISI (payments ~2019), RMH+Sola (preferred plugin среди нескольких), CounselEAR (нет публичного Pay SKU), Helcim Payment Extension (это сам Helcim, до 2021).

**Раунд 8 (2026-08-30):** Winworks Pay, Limo Anywhere Pay, Arryved Pay.  
Не клали: WineDirect (тот же Fullsteam Payments, что Commerce7), StarPay (Oct 2020), EZClaimPay (Aug 2020), Coolfront Payments (2018 / теперь FieldEdge), Compassmax (слит в SPOT, CC с 1996), DRSPay (тот же ERSPay-стек 2018; help даже пишет ERSPay Reports), Eye Cloud Pro (Fullsteam есть, first SKU до окна), Integrapark (нет named Pay SKU; сайт всё ещё «variety of settlement agents»), Livery Coach / GroundSpan (нет named Fullsteam Pay; Livery публично PayPal/Moneris), Bay-Master BM Pay (Fullsteam владеет; процессор на публичных страницах не назван; год first SKU не доказан), Aluvii/Pangea/AbanteCart/B2B Wave/Holland/Paynow+Sola (gateway / preferred, не exclusive in-app apply), Aesthetic Record (AR Pay = Stripe; Clearent VT legacy), Stax Connect (новых named ISV нет кроме уже в таблице), NMI white-label SaaS frontend (новых named нет кроме Everyware).

**Раунд 9 (2026-08-30) — acquirer/ISO hunt:** BILL Receivables (Adyen acquiring 2024-02; payment-link test form = routing+account).  
Не клали: Atlas (SG), Toast/Roller/Crisp/Wix Payments (SKU до 2021 или уже out), Vagaro (Adyen = CashOut payouts; карты = ISO of PNC, процессор не назван), Rectangle Health PayerSync (insurance reimbursements), Goose (Capital), Etsy/eBay/GoFundMe (marketplace / до окна), Sharetribe (Stripe out of box; Adyen DIY), Moneybird (не US), HotelKey (Paysafe press 2022; сайт = BYO Shift4/FreedomPay/Elavon), Sylogist/Promise (Nuvei/Paya enterprise demo), Tebex/FastSpring (gaming / MoR до 2021), UPay360 (Elavon WorksWith, gov sales), Genius POS 2025 (owned POS, sales), Taplist/7shifts (Genius data sync, не accept), Ovvi (Priority resells POS), MX Merchant (sales form), ConsignCloud/Lizzy/FROG (Gravity sales apply, не in-product), TimeSolv+LexCharge (in-app apply, Nov 2020), Tabs3Pay (2021 in-app + keyed ACH, процессор на публичных страницах не назван; LexCharge отдельно), Rocket Matter Pay (PayPal/Venmo; LexCharge не доказан), 8am AffiniPay/MedPay (SKU до 2021 / нет публичного apply), FreshBooks WePay (в каталоге Stripe-only; SKU старый), Jack Henry Rapid Transfers (Moov A2A, не accept), Payarc/PaymentCloud/CDG/Dharma/Easy Pay Direct/Signature Payments (ISO до окна / sales), Fiserv ISV merchant-signup (lead form).

**Раунд 10 (2026-08-30) — vertical hunt:** Haulvana (Xplor Pay, press 2025-11; Kickstart free + Get Started), MyKidReports (Deluxe ACH + Stripe cards, blog 2025-07; `app.mykidreports.com/signup`), Canopy Payments (Adyen, help + 2022-01 feature post; in-app enroll after demo).  
Не клали: Tithe.ly / Planning Center / ChurchTrac / Breeze (Stripe); Vantaca Pay (ToS = Stripe); Smartwebs (Payabli payouts, уже out); Ministry Brands + AvidXchange (AP); Connect Childcare / Tapestry (UK Unipaas); PestPac / RealGreen (WorkWave Payments, first SKU 2019 — ALREADY WorkWave); FieldRoutes (ALREADY Payrix); LMN Pay / LawnPro / Digitail / Tekion Pay / TaxDome Payments (Stripe-only); ezyVet+PayJunction (2017); DaySmart+CardConnect (2017); IDEXX Payments (Fiserv rebrand of Neo/CardConnect, SKU до окна); CCC+Xplor («6+ years», до окна); PantherPayments/Headnote (2020); Shepherd Pay / Provet Pay / Bittsi / AMCS Pay / UnitFull / Pushpay (процессор на first-party не назван); Vetspire Pay (CardConnect+Stripe+Square+Worldpay; год first SKU не доказан; sales); Supermove Payments (glossary = Payengine; activate = sales; год не доказан; ACH только record); Smart Storage Software (Fortis named; год first SKU не доказан; quote/demo); CCStorage / iSmart (Full Stack Payments / Coastal ISO; underlying acquirer не назван); Routeware+Worldpay (sales AE; first SKU year не доказан); VWS PurGo+Elavon (UK, не US); Product Hunt 2024–26 payments (Fungies MoR / PaymentKit orchestration / UniwebPay — не vertical SaaS merchant embed).

**Раунд 11 (2026-08-30) — план + Fullsteam/Payload/Adyen leftovers:** Recur360Pay (Fullsteam, notice 2023-06; trial + in-app «Sign up for RECUR360PAY»), Automaid Pay / Launch27 (Fullsteam boarding `boarding.fullsteampay.net/AutoMaid`, help 2025-05), Brokerage Engine (Payload, ALTA 2023-06, in-app activate), SkySlope Keybox (Payload EMD, 2022), Stayntouch Pay (Adyen, Stayntouch 2.0 press 2022-10), Print Reach Pay (Fullsteam, Midnight 7.0.0 2021-03), RaccoonPay (Adyen, NA launch 2023-03; in-PMS onboarding).  
Не клали: Flybook Pay (Fullsteam contactless **2020-01**), WineDirect Classic (тот же Fullsteam Payments, что Commerce7), BridalLive Pay (sales@ email, не in-app), Cloudbeds Payments (US primarily Stripe Connect; Adyen ToS есть, но Stripe case study), Little Hotelier / SiteMinder (Stripe с 2015/2025 Terminal), AmenitizPay (Stripe Connect), EnrollwarePay (год first SKU не доказан), RosyPay (старше окна), StarPay (2020), PaymentCloud / CDG / Flagship / Anedot / Stax Pay self-reg (ISO/PayFac до окна / горизонтальный signup как Square), Payzli / Payarc / Bankful (partner/agent apps, не merchant self-serve), NexHealth (Stripe), Tekmetric (Stripe), PracticePanther PantherPayments (2020 / AffiniPay).

**Раунд 12 (2026-08-30) — окно 2020+, неизвестен OK если не Stripe, демо+заявка OK:** StarPay, EZClaimPay, Flybook Pay, TimeSolv+LexCharge, PantherPayments, Fresha / ROLLER / Zenoti (с appendix в главную), ThryvPay, EnrollwarePay, Tabs3Pay (Stax), Vagaro (ISO of PNC), Pushpay (Fiserv+CheckCommerce), BridalLive, ConsignCloud / FROG / Lizzy (Gravity partner apply), Smart Storage (Fortis), Supermove (PayEngine), SylogistPay (Nuvei 2023), UPay360 (Elavon), Vetspire Pay (CardConnect+…), Bay-Master BM Pay (Fullsteam-owned, rail не назван), Provet Pay (Adyen в ToS), DockMaster / ValPay (Adyen whitelist). ISO с живой заявкой — секция ниже (+ Payment Depot = Stax ISO).  
Не клали: Shepherd Pay (сторонний блог пишет Stripe; first-party молчит — строго без Stripe); WineDirect (= Commerce7 Fullsteam); RoomKeyPAYMENTS (Fullsteam, first SKU ~2019, тот же стек что уже покрыт); Cloudbeds US (Stripe Connect primary); Little Hotelier / SiteMinder / AmenitizPay / NexHealth / Tekmetric / Jobber / Housecall (Stripe-only); Payzli / Payarc / Bankful (agent CRM); RosyPay / Coolfront 2018 / SPOT 1996 / DRSPay=ERS 2018 / Eye Cloud Pro (первый SKU до 2020 без нового SKU); HotelKey (BYO Shift4/FreedomPay/Elavon); Routeware+Worldpay (нет first-party Pay SKU URL).

**Раунд 13 (2026-08-30) — целенаправленно Finix:** `/customers` выжат (Change payouts, Contractor+, Meadow, AgVend, Beyond, Pay Theory, Passport; Archy/Vroom — отдельные story URL). Press boilerplate = Clubessential / Passport / Lunchbox / Cargas. First-party help: Lunchbox Payments (Finix) onboarding + eCheck; TherapyAppointment Finix Dashboard; Ticketbud Payments press; Omella ToS = Stripe **и** Finix; Contractor+ Pay = Card & ACH.  
Новых named ISV с first-party/press не нашли.  
Не клали: Fexco payUnite (оркестрация, Finix = один из эквайеров на select verticals; не US SaaS merchant apply); Finix Direct / Woo plugin (сам процессор, appendix); Practice Better / Dubsado / ParkMobile / Flowbird / GolfNow / Cvent / Service Fusion / TheraNest / Jane / Qgiv (Finix не назван); Jonas ClubPay / Northstar (не Finix; Clubessential уже в таблице).  
ACH апдейт: Lunchbox `?`, Contractor+ `?`.

---

## Finix — все публичные (22 в главной)

Официальный каталог короткий. Это всё, что удалось назвать без выдумок.

| Бренд | Путь | Dual |
|---|---|---|
| Easy · Trailing Paper | **моментально** | |
| Omella · CharityStack | **моментально** | + Stripe |
| TherapyAppointment · Ticketbud · SpiceApp · Contractor+ · Candid · Lunchbox | **триал→заявка** | |
| Shopmonkey | **триал→заявка** | + Stripe |
| Meadow · Archy · X-CD · Vroom · T2 · foreUP · Clubessential · Cargas · Passport · AgVend · Beyond/Tally | **демо** | T2 ещё Auth.net |

**Ушли / не accept:** Wave, Lightspeed US, Pay Theory → другой процессор. Change = payouts. Finix Direct / Woo = сам вендор.

---

## ISO / PayFac с живой публичной заявкой (первый SKU до 2020)

Горизонтальный signup как у Square: мерчант сам заполняет apply. Не SaaS-embed. Клали, потому что путь открытый и **не Stripe**.

| Бренд | Процессор | Год | Вертикаль | Путь | Keyed ACH |
|---|---|---|---|---|---|
| [Stax Pay](https://docs.staxpayments.com/docs/merchant-enrollment) | Stax / Fattmerchant | * | любой SMB | **заявка** | — |
| [PaymentCloud](https://paymentcloudinc.com/credit-card-processing/) | ISO (Elavon / Paysafe / Global / EMS / EVO) | 2015* | high-risk SMB | **заявка** | — |
| [CDGcommerce](https://www.cdgcommerce.com/applynow) | ISO (Pinnacle / Synovus / Citizens) | 1998* | любой SMB | **заявка** | — |
| [Flagship](https://www.flagshipmerchantservices.com/apply/) | ISO (historically First Data / Fiserv) | 2001* | любой SMB | **заявка** | — |
| [Anedot](https://www.anedot.com/nonprofits) | own (явно не Stripe; «we are the processor») | * | nonprofit / political | **моментально** | ? |
| [Dharma](https://dharmamerchantservices.com/getting-started/) | ISO (не Stripe) | * | любой SMB | **заявка** | — |
| [Payment Depot](https://www.paymentdepot.com/) | Stax ISO (Wells Fargo; TSYS / Fiserv) | 2013* | любой SMB | **заявка** | — |

---

## Не в главном

| Бренд | Почему |
|---|---|
| [Square](https://squareup.com/) / [Helcim](https://www.helcim.com/) / [QBO](https://quickbooks.intuit.com/) / [Auth.net](https://www.authorize.net/) | payments до 2020; у самих **моментально** (эталон горизонтального signup; не дублируем в ISO-секции) |
| [Wave](https://www.waveapps.com/) | был Finix → Adyen + WP + Stripe; payer ToS = **keyed ACH да** |
| [Lightspeed US](https://www.lightspeedhq.com/) | Finix 2019 → Stripe 2020 |
| [Pay Theory](https://www.paytheory.com/) | Finix → Fiserv |
| [Change](https://www.getchange.io/) | Finix payouts |
| [Finix WooCommerce](https://finix.com/integrations/woocommerce) / [Finix Direct](https://finix.com/) | вендор, live = sales / заявка |
| [Infinite Campus](https://www.infinitecampus.com/) | Payrix → Stripe |
| [PayHOA](https://www.payhoa.com/) | PR Payabli; help = Stripe (**моментально**, но Stripe) |
| [Edstruments](https://edstruments.com/) / [Smartwebs](https://smartwebs.com/) | Payabli pay-out |
| [TEC](https://www.theeventcommunity.com/) | Payabli, payments Soon |
| [STRYD](https://stryd.us/) | ACH / Paya |
| Setmore и др. старый Square BYO | до окна / BYO |

**Не подтверждено:** Sublime, Enwoven, Revvable, Abre, Real Green, Resman, PatientPal.

**Stripe-only:** [Lemon Squeezy](https://www.lemonsqueezy.com/), [Fourthwall](https://fourthwall.com/), [Stan](https://stan.store/), [Whop](https://whop.com/), [WooPayments](https://woocommerce.com/products/woocommerce-payments/), [Clio](https://www.clio.com/), [Polar](https://polar.sh/), [FreshBooks](https://www.freshbooks.com/accept-payments), [Zoho Payments](https://www.zoho.com/us/payments/), [Pixieset](https://pixieset.com/), [Mindbody](https://www.mindbodyonline.com/), [ChowNow](https://www.chownow.com/)…

---

## Дыры

| Стек | Публично | Заявлено |
|---|---|---|
| Rainforest | 19 | ~100 |
| Payabli | 12 pay-in | 60–100 |
| Finix | 22 (+ Direct/Woo appendix) | каталог короткий; `/customers` выжат |
| Payrix | 22 + 6 | «40+» без имён |
| JustiFi / Tilled | 3 + 3 | нет каталога |
| Stax | 5 (+ Tabs3Pay; Stax Pay self-reg в ISO-секции) | «150+» |

---

## План поиска (огромный, все процессинги кроме Stripe)

Критерии: US; signup / триал / **демо+заявка** (in-app не обязателен); PayFac · ISO/MSP · PSP · gateway frontend · embedded SaaS · PFaaS · MoR; процессор из ToS/help/press **или `неизвестен`, если не Stripe**; first SKU **2020–2026** (год не доказан OK); keyed ACH колонка. Dual Stripe+X — класть, если X назван.

### A. PFaaS / embedded — клиентские каталоги (выжаты, leftover-only)

1. Rainforest — ToS `legal.rainforestpay.com`, Vertex speakers, `rainforest_id` (~19/100)
2. Payabli — customers / Huntington portal, **pay-in only** (~12/60–100)
3. Finix — `/customers` + press boilerplate выжаты (раунд 13); leftover только G2/subprocessors/boarding slugs
4. Payrix / Worldpay for Platforms — `/customers` leftovers
5. Stax Connect — «150+» без имён; G2 / help / press
6. JustiFi / Tilled / Launchpay / Payops / Infinicept
7. PayEngine — кроме Flex / CurbWaste / Supermove
8. Payload — кроме Innago / Brokerage Engine / SkySlope
9. Propelr / CardPointe — кроме Act / DrivePay / Cerbo / Lever360 / vinSUITE / Atrium / InvoiceSherpa
10. Fortis / Payroc — кроме Visual Matrix / Roc / FieldServio / Smart Storage
11. Moov — кроме Tap2Local
12. WePay / JPM Payments ISV
13. Sola / Cardknox Go — кроме RMH preferred
14. NMI white-label frontends (не gateway-only; Everyware уже)
15. Exact Payments / Paynt PFaaS — Ordway ( Exact+много BYO, не exclusive)
16. Fiska / Zift / Unipaas (US only)
17. Frame / Coastal / MannyPay аналоги (open ISO signup)

### B. Эквайеры / ISO / MSP с публичной заявкой или ISV-программой

18. **Adyen for Platforms US** — кроме уже в таблице; Stayntouch / BILL / Fresha / ROLLER / Zenoti / Provet / DockMaster добавлены
19. **Elavon** WorksWith + ISO frontends — UPay360 in
20. **Fiserv** Clover / Carat / Commerce Hub / First Data / Clover Go / Clover App Market boarding
21. **Heartland / GPI / Genius / TSYS** TransIT / Premier named ISVs 2021+
22. **Worldpay / FIS** (не Payrix catalog)
23. **Nuvei / Paya / ProfitStars / Paysafe**
24. **Checkout.com** Platforms US
25. **Shift4** SkyTab / Lighthouse named SaaS (не hotel gateway-only)
26. **FreedomPay** кроме DrivePay
27. **Priority Commerce / MX Merchant** — sales form теперь OK, если это merchant apply (не agent CRM)
28. **Gravity Payments** кроме Confido / ConsignCloud / FROG / Lizzy
29. **Helcim ISV** (не сам Helcim)
30. **AffiniPay / 8am** leftovers; LexCharge кроме CosmoLex
31. **Fullsteam** portfolio 50+ — 2020+ in (StarPay/EZClaim/Flybook/Enrollware/BridalLive/Bay-Master); ERS/RoomKey/WineDirect/Maxanet still out (дубль / до 2020 без нового SKU)
32. **Xplor Pay / Clearent** — Coolfront/SPOT out; leftovers кроме FieldEdge / SA / improviPay / Dental Intel / Haulvana
33. **ISO с merchant apply (не agent CRM):** PaymentCloud / CDG / Dharma / Flagship / Anedot / Stax Pay — **в ISO-секции**; leftover: Payment Depot, National Processing, Durango, Easy Pay Direct, PayKings, Host Merchant, Electronic Payments, Payline, PaymentSpring. Payzli / Payarc / Bankful = agent CRM — out
34. **Bank merchant:** Chase Paymentech, Wells, BofA, Elavon direct, Synovus, Fifth Third, Pathward, Woodforest — self-serve 2020+
35. **Deluxe** кроме MyKidReports
36. **Remedy** кроме SmartMoving
37. **LexCharge / Headnote** leftovers после TimeSolv / PantherPayments / CosmoLex
38. **Jack Henry / ProfitStars** кроме Tap2Local
39. **Paddle / Dodo / FastSpring / Tebex** — Tebex/FastSpring до окна
40. **Airwallex / Payoneer / WorldFirst** accept-side US

### C. Вертикали SaaS (US, «Payments» / «accept cards» / «powered by»)

41. HVAC / plumbing / electrical / pest / lawn / pool / snow
42. Roofing / restoration / remodeling / materials / AV
43. Auto / collision / towing / detailing / PPF / dealers
44. Dental / ortho / chiro / vet / mental health / cash-pay / DPC — Provet / Vetspire / Vagaro in; Shepherd out (Stripe rumor)
45. Legal / tax / accounting / bookkeeping
46. Property / HOA / rent / CRE / self-storage / moving
47. Hotel / lodging / STR / winery / brewery / golf / parking / attractions
48. Events / tickets / class / youth / associations
49. Fitness / gym / childcare / church / nonprofit / gov
50. Print / sign / apparel / waste / ISP / grocery / manufacturing / ERP
51. Booking / invoicing / CRM / AR / field service 2020–26
52. Church/giving не-Stripe: Pushpay + Anedot in; Tithely/PC/Breeze = Stripe
53. Hotel не-Stripe: Stayntouch in; Cloudbeds US Stripe; Mews/RMS/Oracle/Visual Matrix/Mezzo already; Guestline / Opera / Infor / RoomRaccoon / HotelKey leftovers
54. Moving: SmartMoving in; MoversSuite+Remedy = no public apply
55. Waste: Haulvana / DocketPay / CurbWaste in; Routeware — нужен first-party Pay SKU URL

### D. Источники запросов (не выдумывать имена)

56. Press: PR Newswire / Business Wire / GlobeNewswire «launches payments» / «powered by» / «selects» 2020–26
57. `isvpaymentintegration.com` compare pages — named ISVs only
58. Charge Forward / Vertex / Rainforest conference speaker lists
59. Product Hunt / G2 / Capterra «payment processing» software 2024–26
60. Help: «powered by», merchant apply, Rainforest/Finix/Stax/Payabli/Fullsteam/Adyen/Xplor
61. `merchantapp.io/*` / `boarding.fullsteampay.net/*` / `signup.staxpayments.com`
62. PitchBook / Mergr acquirer lists → first-party Pay SKU check
63. LinkedIn processor+ISV — только с first-party URL

### E. Порядок прохода (чтобы не крутить одно и то же)

64. Сначала named leftover у Fullsteam / Xplor / Adyen / Payload / Propelr
65. Потом ISO с **видимой** merchant apply (не agent CRM)
66. Потом вертикаль × «Payments» − Stripe
67. В конце Product Hunt / press sweep

**Не класть:** Stripe-only (в т.ч. если процессор неизвестен и есть правдоподобный first-party/help hint на Stripe); payouts/issuing; BYO-orchestration only; выдуманные бренды; повтор skip-листа раундов 5–12, если причина не снята новыми правилами. Sales/демо + заявка — **класть**. First SKU до 2020 — только ISO-секция с живым apply или `*` в главной, если путь открытый и не Stripe.
