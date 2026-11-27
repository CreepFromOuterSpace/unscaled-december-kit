# -*- coding: utf-8 -*-
"""All post content for the 4-week sample calendar (Nov 30 – Dec 26, 2026).

Facts were checked against the sources listed on each post on Nov 27, 2026.
Hiring posts reflect postings live on that date: re-check before publishing.
Edit BRAND_HANDLE, then run render.py to regenerate every image.
"""

BRAND_HANDLE = "@unscaled.co"
TZ_OFFSET = "-05:00"  # US Eastern (standard time) for every December date below

HIRE_NOTE = "Re-check the posting the day before. If the role is closed or the range changed, update or swap the post."
DATE_NOTE = "Date-specific: keep on this day."

POSTS = [
    # ───────────────────────── WEEK 1 ─────────────────────────
    {
        "id": "2026-11-30-ipo-wait",
        "date": "2026-11-30", "time": "08:30", "pillar": "Data",
        "title": "How long they waited to go public",
        "slides": [
            {"tpl": "data_cover", "title": "How long they waited to go public",
             "stats": [("12", "years for Airbnb, 2008 to 2020"), ("3", "years for Amazon, 1994 to 1997")]},
            {"tpl": "bars", "title": "From founding to IPO",
             "sub": "Years between the founding year and the IPO year",
             "rows": [("Airbnb", "2008–2020", 12), ("Microsoft", "1975–1986", 11), ("Uber", "2009–2019", 10),
                      ("Facebook", "2004–2012", 8), ("Snowflake", "2012–2020", 8), ("Google", "1998–2004", 6),
                      ("Nvidia", "1993–1999", 6), ("Netflix", "1997–2002", 5), ("Apple", "1976–1980", 4),
                      ("Amazon", "1994–1997", 3)],
             "unit": "yrs", "foot": "Sources: company histories and SEC filings"},
            {"tpl": "note", "text": "The four founded after 2000 took 8 to 12 years. The four founded in the 1990s took 3 to 6.",
             "small": "Would you rather go public at year 3 or year 12?"},
        ],
        "caption": (
            "Airbnb waited 12 years to go public. Amazon waited 3.\n\n"
            "We lined up 10 giants by the gap between the year they were founded and the year they listed. "
            "The four founded after 2000 (Facebook, Airbnb, Uber, Snowflake) took 8 to 12 years. "
            "The four founded in the 1990s (Nvidia, Amazon, Netflix, Google) took 3 to 6.\n\n"
            "Microsoft is the outlier from the ’70s: 11 years, from 1975 to its 1986 IPO.\n\n"
            "Which number surprised you most?\n\n"
            "Sources: company histories and SEC filings\n\n"
            "#startups #ipo #venturecapital #founders"),
        "alt": "Leaderboard of ten companies ranked by years from founding to IPO, from Airbnb at 12 years to Amazon at 3.",
        "sources": [("Engadget: Apple IPO, Dec 12, 1980", "https://www.engadget.com/2013/12/12/33-years-ago-today-apple-launched-its-ipo/"),
                    ("Wikipedia: Airbnb IPO, Dec 10, 2020 (via Joe Gebbia)", "https://wikipedia.com/wiki/Joe_Gebbia")],
        "notes": "Other founding and IPO years are standard company-history facts.",
    },
    {
        "id": "2026-12-01-airbnb-cereal",
        "date": "2026-12-01", "time": "08:30", "pillar": "Founder story",
        "title": "In 2008, cereal kept Airbnb alive",
        "year": "2008",
        "slides": [
            {"tpl": "story_cover", "headline": "In 2008, cereal kept Airbnb alive."},
            {"tpl": "story", "text": "Summer 2008. Brian Chesky, Joe Gebbia and Nathan Blecharczyk had a site called AirBed & Breakfast, a pile of credit card debt and no investors who wanted in."},
            {"tpl": "story", "fig": "$40", "text": "So they designed election-themed cereal, Obama O’s and Cap’n McCain’s, and sold the boxes as collector’s items for $40 each."},
            {"tpl": "story", "fig": "$30,000", "text": "The stunt brought in about $30,000 and helped pay down their credit cards."},
            {"tpl": "story", "text": "At their Y Combinator interview, Paul Graham didn’t like the idea of strangers sleeping in each other’s homes. As they were leaving, Gebbia handed him a box."},
            {"tpl": "story", "text": "As Chesky tells it, Graham’s logic was simple: anyone who can get people to pay $40 for $4 cereal might get strangers to share a home."},
            {"tpl": "story", "text": "Y Combinator invested $20,000 for 6% in January 2009. Airbnb went public in December 2020."},
            {"tpl": "story_end", "text": "Investors couldn’t judge the idea yet. They could judge the founders, and the cereal proved they wouldn’t quit."},
        ],
        "caption": (
            "In 2008, cereal kept Airbnb alive.\n\n"
            "Out of cash and with investors uninterested, the founders designed two election-themed cereals, "
            "Obama O’s and Cap’n McCain’s, and sold the boxes for $40 each. They made about $30,000.\n\n"
            "The boxes did something better than pay the bills: they won over Paul Graham, who had doubts about the idea itself. "
            "Y Combinator invested $20,000 for 6% in January 2009.\n\n"
            "Save this for the next time someone says you need funding to start.\n\n"
            "Sources: Fortune (2023), UChicago Polsky Center (2021)\n\n"
            "#airbnb #founders #startups #ycombinator"),
        "alt": "Text slides telling how Airbnb’s founders sold $40 election-themed cereal boxes in 2008 to fund the company.",
        "sources": [("Fortune (2023)", "https://fortune.com/2023/04/19/airbnb-ceo-cereal-box-investors-changed-everything-billion-dollar-company/"),
                    ("UChicago Polsky Center (2021)", "https://polsky.uchicago.edu/2021/05/24/fireside-chat-polsky-airbnb-cofounder-nathan-blecharczyk/")],
        "notes": "",
    },
    {
        "id": "2026-12-02-hiring-ramp",
        "date": "2026-12-02", "time": "08:30", "pillar": "Hiring",
        "title": "Ramp: Software Engineer, Backend, AI Ventures",
        "slides": [
            {"tpl": "hire", "headline": "Ramp is hiring builders and former founders",
             "role": "Software Engineer, Backend, AI Ventures", "loc": "New York, hybrid",
             "salary": "$204K–$330K", "sub": "Base salary, plus equity",
             "asof": "Posted range as of Nov 27, 2026. Source: Ramp careers page."},
        ],
        "caption": (
            "Ramp is hiring builders and former founders for its AI Ventures team.\n\n"
            "Role: Software Engineer, Backend, AI Ventures\n"
            "Location: New York (hybrid)\n"
            "Posted base salary: $204K–$330K, plus equity\n\n"
            "Ramp says final pay depends on location and level. Range checked on Nov 27, 2026. Roles close, so confirm on Ramp’s careers page before applying.\n\n"
            "Know someone who should see this? Send it to them.\n\n"
            "We’re not affiliated with Ramp, and this isn’t sponsored.\n\n"
            "#hiring #startupjobs #softwareengineering #ai"),
        "alt": "Hiring card: Ramp is hiring builders and former founders. Software Engineer, Backend, AI Ventures, New York, $204K to $330K base salary plus equity.",
        "sources": [("Ramp job posting (Ashby)", "https://jobs.ashbyhq.com/ramp/3cfbf693-58e3-423f-87a8-a93dbd0839b0")],
        "notes": HIRE_NOTE,
    },
    {
        "id": "2026-12-03-jevons-paradox",
        "date": "2026-12-03", "time": "08:30", "pillar": "Explainer",
        "title": "Will cheaper AI mean more AI? The Jevons paradox",
        "slides": [
            {"tpl": "ex_cover", "headline": "Will cheaper AI mean more AI?", "sub": "The Jevons paradox, explained", "art": "jevons"},
            {"tpl": "ex_text", "text": "1865. Britain ran on coal and worried about running out. The hoped-for fix was more efficient steam engines."},
            {"tpl": "ex_text", "text": "Economist William Stanley Jevons argued the opposite. In his book The Coal Question, he said efficiency would raise coal use, not cut it."},
            {"tpl": "ex_diagram", "diagram": "jevons_chain", "caption": "His reasoning, in four steps."},
            {"tpl": "ex_text", "text": "Jan 27, 2025. DeepSeek’s low-cost model rattled AI stocks. Microsoft CEO Satya Nadella answered by citing Jevons: as AI gets cheaper, use should soar."},
            {"tpl": "ex_text", "text": "The catch: economists find efficiency usually causes a partial rebound in use, not a full reversal. A true Jevons paradox needs demand to explode."},
            {"tpl": "ex_end", "text": "When something gets 10x cheaper, don’t only ask who saves money. Ask what people will start doing that they never did before."},
        ],
        "caption": (
            "Will cheaper AI mean more AI?\n\n"
            "In 1865, economist William Stanley Jevons argued that more efficient steam engines wouldn’t save Britain’s coal. "
            "Cheaper power would invite new uses, and total coal use would climb. That idea is now called the Jevons paradox.\n\n"
            "It came roaring back in January 2025, when Microsoft CEO Satya Nadella cited it the day DeepSeek’s low-cost model shook AI stocks.\n\n"
            "Economists add a caveat: efficiency usually produces a partial rebound in demand, not a full backfire.\n\n"
            "Sources: NPR Planet Money (2025), Fortune (Jan 27, 2025), Northeastern University (2025)\n\n"
            "#ai #economics #startups #tech"),
        "alt": "Explainer carousel on the Jevons paradox: more efficient steam engines in 1865 Britain led to more coal use, and the idea’s revival in AI in 2025.",
        "sources": [("NPR Planet Money (2025)", "https://npr.org/sections/planet-money/2025/02/04/g-s1-46018/ai-deepseek-economics-jevons-paradox"),
                    ("Fortune (Jan 27, 2025)", "https://www.fortune.com/2025/01/27/microsoft-ceo-satya-nadella-deepseek-optimism-jevons-paradox/"),
                    ("Northeastern University (2025)", "https://news.northeastern.edu/2025/02/07/jevons-paradox-ai-future")],
        "notes": "The four-step diagram is a schematic of Jevons’s argument, not data.",
    },
    {
        "id": "2026-12-04-microsoft-basic",
        "date": "2026-12-04", "time": "08:30", "pillar": "Founder story",
        "title": "Microsoft’s first product was sold before it existed",
        "year": "1975",
        "slides": [
            {"tpl": "story_cover", "headline": "Microsoft’s first product was sold before it existed."},
            {"tpl": "story", "text": "December 1974. Bill Gates and Paul Allen see the Altair 8800, a build-it-yourself computer, in the January 1975 issue of Popular Electronics."},
            {"tpl": "story", "text": "They contact its maker, MITS, offering a version of the BASIC programming language for it. They haven’t written it yet."},
            {"tpl": "story", "text": "They don’t own an Altair either. Allen builds a simulator of its chip on Harvard’s PDP-10, and they code day and night for about two months. Classmate Monte Davidoff writes the math routines."},
            {"tpl": "story", "text": "March 1975. On the flight to Albuquerque, Allen realizes they never wrote the loader that gets the program into the machine. He writes it in machine code before landing."},
            {"tpl": "story", "text": "The demo works. MITS licenses the software, the first product of a company its founders spelled “Micro-Soft.”"},
            {"tpl": "story_end", "text": "They found the customer first, then built against a deadline they couldn’t miss."},
        ],
        "caption": (
            "Microsoft’s first product was sold before it existed.\n\n"
            "In early 1975, Bill Gates and Paul Allen told MITS, maker of the Altair 8800, that they had BASIC software for its new computer. They didn’t. "
            "With no Altair of their own, they wrote it on a simulator Allen built on Harvard’s PDP-10, with Monte Davidoff writing the math routines.\n\n"
            "Allen wrote the last missing piece, the loader, on the plane to the demo. It worked, MITS licensed it, and Microsoft was officially founded on April 4, 1975.\n\n"
            "Sources: Computer History Museum, The New Stack, Wikipedia (Altair BASIC)\n\n"
            "#microsoft #founders #startups #techhistory"),
        "alt": "Text slides on how Bill Gates and Paul Allen sold Altair BASIC to MITS in 1975 before writing it.",
        "sources": [("Computer History Museum", "https://www.computerhistory.org/revolution/personal-computers/17/312/1144"),
                    ("The New Stack", "https://thenewstack.io/bill-gates-paul-allen-and-the-code-that-started-microsoft/"),
                    ("Wikipedia: Altair BASIC", "https://en.wikipedia.org/wiki/Altair_BASIC"),
                    ("heise: April 4, 1975", "https://heise.de/-10339711")],
        "notes": "",
    },
    {
        "id": "2026-12-05-first-text-message",
        "date": "2026-12-05", "time": "10:00", "pillar": "History",
        "title": "This week in 1992: the first text message",
        "slides": [
            {"tpl": "hist_cover", "label": "This week in 1992", "big": "Dec 3", "title": "The first text message", "art": "sms"},
            {"tpl": "hist_facts", "facts": [
                "Neil Papworth, a 22-year-old test engineer at Sema Group, sent it.",
                "He typed it on a PC. Phones didn’t have keyboards yet.",
                "It went to Vodafone director Richard Jarvis, who was at the office holiday party.",
                "Jarvis read it on an Orbitel 901 that weighed about 2.1 kg. He had no way to reply."]},
        ],
        "caption": (
            "34 years ago this week, someone sent the first text message. It said “Merry Christmas.”\n\n"
            "On Dec 3, 1992, Neil Papworth, a 22-year-old engineer at Sema Group, typed it on a computer and sent it over Vodafone’s network "
            "to director Richard Jarvis, who was at the company holiday party.\n\n"
            "Jarvis’s phone, an Orbitel 901, weighed about 2.1 kg and had no way to type a reply.\n\n"
            "Sources: Vodafone UK News Centre (2022), History.com, Wikipedia\n\n"
            "#techhistory #sms #mobile #onthisday"),
        "alt": "History card: Dec 3, 1992, the first text message, which read Merry Christmas.",
        "sources": [("Vodafone UK News Centre (2022)", "https://www.vodafone.co.uk/newscentre/our-network/merry-christmas-the-30th-anniversary-of-the-first-text-message/"),
                    ("History.com", "https://history.com/this-day-in-history/first-sms-text-message-sent"),
                    ("Wikipedia: Neil Papworth", "https://en.wikipedia.org/wiki/Neil_Papworth")],
        "notes": DATE_NOTE,
    },
    # ───────────────────────── WEEK 2 ─────────────────────────
    {
        "id": "2026-12-07-before-they-were-famous",
        "date": "2026-12-07", "time": "08:30", "pillar": "Data",
        "title": "Before they were famous",
        "slides": [
            {"tpl": "data_cover", "title": "Before they were famous",
             "stats": [("9", "companies that started as something else")]},
            {"tpl": "pivots", "title": "What they were first",
             "rows": [("Nokia", "A paper mill, founded in 1865"),
                      ("Nintendo", "A playing-card maker, founded in 1889"),
                      ("Wrigley", "Soap and baking powder, with gum as a freebie"),
                      ("Flickr", "A feature of an online game"),
                      ("Shopify", "An online snowboard shop"),
                      ("YouTube", "A video dating site"),
                      ("Twitter", "A side project at a podcasting startup"),
                      ("Instagram", "A check-in app called Burbn"),
                      ("Slack", "A tool built inside a game studio")],
             "foot": "Sources: company histories; Tubefilter (2016) on YouTube"},
            {"tpl": "note", "text": "Stewart Butterfield did it twice. Flickr and Slack both grew out of online games that didn’t work out.",
             "small": "The first idea is rarely the one that wins."},
        ],
        "caption": (
            "Before they were famous.\n\n"
            "Nintendo made playing cards. Nokia was a paper mill. YouTube was pitched as a video dating site. "
            "Twitter was a side project at a podcasting startup. Instagram began as Burbn, a check-in app.\n\n"
            "And Stewart Butterfield pulled it off twice: Flickr and Slack both grew out of online games that didn’t work out.\n\n"
            "Save this for your next pivot.\n\n"
            "Sources: company histories; Tubefilter (2016) on YouTube’s dating-site origins\n\n"
            "#startups #pivot #founders #entrepreneurship"),
        "alt": "List of nine companies and what they started as, from Nokia as a paper mill to Slack as a tool inside a game studio.",
        "sources": [("Tubefilter (2016): YouTube’s dating-site origin", "https://tubefilter.com/2016/03/15/youtube-dating-site-steve-chen/")],
        "notes": "",
    },
    {
        "id": "2026-12-08-dropbox-usb",
        "date": "2026-12-08", "time": "08:30", "pillar": "Founder story",
        "title": "Dropbox started with a forgotten USB drive",
        "year": "2008",
        "slides": [
            {"tpl": "story_cover", "headline": "Dropbox started with a forgotten USB drive."},
            {"tpl": "story", "text": "Drew Houston was on a bus from Boston to New York with work to do. He’d forgotten his thumb drive. Again."},
            {"tpl": "story", "text": "Annoyed with himself, he opened his laptop and started coding a fix: files that keep themselves in sync."},
            {"tpl": "story", "text": "Syncing was hard to explain in words, so he showed it instead, in a short demo video."},
            {"tpl": "story", "fig": "75,000", "text": "In March 2008, a new demo packed with in-jokes for Digg’s audience took the beta waitlist from 5,000 to 75,000 in a day."},
            {"tpl": "story", "text": "Ten years later, in 2018, Dropbox went public."},
            {"tpl": "story_end", "text": "If your product is hard to describe, stop describing it. Show it."},
        ],
        "caption": (
            "Dropbox started with a forgotten USB drive.\n\n"
            "On a bus from Boston to New York, Drew Houston realized he’d left his thumb drive behind, again. He started writing code to make the problem go away.\n\n"
            "Syncing was hard to explain, so he made demo videos. The March 2008 one, stuffed with in-jokes for Digg readers, took the beta waitlist from 5,000 to 75,000 overnight.\n\n"
            "Sources: Fortune (2017), TechCrunch (2011), Drew Houston’s Startup Lessons Learned talk\n\n"
            "#dropbox #founders #startups #productmarketing"),
        "alt": "Text slides on how a forgotten thumb drive led Drew Houston to build Dropbox, and how a demo video grew its waitlist to 75,000.",
        "sources": [("Fortune (2017)", "https://fortune.com/2017/06/14/founder-dropbox-got-idea-chinatown-bus/"),
                    ("TechCrunch (2011)", "https://techcrunch.com/2011/10/19/dropbox-minimal-viable-product"),
                    ("Drew Houston, Startup Lessons Learned slides", "https://www.slideshare.net/gueste94e4c/dropbox-startup-lessons-learned-3836587")],
        "notes": "",
    },
    {
        "id": "2026-12-09-hiring-openai",
        "date": "2026-12-09", "time": "08:30", "pillar": "Hiring",
        "title": "OpenAI: Research Engineer, Codex",
        "slides": [
            {"tpl": "hire", "headline": "OpenAI is hiring a research engineer for Codex",
             "role": "Research Engineer, Codex", "loc": "San Francisco",
             "salary": "$380K–$500K", "sub": "Base salary, plus equity",
             "asof": "Posted range as of Nov 27, 2026. Source: OpenAI careers page."},
        ],
        "caption": (
            "OpenAI is hiring a research engineer for Codex.\n\n"
            "Role: Research Engineer, Codex\n"
            "Location: San Francisco\n"
            "Posted base salary: $380K–$500K, plus equity\n\n"
            "Range as listed on OpenAI’s careers site on Nov 27, 2026. Postings change, so confirm before applying.\n\n"
            "Tag an engineer who should see this.\n\n"
            "We’re not affiliated with OpenAI, and this isn’t sponsored.\n\n"
            "#hiring #ai #machinelearning #techjobs"),
        "alt": "Hiring card: OpenAI is hiring a research engineer for Codex in San Francisco, $380K to $500K base salary plus equity.",
        "sources": [("OpenAI careers: Research Engineer, Codex", "https://openai.com/careers/research-engineer-codex-san-francisco/")],
        "notes": HIRE_NOTE,
    },
    {
        "id": "2026-12-10-bitter-lesson",
        "date": "2026-12-10", "time": "08:30", "pillar": "Explainer",
        "title": "The Bitter Lesson, explained",
        "slides": [
            {"tpl": "ex_cover", "headline": "The bitter lesson", "sub": "The short 2019 essay that still frames AI", "art": "chess"},
            {"tpl": "ex_text", "text": "March 13, 2019. Rich Sutton, a pioneer of reinforcement learning, posted a short essay on his website."},
            {"tpl": "ex_text", "text": "Looking back across seven decades of AI research, he saw one pattern: methods that simply scale with more computing power keep beating methods that encode human expertise."},
            {"tpl": "ex_text", "text": "Chess: massive search beat Kasparov in 1997. Go: search plus self-play learning, about 20 years later. Speech and vision: learned methods beat hand-built rules."},
            {"tpl": "ex_diagram", "diagram": "bitter_curves", "caption": "The pattern he described, drawn as a sketch."},
            {"tpl": "ex_text", "text": "Why “bitter”? Because the clever, hand-designed approaches researchers love tend to lose in the long run, and that’s hard to accept."},
            {"tpl": "ex_text", "text": "Sutton went on to share the 2024 Turing Award with Andrew Barto, his former PhD advisor, for their work on reinforcement learning."},
            {"tpl": "ex_end", "text": "For builders: favor approaches that get better on their own as compute gets cheaper."},
        ],
        "caption": (
            "The bitter lesson, in one swipe.\n\n"
            "In 2019, AI researcher Rich Sutton looked back across seven decades of AI research and saw one pattern: "
            "methods that simply scale with more computing power keep beating methods that encode human expertise.\n\n"
            "His examples: chess, where massive search beat Kasparov in 1997; Go, about two decades later; and speech and vision, where learning beat hand-built rules.\n\n"
            "Sutton later shared the 2024 Turing Award with Andrew Barto for their work on reinforcement learning.\n\n"
            "Sources: Rich Sutton, The Bitter Lesson (2019); Wikipedia\n\n"
            "#ai #machinelearning #deeplearning #startups"),
        "alt": "Explainer carousel on Rich Sutton’s 2019 essay The Bitter Lesson, with a sketch of scaling methods overtaking hand-built approaches.",
        "sources": [("Rich Sutton, The Bitter Lesson (2019)", "http://www.incompleteideas.net/IncIdeas/BitterLesson.html"),
                    ("Wikipedia: Richard S. Sutton", "https://en.wikipedia.org/wiki/Richard_S._Sutton")],
        "notes": "The curve slide is a sketch labeled as illustrative, not data.",
    },
    {
        "id": "2026-12-11-spanx-5000",
        "date": "2026-12-11", "time": "08:30", "pillar": "Founder story",
        "title": "Spanx started with $5,000 and a pair of scissors",
        "year": "2000",
        "slides": [
            {"tpl": "story_cover", "headline": "Spanx started with $5,000 and a pair of scissors."},
            {"tpl": "story", "text": "Sara Blakely spent seven years selling fax machines door to door."},
            {"tpl": "story", "text": "Before a party, she cut the feet off her control-top pantyhose so she could wear them under white pants."},
            {"tpl": "story", "fig": "$5,000", "text": "She put her $5,000 in savings into the idea and spent two years developing it while keeping her day job."},
            {"tpl": "story", "text": "To save on legal fees, she wrote her own patent. Her first big account, Neiman Marcus, came from a cold call."},
            {"tpl": "story", "text": "She launched in 2000 and funded Spanx herself for 21 years. In 2012, Forbes named her the world’s youngest self-made female billionaire."},
            {"tpl": "story_end", "text": "Start with the scrappy prototype. Then do the unglamorous work: the patent, the factory, the first buyer."},
        ],
        "caption": (
            "Spanx started with $5,000 and a pair of scissors.\n\n"
            "Sara Blakely sold fax machines door to door for seven years. One day she cut the feet off her pantyhose to wear under white pants, and saw a product.\n\n"
            "She put $5,000 of savings into it, wrote her own patent, and cold-called Neiman Marcus for her first account. She funded the company herself for 21 years.\n\n"
            "Sources: Fortune (2025), Stanford GSB (2018), Yahoo Finance UK (2012)\n\n"
            "#spanx #founders #bootstrapping #entrepreneurship"),
        "alt": "Text slides on how Sara Blakely started Spanx with $5,000 in savings after cutting the feet off her pantyhose.",
        "sources": [("Fortune (2025)", "https://fortune.com/2025/09/20/sara-blakely-spanx-fax-machines-investors-career-advice/"),
                    ("Stanford GSB (2018)", "https://gsb.stanford.edu/insights/sara-blakely-start-small-think-big-scale-fast"),
                    ("Yahoo Finance UK (2012)", "https://uk.finance.yahoo.com/news/sara-blakely--how-one-woman-made-a-billion-from-big-pants.html")],
        "notes": "",
    },
    {
        "id": "2026-12-12-apple-ipo",
        "date": "2026-12-12", "time": "10:00", "pillar": "History",
        "title": "46 years ago today, Apple went public",
        "slides": [
            {"tpl": "hist_cover", "label": "46 years ago today", "big": "$22", "title": "Apple went public on Dec 12, 1980", "art": "ipo"},
            {"tpl": "hist_facts", "facts": [
                "4.6 million shares sold almost immediately at $22 each.",
                "The IPO raised about $100 million, more than any since Ford’s in 1956.",
                "The stock closed its first day near $29, valuing Apple at about $1.8 billion.",
                "Roughly 300 people became millionaires overnight. Apple was four years old."]},
        ],
        "caption": (
            "46 years ago today, Apple went public.\n\n"
            "On Dec 12, 1980, Apple sold 4.6 million shares at $22. They sold out fast, raising more money than any IPO since Ford’s in 1956. "
            "The stock closed the day around $29, valuing the company at about $1.8 billion, and roughly 300 people became millionaires.\n\n"
            "Apple was four years old.\n\n"
            "Sources: Engadget (2013), Cult of Mac, AppleInsider\n\n"
            "#apple #ipo #techhistory #onthisday"),
        "alt": "History card: Apple went public on Dec 12, 1980 at $22 a share.",
        "sources": [("Engadget (2013)", "https://www.engadget.com/2013/12/12/33-years-ago-today-apple-launched-its-ipo/"),
                    ("Cult of Mac", "https://www.cultofmac.com/457878/tiah-apple-goes-public"),
                    ("AppleInsider", "https://forums.appleinsider.com/discussion/comment/2445998/")],
        "notes": DATE_NOTE,
    },
    # ───────────────────────── WEEK 3 ─────────────────────────
    {
        "id": "2026-12-14-founder-ages",
        "date": "2026-12-14", "time": "08:30", "pillar": "Data",
        "title": "How old they were when they started",
        "slides": [
            {"tpl": "data_cover", "title": "How old they were when they started",
             "stats": [("19", "the youngest on our list"), ("52", "the oldest")]},
            {"tpl": "ages", "title": "Age at founding",
             "rows": [("19", "Bill Gates", "Microsoft, 1975"), ("19", "Mark Zuckerberg", "Facebook, 2004"),
                      ("19", "Michael Dell", "Dell, 1984"), ("21", "Steve Jobs", "Apple, 1976"),
                      ("25", "Larry Page", "Google, 1998"), ("29", "Sara Blakely", "Spanx, 2000"),
                      ("30", "Jeff Bezos", "Amazon, 1994"), ("36", "Reed Hastings", "Netflix, 1997"),
                      ("44", "Sam Walton", "first Walmart, 1962"), ("52", "Ray Kroc", "McDonald’s, 1955*")],
             "foot": "*Kroc founded the company that franchised McDonald’s; the McDonald brothers ran the original restaurant."},
            {"tpl": "note", "text": "There’s no right age to start. There’s only the age you are when you do.", "small": "Which founder surprised you?"},
        ],
        "caption": (
            "There’s no right age to start.\n\n"
            "Bill Gates, Mark Zuckerberg and Michael Dell were 19. Larry Page was 25. Jeff Bezos was 30. Reed Hastings was 36. "
            "Sam Walton opened the first Walmart at 44, and Ray Kroc started the company that franchised McDonald’s at 52.\n\n"
            "Pick your number. Then start.\n\n"
            "Sources: public biographies and company histories\n\n"
            "#founders #entrepreneurship #startups #motivation"),
        "alt": "List of ten founders and their age at founding, from 19 for Bill Gates, Mark Zuckerberg and Michael Dell to 52 for Ray Kroc.",
        "sources": [("Fortune (2025): Blakely began Spanx at 29 in 2000", "https://fortune.com/2025/09/20/sara-blakely-spanx-fax-machines-investors-career-advice/")],
        "notes": "Ages computed from public birth dates and founding dates.",
    },
    {
        "id": "2026-12-15-google-excite",
        "date": "2026-12-15", "time": "08:30", "pillar": "Founder story",
        "title": "In 1999, Google tried to sell itself for $1 million",
        "year": "1999",
        "slides": [
            {"tpl": "story_cover", "headline": "In 1999, Google tried to sell itself for $1 million."},
            {"tpl": "story", "text": "Larry Page and Sergey Brin wanted to get back to their studies at Stanford. Their search engine was eating their time."},
            {"tpl": "story", "fig": "$1M", "text": "They offered it to Excite, one of the web’s big portals, for $1 million. Excite’s CEO, George Bell, said no."},
            {"tpl": "story", "fig": "$750K", "text": "Vinod Khosla, an Excite backer, talked the founders down to $750,000. Bell passed again."},
            {"tpl": "story", "text": "Khosla told the story onstage at TechCrunch Disrupt in 2010. By then Excite had been sold to Ask Jeeves, back in 2004."},
            {"tpl": "story_end", "text": "The deals that look obvious in hindsight rarely looked obvious at the time."},
        ],
        "caption": (
            "In 1999, Google tried to sell itself for $1 million.\n\n"
            "Larry Page and Sergey Brin offered their search engine to Excite. CEO George Bell turned it down. "
            "Vinod Khosla, an Excite backer whose firm, Kleiner Perkins, later invested in Google, got the price down to $750,000. Bell still said no.\n\n"
            "Khosla recounted the story onstage at TechCrunch Disrupt in 2010.\n\n"
            "Sources: TechCrunch (2010), Fortune (2010)\n\n"
            "#google #startups #venturecapital #founders"),
        "alt": "Text slides on how Excite turned down buying Google for $1 million, then $750,000, in 1999.",
        "sources": [("TechCrunch (2010)", "https://techcrunch.com/2010/09/29/google-excite/"),
                    ("Fortune (2010)", "https://fortune.com/2010/09/29/excite-passed-up-buying-google-for-750000-in-1999/")],
        "notes": "",
    },
    {
        "id": "2026-12-16-hiring-perplexity",
        "date": "2026-12-16", "time": "08:30", "pillar": "Hiring",
        "title": "Perplexity: Software Engineer, Monetization",
        "slides": [
            {"tpl": "hire", "headline": "Perplexity is hiring an engineer to run billing for its AI agents",
             "role": "Member of Technical Staff (Software Engineer, Monetization)", "loc": "",
             "salary": "$220K–$405K", "sub": "Base salary, plus equity",
             "asof": "Posted range as of Nov 27, 2026. Source: Perplexity careers page."},
        ],
        "caption": (
            "Perplexity is hiring an engineer to own billing for its AI agents.\n\n"
            "Role: Member of Technical Staff (Software Engineer, Monetization)\n"
            "Posted base salary: $220K–$405K, plus equity\n\n"
            "Per the posting, the team’s billing platform meters every action an agent takes. Range as listed on Nov 27, 2026. Confirm on Perplexity’s careers page before applying.\n\n"
            "We’re not affiliated with Perplexity, and this isn’t sponsored.\n\n"
            "#hiring #ai #startupjobs #softwareengineering"),
        "alt": "Hiring card: Perplexity is hiring an engineer to run billing for its AI agents, $220K to $405K base salary plus equity.",
        "sources": [("Perplexity job posting (Ashby)", "https://jobs.ashbyhq.com/Perplexity/043d6a58-87a1-4e3c-bf47-4dc351b94cf4")],
        "notes": HIRE_NOTE + " Location isn’t shown in our snapshot; add it from the posting.",
    },
    {
        "id": "2026-12-17-conways-law",
        "date": "2026-12-17", "time": "08:30", "pillar": "Explainer",
        "title": "Your org chart ships with your product: Conway’s law",
        "slides": [
            {"tpl": "ex_cover", "headline": "Your org chart ships with your product", "sub": "Conway’s law, explained", "art": "org"},
            {"tpl": "ex_text", "text": "1967. Programmer Melvin Conway sent a paper to Harvard Business Review. HBR turned it down: he hadn’t proved his thesis."},
            {"tpl": "ex_text", "text": "In April 1968, the IT magazine Datamation published it as “How Do Committees Invent?”"},
            {"tpl": "ex_text", "text": "His idea: the systems an organization builds end up mirroring the way its people communicate."},
            {"tpl": "ex_diagram", "diagram": "conway", "caption": "Teams that talk build parts that connect. Teams that don’t, don’t."},
            {"tpl": "ex_text", "text": "Fred Brooks named it Conway’s law in The Mythical Man-Month in 1975. Later research, including MIT and Harvard Business School work on “mirroring,” found evidence for it."},
            {"tpl": "ex_end", "text": "Want a different architecture? Change how your teams communicate first."},
        ],
        "caption": (
            "Your org chart ships with your product.\n\n"
            "In 1967, programmer Melvin Conway argued that the systems an organization builds end up mirroring how its people communicate. "
            "Harvard Business Review rejected the paper. Datamation published it in 1968, and Fred Brooks later named the idea Conway’s law.\n\n"
            "Teams that don’t talk build parts that don’t fit.\n\n"
            "Sources: Mel Conway (melconway.com), O’Reilly, Making Software (ch. 11)\n\n"
            "#softwareengineering #startups #management #engineering"),
        "alt": "Explainer carousel on Conway’s law, with a diagram of three teams mirrored by three software components.",
        "sources": [("Mel Conway: Conway’s Law", "https://www.melconway.com/Home/Conways_Law.html"),
                    ("O’Reilly, Making Software, ch. 11", "https://www.oreilly.com/library/view/making-software/9780596808310/ch11s01.html"),
                    ("Wikipedia: Conway’s law", "https://en.wikipedia.org/wiki/Conway%27s_law")],
        "notes": "",
    },
    {
        "id": "2026-12-18-canva-rejections",
        "date": "2026-12-18", "time": "08:30", "pillar": "Founder story",
        "title": "Canva was turned down by more than 100 investors",
        "year": "2013",
        "slides": [
            {"tpl": "story_cover", "headline": "Canva was turned down by more than 100 investors."},
            {"tpl": "story", "text": "Before Canva, Melanie Perkins ran Fusion Books, a school-yearbook design business, out of her mom’s living room in Perth."},
            {"tpl": "story", "fig": "100+", "text": "Her bigger idea was design tools simple enough for anyone. Investors kept passing, more than 100 of them."},
            {"tpl": "story", "text": "Their doubts: a startup based in Australia, co-founders who were a couple, and no technical background between them."},
            {"tpl": "story", "text": "Investor Bill Tai ran a kitesurfing retreat for founders and VCs. Perkins, who has said kitesurfing terrified her, learned anyway."},
            {"tpl": "story", "text": "Tai became an early investor, and the connections helped Canva raise its first round. Canva launched in 2013."},
            {"tpl": "story_end", "text": "Treat each no as notes. Perkins kept sharpening the pitch, and the product."},
        ],
        "caption": (
            "Canva was turned down by more than 100 investors.\n\n"
            "Melanie Perkins started with Fusion Books, a yearbook design business run from her mom’s living room in Perth. "
            "When she pitched the bigger idea, design tools anyone could use, investors kept saying no, citing everything from her location to the founders’ lack of technical backgrounds.\n\n"
            "She even learned to kitesurf to get time with investor Bill Tai, who hosted founder-and-VC kitesurfing retreats. He invested. Canva launched in 2013.\n\n"
            "Sources: Business Insider (2016), Inc., Wikipedia\n\n"
            "#canva #founders #startups #fundraising"),
        "alt": "Text slides on how Melanie Perkins was rejected by more than 100 investors before launching Canva in 2013.",
        "sources": [("Business Insider (2016)", "https://businessinsider.in/this-28-year-old-startup-founder-learned-to-kiteboard-to-impress-investors-and-it-paid-off-big-time/amp_articleshow/53619090.cms"),
                    ("Inc.", "https://www.inc.com/larry-kim/10-facts-about-canva-ceo-melanie-perkins.html"),
                    ("Wikipedia: Melanie Perkins", "https://en.wikipedia.org/wiki/Melanie_Perkins"),
                    ("Women’s Agenda", "https://womensagenda.com.au/business/entrepreneurs/now-leading-1-billion-startup-australias-melanie-perkins-advice")],
        "notes": "",
    },
    {
        "id": "2026-12-19-first-flight",
        "date": "2026-12-19", "time": "10:00", "pillar": "History",
        "title": "This week in 1903: the first powered flight",
        "slides": [
            {"tpl": "hist_cover", "label": "This week in 1903", "big": "12 sec", "title": "The first powered flight", "art": "flight"},
            {"tpl": "hist_facts", "facts": [
                "Dec 17, 1903, near Kitty Hawk, North Carolina: Orville Wright flew 120 feet in 12 seconds.",
                "That first flight was shorter than a Boeing 747’s wingspan.",
                "The brothers made four flights that day. Wilbur’s last went 852 feet in 59 seconds.",
                "Five people watched. The builders were two bicycle-shop owners from Dayton, Ohio."]},
        ],
        "caption": (
            "The first powered flight lasted 12 seconds.\n\n"
            "On Dec 17, 1903, at Kill Devil Hills near Kitty Hawk, Orville Wright flew 120 feet, shorter than a Boeing 747’s wingspan. "
            "By the fourth flight that day, Wilbur stayed up for 59 seconds and covered 852 feet.\n\n"
            "The team behind it: two bicycle-shop owners from Dayton, Ohio.\n\n"
            "Sources: National Park Service, NASA, Smithsonian National Air and Space Museum\n\n"
            "#techhistory #wrightbrothers #innovation #onthisday"),
        "alt": "History card: Dec 17, 1903, the first powered flight lasted 12 seconds, with bars comparing the 120-foot first flight to the 852-foot fourth flight.",
        "sources": [("National Park Service", "https://www.nps.gov/articles/firstflight.htm"),
                    ("NASA", "https://www.nasa.gov/history/120-years-ago-the-first-powered-flight-at-kitty-hawk/"),
                    ("Smithsonian National Air and Space Museum", "https://www.airandspace.si.edu/stories/editorial/wright-brothers-made-history-kitty-hawk")],
        "notes": DATE_NOTE,
    },
    # ───────────────────────── WEEK 4 ─────────────────────────
    {
        "id": "2026-12-21-small-teams",
        "date": "2026-12-21", "time": "08:30", "pillar": "Data",
        "title": "Small teams, giant exits",
        "slides": [
            {"tpl": "data_cover", "title": "Small teams, giant exits",
             "stats": [("13", "people at Instagram when Facebook agreed to pay $1 billion")]},
            {"tpl": "compare", "title": "Headline price per employee",
             "cards": [{"big": "13", "unit": "employees", "deal": "Instagram, bought by Facebook, April 2012", "price": "$1B headline price", "per": "≈ $77M per employee"},
                       {"big": "55", "unit": "employees", "deal": "WhatsApp, bought by Facebook, February 2014", "price": "$19B headline price", "per": "≈ $345M per employee"}],
             "foot": "Headline deal values. Instagram’s final price was about $715M after Facebook’s stock fell before closing."},
            {"tpl": "note", "text": "In 2009, Facebook turned down WhatsApp co-founder Brian Acton for a job. Less than five years later, it agreed to pay $19 billion for his company.",
             "small": "Sources: Fortune (2016), ABC News (2014), TechCrunch (2014)"},
        ],
        "caption": (
            "13 people. $1 billion.\n\n"
            "When Facebook agreed to buy Instagram in April 2012, Instagram had 13 employees. When it agreed to buy WhatsApp in February 2014, WhatsApp had 55. "
            "At headline prices, that’s roughly $77M and $345M per employee.\n\n"
            "One more detail: in 2009, Facebook rejected WhatsApp co-founder Brian Acton for a job.\n\n"
            "(Instagram’s final price landed near $715M after Facebook’s stock dropped before closing.)\n\n"
            "Sources: Fortune (2016), ABC News (2014), TechCrunch (2014)\n\n"
            "#startups #acquisitions #instagram #whatsapp"),
        "alt": "Comparison: Instagram had 13 employees at a $1 billion headline price, WhatsApp had 55 at $19 billion.",
        "sources": [("Fortune (2016): 13 employees; $715M final", "https://fortune.com/2016/04/19/facebook-instagram-acquisitionheres-proof-that-instagram-was-one-of-the-smartest-acquisitions-ever/"),
                    ("ABC News / GMA (2014): 55 employees", "https://www.goodmorningamerica.com/news/story/facebook-makes-billionaire-college-dropout-family-food-stamps-22601936"),
                    ("TechCrunch (2014): Acton’s job rejections", "https://techcrunch.com/2014/02/19/how-things-change/")],
        "notes": "Per-employee figures are headline price divided by headcount.",
    },
    {
        "id": "2026-12-22-nike-35-logo",
        "date": "2026-12-22", "time": "08:30", "pillar": "Founder story",
        "title": "Nike paid $35 for its logo",
        "year": "1971",
        "slides": [
            {"tpl": "story_cover", "headline": "Nike paid $35 for its logo."},
            {"tpl": "story", "text": "1971. Phil Knight, who also taught accounting at Portland State, needed a logo for a new line of shoes, and fast."},
            {"tpl": "story", "text": "He asked Carolyn Davidson, a graphic design student he’d overheard saying she couldn’t afford an oil painting class."},
            {"tpl": "story", "fig": "$35", "text": "She billed $2 an hour for 17.5 hours of work."},
            {"tpl": "story", "text": "Knight’s reaction: he didn’t love it, but thought it might grow on him."},
            {"tpl": "story", "text": "In 1983, Knight gave her a gold Swoosh ring set with a diamond, plus 500 shares of Nike stock."},
            {"tpl": "story_end", "text": "Logos don’t start out iconic. Years of consistent use make them that way."},
        ],
        "caption": (
            "Nike paid $35 for its logo.\n\n"
            "In 1971, Phil Knight needed a mark for his shoes and hired Carolyn Davidson, a Portland State design student. She billed 17.5 hours at $2 an hour. "
            "Knight wasn’t thrilled with the result, but he figured it would grow on him.\n\n"
            "In 1983, he thanked her with a gold Swoosh ring set with a diamond and 500 shares of Nike stock, since split into 32,000 shares.\n\n"
            "Sources: Nike, ESPN, Wikipedia\n\n"
            "#nike #branding #design #founders"),
        "alt": "Text slides on how Carolyn Davidson designed Nike’s logo for $35 in 1971.",
        "sources": [("Nike: the Swoosh story", "https://about.nike.com/stories/nike-swoosh-logo-history"),
                    ("ESPN", "https://www.espn.com/espn/story/_/id/16286876/how-college-student-carolyn-davidson-created-nike-swoosh"),
                    ("Wikipedia: Carolyn Davidson", "https://en.wikipedia.org/wiki/Carolyn_Davidson_(graphic_designer)"),
                    ("Wallpaper: $2 an hour, 17.5 hours", "https://www.wallpaper.com/fashion-beauty/nike-swoosh-logo")],
        "notes": "Text only by design: don’t add the logo artwork itself.",
    },
    {
        "id": "2026-12-23-hiring-figma",
        "date": "2026-12-23", "time": "08:30", "pillar": "Hiring",
        "title": "Figma: Software Engineer, Application Platform",
        "slides": [
            {"tpl": "hire", "headline": "Figma is hiring a Ruby backend engineer",
             "role": "Software Engineer, Application Platform", "loc": "San Francisco or New York, or remote in the US",
             "salary": "$235K–$376K", "sub": "Base salary, plus equity",
             "asof": "Posted Nov 7, 2026; range checked Nov 27, 2026."},
        ],
        "caption": (
            "Figma is hiring a Ruby backend engineer.\n\n"
            "Role: Software Engineer, Application Platform\n"
            "Location: San Francisco or New York hubs, or remote in the US\n"
            "Posted base salary: $235K–$376K, plus equity\n\n"
            "The role asks for 5+ years of engineering, including 3+ building production systems in Ruby. Posted Nov 7, 2026. Confirm on Figma’s careers page before applying.\n\n"
            "We’re not affiliated with Figma, and this isn’t sponsored.\n\n"
            "#hiring #figma #ruby #techjobs"),
        "alt": "Hiring card: Figma is hiring a Ruby backend engineer, Software Engineer, Application Platform, $235K to $376K base salary plus equity.",
        "sources": [("Figma posting (via Thrive Capital job board)", "https://jobs.thrivecap.com/companies/figma-2/jobs/99231033-software-engineer-application-platform")],
        "notes": HIRE_NOTE,
    },
    {
        "id": "2026-12-24-metcalfes-law",
        "date": "2026-12-24", "time": "10:00", "pillar": "Explainer",
        "title": "Networks grow by squares: Metcalfe’s law",
        "slides": [
            {"tpl": "ex_cover", "headline": "Networks grow by squares", "sub": "Metcalfe’s law, explained", "art": "network"},
            {"tpl": "ex_text", "text": "Around 1980, Ethernet co-inventor Bob Metcalfe made a slide to persuade customers to build bigger networks."},
            {"tpl": "ex_diagram", "diagram": "metcalfe", "caption": "Possible connections grow roughly with the square of the users."},
            {"tpl": "ex_text", "text": "His real point was critical mass: a network costs money to build and only pays off once enough people are on it."},
            {"tpl": "ex_text", "text": "Writer George Gilder named the idea Metcalfe’s law in a 1993 Forbes article."},
            {"tpl": "ex_text", "text": "Critics argue the real curve is flatter, closer to n log n, because not every connection is worth the same."},
            {"tpl": "ex_end", "text": "Early on, density beats size. Win one campus, one city or one team before going wide."},
        ],
        "caption": (
            "Why do networks get more valuable as they grow?\n\n"
            "Around 1980, Ethernet co-inventor Bob Metcalfe sketched a simple idea: the possible connections in a network grow roughly with the square of its users. "
            "Two users share one link. Twelve can form 66.\n\n"
            "His real point was critical mass. A network has to get big enough to be worth what it costs.\n\n"
            "George Gilder named it Metcalfe’s law in 1993. Critics say the true curve is flatter, since not every connection is equally valuable. "
            "Metcalfe later received the 2022 Turing Award for Ethernet.\n\n"
            "Sources: IEEE Spectrum (2006), Wikipedia\n\n"
            "#networkeffects #startups #tech #venturecapital"),
        "alt": "Explainer carousel on Metcalfe’s law, with diagrams of networks of 2, 5 and 12 users forming 1, 10 and 66 connections.",
        "sources": [("IEEE Spectrum (2006)", "https://spectrum.ieee.org/metcalfes-law-is-wrong"),
                    ("Wikipedia: Metcalfe’s law", "https://en.wikipedia.org/wiki/Metcalfe%27s_law"),
                    ("Wikipedia: Bob Metcalfe", "https://en.wikipedia.com/wiki/Bob_Metcalfe")],
        "notes": "Christmas Eve: posts at 10:00 a.m.",
    },
    {
        "id": "2026-12-25-dyson-prototypes",
        "date": "2026-12-25", "time": "10:00", "pillar": "Founder story",
        "title": "James Dyson built 5,127 prototypes",
        "year": "1993",
        "slides": [
            {"tpl": "story_cover", "headline": "James Dyson built 5,127 prototypes."},
            {"tpl": "story", "text": "Starting in 1979, fed up with vacuums that lost suction, he built cyclone prototypes in a shed behind his house."},
            {"tpl": "story", "fig": "5,126", "text": "That’s how many failed, by his count. He has said each one taught him something."},
            {"tpl": "story", "text": "The big manufacturers wouldn’t take the idea. He licensed it in Japan instead and used that income to start his own company."},
            {"tpl": "story", "text": "In 1993, his DC01 vacuum went on sale in the UK. Within about two years, it was the country’s best seller."},
            {"tpl": "story_end", "text": "Persistence isn’t trying the same thing again. It’s running thousands of different experiments."},
        ],
        "caption": (
            "James Dyson built 5,127 prototypes.\n\n"
            "Starting in 1979, frustrated by vacuums that lost suction, he built cyclone after cyclone in a shed behind his house. By his count, 5,126 failed. "
            "Manufacturers wouldn’t license the idea, so he licensed it in Japan and used the income to start his own company.\n\n"
            "The DC01 launched in the UK in 1993 and became the country’s best-selling vacuum within about two years.\n\n"
            "Sources: Dyson, TIME (2007), Britannica\n\n"
            "#dyson #founders #engineering #persistence"),
        "alt": "Text slides on how James Dyson built 5,127 prototypes before launching his first vacuum, the DC01, in 1993.",
        "sources": [("Dyson", "https://www.dyson.com/discover/innovation/behind-the-invention/only-a-dyson-works-like-a-dyson"),
                    ("TIME (2007)", "https://content.time.com/time/specials/2007/article/0,28804,1663316_1684619_1707062,00.html"),
                    ("Britannica", "https://www.Britannica.Com/money/James-Dyson"),
                    ("Wikipedia: Dyson Ltd", "https://wikipedia.com/wiki/Dyson_Ltd")],
        "notes": "Christmas Day: posts at 10:00 a.m.",
    },
    {
        "id": "2026-12-26-transistor-demo",
        "date": "2026-12-26", "time": "10:00", "pillar": "History",
        "title": "This week in 1947: the transistor’s first demo",
        "slides": [
            {"tpl": "hist_cover", "label": "This week in 1947", "big": "Dec 23", "title": "The transistor’s first demo", "art": "transistor"},
            {"tpl": "hist_facts", "facts": [
                "At Bell Labs on Dec 16, 1947, John Bardeen and Walter Brattain got a sliver of germanium to amplify a signal.",
                "Two gold contacts, held by a plastic wedge, boosted signals up to 100 times.",
                "On Dec 23, they demonstrated it to Bell Labs leadership in Murray Hill, New Jersey.",
                "AT&T licensed it to other companies for a $25,000 advance against royalties. Bardeen, Brattain and William Shockley shared the 1956 Nobel Prize in Physics."]},
        ],
        "caption": (
            "This week in 1947, the transistor got its first demo.\n\n"
            "At Bell Labs in December 1947, John Bardeen and Walter Brattain pressed two gold contacts onto a sliver of germanium and amplified a signal up to 100 times. "
            "On Dec 23, they showed Bell Labs leadership.\n\n"
            "AT&T then licensed the transistor to other companies for a $25,000 advance against royalties. "
            "Bardeen, Brattain and William Shockley shared the 1956 Nobel Prize in Physics.\n\n"
            "Sources: Computer History Museum, IEEE ETHW\n\n"
            "#techhistory #semiconductors #belllabs #onthisday"),
        "alt": "History card: Dec 23, 1947, the transistor’s first demonstration at Bell Labs, with a schematic of the point-contact device.",
        "sources": [("Computer History Museum", "https://www.computerhistory.org/siliconengine/invention-of-the-point-contact-transistor/"),
                    ("IEEE ETHW", "https://ethw.org/Bell_Demonstrates_Transistor")],
        "notes": DATE_NOTE,
    },
]
