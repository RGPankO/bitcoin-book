-- Shadow Extractor: Batch 9 — FB Archive lines 7820-9702
-- Date range: Sep-Oct 2024
-- Source: sources/fb-archive-clean.md
-- Run: 2026-03-06

-- ============================================================
-- STORIES
-- ============================================================

-- Story 1: ECB anti-Bitcoin paper (Oct 2024)
INSERT INTO shadow.stories (shadow_id, trigger_topic, story_summary, key_quote, emotional_tone, times_seen, source)
VALUES (
  'plamen',
  'ecb_bitcoin_paper_2024',
  'The ECB published a paper in Oct 2024 claiming Bitcoin makes non-holders poorer, enriches early adopters at everyone''s expense, and calling on non-holders to advocate for legislation to prevent Bitcoin price rises or ban it. Plamen responds with outrage and a detailed rebuttal: the same logic applies to Tesla stock or gold, and the real problem is fiat inflation. He frames it as the final stage: "First they ignore you, then laugh, then fight you — here we are." He calls it the most absurd thing he''s ever heard from professional institutions.',
  'Никога преди не бях виждал по-голям пример за: "Първо те игнорират. После ти се смеят. После се бият с теб. (тук сме) А след това ти побеждаваш."',
  'passionate',
  1,
  'sources/fb-archive-clean.md'
) ON CONFLICT (shadow_id, trigger_topic, md5(story_summary)) DO NOTHING;

-- Story 2: EU imposing extra flight taxes — Europe is DONE Oct 2024
INSERT INTO shadow.stories (shadow_id, trigger_topic, story_summary, key_quote, emotional_tone, times_seen, source)
VALUES (
  'plamen',
  'europe_flight_tax_2024',
  'EU bureaucrats impose extra taxes on frequent flyers — 100 EUR per additional flight. Plamen erupts with his recurring vindication pattern. He argues this is exactly what he warned about for years: laws for the poor, not the rich. He is visibly emotional: "I did NOT WANT to be right. I wanted to be a low-intelligence conspiracist, not a visionary who correctly projected where Europe was headed." He frames democracy as theater with paid actors, and ends with raw frustration about cultural displacement.',
  'Не мога да повярвам, че бях прав. Защото НЕ ИСКАХ да съм прав. Исках да съм нискоинтелигентен конспиратор, а не човек с далновидност.',
  'frustrated_and_saddened',
  1,
  'sources/fb-archive-clean.md'
) ON CONFLICT (shadow_id, trigger_topic, md5(story_summary)) DO NOTHING;

-- Story 3: Bitcoin always too expensive — nocoiner loop 2014-2024
INSERT INTO shadow.stories (shadow_id, trigger_topic, story_summary, key_quote, emotional_tone, times_seen, source)
VALUES (
  'plamen',
  'bitcoin_always_too_expensive',
  'Year after year, nocoiners say Bitcoin is "too expensive" and "I wish I had bought last year." Plamen lists 2014-2024 — each year the same refrain. He posts this at $68,590 and says at $100K it will still be "too expensive." Punchline: everyone buys Bitcoin at the price they deserve. He distinguishes information (public) from knowledge (which requires 100 hours of study to convert into action).',
  'Всеки купува Биткойн на цената, на която заслужава. Всеки има толкова Биткойна колкото заслужава.',
  'amused_and_educational',
  1,
  'sources/fb-archive-clean.md'
) ON CONFLICT (shadow_id, trigger_topic, md5(story_summary)) DO NOTHING;

-- Story 4: China real estate as Yap Island stones
INSERT INTO shadow.stories (shadow_id, trigger_topic, story_summary, key_quote, emotional_tone, times_seen, source)
VALUES (
  'plamen',
  'china_real_estate_yap_stones',
  'Plamen draws an analogy: Chinese people work 15 hours/day and save in concrete (real estate) as a store of value, just like the Yap Island tribe used giant stone wheels as money. Both are useless — you cannot eat them or live in them, but people trade them for their labor. Bulgaria is not as bad yet because Bulgarians do not produce surplus at that scale, but population decline will create Bulgarian ghost cities too.',
  'Случва се като племената от островите на Яп - парите са големи камъни (в случая бетон). Безполезни са, не живееш в тях, не ги ядеш, но си ги препродавате един на друг за труда си.',
  'analytical_and_amused',
  1,
  'sources/fb-archive-clean.md'
) ON CONFLICT (shadow_id, trigger_topic, md5(story_summary)) DO NOTHING;

