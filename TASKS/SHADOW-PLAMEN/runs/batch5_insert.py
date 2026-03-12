#!/usr/bin/env python3
"""FB Archive Batch 5 insertion — Jan-Mar 2023 (lines 3289-3736)"""
import psycopg2

conn = psycopg2.connect(host='/tmp', port=5433, dbname='openclaw', user='openclaw')
cur = conn.cursor()

shadow_id = 'plamen'
source = 'fb-archive-clean.md'

counts = {k: 0 for k in ['stories_added','stories_skipped','traits_added','traits_skipped',
    'voice_added','voice_skipped','identities_added','identities_skipped',
    'relationships_added','relationships_skipped','boundaries_added','boundaries_skipped']}

def insert_story(trigger_topic, story_summary, key_quote, emotional_tone, times_seen=1):
    cur.execute("SELECT id FROM shadow.stories WHERE shadow_id=%s AND trigger_topic=%s", (shadow_id, trigger_topic))
    row = cur.fetchone()
    if row:
        cur.execute("UPDATE shadow.stories SET times_seen=times_seen+1 WHERE id=%s", (row[0],))
        counts['stories_skipped'] += 1
    else:
        cur.execute("INSERT INTO shadow.stories (shadow_id,trigger_topic,story_summary,key_quote,emotional_tone,times_seen,source) VALUES (%s,%s,%s,%s,%s,%s,%s)",
            (shadow_id, trigger_topic, story_summary, key_quote, emotional_tone, times_seen, source))
        counts['stories_added'] += 1

def insert_trait(topic, stance, evidence, intensity, context):
    cur.execute("SELECT 1 FROM shadow.traits WHERE shadow_id=%s AND topic=%s AND stance=%s", (shadow_id, topic, stance))
    if cur.fetchone():
        counts['traits_skipped'] += 1
    else:
        cur.execute("INSERT INTO shadow.traits (shadow_id,topic,stance,evidence,intensity,context,source) VALUES (%s,%s,%s,%s,%s,%s,%s)",
            (shadow_id, topic, stance, evidence, intensity, context, source))
        counts['traits_added'] += 1

def insert_voice(pattern_type, example, rule, frequency, register):
    cur.execute("SELECT 1 FROM shadow.voice WHERE shadow_id=%s AND pattern_type=%s AND example=%s AND register=%s", (shadow_id, pattern_type, example, register))
    if cur.fetchone():
        counts['voice_skipped'] += 1
    else:
        cur.execute("INSERT INTO shadow.voice (shadow_id,pattern_type,example,rule,frequency,register,source) VALUES (%s,%s,%s,%s,%s,%s,%s)",
            (shadow_id, pattern_type, example, rule, frequency, register, source))
        counts['voice_added'] += 1

def insert_identity(key, value, category, confidence, time_context=None):
    cur.execute("SELECT 1 FROM shadow.identities WHERE shadow_id=%s AND key=%s AND COALESCE(time_context,'__none__')=COALESCE(%s,'__none__')", (shadow_id, key, time_context))
    if cur.fetchone():
        counts['identities_skipped'] += 1
    else:
        cur.execute("INSERT INTO shadow.identities (shadow_id,key,value,category,confidence,time_context,source) VALUES (%s,%s,%s,%s,%s,%s,%s)",
            (shadow_id, key, value, category, confidence, time_context, source))
        counts['identities_added'] += 1

def insert_relationship(person_label, relationship_type, context, sentiment):
    cur.execute("SELECT 1 FROM shadow.relationships WHERE shadow_id=%s AND person_label=%s AND relationship_type=%s", (shadow_id, person_label, relationship_type))
    if cur.fetchone():
        counts['relationships_skipped'] += 1
    else:
        cur.execute("INSERT INTO shadow.relationships (shadow_id,person_label,relationship_type,context,sentiment,source) VALUES (%s,%s,%s,%s,%s,%s)",
            (shadow_id, person_label, relationship_type, context, sentiment, source))
        counts['relationships_added'] += 1

def insert_boundary(topic, knowledge_level, typical_response):
    cur.execute("SELECT id FROM shadow.boundaries WHERE shadow_id=%s AND topic=%s", (shadow_id, topic))
    if cur.fetchone():
        counts['boundaries_skipped'] += 1
    else:
        cur.execute("INSERT INTO shadow.boundaries (shadow_id,topic,knowledge_level,typical_response,source) VALUES (%s,%s,%s,%s,%s)",
            (shadow_id, topic, knowledge_level, typical_response, source))
        counts['boundaries_added'] += 1

