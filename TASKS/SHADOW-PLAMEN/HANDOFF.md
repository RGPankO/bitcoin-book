# Extraction Progress

## Stats
- sources/ files: 168 / 168 ✅ COMPLETE
- sources-full/ files: 243 / 243 ✅ COMPLETE
- Total processed_srts.txt entries: 411
- Last SRT run: 2026-02-28 05:21 (Saturday) — fully complete

## ✅ ALL SRT SOURCES FULLY PROCESSED

---

## DB State (2026-03-06 20:45 — After Dedup + FB Batches 1-15) ← CURRENT
| Table | Rows | Change |
|-------|------|--------|
| identities | 179 | was 162 (+17 batch 15) |
| traits | 922 | was 883 (+39 batch 15) |
| stories | 728 | was 707 (+21 batch 15) |
| voice | 586 | was 571 (+15 batch 15) |
| boundaries | 211 | was 197 (+14 batch 15) |
| relationships | 553 | was 538 (+15 batch 15) |
| **TOTAL** | **3,179** | **+121 this run (batch 15)** |

## ✅ FB ARCHIVE FULLY COMPLETE — ALL 23,790 LINES PROCESSED
- Batch 15: lines 16840–23790 (Aug 2025 – Mar 2026) — done 2026-03-06 20:45
- Period covered: August 2025 through early March 2026
- Key themes: BTC $100k milestone, ZapArc launch, Bitcoin standard app, gold→BTC swap, Thailand scouting, Kopeyky group creation, OpenClaw agents paying in BTC, BTC Balkans + BenchMark speeches, MSTR buys, Dancho Shurta court win

---

## DB State (2026-03-06 20:30 — After Dedup + FB Batches 1-14) [PREVIOUS]
| Table | Rows | Change |
|-------|------|--------|
| identities | 162 | was 157 (+5 batch 14) |
| traits | 883 | was 875 (+8 batch 14) |
| stories | 707 | was 700 (+7 batch 14) |
| voice | 571 | was 568 (+3 batch 14) |
| boundaries | 197 | was 195 (+2 batch 14) |
| relationships | 538 | was 536 (+2 batch 14) |
| **TOTAL** | **3,058** | **+27 this run (batch 14)** |

---

## Dedup Phase (2026-03-06)
Completed dedup of identities and traits tables.

**Identities cleaned (-23 rows):**
- Bitcoin educator key: 520, 543, 547, 563, 579, 581, 596 (7 — keep id=505 generic)
- Bitcoin role dupes: 519, 525, 1202, 1337 (4 — keep id=42, 23)
- Name dupes: 533, 562 (2 — keep id=524)
- Location Varna/Sofia dupes: 43, 183, 495, 507, 521, 1338 (6 — keep 24, 26, 28, 45)
- Programmer dupes: 59, 545 (2 — keep 22, 828)
- Engaging personality dupes: 488, 1098 (2 — keep 646, 1056)

**Traits cleaned (-15 rows):**
- Case/duplicate topic+stance combos: 88, 172, 224, 232, 366, 414, 476, 505, 581, 609, 635, 775, 797, 808, 833

---

## FB Archive Extraction Progress

### Source: `sources/fb-archive-clean.md`
- Total posts: 1,464 (May 2020 → March 2026)
- Delimiter: `---` (1,465 occurrences)
- Total lines: 23,789

### Batch 1 ✅ (2026-03-06)
- **Posts processed:** approximately 1-90 (file lines 1-886)
- **Date range:** May 2020 → May 2022
- **Rows added:** +13 identities, +9 traits, +10 stories, +6 voice, +11 relationships = **+49 rows**
- **Key extractions:**
  - Travel: Dubai (Jun 2021), Corfu GR (Aug 2021), Zagreb HR (Sep 2021), Italy (Dec 2021), Dubai Expo + Abu Dhabi (Jan-Mar 2022), Istanbul (Mar 2022), Croatia Krk (Apr 2022)
  - Events: 10K FB group milestone, crypto t-shirts, 300 streams/70 podcasts, first major BG crypto conference March 2022
  - Traits: mainstream media skepticism, financial sovereignty advocacy, fiat slavery framing, generational wealth transfer, community building mission
  - Stories: Bitcoin Icon gift, conference history, Italy trip, May 2022 crash manifesto
  - Voice: self-archival FB behavior, epic prophetic framing, slavery metaphor, Bitcoin humor, source verification, mission framing
  - Relationships: Michael Saylor, Peter Schiff, Erik Voorhees, Davinci Jeremie, Tucker Carlson, Charlie Munger, conference speakers (Николай Делчев, Иван Иванов, Красимир Петров, Владислав Драмалиев), fan gifters (Памела Георгиева, Виктор Георгиев)