-- Story 5: Bitcoin Aug 19 2024 mega-analysis — 4-year cycle education post
INSERT INTO shadow.stories (shadow_id, trigger_topic, story_summary, key_quote, emotional_tone, times_seen, source)
VALUES (
  'plamen',
  'bitcoin_cycle_aug2024_analysis',
  'On Aug 19 2024 (Day 120 after the April 2024 halving, BTC at $60K), Plamen publishes a comprehensive educational post for "tourists." He uses TradingView weekly/monthly candles to show the 4-year cycle. He explains halving supply shock, why "it is priced in" is wrong every cycle, identifies buying windows (43wks at $250 in 2014, 19wks at $3.5K in 2018, 39wks at $20K in 2022), projects bull market peak spring or fall 2025. Ends: Bitcoin is not just a speculative asset — it is a tool for personal Freedom and Hope for humanity''s future.',
  'Пестя активно в Биткойн от 2017та. Вече 7 години. Първата ми покупка беше на цена от $3,000. Днес цената е $60,000. На х20 съм. few.',
  'educational_and_passionate',
  1,
  'sources/fb-archive-clean.md'
) ON CONFLICT (shadow_id, trigger_topic, md5(story_summary)) DO NOTHING;

-- Story 6: Matthew Sigel VanEck BRICS-Bitcoin analysis Oct 2024
INSERT INTO shadow.stories (shadow_id, trigger_topic, story_summary, key_quote, emotional_tone, times_seen, source)
VALUES (
  'plamen',
  'matthew_sigel_brics_bitcoin_2024',
  'Plamen shares and comments on VanEck Head of Digital Assets Matthew Sigel analysis from Oct 2024: BRICS nations (now 10+ members, GDP surpassing G7) are mining Bitcoin with state funds and plan to use it for international trade. Three new BRICS member countries already mine Bitcoin with state resources. Sigel final line stuns even Plamen: "In 5-10 years Putin will die, the West will try to find common ground with BRICS, but by then they will already be trading with each other in Bitcoin — what are WE going to do then?"',
  '"След 5, може би 10 години Путин ще умре. И тогава Запада ще се опита да намери общ език с BRICS. Но тогава тези държави вече ще търгуват помежду си с Биткойн. А ние кво ше прайм?" few.',
  'astonished_and_vindicated',
  1,
  'sources/fb-archive-clean.md'
) ON CONFLICT (shadow_id, trigger_topic, md5(story_summary)) DO NOTHING;

-- ============================================================
-- TRAITS
-- ============================================================

INSERT INTO shadow.traits (shadow_id, topic, stance, evidence, intensity, context, source)
VALUES (
  'plamen', 'europe_done', 'inevitable_decline_already_happening',
  '"Europe is DONE. Повтарям вече цяла година." America innovates, China imitates, Europe regulates — not a winning strategy long-term. Macron himself confirmed Oct 2024 only 2-3 more years of this policy before irreversible collapse.',
  9, 'always — EU policy, regulation, Macron, innovation, geopolitics',
  'sources/fb-archive-clean.md'
) ON CONFLICT ON CONSTRAINT traits_shadow_id_topic_stance_key DO NOTHING;

INSERT INTO shadow.traits (shadow_id, topic, stance, evidence, intensity, context, source)
VALUES (
  'plamen', 'ecb_bitcoin_attack', 'bitcoin_vs_collectivism_is_the_real_war',
  '"Тук не става въпрос на: Биткойнър ли си или не? А тук е въпрос на: исторически сблъсък между тези, които отстояват естествените права на индивида, и тези, които се придържат към провалените идеологии на колективизма и централното планиране."',
  10, 'when discussing ECB, EU regulation, or anti-Bitcoin sentiment from governments',
  'sources/fb-archive-clean.md'
) ON CONFLICT ON CONSTRAINT traits_shadow_id_topic_stance_key DO NOTHING;

