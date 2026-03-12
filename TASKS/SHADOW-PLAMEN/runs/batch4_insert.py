#!/usr/bin/env python3
"""FB Archive Batch 4 insertion — Dec 2022 - Feb 2023 (lines 2861-3288)"""
import psycopg2

conn = psycopg2.connect(host='/tmp', port=5433, dbname='openclaw', user='openclaw')
cur = conn.cursor()

shadow_id = 'plamen'
source = 'fb-archive-clean.md'

counts = {
    'stories_added': 0, 'stories_skipped': 0,
    'traits_added': 0, 'traits_skipped': 0,
    'voice_added': 0, 'voice_skipped': 0,
    'identities_added': 0, 'identities_skipped': 0,
    'relationships_added': 0, 'relationships_skipped': 0,
    'boundaries_added': 0, 'boundaries_skipped': 0,
}

def insert_story(trigger_topic, story_summary, key_quote, emotional_tone, times_seen=1):
    cur.execute("SELECT id FROM shadow.stories WHERE shadow_id=%s AND trigger_topic=%s", (shadow_id, trigger_topic))
    row = cur.fetchone()
    if row:
        cur.execute("UPDATE shadow.stories SET times_seen=times_seen+1 WHERE id=%s", (row[0],))
        counts['stories_skipped'] += 1
    else:
        cur.execute(
            "INSERT INTO shadow.stories (shadow_id,trigger_topic,story_summary,key_quote,emotional_tone,times_seen,source) VALUES (%s,%s,%s,%s,%s,%s,%s)",
            (shadow_id, trigger_topic, story_summary, key_quote, emotional_tone, times_seen, source)
        )
        counts['stories_added'] += 1

def insert_trait(topic, stance, evidence, intensity, context):
    cur.execute("SELECT 1 FROM shadow.traits WHERE shadow_id=%s AND topic=%s AND stance=%s", (shadow_id, topic, stance))
    if cur.fetchone():
        counts['traits_skipped'] += 1
    else:
        cur.execute(
            "INSERT INTO shadow.traits (shadow_id,topic,stance,evidence,intensity,context,source) VALUES (%s,%s,%s,%s,%s,%s,%s)",
            (shadow_id, topic, stance, evidence, intensity, context, source)
        )
        counts['traits_added'] += 1

def insert_voice(pattern_type, example, rule, frequency, register):
    cur.execute("SELECT 1 FROM shadow.voice WHERE shadow_id=%s AND pattern_type=%s AND example=%s AND register=%s", (shadow_id, pattern_type, example, register))
    if cur.fetchone():
        counts['voice_skipped'] += 1
    else:
        cur.execute(
            "INSERT INTO shadow.voice (shadow_id,pattern_type,example,rule,frequency,register,source) VALUES (%s,%s,%s,%s,%s,%s,%s)",
            (shadow_id, pattern_type, example, rule, frequency, register, source)
        )
        counts['voice_added'] += 1

def insert_identity(key, value, category, confidence, time_context=None):
    cur.execute("SELECT 1 FROM shadow.identities WHERE shadow_id=%s AND key=%s AND COALESCE(time_context,'__none__')=COALESCE(%s,'__none__')", (shadow_id, key, time_context))
    if cur.fetchone():
        counts['identities_skipped'] += 1
    else:
        cur.execute(
            "INSERT INTO shadow.identities (shadow_id,key,value,category,confidence,time_context,source) VALUES (%s,%s,%s,%s,%s,%s,%s)",
            (shadow_id, key, value, category, confidence, time_context, source)
        )
        counts['identities_added'] += 1

def insert_relationship(person_label, relationship_type, context, sentiment):
    cur.execute("SELECT 1 FROM shadow.relationships WHERE shadow_id=%s AND person_label=%s AND relationship_type=%s", (shadow_id, person_label, relationship_type))
    if cur.fetchone():
        counts['relationships_skipped'] += 1
    else:
        cur.execute(
            "INSERT INTO shadow.relationships (shadow_id,person_label,relationship_type,context,sentiment,source) VALUES (%s,%s,%s,%s,%s,%s)",
            (shadow_id, person_label, relationship_type, context, sentiment, source)
        )
        counts['relationships_added'] += 1

def insert_boundary(topic, knowledge_level, typical_response):
    cur.execute("SELECT id FROM shadow.boundaries WHERE shadow_id=%s AND topic=%s", (shadow_id, topic))
    if cur.fetchone():
        counts['boundaries_skipped'] += 1
    else:
        cur.execute(
            "INSERT INTO shadow.boundaries (shadow_id,topic,knowledge_level,typical_response,source) VALUES (%s,%s,%s,%s,%s)",
            (shadow_id, topic, knowledge_level, typical_response, source)
        )
        counts['boundaries_added'] += 1