### Batch 2 ✅ (2026-03-06 18:30)
- **Lines processed:** 887-1559 (May 2022 → Aug 2022)
- **Rows added:** +46 (7 stories, 12 traits, 12 voice, 9 identities, 3 relationships, 3 boundaries)
- **Key extractions:** Travel to London, New York, Turkey, Stuttgart, Edinburgh; property-as-anchor philosophy; "invisible labor" story; Bitcoin 8-discipline post; Edinburgh Bitcoin conference with Jeff Booth; Kripo Revolucia Sofia 400+ attendees; voice patterns: "Few.", "HFSP", "Събуди се, робе", rhetorical question chains

### Batch 3 ✅ (2026-03-06 18:30)
- **Lines processed:** 1560-2208 (Sep 2022 → Nov 2022)
- **Rows added:** +33 (4 stories, 7 traits, 8 voice, 8 identities, 4 relationships, 2 boundaries)
- **Key extractions:** El Salvador trip (Bitcoin Beach), last-chance-for-1-BTC argument, fortune-favors-the-brave at $15,800, Bulgarian hyperinflation childhood memory (1996-97), age confirmed 33 in 2022, birth year ~1989, Jeff Booth/Price of Tomorrow recommendation; voice: "HFSP", "Рано сме", "Fortune favors the brave", "1 Bitcoin = 1 Bitcoin"

### Batch 4 ✅ (2026-03-06 18:30)
- **Lines processed:** 2209-2860 (Nov 2022 → Dec 2022)
- **Rows added:** +28 (5 stories, 8 traits, 7 voice, 2 identities, 3 relationships, 3 boundaries)
- **Key extractions:** "Why programmers don't get Bitcoin" essay (Satoshi design decisions), Nigeria CBDC Bitcoin premium story, no-exit-from-Bitcoin stance, Washington DC trip, Vancouver/Sofia/Burgas/Varna "секта" communities; voice: "Биткойн е ключът. Трудно се разбира защото хората не разбират, че има ключалка", structured asset comparison format

### Batch 5 ✅ (2026-03-06 18:30)
- **Lines processed:** 2861-3736 (Dec 2022 → Mar 2023)
- **Rows added:** +22 (3 stories, 6 traits, 6 voice, 2 identities, 3 relationships, 2 boundaries)
- **Key extractions:** Miroluba Benatova public confrontation, money-as-human-energy philosophical argument, Charlie Munger vs Saylor debate; identified YouTube show "Добро утро, Крипто!"; Bitcoin price target $22M/BTC; voice: "ngmi", "Роден си роб. Не е нужно да умреш роб.", SpongeBob mock caps format

### Batch 6 ✅ (2026-03-06 18:49)
- **Lines processed:** 3737-6303 (Mar 2023 → Jun 2024)
- **Rows added:** +30 (4 stories, 7 traits, 8 voice, 4 identities, 4 relationships, 3 boundaries)
- **Key extractions:**
  - Stories: SVB bank collapse explanation, Tim Draper 285 BTC HODL lesson, Elections-as-illusion slavery essay, Bitcoin energy defense detailed
  - Traits: bitcoin_as_insurance, asymmetric_500x_risk_tolerance, taxes_as_theft_without_consent, fix_money_fix_world_war, vote_with_portfolio, covid_media_facts_propaganda, fiat_monetary_endgame
  - Voice: "ЛУД НИ ЦА", "Анон" addressing, "#пишемистория", "Чудя се...", numbered Заключение format, Swiss-bank reversal humor, "Робе" direct address, "Въпроси, въпроси..." endings
  - Identities: Bitcoin conference IEC Sofia June 2024, Slavi Trifonov show May 2024, Paraguay tax residency consideration, Sedemo Osmi TV appearance
  - Relationships: Крум Атанасов (podcast guest x2), Слави Трифонов (media host), Tim Draper (referenced), Cathie Wood (referenced)
  - Boundaries: covid_vaccines (surface/skeptic), bitcoin_energy (deep expert), fiat_monetary_mechanics (deep expert)