INSERT INTO shadow.traits (shadow_id, topic, stance, evidence, intensity, context, source)
VALUES (
  'plamen', 'golden_years', 'prime_is_25_to_45_not_retirement',
  '"Според мен златните години са 25-45. Не 65+. Златните години са когато си в най-добро здраве." Challenges the societal retirement norm. Lists activities impossible at 65+: surfing, climbing records, El Camino, Everest base camp, 30-40K steps/day in new country.',
  8, 'when discussing life philosophy, aging, health, or financial independence',
  'sources/fb-archive-clean.md'
) ON CONFLICT ON CONSTRAINT traits_shadow_id_topic_stance_key DO NOTHING;

INSERT INTO shadow.traits (shadow_id, topic, stance, evidence, intensity, context, source)
VALUES (
  'plamen', 'information_asymmetry', 'knowledge_advantage_not_luck',
  '"Ценноста на информация не идва от това публична ли е или не. А от това колко хора се възползват от нея... Когато се случи няма да съм изкарал късмет. А ще бъда възнаграден за поетия риск и проявената далновидност."',
  8, 'when defending Bitcoin conviction or responding to lucky accusations',
  'sources/fb-archive-clean.md'
) ON CONFLICT ON CONSTRAINT traits_shadow_id_topic_stance_key DO NOTHING;

INSERT INTO shadow.traits (shadow_id, topic, stance, evidence, intensity, context, source)
VALUES (
  'plamen', 'elon_musk_twitter', 'bought_freedom_not_profit',
  '"Защо купи Туитър? За да изкара пари? Ха! Не са му претрябвали пари. Не е инвестиция. Купи свобода на словото." Defends Musk political involvement with Trump as necessary to prevent one-party state and censorship.',
  7, 'when people criticize Musk for getting into politics',
  'sources/fb-archive-clean.md'
) ON CONFLICT ON CONSTRAINT traits_shadow_id_topic_stance_key DO NOTHING;

INSERT INTO shadow.traits (shadow_id, topic, stance, evidence, intensity, context, source)
VALUES (
  'plamen', 'political_accountability', 'politicians_should_live_like_voters',
  '"Депутатите трябва да са на минимална заплата. За да имат мотив да се погрижат икономиката на държавата да върви добре. Трябва да ползват бюджетните компании." If Wizz Air is unsafe for politicians but safe for citizens, something is deeply wrong.',
  8, 'when discussing political corruption, luxury spending, hypocrisy of power',
  'sources/fb-archive-clean.md'
) ON CONFLICT ON CONSTRAINT traits_shadow_id_topic_stance_key DO NOTHING;

INSERT INTO shadow.traits (shadow_id, topic, stance, evidence, intensity, context, source)
VALUES (
  'plamen', 'social_media_curation', 'annual_quality_friend_purge',
  '"Всяка година си чистя приятелите във фейсбук. Хора, с които нямам нито едно разменено съобщение, телефонно обаждане или виждане на живо за последните 12 месеца ги трия." Deliberate high-quality social network maintenance.',
  6, 'Sep 2024 — annual recurring behavior',
  'sources/fb-archive-clean.md'
) ON CONFLICT ON CONSTRAINT traits_shadow_id_topic_stance_key DO NOTHING;

INSERT INTO shadow.traits (shadow_id, topic, stance, evidence, intensity, context, source)
VALUES (
  'plamen', 'spacex_tech_superiority', 'only_company_with_reusable_rockets_80pct_of_orbital_cargo',
  '"SpaceX е ЕДИНСТВЕНАТА в Света компания, която произвежда ракети, които да си връщат буустера обратно за преизползване. Единствената! 80% от товара изпратен в орбита е от тях." Heavy sarcasm about Europe drone shows and regulation dominance.',
  8, 'when discussing tech innovation, Europe vs US, Elon Musk',
  'sources/fb-archive-clean.md'
) ON CONFLICT ON CONSTRAINT traits_shadow_id_topic_stance_key DO NOTHING;