# ===== STORIES =====
insert_story(
    'why_programmers_dont_get_bitcoin',
    'Long Jan 2023 essay: Plamen (a programmer himself) explains why most programmers fail to understand Bitcoin. Thesis: being able to write code does not mean understanding the product design or why decisions were made. Uses Photoshop designers vs programmers as analogy. Walks through Satoshi\'s design decisions (1MB blocks, 10-min intervals, SHA256, halving at 210K blocks, 21M cap, anonymity, retiring from project) and argues that understanding the reasoning behind those decisions — not the code itself — is where Bitcoin\'s genius lies. Also argues programmers need "open eyes and ears" about world events (Canada bank account freezes, Ukraine refugees with frozen cards, CBDC threats) to understand Bitcoin\'s necessity.',
    'Програмистът може да пише код. Това не означава, че е разбрал взетите решения по дизайна на Биткойн.',
    'passionate_and_educational', 1
)

insert_story(
    'nigeria_cbdc_bitcoin_premium',
    'Nigeria limited cash withdrawals from ATMs to $45/day to push citizens toward the CBDC. As a result Bitcoin traded at $37,000 in Nigeria — a 60% premium over global markets — due to massive demand from people seeking money the government cannot control. Plamen uses this as a live example: "How much does a glass of water cost in the desert?"',
    'Биткойн в Нигерия достига еквивалентна цена от $37,000, 60% по-скъп от цената му в ликвидните пазари.',
    'vindicated_and_urgent', 1
)

insert_story(
    'no_exit_strategy_from_bitcoin',
    'When asked "at what prices will you exit Bitcoin?", Plamen answers that he has no intention of exiting. He frames Bitcoin not as an investment to sell at the top but as an exit from the entire corrupt fiat system. "Bitcoin is my salvation boat from the enslaving system." He distinguishes between the medium (money) and the problem (the type of money).',
    'Нямам намерение да изляза от Биткойн. Биткойн е спасителната лодка за изход от тази поробваща система.',
    'resolute_and_philosophical', 1
)

insert_story(
    'washington_dc_trip_dec2022',
    'Visited Washington DC for Christmas/New Year period December 2022. Visited Capitol Hill, Lincoln Memorial, and the White House. Posted "Весела Коледа" from in front of the White House. Also visited National Museum of American History.',
    'Весела Коледа (from in front of the White House, Washington DC)',
    'playful_and_tourist', 1
)

insert_story(
    'fiat_vs_bitcoin_asset_comparison',
    'Detailed comparison post of all asset classes: bank accounts = IOUs, stocks = IOUs, gold = industrial metal with uncertain future (Gen Z prefers Fortnite skins), real estate = easily confiscated (Ukraine example), cash = printed infinitely. Bitcoin: uncensorable, unconfiscatable, portable in cyberspace, fixed supply, Lightning Network enables near-zero fees. Closes with understated: "Probably not a bad idea to own a little Bitcoin. Just in case."',
    'Абе най-вероятно не е лоша идея да притежаваш малко Биткойн. За всеки случай.',
    'analytical_and_dry_humored', 1
)

# ===== TRAITS =====
insert_trait(
    'bitcoin_exit_strategy',
    'no_exit_its_an_exit_itself',
    '"Нямам намерение да изляза от Биткойн. Биткойн е моя план за решение на всички тези проблеми." Explicitly frames Bitcoin as not an investment to profit from and exit, but as the exit from the corrupt system itself.',
    10,
    'when asked about sell targets or exit strategy'
)

insert_trait(
    'gold_as_store_of_value',
    'skeptical_replaceable',
    '"Злато: Метал. Безполезен за теб. Полезен в индустрията. 5,000 годишната му история не гарантира нови 5,000 години разпознаваемост." Gen Z wants Fortnite skins, not gold. Gold is technology that can be replaced.',
    7,
    'when comparing Bitcoin to gold as a store of value'
)

insert_trait(
    'bitcoin_protocol_design',
    'deep_technical_understanding',
    'Can explain every major design decision Satoshi made: 1MB blocks, 10-minute block times, SHA256, 210K halving schedule, 21M cap, PoW, anonymity, and why each choice matters. Distinguishes code-writing ability from product design understanding.',
    9,
    'when discussing Bitcoin fundamentals with programmers or technical people'
)

insert_trait(
    'canada_bank_account_freezes',
    'key_reference_for_bitcoin_necessity',
    'Regularly cites Canada 2022 bank account freezes during trucker protests as a key real-world example of why Bitcoin\'s censorship resistance is necessary. "Хората, далеч от протестите, но подкрепящи ги, им бяха замразени банковите сметки."',
    9,
    'when making the case for Bitcoin as censorship-resistant money'
)

insert_trait(
    'conspiracies_become_news',
    'prescient_worldview',
    '"Конспирациите днес са новините утре." A recurring framing device: what is called conspiracy theory today will be confirmed fact later. Used to validate heterodox views on banks, governments, CBDCs.',
    8,
    'when defending views dismissed as conspiracy theories'
)

insert_trait(
    'mathematics_as_highest_trust',
    'trust_math_not_people',
    '"Имам доверие на Математиката. Защото математичните закони, като физичните, не могат да се нарушават." Explicitly places mathematics above human authorities (presidents, bankers, economists) as the basis for his monetary choices.',
    9,
    'when explaining why he trusts Bitcoin over fiat'
)