### Batch 7 ✅ (2026-03-06 18:49)
- **Lines processed:** 6304-6900 (Jun-Jul 2024)
- **Rows added:** +10 (3 stories, 2 traits, 3 voice, 2 identities)
- **Key extractions:**
  - Stories: Germany sells 50,000 BTC (historic mistake), deflation vs inflation philosophical essay, Zambia local currency coercion
  - Traits: minimalism_experiences_over_things, proud_minority_not_lucky (early Bitcoin adopters)
  - Voice: "Днес съм луд. Тогава ще съм визионер.", "Bitcoin has no top as Fiat has no bottom.", "Малцина" self-positioning
  - Identities: Ledger affiliate partner (code COLOR20, Jul 2024), Крипто Революция 3rd edition Jun 2024 confirmed

### Batch 8 ✅ (2026-03-06 19:05)
- **Lines processed:** 6901-7819 (Jul-Sep 2024)
- **Rows added:** +8 (2 stories, 3 traits, 3 voice)
- **Key extractions:**
  - Stories: Pension Ponzi with Bulgarian math (50yr in / 1yr out), Trump assassination attempt reaction
  - Traits: innovators_should_pay_zero_tax (Musk 0%), EU_Green_Deal_destroying_Europe (never vote PP-DB/Ursula), bitcoiner_vs_shitcoiner_are_different
  - Voice: hard-times-strong-men generational cycle, "Don t be this guy", Bitcoin-for-risk-averse reframing

### Batch 9 ✅ (2026-03-06 19:15)
- **Lines processed:** 7820-9702 (Sep-Oct 2024)
- **Rows added:** +35 (6 stories, 11 traits, 8 voice, 4 identities, 3 boundaries, 3 relationships)
- **Key extractions:**
  - Stories: ECB anti-Bitcoin paper Oct 2024 (massive, Plamen frames as "they fight us" stage), EU flight tax vindication, Bitcoin-always-too-expensive nocoiner loop 2014-2024, China real estate as Yap stones analogy, Aug 19 2024 mega cycle analysis, Matthew Sigel VanEck BRICS-Bitcoin stunner
  - Traits: europe_done (intensity 9), ecb_bitcoin_attack (intensity 10 — Bitcoin vs collectivism as civilizational war), golden_years_25-45, information_asymmetry_as_wealth, elon_musk_bought_freedom_not_profit, politicians_should_live_like_voters, annual_social_media_purge, spacex_80pct_orbital_cargo, vote_with_wallet_not_ballot, AML_as_control_not_crime, gold_standard_will_never_return
  - Voice: "Всеки купува Биткойн на цената, на която заслужава", explosive all-caps КОНСПИРАТОРИТЕ vindication, "Америка иновира. Китай копира. Европа регулира." 3-part parallel, year-by-year enumeration format, /s sarcasm, "few, but hopefully just enough...", info vs knowledge distinction, weakness-as-opportunity self-positioning
  - Identities: Bitcoin x20 from $3K first purchase (Aug 2024), annual FB friend cleanup, Oct 2024 conference (Vladislav Dramaliev), US political preference Trump 2024
  - Relationships: Matthew Sigel (VanEck), Vladislav Dramaliev (event_organizer), Elon Musk (admired_innovator)
  - Boundaries: EU climate/green deal (deep), BRICS geopolitics (surface), US Democrat politics (surface)

