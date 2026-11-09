"""Page content, one dict per app. Facts come from each app's live store listing.

House rules: no prices, plans or limits; no claims the listing does not make; features that only exist on
iPhone say so. `key` is the icon file name in assets/icons and the key in meta.json.
"""
import json
from pathlib import Path

META = json.loads((Path(__file__).parent / "meta.json").read_text())

_APPS = [
    # ------------------------------------------------------------------ Ouch Log
    dict(
        slug="ouchlog", key="ouchlog", name="Ouch Log", kind="Pain tracker and symptom diary",
        title="Ouch Log — Pain tracker and symptom diary you can fill in while it hurts",
        desc="Ouch Log is a private pain tracker and symptom diary for chronic pain, migraine, fibromyalgia and arthritis. "
             "Log a flare in five seconds on a body map, see which medication helps, and bring a PDF report to your doctor. "
             "Works offline, no account.",
        h1="Log a flare in <em>five seconds</em>. See what actually helps.",
        lead="Ouch Log is a pain tracker and symptom diary for people living with chronic pain, migraine, fibromyalgia, "
             "arthritis and other long-term conditions. Tap a pain level, tap where it hurts, done — then walk into your "
             "next appointment with a report.",
        facts="iPhone, iPad and Android · Works offline · No account",
        audience="People living with chronic pain, migraine, fibromyalgia, arthritis and other long-term conditions",
        feat_title="A pain diary made for your worst days",
        feat_sub="Large targets, high contrast and almost no typing. Add the details later, once the flare has passed.",
        features=[
            ("Five-second logging", "Tap a pain level and the spot on a body map — left, right, front and back. Triggers, pain types, medication and notes can wait."),
            ("Flare timer", "During a flare, Home shows how long it has lasted. Tap “No pain now” when it eases."),
            ("Medication relief", "Your pain before each dose next to your pain 30 minutes to 4 hours after it, for every medication."),
            ("Dose limits you set", "A daily maximum and the hours between doses, with a count of where you stand. Ouch Log only counts; it never blocks a dose."),
            ("Patterns and trends", "7, 30 or 90 days compared with the period before: flares, time of day, body regions, pain types, triggers and days of work or school missed."),
            ("Reports for your doctor", "Add your visits and the questions you want to ask. PDF reports for any range, with your questions printed at the top, and CSV export of every entry."),
        ],
        how_title="From a bad day to a clear picture",
        steps=[
            ("Log while it hurts", "Two taps on the level and the body map. On iPhone you can also log from a widget or Apple Watch without opening the app."),
            ("Look back", "A calendar with a color dot for every day, and a one-page summary each month."),
            ("Walk in with proof", "A reminder the evening before your appointment, with a report covering everything since your last visit."),
        ],
        shots_alt=["Ouch Log home screen with pain level buttons", "Ouch Log body map for marking where it hurts",
                   "Ouch Log trends over 30 days", "Ouch Log insights: triggers and medication relief"],
        keep_title="Private by design",
        keep=[
            "<b>Entries stay on your device.</b> Pain entries, notes and medications are never sent to us.",
            "<b>No account and no sign-up.</b> Open the app and log.",
            "<b>Works fully offline</b>, and you can export a backup whenever you like.",
            "<b>Lock the diary</b> with Face ID or your passcode.",
            "<b>Apple Health is optional</b> on iPhone and off until you connect it.",
        ],
        note="Ouch Log is a pain diary, not a medical device. It does not diagnose or treat, and does not give medical advice. "
             "Always talk to a healthcare professional about your symptoms and before making decisions about medication.",
        faq=[
            ("Do I need an account to use Ouch Log?", "No. There is no account and no sign-up. Your entries stay on your device."),
            ("Can I show my pain history to my doctor?", "Yes. Ouch Log makes PDF reports for 7, 30 or 90 days, a custom range, or since your last visit, with the questions you want to ask printed at the top. You can also export every entry as CSV."),
            ("Does Ouch Log tell me which medication works?", "It shows your own log: the pain level before each dose next to the level 30 minutes to 4 hours after it, for every medication. It is a pattern in your entries, not medical advice."),
            ("Does it work without internet?", "Yes. Ouch Log works fully offline."),
            ("Is Ouch Log a medical device?", "No. It is a diary. It does not diagnose, treat or give medical advice."),
        ],
        cta="Start with the next flare",
        theme=dict(bg="#FBF5F3", accent="#E2556B", font="rounded", body="rounded", radius=24, hero="split", features="cards",
                   strip="bands", strip_colors=["#FBE3DE", "#F8CFC9", "#F5B8B2", "#F29E9D", "#EE8389", "#E96A78", "#E2556B", "#CF4760", "#B63B55", "#98304A"]),
    ),
    # ------------------------------------------------------------------ Jars
    dict(
        slug="jars", key="jars", name="Jars", kind="Savings goal tracker",
        title="Jars — Savings goal tracker with a jar for every goal",
        desc="Jars is a savings goal tracker and sinking funds app. Give every goal its own jar, add money in a few taps and "
             "watch it fill up. Savings plans, 52-week and envelope challenges, widgets. No account, works offline.",
        h1="A jar for every goal. <em>Watch it fill up.</em>",
        lead="Save for the trip, the emergency fund, next year's taxes. Give every goal its own jar, add money in a few taps, "
             "and see whether you are on track. Jars keeps score — it never holds or moves your money.",
        facts="iPhone, iPad and Android · Works offline · No account",
        audience="People saving toward goals: sinking funds, emergency fund, travel, taxes, savings challenges",
        feat_title="Sinking funds with a plan",
        features=[
            ("One jar per goal", "Name it, pick an icon and a color, set a target and a deadline. Templates for an emergency fund, travel, taxes, a car, a gift, a home."),
            ("A pace that adds up", "Jars works out how much to set aside each week or month, and tells you which month you will get there at the pace you are actually saving."),
            ("Payday reminders", "Savings plans remind you on payday. Missed a week? Catch up, snooze it or skip it — Jars never invents money you did not save."),
            ("Split a payday", "Spread one deposit across several jars: evenly, by what each jar still needs, or in the order you choose."),
            ("Savings challenges", "52-week, 26-week, 100 envelopes, the penny challenge, or a schedule you build yourself. Tick off weeks in any order."),
            ("Where you stand", "Everything saved so far, this month's deposits and withdrawals, jars on track, and how your balance grew over time."),
        ],
        how_title="Deposit, withdraw, move — all with a note",
        steps=[
            ("Add money in a few taps", "Every entry keeps a date and a note you can edit later, and anything you just did can be undone."),
            ("Counted wrong?", "Type the balance you actually have and Jars records the difference."),
            ("Keep jars your way", "Each jar in its own currency, with a cover photo and a note of where the money really sits."),
        ],
        shots_alt=["Jars home screen with savings jars filling up", "Jars goal progress", "Jars savings plan schedule", "Jars savings challenge board"],
        keep_title="Your data, your files",
        keep=[
            "<b>Your jars stay on your phone.</b> They only leave when you send them somewhere: a backup or a file you export.",
            "<b>No account, no sign-in, no ads</b>, and it all works offline.",
            "<b>Automatic backups</b> to your own iCloud Drive on iPhone; export everything as a ZIP, or transactions as CSV.",
            "<b>Lock Jars</b> behind Face ID or your passcode, and hide every amount until you tap it.",
            "<b>It never touches your bank.</b> Jars keeps score of money you move yourself.",
        ],
        faq=[
            ("Does Jars connect to my bank account?", "No. Jars never holds or moves your money and has no bank connection. You record deposits and withdrawals yourself."),
            ("Do I need an account?", "No. There is no account and nothing to sign up for."),
            ("Can I use Jars for sinking funds?", "Yes. Set a target and a date for each jar; Jars works out how much to set aside each week or month and shows which month you will reach it."),
            ("Which savings challenges are included?", "52-week, 26-week, 100 envelopes, the penny challenge, and a custom schedule you build yourself."),
            ("Can I keep jars in different currencies?", "Yes. Each jar can have its own currency."),
        ],
        cta="Give your first goal a jar",
        theme=dict(bg="#F2F7FD", accent="#1F6FD0", font="rounded", body="rounded", radius=26, hero="center", features="cards", weight=800,
                   strip="dots", strip_colors=["#F2B632", "#1F6FD0", "#5BB36A", "#F2B632", "#E8862E"]),
    ),
    # ------------------------------------------------------------------ SOAP Notes
    dict(
        slug="soapnotes", key="soapnotes", name="SOAP Notes", kind="Client charting for solo therapists",
        title="SOAP Notes — Body chart, intake and consent for massage therapists and physios",
        desc="SOAP Notes is a client charting app for massage therapists, physical therapists, chiropractors and acupuncturists "
             "who work on their own. SOAP notes in two minutes, body charts, signed intake and consent, PDF records. "
             "Records stay on your device; no account.",
        h1="Write a SOAP note in <em>two minutes</em> between clients.",
        lead="SOAP Notes is charting for therapists who work on their own: massage therapists, physical therapists and physios, "
             "chiropractors and acupuncturists. Chart the visit, mark where it hurts, collect intake and consent with a real "
             "signature, and print a clean record when a client, an insurer or a lawyer asks for one.",
        facts="iPhone, iPad and Android · No account · Records stay on your device",
        audience="Massage therapists, physical therapists, physiotherapists, chiropractors and acupuncturists in solo practice",
        feat_title="A complete client record, kept by you",
        features=[
            ("Notes in the format you use", "SOAP, SOAP with goals, DAP, CARE or narrative, with prompts written for your profession. Copy last note in one tap, then edit what changed."),
            ("Quick phrases and chips", "The words you type every day, your own abbreviations, and technique, area and home-care chips instead of typing."),
            ("Body chart", "Front, back, spine and face views, or your own picture. Twelve symbols you can rename and recolor, with last visit's marks shown faintly for comparison."),
            ("Intake and consent", "Health history forms that flag possible contraindications for you to review, and informed consent your client signs on your device."),
            ("Signed and locked", "Signed notes are locked; later changes become dated addenda. ROM, manual muscle tests, PSFS, LEFS and a PART grid for chiropractors."),
            ("Print what they ask for", "One note, a date range or the complete record as a PDF with your letterhead. Receipts and superbills with CPT and ICD-10 codes."),
        ],
        how_title="Chart the visit, then hand over the record",
        steps=[
            ("Mark where it hurts", "Draw on the chart with your finger or a stylus, pinch to zoom. Everything prints onto the PDF exactly where you placed it."),
            ("Write the note", "Start from last time, tap your phrases, and let Compose turn your chart marks and techniques into a first draft you edit."),
            ("Stay organized", "A light schedule with reminders and one-tap rebooking, and search across clients, notes, addenda and form answers."),
        ],
        shots_alt=["SOAP Notes body chart, posterior view", "SOAP Notes note editor in SOAP format",
                   "SOAP Notes client intake form in client mode", "SOAP Notes PDF record preview"],
        keep_eyebrow="Your records",
        keep_title="No account, no server — we never see your clients",
        keep=[
            "<b>Records stay on your device.</b> There is no account and no sign-up.",
            "<b>Lock the app</b> with Face ID or its own passcode.",
            "<b>Encrypted backups you keep yourself</b> — in iCloud on iPhone and iPad, or in a folder you pick on Android.",
            "<b>Export everything</b> as CSV or JSON at any time, with an optional password on PDFs.",
        ],
        note="SOAP Notes is a record-keeping tool. It does not give medical advice or diagnoses, and following your local "
             "record-keeping rules remains your responsibility.",
        faq=[
            ("Who is SOAP Notes for?", "Therapists who work on their own: massage therapists, physical therapists and physios, chiropractors and acupuncturists."),
            ("Where are my client records stored?", "On your own device. There is no account and no server holding your records. You make encrypted backups that you keep yourself."),
            ("Which note formats are supported?", "SOAP, SOAP with goals, DAP, CARE and narrative notes, with prompts written for your profession."),
            ("Can clients sign intake and consent forms?", "Yes. Hand the device to your client in client mode; they fill in the health history and sign informed consent on screen."),
            ("Can I produce records for insurers?", "Yes. Export one note, a date range or the complete record as a PDF with your letterhead, and create receipts and superbills with CPT and ICD-10 codes."),
        ],
        cta="Chart your next client in two minutes",
        theme=dict(bg="#F5F7FA", accent="#2A4FA0", font="serif", radius=10, hero="split", features="ruled",
                   strip="bands", strip_colors=["#2A4FA0", "#2A4FA0", "#2A4FA0", "#E4A93B", "#2A4FA0", "#2A4FA0", "#2A4FA0", "#2A4FA0"]),
    ),
    # ------------------------------------------------------------------ Plant Journal
    dict(
        slug="plantjournal", key="plantjournal", name="Plant Journal", kind="Plant care journal and photo diary",
        title="Plant Journal — Plant care journal and photo diary for houseplants",
        desc="Plant Journal is a plant care journal and photo diary for the houseplants you grow at home. A page for each pot, "
             "watering on the plant's own rhythm with one reminder each morning, and a dated photo timeline of every plant growing up.",
        h1="A plant is a <em>slow thing</em>. Keep the pages.",
        lead="Plant Journal is a private notebook for the houseplants you grow at home. Each pot gets its own page, watering "
             "follows the plant's own rhythm, and every photo becomes a dated, pressed page — a timeline of the plant growing up.",
        facts="iPhone and Android · No account · Everything lives on your phone",
        audience="People who grow houseplants and want a care journal and photo diary",
        feat_title="Care on the plant's own rhythm",
        features=[
            ("A page for each pot", "What it is, where you found it, who gave it to you, which windowsill it lives on, how much light it likes, whether it is toxic to pets."),
            ("Watering that does not pile up", "This one every three days, that one once a week. The next date counts from the day you actually did it, and intervals stretch through the dormant months."),
            ("One reminder each morning", "The day's work in a single line — “today: water the Monstera, mist the fern”. Name the jobs yourself: water, feed, mist, or whatever yours needs."),
            ("A photo timeline", "Every photo becomes a pressed page, dated and labeled like a herbarium. Drag a slider between any two photos, or flip the album and watch it grow."),
            ("Pest log", "A photo of the damaged leaf and what you did about it. The plant wears a tag — healthy, watching, treating — until it is itself again."),
            ("The year at a glance", "Height and leaf count charted, this day a year ago, and a tally of every watering and every new arrival. Export the herbarium as a PDF."),
        ],
        how_title="Cuttings remember where they came from",
        steps=[
            ("Add a pot", "Give it a page and a rhythm. A cutting keeps the name of the pot it came from."),
            ("Do the morning line", "Water, mist or feed, and tick it off. A late watering never turns into debt."),
            ("Take a photo now and then", "Leave it a season and it is a different plant. The timeline shows you."),
        ],
        keep_title="Just you and the things you have grown",
        keep=[
            "<b>No accounts.</b> Nothing to sign up for.",
            "<b>Everything lives on your phone</b> and is exportable whenever you want it.",
            "<b>No plant ID sending your garden to a server.</b> You name your plants yourself.",
            "<b>Optional backup</b> to your own iCloud on iPhone.",
        ],
        faq=[
            ("Does Plant Journal identify plants from photos?", "No. It is a journal, not a plant identifier. You name your plants yourself and nothing is sent to a server."),
            ("How do watering reminders work?", "Each plant has its own interval. One gentle reminder each morning gathers the day's jobs into a single line, and the next date counts from the day you actually watered."),
            ("Can I track more than watering?", "Yes. Name the jobs yourself — water, feed, mist or anything else — and keep a pest log, height and leaf counts for each plant."),
            ("Do I need an account?", "No. There are no accounts, and everything lives on your phone."),
            ("Can I export my plant journal?", "Yes. Your data is exportable whenever you want it, and the photo herbarium exports as a PDF."),
        ],
        cta="Give your first pot a page",
        theme=dict(bg="#F4F1E7", accent="#3F6B4F", ink="#23261F", font="serif", radius=6, hero="center", features="rows", em="italic",
                   strip="bands", strip_colors=["#DDE5CF", "#BFD0AE", "#9DB98C", "#789F6C", "#56835A", "#3F6B4F", "#2F5440"]),
    ),
    # ------------------------------------------------------------------ SiteCalc
    dict(
        slug="sitecalc", key="sitecalc", name="SiteCalc", kind="Construction calculator",
        title="SiteCalc — Feet-inch construction calculator for concrete, framing, stairs and roofs",
        desc="SiteCalc is a construction calculator for carpenters, contractors and DIYers. Feet-inch-fraction and metric math, "
             "concrete, framing, rafters, stairs and roofing, with every result showing how it was worked out. No account, works offline.",
        h1="Feet, inches and fractions. <em>Right the first time.</em>",
        lead="Add 16′ 6-1/2″ to 3′ 7-3/4″ and read the answer three ways at once: feet-inch, decimal inches and millimetres. "
             "SiteCalc is a construction calculator for carpenters, contractors and serious DIYers — count the concrete bags, "
             "lay out the stringer, order the shingles.",
        facts="iPhone and Android · No signal needed · No account",
        audience="Carpenters, framers, contractors, builders and serious DIYers working in feet-inch-fraction or metric",
        feat_eyebrow="Six tools, one app",
        feat_title="The calculator in your tool pouch, plus the ones you wish it had",
        features=[
            ("Feet-Inch", "A keypad that takes 9-5/8″, 10′ 3.5″, 5 ft 14 in or 2400 mm as you go, with a running paper tape. Divide a span into equal marks, space balusters or joists evenly."),
            ("Concrete", "Slabs, footings, columns, tubes and steps in cubic yards or metres. Bags by brand yield, truck loads rounded up, waste included."),
            ("Framing", "Studs, plates and headers; joists; common, hip, valley and irregular rafters with the birdsmouth worked out; jack rafter lists; rake walls."),
            ("Stairs", "Risers, treads, both stringer lengths clearly labelled, the first-riser cut, a running-measurement table, and the code limits beside the results."),
            ("Roof", "Pitch in x/12, degrees or percent; area, squares, shingles, ridge cap, underlayment, tiles and sheets."),
            ("Convert", "Exact factors for length, area, volume, mass and density. Switch to metric and the whole app follows."),
        ],
        extra=dict(eyebrow="Every number shows its work", title="Tap any result to see how it was calculated",
                   sub="The formula with your numbers in it, the convention it used, and where that convention comes from.",
                   items=[("Pitch, rise, run, diagonal", "Enter any two and read the rest. Hip, valley and jack rafters, compound miters, circles and arcs from the keypad."),
                          ("Rounding you control", "Results snap to 1/16, or anything from 1/2 to 1/64, and show the rounding error when they do."),
                          ("Regional defaults", "Conventions for the US, UK and Australia are built in — IRC, Approved Document K, NCC — and every one can be changed."),
                          ("Jobs and material lists", "Keep calculations in jobs, total the materials for a whole job and share a PDF material list with the yard or the client.")]),
        how_title="Made for the site, not the cloud",
        keep_title="No account, no ads, no signal needed",
        keep=[
            "<b>Works offline.</b> Nothing needs a signal on site.",
            "<b>Your jobs and calculations stay on your phone.</b>",
            "<b>Back up to a file</b> whenever you like.",
            "<b>No account and no ads.</b>",
        ],
        note="Reference only. Verify against your local code and supplier before cutting or ordering.",
        faq=[
            ("Can SiteCalc add feet, inches and fractions?", "Yes. Type lengths the way you say them — 16′ 6-1/2″, 9-5/8″, 5 ft 14 in or 2400 mm — and read every result in feet-inch, decimal inches and millimetres."),
            ("Does it calculate rafters and stairs?", "Yes. Common, hip, valley, jack and irregular rafters with the birdsmouth, and stairs with risers, treads, stringer lengths and the first-riser cut."),
            ("Does it work in metric?", "Yes. Switch to metric and the whole app follows, with defaults for the US, UK and Australia."),
            ("Does SiteCalc work without a signal?", "Yes. No account, no ads and no signal needed."),
            ("Can I see how a result was calculated?", "Yes. Tap “How it's calculated” on any result to see the formula with your numbers in it and the convention it used."),
        ],
        cta="Measure once, calculate once",
        theme=dict(bg="#F3F5F8", accent="#1E5AA8", ink="#141A22", font="mono", radius=4, hero="split", features="ruled", weight=700,
                   track="-.03em", h1=(30, 46), h2=32, em="normal", strip="ticks", strip_colors=["#F2B705", "#141A22"]),
    ),
    # ------------------------------------------------------------------ Prayline
    dict(
        slug="prayline", key="prayline", name="Prayline", kind="Muslim prayer times and prayer tracker",
        title="Prayline — Muslim prayer times, Qibla and prayer tracker that works offline",
        desc="Prayline shows the next prayer, the time until it, and one tap to record the one you just prayed. Prayer times "
             "calculated on your phone, Qibla, Qada counter, fasting log and tasbih. No account, no ads, works offline.",
        h1="The next prayer, the time until it, <em>one tap to record it.</em>",
        lead="Prayer times are calculated on your phone, so they work at home, at the office and on a plane. Your five daily "
             "prayers, the ones you still owe, your fasts and your tasbih are kept in one place that never asks you to sign in "
             "and never shows an ad.",
        facts="iPhone and Android · Works offline · No account, no ads",
        audience="Muslims who want prayer times, Qibla direction and a private record of their prayers and fasts",
        feat_title="Today, at a glance",
        features=[
            ("Prayer times that work offline", "Fajr, Dhuhr, Asr, Maghrib and Isha calculated on the device from your location or a city you pick. No internet needed."),
            ("The method you follow", "MWL, ISNA, Umm al-Qura, Egyptian, Karachi, Dubai, Qatar, Kuwait, Singapore, Turkey, Tehran, Moonsighting Committee or Jafari; Shafi or Hanafi Asr; a minute adjustment for each prayer."),
            ("One tap to record", "Record a prayer as prayed on time, late or missed, and undo any change. Nothing is marked for you."),
            ("Qibla", "The direction to the Kaaba calculated on your phone, with a dial that turns with you and a gentle tap when you are facing it."),
            ("Qada, counted your way", "Enter the prayers you still owe for each of the five and count one down each time you make one up."),
            ("Ramadan and fasting", "Suhoor and iftar times with a countdown to each. Record each day as fasted or not, and keep the fasts to make up."),
        ],
        how_title="A record that stays between you and your phone",
        steps=[
            ("See the next prayer", "A countdown at the top, today's Hijri date beside the day, and a reminder for each prayer if you want one."),
            ("Record what happened", "On time, late or missed. Turn on Witr, Duha or Tahajjud and record them under the five."),
            ("Look back", "A calendar of every day, a streak of complete days, and stats for the week, the month or any dates you choose."),
        ],
        keep_title="Never asks you to sign in, never sends what you record",
        keep=[
            "<b>Calculated on your phone.</b> Prayer times and Qibla need no server.",
            "<b>No account and no ads.</b>",
            "<b>Your record stays on your device.</b> What you record is not sent anywhere.",
            "<b>Hijri date</b> by Umm al-Qura or the tabular calendar, adjustable by up to two days either way.",
        ],
        faq=[
            ("Does Prayline work offline?", "Yes. Prayer times and the Qibla direction are calculated on the device, so they work without internet — at home, at the office and on a plane."),
            ("Which calculation methods are supported?", "MWL, ISNA, Umm al-Qura, Egyptian, Karachi, Dubai, Qatar, Kuwait, Singapore, Turkey, Tehran, Moonsighting Committee and Jafari, with Shafi or Hanafi Asr, three high-latitude rules and a minute adjustment for each prayer."),
            ("Can I keep track of missed prayers (Qada)?", "Yes. Enter the prayers you still owe for each of the five and count one down each time you make one up. A missed prayer can be added to Qada with a tap."),
            ("Are there ads or an account?", "No. Prayline never asks you to sign in and never shows an ad."),
            ("Does it include a Qibla compass and tasbih?", "Yes. Both are in the app, along with a fasting log for Ramadan and voluntary fasts."),
        ],
        cta="The whole screen is the next prayer",
        theme=dict(bg="#FAF5EC", accent="#2B3A7A", ink="#1B1E2B", font="serif", radius=20, hero="center", features="rows",
                   strip="gradient", strip_colors=["#131A3D", "#2B3A7A", "#7C5A9B", "#E88B4A", "#F7C873", "#FBE9C2"]),
    ),
    # ------------------------------------------------------------------ Shelflife
    dict(
        slug="shelflife", key="shelflife", name="Shelflife", kind="Book journal and home library",
        title="Shelflife — Book tracker and reading journal for paper books",
        desc="Shelflife is a book tracker and reading journal for paper books. Scan an ISBN, set the book on its shelf, log every "
             "reading and reread, keep notes and quotes by page. A private home library with no account that works offline.",
        h1="A home library <em>with a memory.</em>",
        lead="Some books are more than their pages — the one from a street market, the one your mother gave you, the one you "
             "have read three times. Shelflife is a book tracker and reading journal for paper books: scan an ISBN, set the "
             "book on its shelf, and keep everything it means to you.",
        facts="iPhone and Android · Works offline · No account",
        audience="Readers who own paper books and want a home library catalog and a reading journal",
        feat_title="Built for paper books and for rereading",
        features=[
            ("ISBN barcode scanner", "Add books in seconds by scanning the barcode, or by hand."),
            ("Where the book really lives", "Shelve every book by room, shelf or box, and find it again with search."),
            ("What makes the copy yours", "Edition, condition, receipt, what you paid and what it is worth."),
            ("Lending tracker", "Mark a book as loaned and always know who has it."),
            ("Every reading is its own entry", "Reread a book years later and both readings stand side by side. Log sessions with pages and minutes."),
            ("Notes, quotes and moments", "Keep notes and quotes by page, turn a favorite line into a quote card, and attach photos and moments to any book."),
        ],
        how_title="A reading log that becomes an album",
        steps=[
            ("Scan and shelve", "Point at the barcode, pick the shelf."),
            ("Read and note", "Want to read, reading, finished, did not finish — with sessions, pages and quotes."),
            ("Look back", "A timeline of your reading life and yearbook stats: books read, pages turned, top authors."),
        ],
        keep_title="Quiet by design",
        keep=[
            "<b>No account.</b> No feed, no one reading over your shoulder.",
            "<b>Your whole library lives on your phone</b> and works offline.",
            "<b>Export a ZIP backup</b> whenever you want.",
        ],
        faq=[
            ("Is Shelflife for paper books or ebooks?", "It is built for paper books: where each copy lives, its edition and condition, who borrowed it."),
            ("Can I add books by scanning the barcode?", "Yes. Scan the ISBN barcode to add a book in seconds, or enter it by hand."),
            ("Can I track rereads?", "Yes. Every reading is its own journal entry, so a reread years later stands beside the first one."),
            ("Is there a social feed?", "No. There is no account and no feed. Your library is private and lives on your phone."),
            ("Can I back up my library?", "Yes. Export everything to a ZIP backup whenever you want."),
        ],
        cta="Your shelf, your ink, your story",
        theme=dict(bg="#F6F1E6", accent="#8A3B2E", ink="#231C17", font="serif", radius=6, hero="split", features="ruled", weight=700,
                   strip="bands", strip_colors=["#3F5E4A", "#3F5E4A", "#C9A36A", "#8A3B2E", "#8A3B2E", "#2E3F52", "#C9A36A", "#3F5E4A", "#8A3B2E"]),
    ),
    # ------------------------------------------------------------------ Memento
    dict(
        slug="memento", key="anniversary", name="Memento", kind="Anniversary countdown and memories",
        title="Memento — Anniversary countdown and day counter that keeps the memories",
        desc="Memento counts down to the days ahead and up through the ones you have shared, then asks for one photo and a few "
             "words each year. Milestones, On This Day, a photo album and journal for every event. No account, works offline.",
        h1="Some days deserve more than <em>a number on a calendar.</em>",
        lead="The first date. The wedding. The day the dog came home. Memento counts those days for you — down to the ones "
             "ahead, up through the ones you have shared — and each year, when the day comes around, it asks for one photo "
             "and a few words. That is how a countdown becomes a timeline.",
        facts="iPhone and Android · Works offline · No account",
        audience="Couples, families and anyone who wants to count and remember anniversaries, birthdays and milestones",
        feat_title="A countdown that grows into a story",
        features=[
            ("Counts down and counts up", "Days left, days together, years passed — for birthdays, weddings, first dates, pets."),
            ("Milestones on its own", "100 days, 365, 1,000, five years, ten. Memento marks them without being asked."),
            ("On This Day", "The same date, remembered across the years."),
            ("An album and a journal for every event", "One photo and a few words each year, kept together under the day they belong to."),
            ("Reminders ahead of time", "30, 7 or 1 day before, so no day slips by."),
            ("Solar or lunar dates", "Count by the solar calendar or the Vietnamese lunar calendar. Templates, colour themes and app icons to make it yours."),
        ],
        how_title="Year after year",
        steps=[
            ("Add the day", "Pick a template or start blank."),
            ("Watch it count", "Down to the next one, up from the first."),
            ("Add one photo a year", "When the day comes around, keep a photo and a few words."),
        ],
        keep_title="Quiet by design",
        keep=[
            "<b>No account.</b> Works offline.",
            "<b>Locks behind a PIN</b> only you know.",
            "<b>Back up</b> to iCloud on iPhone or to a ZIP file, and export everything anytime.",
        ],
        faq=[
            ("Can Memento count both down and up?", "Yes. It counts down to days ahead and up from days that have passed — days left, days together, years passed."),
            ("Does it remind me before an anniversary?", "Yes. Reminders 30, 7 or 1 day ahead."),
            ("Can I add photos and notes?", "Yes. Every event has a photo album and a journal, with one photo and a few words for each year."),
            ("Does it support lunar dates?", "It supports solar dates and the Vietnamese lunar calendar."),
            ("Do I need an account?", "No. There is no account and it works offline."),
        ],
        cta="Start with the day that matters most",
        theme=dict(bg="#FFF5EE", accent="#E2632B", font="serif", radius=28, hero="center", features="cards",
                   strip="gradient", strip_colors=["#F7B267", "#F4845F", "#E2632B", "#F25C7A", "#F7B5C4"]),
    ),
    # ------------------------------------------------------------------ Focal
    dict(
        slug="focal", key="focal", name="Focal", kind="Visual timer and routines",
        title="Focal — Visual timer and routine timer for ADHD time blindness",
        desc="Focal is a visual timer: a colored disk that shrinks as your time runs out. Chain short steps into routines, see "
             "the countdown on your lock screen, and get a gentle nudge when you overrun. No account, works in airplane mode.",
        h1="See the time <em>you have left.</em>",
        lead="Focal turns a countdown into something you can look at: a colored disk that shrinks as your time runs out — the "
             "same idea as the timer on a classroom wall, in your pocket. A routine is a chain of short steps; Focal shows you "
             "the one you are on and nothing else.",
        facts="iPhone and Android · No internet needed · No account",
        audience="People with ADHD or time blindness, students, parents and anyone who works better with a visual timer",
        feat_title="Built for the way attention actually works",
        features=[
            ("A timer you can see", "Full-screen countdown in three shapes: disk, bar or pie."),
            ("One thing at a time", "A routine is a chain of short steps, each with its own length. Focal moves to the next one by itself."),
            ("Ready-made routines", "Morning launch, shutdown, cleaning sprint, a study block — start with ten or build your own."),
            ("Gentle nudges", "Haptics at the halfway mark and in the final minute. When time is up the clock keeps counting, and Focal taps you again at five and fifteen minutes."),
            ("Add a minute", "Extend the step without losing your place."),
            ("Eight themes", "Including a high-contrast theme and a quiet monochrome one."),
        ],
        extra=dict(eyebrow="On iPhone", title="Time you can see, everywhere",
                   items=[("Lock Screen and Dynamic Island", "A Live Activity keeps the countdown running on your lock screen."),
                          ("Widgets", "Home and Lock Screen widgets for your next routine."),
                          ("StandBy", "Put the phone on its side while charging and it becomes a desk timer."),
                          ("Start hands-free", "From Siri, the Action Button or Control Center.")]),
        how_title="For when “five more minutes” quietly becomes an hour",
        keep_title="No internet needed",
        keep=[
            "<b>No account. No cloud.</b>",
            "<b>Nothing you make leaves your phone.</b>",
            "<b>Works in airplane mode</b>, because the timer never needed the internet.",
        ],
        faq=[
            ("What is a visual timer?", "A timer that shows the time left as a shape instead of only digits. In Focal it is a colored disk, bar or pie that shrinks as your time runs out."),
            ("Is Focal designed for ADHD?", "It is designed around time blindness: one step on screen at a time, gentle haptics at the halfway mark and the final minute, and a nudge at five and fifteen minutes after time is up."),
            ("Can I chain timers into a routine?", "Yes. A routine is a chain of short steps, each with its own length, and Focal moves from one to the next by itself."),
            ("Does the timer show on the lock screen?", "On iPhone, yes — as a Live Activity on the Lock Screen and in the Dynamic Island, and as a desk timer in StandBy."),
            ("Does Focal need an account or internet?", "No. There is no account and the timer works in airplane mode."),
        ],
        cta="Start a timer you can see",
        theme=dict(bg="#FBF2EA", accent="#E0533A", font="sans", radius=30, hero="split", features="cards", weight=800, track="-.035em",
                   h1=(38, 62), em="normal", strip="gradient", strip_colors=["#E0533A", "#E0533A 62%", "#F3D9CC 62%", "#F3D9CC"]),
    ),
]

APPS = []


def _register(items):
    for a in items:
        APPS.append({**META[a["key"]], **a, "icon": a["key"]})


from content2 import APPS2  # noqa: E402

_register(_APPS + APPS2)