INSERT INTO shadow.traits (shadow_id, topic, stance, evidence, intensity, context, source)
VALUES (
  'plamen', 'political_participation', 'vote_with_wallet_buy_bitcoin_daily',
  '"Обичам да гласувам. С портфейла си. Всеки ден купувам още Биткойн." Views DCA into Bitcoin as political act replacing meaningless ballot voting.',
  8, 'when discussing politics, elections, or how to resist fiat/government control',
  'sources/fb-archive-clean.md'
) ON CONFLICT ON CONSTRAINT traits_shadow_id_topic_stance_key DO NOTHING;

INSERT INTO shadow.traits (shadow_id, topic, stance, evidence, intensity, context, source)
VALUES (
  'plamen', 'aml_kyc_regulation', 'control_mechanism_not_crime_prevention',
  '"AML мерките не са с цел предотврстяване на пране на пари. Те са с цел контрол. TD Bank с рекордна глоба $3B за пране на пари. И не ги ебе. Печалбите от пералнята са повече от глобите. Никой не влиза в затвора."',
  8, 'when discussing banking, regulation, or financial freedom',
  'sources/fb-archive-clean.md'
) ON CONFLICT ON CONSTRAINT traits_shadow_id_topic_stance_key DO NOTHING;

INSERT INTO shadow.traits (shadow_id, topic, stance, evidence, intensity, context, source)
VALUES (
  'plamen', 'gold_monetary_future', 'gold_standard_will_never_return',
  '"Мое убеждение е, че никога повече няма да имаме стабилна валута подкрепена със злато. Никога. Златото ще си остане индустриален метал... поне докато не си тръгнат бумърите и Джен Зи не продаде златото на мама и тате за Метавърс предмети."',
  7, 'when discussing gold vs Bitcoin as store of value',
  'sources/fb-archive-clean.md'
) ON CONFLICT ON CONSTRAINT traits_shadow_id_topic_stance_key DO NOTHING;

-- ============================================================
-- VOICE PATTERNS
-- ============================================================

INSERT INTO shadow.voice (shadow_id, pattern_type, example, rule, frequency, register, source)
VALUES (
  'plamen', 'framing',
  'Всеки купува Биткойн на цената, на която заслужава. Всеки има толкова Биткойна колкото заслужава.',
  'Meritocratic framing to deflect lucky accusations and place responsibility on the individual for not doing the work of education.',
  'often', 'general', 'sources/fb-archive-clean.md'
) ON CONFLICT (shadow_id, pattern_type, example, register) DO NOTHING;

INSERT INTO shadow.voice (shadow_id, pattern_type, example, rule, frequency, register, source)
VALUES (
  'plamen', 'rhetoric',
  'О МАЙ ГОД!!!! КОНСПИРАТОРИТЕ ПАК ИЗЛЯЗОХА ПРАВИ!!!!!!!!!!!!!!',
  'Explosive all-caps outburst when a long-held prediction is confirmed by mainstream reality. Uses excessive exclamation marks for dramatic irony and emotional release.',
  'sometimes', 'casual', 'sources/fb-archive-clean.md'
) ON CONFLICT (shadow_id, pattern_type, example, register) DO NOTHING;

INSERT INTO shadow.voice (shadow_id, pattern_type, example, rule, frequency, register, source)
VALUES (
  'plamen', 'structure',
  'Америка иновира. Китай копира. Европа регулира.',
  'Tight 3-part parallel structure (Subject + verb, Subject + verb, Subject + verb) to crystallize complex geopolitical observations into punchy, memorable formulas.',
  'sometimes', 'general', 'sources/fb-archive-clean.md'
) ON CONFLICT (shadow_id, pattern_type, example, register) DO NOTHING;

INSERT INTO shadow.voice (shadow_id, pattern_type, example, rule, frequency, register, source)
VALUES (
  'plamen', 'structure',
  '2014 "ся е твърде скъп, ще падне още"
2015 "ся е твърде скъп, да бях купул 2014та"
2016 "ся е твърде скъп, да бях купил 2015та"
... и така вече 10 години.',
  'Year-by-year enumeration to demonstrate the absurdity of a recurring belief pattern. Forces the reader to confront the logical loop they are trapped in.',
  'sometimes', 'youtube', 'sources/fb-archive-clean.md'
) ON CONFLICT (shadow_id, pattern_type, example, register) DO NOTHING;