### Batch 10 ✅ (2026-03-06 19:30)
- **Lines processed:** 9703-10495 (Oct 25 → Nov 11, 2024)
- **Rows added:** +36 (6 stories, 9 traits, 9 voice, 4 identities, 4 boundaries, 4 relationships)
- **Key extractions:**
  - Stories: Joe Rogan/Trump 3hr interview as NPC litmus test, Румен Виста/Цветан Радушев sold-at-bottom betrayers, Bulgaria 3 conferences/1 politician story, 4yr-ago YouTube prediction of state Bitcoin adoption vindicated, bear market credibility litmus test framework, Bitcoin political platform wishlist (0% tax + curriculum + reserve)
  - Traits: long_form_media_required_for_valid_opinion (9), anti-DEI meritocracy (9), bitcoin_zero_tax_legal_tender_platform (10), bear_market_credibility_test (10), signal_vs_noise selective posting (8), Saylor will be in textbooks (9), ego_as_obstacle_to_bitcoin_truth (8), institutional dominos falling (9), Bitcoin inelastic supply (9)
  - Voice: "Доминото пада", "my 2 sats", "РЕВААААА" celebration, progress bar milestone format, "Шум ли е, че..." anaphora, "Ако съм в грешка ще си нося кръста / ако съм прав няма да съм бил късметлия", NPC vocabulary, signal vs capacity rhetorical question
  - Identities: $80K milestone Nov 2024, 3 conferences organized in BG, 2020 YouTube prediction of state adoption, probability revision 10%→90% by 2024
  - Relationships: Румен Виста (negative, sold at bottom), Цветан Радушев (negative, sold at bottom), Синтия Лумис (hopeful, 1M BTC reserve bill), Киро Брейка (notable, mentioned BTC at $15K)
  - Boundaries: DEI (deep anti), Bulgarian political parties (deep expert frustration), long-form media methodology (deep), Bitcoin price modeling (deep)

### Batch 11 ✅ (2026-03-06 19:45)
- **Lines processed:** 10496-12490 (Nov 11, 2024 → Jan 8, 2025)
- **Rows added:** +29 (6 stories, 8 traits, 5 voice, 4 identities, 2 boundaries, 4 relationships)
- **Key extractions:**
  - Stories: Mission burnout (Nov 11 emotional breakdown), Proof-of-Work letter (Аз/Ти parallel at $100K), Bitcoin luck sarcasm essay (Dec 5, "pure luck"), $100K citadel moment, 2024 year-in-review catalog, 0.1 BTC window closing warning (Jan 5 2025)
  - Traits: bitcoin_ownership_proof_of_work, bulgarian_mainstream_media (still pyramid), bitcoin_discomfort_is_the_point, whole_coiner_is_new_millionaire, bitcoin_standard_save_not_invest, elon_musk_critics_are_jealous, gold_value_is_narrative, bitcoin_01btc_window_closing_2028
  - Voice: "Ще се срещнем в цитаделата" (citadel metaphor), "Нося цветя за мечките" (victory over bears), sarcastic luck essay format, Аз/Ти parallel contrast structure, aphoristic Bitcoin wisdom quoting
  - Identities: DCA in MSTR + wBTC DeFi (Nov 2024), speaker at 360 Market Insights event (Jan 2025), BTC $200K prediction for 2025, 0.1 BTC window prediction public statement
  - Relationships: Щерьо Ножаров (debate_opponent), Patrick Bet-David (media_reference), Нейчо/Neychev (event_organizer), Greg Foss (bitcoin_thought_leader)
  - Boundaries: us_2020_election_fraud (deep believer, rejects fact-checkers), bitcoin_as_savings_technology (deep, refuses investment framing)