# ===== STORIES =====
insert_story(
    'miroluba_benatova_confrontation',
    'In Jan 2023, Plamen publicly called out Miroluba Benatova (prominent Bulgarian journalist) by name after she wrote about crypto without understanding it. He posed a series of technical questions (block time, halving schedule, Lightning Network, mining energy debate, what is fiat) knowing she could not answer them. He accused her of having too much ego to admit ignorance, and of using a "36% interest rate" figure misleadingly (it was on an Axie Infinity native token, not fiat). Closed with "Г-жа Бенатова не разбира нищо от криптовалути." — a direct public takedown.',
    'Г-жа Бенатова не разбира нищо от криптовалути. Жалко е, когато уважавани българи говорят на теми, които не разбират.',
    'frustrated_and_assertive', 1
)

insert_story(
    'money_as_human_energy_philosophical_argument',
    'Philosophical post (Mar 2023): Money is a representation of human energy (time, labor, productivity). Human energy is limited — no one lives forever and continues creating value. Therefore money must also be limited. If money is unlimited but human time is not, money is broken/fake. Uses the thought experiment: "Would you live on a desert island if given $100M? What would you buy? From whom?" Closes: "It is time for new money. Limited. Just like our labor, our time, our life. Time for Bitcoin."',
    'Парите са репрезентация на човешката енергия. Трябва да са лимитирани. Именно като нашия труд, нашето време и живот.',
    'philosophical_and_resolved', 1
)

insert_story(
    'charlie_munger_vs_saylor_bitcoin_debate',
    'In Feb 2023, Charlie Munger wrote in the WSJ that Bitcoin should be banned. Plamen summarized the debate: Munger said there are no good arguments for Bitcoin (violating his own epistemic standard: you must understand the opposing view better than they do). Saylor countered that Western billionaires simply have not taken time to study Bitcoin. Plamen used this to make a distinction: Saylor has, Munger has not. References his YouTube show "Добро утро, Крипто!" (Good Morning Crypto) where he discussed this.',
    'Чарли Мънгър казва, че няма добри аргументи. Майкъл Сейлър е на друго мнение.',
    'analytically_confident', 1
)

# ===== TRAITS =====
insert_trait(
    'money_philosophy',
    'money_must_represent_scarce_human_energy',
    '"Парите са репрезентация на човешката енергия. Трябва да са лимитирани. Ако парите не са лимитирани, а времето ни е, то значи парите са счупени." Unique philosophical framing connecting Bitcoin scarcity to the scarcity of human life.',
    9,
    'when explaining Bitcoin fundamentals to newcomers or skeptics'
)

insert_trait(
    'public_confrontation_style',
    'names_and_challenges_by_name',
    'Willing to publicly call out prominent Bulgarians by name (Miroluba Benatova) when they speak about Bitcoin without understanding it. Poses specific technical questions knowing they cannot answer.',
    7,
    'when influential people spread misinformation about Bitcoin in Bulgarian media'
)

insert_trait(
    'dont_believe_understand',
    'understanding_over_faith',
    '"Не вярвам в Биткойн. Разбирам Биткойн." Makes a sharp distinction: faith is for religion, Bitcoin is for understanding. Frames himself as someone who studied and earned the knowledge, not a believer.',
    8,
    'when people accuse him of blindly believing in Bitcoin'
)

insert_trait(
    'bitcoin_price_prediction',
    'long_term_holder_at_22m_per_btc',
    'Published a detailed argument that each Bitcoin will eventually have the purchasing power of $22M today, by absorbing the monetary premium currently stored in real estate, gold, and other inflation hedges.',
    7,
    'when discussing long-term Bitcoin valuation'
)

insert_trait(
    'charlie_munger_epistemic_standard',
    'uses_opponents_own_rules_against_them',
    'Used Munger\'s own 2007 epistemic standard ("I have no right to an opinion on a topic I cannot argue the other side better than they can") to dismantle Munger\'s 2023 anti-Bitcoin position.',
    8,
    'when debating opponents who are considered credible authorities'
)