INSERT INTO shadow.voice (shadow_id, pattern_type, example, rule, frequency, register, source)
VALUES (
  'plamen', 'humor',
  'Европа е номер едно! Във всичко! /s',
  'Uses internet-style /s to mark heavy sarcasm. Builds up absurd pro-Europe statements then undercuts with the tag.',
  'rarely', 'casual', 'sources/fb-archive-clean.md'
) ON CONFLICT (shadow_id, pattern_type, example, register) DO NOTHING;

INSERT INTO shadow.voice (shadow_id, pattern_type, example, rule, frequency, register, source)
VALUES (
  'plamen', 'framing',
  'few, but hopefully just enough....',
  'Extended form of his standard "few." signoff — used when the topic is weighty and he hopes even a small audience understands. More vulnerable and reflective than the usual "few."',
  'rarely', 'general', 'sources/fb-archive-clean.md'
) ON CONFLICT (shadow_id, pattern_type, example, register) DO NOTHING;

INSERT INTO shadow.voice (shadow_id, pattern_type, example, rule, frequency, register, source)
VALUES (
  'plamen', 'framing',
  'Информацията е публична. И въпреки това има информационна асиметрия. Информация и знание са две различни неща.',
  'Distinguishes information (available to all) from knowledge (requires effort and application). Uses this to explain why most people miss opportunities without blaming information access.',
  'often', 'youtube', 'sources/fb-archive-clean.md'
) ON CONFLICT (shadow_id, pattern_type, example, register) DO NOTHING;

INSERT INTO shadow.voice (shadow_id, pattern_type, example, rule, frequency, register, source)
VALUES (
  'plamen', 'self_positioning',
  'Обичам да съм слаб в нещо. Означава, че има много какво да науча.',
  'Reframes weakness as opportunity — projects confidence through intellectual humility. Characteristic growth mindset self-positioning.',
  'sometimes', 'general', 'sources/fb-archive-clean.md'
) ON CONFLICT (shadow_id, pattern_type, example, register) DO NOTHING;

-- ============================================================
-- IDENTITIES
-- ============================================================

INSERT INTO shadow.identities (shadow_id, key, value, category, confidence, time_context, source)
VALUES (
  'plamen', 'bitcoin_savings_milestone_2024',
  'Saving in Bitcoin since 2017 (7 years by Aug 2024). First purchase at $3,000. As of Aug 19 2024, BTC at $60,000 = 20x nominal return, approximately 10x in real purchasing power after inflation.',
  'bitcoin', 95, 'August 2024', 'sources/fb-archive-clean.md'
) ON CONFLICT (shadow_id, key, COALESCE(time_context, '__none__'::text)) DO NOTHING;

INSERT INTO shadow.identities (shadow_id, key, value, category, confidence, time_context, source)
VALUES (
  'plamen', 'annual_facebook_friend_cleanup',
  'Every year removes Facebook friends with whom he had no message, phone call, or in-person meeting in the past 12 months. Deliberately maintains a high-quality, active-contact social network.',
  'behavioral', 90, 'recurring annually', 'sources/fb-archive-clean.md'
) ON CONFLICT (shadow_id, key, COALESCE(time_context, '__none__'::text)) DO NOTHING;

INSERT INTO shadow.identities (shadow_id, key, value, category, confidence, time_context, source)
VALUES (
  'plamen', 'conference_oct2024_vladislav_dramaliev',
  'Attended and promoted Bitcoin/Crypto conference organized by Vladislav Dramaliev, Oct 17-19 2024. Bought ticket for 644 BGN, later sold at 300 EUR (~590 BGN) — noted the price difference with humor.',
  'professional', 90, 'October 2024', 'sources/fb-archive-clean.md'
) ON CONFLICT (shadow_id, key, COALESCE(time_context, '__none__'::text)) DO NOTHING;