### Batch 12 ✅ (2026-03-06 20:05)
- **Lines processed:** 12491-14074 (Jan 8, 2025 → Mar 8, 2025)
- **Rows added:** +33 (7 stories, 10 traits, 6 voice, 4 identities, 3 boundaries, 3 relationships)
- **Key extractions:**
  - Stories: FTX book rejection (refused promo money for FTX book — "we wrote history"), Sarcastic homeless Bitcoiner parody (BTC $100K→$80K "lost everything"), Norwegian Central Bank MSTR revelation, Credit slavery anaphora, Content binge-watching satisfaction, Zelenskyy gambled and lost at Trump meeting, Bitcoin supply scarcity window closing essay
  - Traits: borrowed_bitcoin_position (holds BTC with leverage, like Saylor), trump_crypto_executive_order (9 — bullish strategic reserve), eu_exit_planning (9 — actively seeking exit before sharia law), free_lunch_doesnt_exist (8 — all welfare paid by taxpayers), technology_deflation_thesis (8 — next 20yr > last 100), doge_elon_government_efficiency (7), bitcoin_price_target_1M_2030 (9 — $1M by 2030-32), impact_over_income (9 — changing worldviews > earning money), bitcoin_supply_window_closing (9), xrp_criticism (8 — centralized fraud)
  - Voice: credit slavery anaphora (Q&A reversal), Ганьо archetype address, Безкрайност/21M formula, Философ Петроф satirical character, "моя едж" minority visionary self-positioning, ironic formal honorific ("многоуважавания")
  - Identities: BTC held with borrowed money (Jan 2025), Sofia Event Center April 9 2025 organizer, BTC $1M by 2030-32 prediction, DCA at $80K confirmed
  - Boundaries: ukraine_russia_conflict (surface, Zelensky ego), eu_immigration_demographics (deep, blunt opinions), mstr_strategy (deep expert)
  - Relationships: J.D. Vance (political figure), Friedrich Hayek (intellectual reference), Войн Варчев (Bulgarian finance figure, mocked sarcastically)

### Batch 13 ✅ (2026-03-06 20:15)
- **Lines processed:** 14075-15637 (Mar 8, 2025 → ~May 28, 2025)
- **Rows added:** +36 (5 identities, 10 traits, 7 stories, 7 voice, 3 boundaries, 4 relationships)
- **Key extractions:**
  - Stories: Corona crash survival (all-in before crash, DCA through it), Financial independence journey from Osaka (life timeline: village 14 → financially free 31), Bitcoin vs Sofia apartment (30 BTC = 1 apartment → now equal → 1 BTC = 30 apartments predicted), Early adopters vindicated letter (poetic, triumphant), Bonex community defense, Bitcoin decade objections essay (Apr 28), Twenty One/Jack Mallers announcement
  - Traits: gold_is_obsolete (digital>analog), bitcoin_cannot_be_banned (TOR/VPN argument), bitcoin_adoption_speed (lightning fast historically), uk_welfare_decline (talent exodus occupied nation), fiat_defenders_enslaved (system enslaves defenders), saylor_actions_match_words, eu_savings_confiscation (Ursula), bitcoin_frugality_identity (Temu not brands), bitcoin_objections_are_era_specific (pattern recognition), delaying_gratification_builds_wealth
  - Voice: year-by-year era objection format, "peanuts", "I was there Gandalf", Temu deflection, "Всеки купува Биткойн на цената, на която заслужава" 3-line mantra, "Днес идея, утре план, вдругиден реалност", "Europe to the Moon" ironic reversal
  - Identities: Japan/China Asia trip early 2025, savings rate £1,500/£3K historical, life timeline (village→FI@31), 360 Market Insights Apr 9 organizer, Bitcoin first purchase ~$3K 2017
  - Boundaries: bitcoin_censorship_resistance (deep), eu_stablecoin_regulation_mica (deep), personal_finance_delayed_gratification (deep)
  - Relationships: Jack Mallers, Ray Dalio, Давид Бонев (respected peer), Мартин Карбовски

### Batch 14 ✅ (2026-03-06 20:30)
- **Lines processed:** 15638-16839 (May 28, 2025 → ~Jul 5, 2025)
- **Rows added:** +27 (7 stories, 8 traits, 3 voice, 5 identities, 2 boundaries, 2 relationships)
- **Key extractions:**
  - Stories: Las Vegas Bitcoin 2025 conference (JD Vance as first speaker, Pakistan national reserve), US state Bitcoin reserve cascade (6 laws in <6 months), BlackRock IBIT beats IVV in fees despite 8x smaller AUM, Nocoiner ego forgiveness essay (8 specific mistakes), Gold fungibility failure vs Bitcoin (1 BTC=1 BTC), Yosemite+Grand Canyon dream trip fulfilled, Bitcoin adoption mission declared over
  - Traits: gambling_industry_morality (moral boycott, intensity 9), covid_fauci_government_coverup (lab leak vindicated, 9), blackrock_bitcoin_alignment (vested interest, 8), bitcoin_adoption_phase_transition (mission complete → accumulate, 9), pension_system_ai_era_fraud (9), climate_crisis_government_control (8), bitcoin_is_the_only_bitcoin (10), frugality_over_status_symbols (drives 20yr Ford Star, 8)
  - Identities: Las Vegas travel (May 2025), Yosemite+Grand Canyon travel (Jun 2025), Bitcoin Balkans rebranding Oct 2025, Ford Star personal vehicle, BTC $104K Jun 2025
  - Boundaries: gambling_industry (deep, moral), covid_origins_fauci (deep, vindicated)
  - Relationships: Синтия Лумис met_in_person (childhood hero, Las Vegas), Larry Fink/BlackRock (institutional reference)
  - Skipped: 1 (Yosemite initially time_context conflict, fixed on second insert)