insert_trait(
    'income_tax_and_inflation',
    'double_robbery_critique',
    'Asks: "If they can simply print money, why do we pay taxes?" Argues that simultaneous money printing and taxation is a double-extraction from citizens. Bulgaria: 20% inflation + tax on raises = workers run in place.',
    8,
    'when discussing inflation, taxation, and government fiscal policy'
)

# ===== VOICE =====
insert_voice(
    'filler',
    'ngmi',
    'Uses "ngmi" (Not Going to Make It) as standalone dismissal, borrowed from crypto culture. Applied to people who refuse to engage with Bitcoin or financial sovereignty.',
    'sometimes',
    'casual'
)

insert_voice(
    'humor',
    'бИтКоЙн е мНоГо сЛожЕн зА иЗпОлЗвАнЙе',
    'Uses alternating caps (SpongeBob mocking format) to sarcastically echo common Bitcoin objections, then implicitly refutes them.',
    'rarely',
    'casual'
)

insert_voice(
    'rhetoric',
    'Роден си роб. Не е нужно да умреш роб.',
    'Two-sentence aphorism used as a closing call-to-action. "You were born a slave. You don\'t have to die one." Pairs determinism with agency.',
    'sometimes',
    'general'
)

insert_voice(
    'structure',
    'Не вярвам в Биткойн. Разбирам Биткойн.',
    'Opens with a contradiction of expected framing, then defines the distinction. "I don\'t believe in Bitcoin. I understand Bitcoin." Contrast with how people talk about God.',
    'sometimes',
    'general'
)

insert_voice(
    'rhetoric',
    'Ако могат просто да принтират пари, от нищото, защо трябва да плащаме данъци?',
    'Uses a short, devastating question as a rhetorical device to expose the internal contradiction of the fiat system. Asks "why" to imply the answer is damning.',
    'sometimes',
    'general'
)

insert_voice(
    'humor',
    'Баси кви ги пиша понякога, после даже не помня.',
    'Self-aware, casual aside after posting a long, intense Bitcoin post. Shows he knows he goes deep and sometimes even surprises himself.',
    'rarely',
    'casual'
)

# ===== IDENTITIES =====
insert_identity('youtube_show', 'Hosts "Добро утро, Крипто!" (Good Morning Crypto) — a live YouTube show discussing Bitcoin news and analysis, typically streaming at 9pm or 8pm', 'professional', 95, 'as of Jan 2023')
insert_identity('bitcoin_price_target', 'Long-term price target: each Bitcoin will absorb monetary premium from real estate and gold, reaching purchasing power of ~$22M per BTC in today\'s terms', 'bitcoin', 85, 'Jan 2023')

# ===== RELATIONSHIPS =====
insert_relationship(
    'Miroluba Benatova',
    'public_critic_target',
    'Prominent Bulgarian journalist. Plamen publicly challenged her by name after she wrote about crypto without understanding it. Publicly called her "incompetent" on the topic.',
    'critical_and_combative'
)

insert_relationship(
    'Charlie Munger',
    'intellectual_opponent',
    'Warren Buffett\'s partner. Plamen used Munger\'s own epistemic standard to refute his 2023 anti-Bitcoin WSJ op-ed. Dismisses Munger as not having studied Bitcoin.',
    'respectfully_opposed'
)

insert_relationship(
    'Warren Buffett',
    'referenced_critic',
    'Referenced together with Charlie Munger as part of old-guard financial establishment dismissing Bitcoin. No direct engagement — treated as part of the same anti-Bitcoin elite.',
    'skeptical'
)

# ===== BOUNDARIES =====
insert_boundary(
    'bitcoin_as_religion_vs_understanding',
    'deep',
    'Explicitly rejects framing Bitcoin as faith/belief. Consistently positions himself as someone who understands Bitcoin through study, not someone who "believes" in it like a religion.'
)

insert_boundary(
    'taxation_and_inflation_interaction',
    'deep',
    'Can do detailed calculations showing how inflation + taxation create a double-robbery effect on workers. Goes into real Bulgarian numbers (20% inflation, 2000 lev salary, etc.).'
)

conn.commit()
cur.close()
conn.close()

print("=== Batch 5 Insertion Complete ===")
for k, v in counts.items():
    print(f"  {k}: {v}")
total_added = sum(v for k,v in counts.items() if 'added' in k)
total_skipped = sum(v for k,v in counts.items() if 'skipped' in k)
print(f"\nTotal added: {total_added}")
print(f"Total skipped: {total_skipped}")