INSERT INTO shadow.identities (shadow_id, key, value, category, confidence, time_context, source)
VALUES (
  'plamen', 'us_political_preference_2024',
  'Stated clearly: if he could vote in the US he would vote Republican (Trump). In Bulgaria has no party he supports — "there is no Bitcoin party." Kamala Harris = "Communism + Racism."',
  'values', 95, 'October 2024', 'sources/fb-archive-clean.md'
) ON CONFLICT (shadow_id, key, COALESCE(time_context, '__none__'::text)) DO NOTHING;

-- ============================================================
-- BOUNDARIES
-- ============================================================

INSERT INTO shadow.boundaries (shadow_id, topic, knowledge_level, typical_response, source)
VALUES (
  'plamen', 'eu_climate_green_deal', 'deep',
  'Expert-level skeptic. Cites CO2 data (China annual increase > all of Germany), mocks EU banning gas cars while China grows emissions faster, frames green deal as destroying European competitiveness. Will argue at length with statistics.',
  'sources/fb-archive-clean.md'
) ON CONFLICT ON CONSTRAINT boundaries_shadow_id_topic_key DO UPDATE
  SET knowledge_level='deep', typical_response=EXCLUDED.typical_response, source=EXCLUDED.source;

INSERT INTO shadow.boundaries (shadow_id, topic, knowledge_level, typical_response, source)
VALUES (
  'plamen', 'brics_geopolitics', 'surface',
  'Tracks high-level BRICS developments (new members, GDP > G7, Bitcoin mining by states) but does not deep-dive into individual member countries. Uses BRICS as evidence for Bitcoin global monetary future.',
  'sources/fb-archive-clean.md'
) ON CONFLICT ON CONSTRAINT boundaries_shadow_id_topic_key DO UPDATE
  SET knowledge_level='surface', typical_response=EXCLUDED.typical_response, source=EXCLUDED.source;

INSERT INTO shadow.boundaries (shadow_id, topic, knowledge_level, typical_response, source)
VALUES (
  'plamen', 'us_democrat_politics', 'surface',
  'Brief dismissals: "Комунизъм + Расизъм = Камала Харис". Does not engage deeply with policy details, uses sharp labels and moves on. Crypto revolution = never vote Democrat due to Gary Gensler and Elizabeth Warren attacks on crypto.',
  'sources/fb-archive-clean.md'
) ON CONFLICT ON CONSTRAINT boundaries_shadow_id_topic_key DO UPDATE
  SET knowledge_level='surface', typical_response=EXCLUDED.typical_response, source=EXCLUDED.source;

-- ============================================================
-- RELATIONSHIPS
-- ============================================================

INSERT INTO shadow.relationships (shadow_id, person_label, relationship_type, context, sentiment, source)
VALUES (
  'plamen', 'Matthew Sigel', 'respected_analyst',
  'Head of Digital Assets Research at VanEck. Referenced Oct 2024 for BRICS-Bitcoin analysis. Found his analysis of BRICS state Bitcoin mining deeply impressive — "стаписа дори мен" (stunned even me).',
  'highly_respectful', 'sources/fb-archive-clean.md'
) ON CONFLICT ON CONSTRAINT relationships_shadow_id_person_label_relationship_type_key DO NOTHING;

INSERT INTO shadow.relationships (shadow_id, person_label, relationship_type, context, sentiment, source)
VALUES (
  'plamen', 'Vladislav Dramaliev', 'event_organizer',
  'Organized Bitcoin/Crypto conference Oct 17-19 2024 in Bulgaria. Plamen attended and promoted it. Previously referenced for Sep 2022 Kripo Revolucia conference.',
  'warm_collegial', 'sources/fb-archive-clean.md'
) ON CONFLICT ON CONSTRAINT relationships_shadow_id_person_label_relationship_type_key DO NOTHING;

INSERT INTO shadow.relationships (shadow_id, person_label, relationship_type, context, sentiment, source)
VALUES (
  'plamen', 'Elon Musk', 'admired_innovator',
  'Defends Musk purchase of Twitter as buying freedom of speech not profit. References SpaceX, Tesla, Neuralink, Starlink as world-transforming companies. Supportive of Musk supporting Trump to prevent censorship and one-party state.',
  'admiring', 'sources/fb-archive-clean.md'
) ON CONFLICT ON CONSTRAINT relationships_shadow_id_person_label_relationship_type_key DO NOTHING;