### Batch 15 (NEXT RUN)
- **Start at:** file line 16840 (approximately Jul 5, 2025 onwards)
- **Remaining:** ~6,950 lines (Jul 2025 → Mar 2026 — ~8 months of posts)
- **Suggested batch size:** ~1600-1800 lines per run
- **Expected themes:** Bitcoin at $100K-$150K+ range, Bitcoin Balkans conference Oct 2025, AI/robotics commentary, political developments, 21Digital SEO work references, possible $200K approach

---

## ✅ EXTRACTION COMPLETE — CRON SELF-DISABLED (2026-03-06 21:00)
- All 411 SRT files: processed ✅
- FB archive (23,790 lines / 1,464 posts): processed ✅
- Shadow Extractor cron (e060870e-04ec-497e-addc-f4e40701925a): **disabled**
- Final DB: 3,179 rows across 6 tables

## Recommended Next Steps (for operator/overseer)
1. **Dedup remaining tables** — stories (728), voice (586), boundaries (211), relationships (553) — lower priority, manual or scripted pass
2. **Profile distillation pass** — synthesize key identity pillars from 3,179 rows into a coherent shadow profile doc
3. **Shadow Writer** (cron 7516d219) can begin using the DB for writing tasks

## Kanban
- Ticket #1205: Shadow DB dedup — in_progress, assigned to shadow-extractor

## Anomalies
- TASK.md does not exist (cron uses CONTEXT.md + HANDOFF.md)
- extract_batch.py was for SRT processing only — FB archive uses direct SQL inserts
- identities UNIQUE index is `idx_identities_shadow_key_time` (index, not named constraint) → use `ON CONFLICT DO NOTHING`
- voice UNIQUE index is `idx_voice_shadow_pattern_example_register` (index, not named constraint) → use `ON CONFLICT DO NOTHING`
- stories, traits, relationships: all have NAMED unique constraints → can use `ON CONFLICT ON CONSTRAINT <name> DO NOTHING`

## Run History
- Batches 1-14 (2026-02-27 → 2026-02-28): SRT processing → 2,677 rows
- Verification (2026-02-28 05:51): all SRT files confirmed processed
- **2026-03-06 18:xx**: Dedup (-38 rows) + FB Batch 1 (+49 rows) → 2,685 total
- **2026-03-06 18:30-19:05**: FB Batches 2-8 → +183 rows → 2,862 total
- **2026-03-06 19:15**: FB Batch 9 (lines 7820-9702, Sep-Oct 2024) → +35 rows → 2,897 total
- **2026-03-06 19:30**: FB Batch 10 (lines 9703-10495, Oct 25-Nov 11, 2024) → +36 rows → 2,933 total
- **2026-03-06 19:45**: FB Batch 11 (lines 10496-12490, Nov 11, 2024-Jan 8, 2025) → +29 rows → 2,962 total
- **2026-03-06 20:05**: FB Batch 12 (lines 12491-14074, Jan 8-Mar 8, 2025) → +33 rows → 2,995 total
- **2026-03-06 20:15**: FB Batch 13 (lines 14075-15637, Mar 8-May 28, 2025) → +36 rows → 3,031 total
- **2026-03-06 20:30**: FB Batch 14 (lines 15638-16839, May 28-Jul 5, 2025) → +27 rows → 3,058 total