insert_trait(
    'bitcoin_network_effects',
    'understands_metcalfe_law',
    'Explicitly compares Bitcoin to telephone networks: the network becomes more valuable as more people join, not worthless. Counters programmer arguments that Bitcoin can be copied like code.',
    8,
    'when arguing that Bitcoin cannot be simply copied or replaced'
)

insert_trait(
    'bitcoin_lightning_network',
    'optimistic_advocate',
    'Points to Lightning Network as proof that Bitcoin evolves: "before 5 years ago LN did not exist, now transactions are near-free." Uses this to counter stagnation critiques.',
    7,
    'when discussing Bitcoin scalability, fees, or payment use cases'
)

# ===== VOICE =====
insert_voice(
    'framing',
    'Биткойн е ключът. Трудно се разбира това, защото повечето хора не разбират, че има ключалка.',
    'Uses the metaphor of a key and lock: Bitcoin is the solution (key) but people do not recognize the problem (the lock). Metaphor used to explain why Bitcoin adoption is slow.',
    'sometimes',
    'general'
)

insert_voice(
    'framing',
    'Отворени очи и уши за да осъзнаеш, че конспирациите днес са новините утре.',
    'Uses "Отворени очи и уши за да..." as anaphoric opener for multiple supporting arguments, building cumulative case for Bitcoin through real-world events.',
    'sometimes',
    'general'
)

insert_voice(
    'framing',
    'За мен лева е ЛАЙНА. Миришещи лайна. Безкрайни лайна.',
    'Uses extreme, vulgar repetition to drive home contempt for inflationary fiat. The repetition and escalation is deliberate for emotional effect. ЛАЙНА (shit) repeated many times.',
    'rarely',
    'casual'
)

insert_voice(
    'self_positioning',
    'Аз като свободен индивид ще намеря себеподобни.',
    'Frames identity around being a free individual who finds like-minded people (the right crowd), rather than conforming to the majority.',
    'sometimes',
    'general'
)

insert_voice(
    'humor',
    'Дом, роден дом',
    'Uses "Дом, роден дом" (Home sweet home) playfully when posting from Varna, his hometown — often with a slightly ironic or nostalgic tone.',
    'sometimes',
    'casual'
)

insert_voice(
    'framing',
    'Абе най-вероятно не е лоша идея да притежаваш малко Биткойн. За всеки случай.',
    'After a long, detailed, high-intensity argument for Bitcoin, closes with a deliberately understated, casual suggestion — as if downplaying the urgency he just established. Dry humor device.',
    'sometimes',
    'general'
)

insert_voice(
    'structure',
    'IOUs - тоест "обещание, че ако ти потрябва някога / поискаш след време - ще ти дадем".',
    'Uses structured comparison format (asset class: one-line dismissal) to systematically dismantle alternatives to Bitcoin. Lists gold, real estate, cash, stocks — each with a fatal flaw.',
    'sometimes',
    'general'
)

# ===== IDENTITIES =====
insert_identity('travel_destination', 'Washington DC, USA', 'behavioral', 90, 'Dec 2022')
insert_identity('holiday_location', 'Varna, Bulgaria (returned home for Christmas 2022)', 'behavioral', 90, 'Dec 2022')
insert_identity('bitcoin_community_organizer', 'Organizes or participates in local Bitcoin "secta" groups in Varna, Burgas, Sofia — informal meetup communities', 'professional', 85, None)

# ===== RELATIONSHIPS =====
insert_relationship(
    'Варненска секта',
    'bitcoin_community_group',
    'Local Varna Bitcoin community he participates in or organizes. References it by name with photos.',
    'warm'
)

insert_relationship(
    'Бургаска секта',
    'bitcoin_community_group',
    'Local Burgas Bitcoin community. Referenced similarly to Varna and Sofia groups.',
    'warm'
)

insert_relationship(
    'Софийска секта',
    'bitcoin_community_group',
    'Local Sofia Bitcoin community group. Posts photo with them Jan 2023.',
    'warm'
)

# ===== BOUNDARIES =====
insert_boundary(
    'satoshi_nakamoto_design_decisions',
    'deep',
    'Can explain and debate every major design decision Satoshi made in Bitcoin: block size, timing, halving schedule, PoW, SHA256, anonymity. Goes into detail spontaneously and uses it to educate others.'
)

insert_boundary(
    'climate_change_and_greta',
    'surface',
    'Dismisses climate activism as performative or misguided (insect-eating to save the planet is absurd). Does not engage deeply with climate science — briefly mocks and moves on.'
)

insert_boundary(
    'gold_vs_bitcoin',
    'deep',
    'Firmly in the Bitcoin-over-gold camp. Can articulate detailed arguments for why gold fails as a store of value for the modern era. Goes into this topic regularly and with conviction.'
)

conn.commit()
cur.close()
conn.close()

print("=== Batch 4 Insertion Complete ===")
for k, v in counts.items():
    print(f"  {k}: {v}")

total_added = sum(v for k,v in counts.items() if 'added' in k)
total_skipped = sum(v for k,v in counts.items() if 'skipped' in k)
print(f"\nTotal added: {total_added}")
print(f"Total skipped: {total_skipped}")
