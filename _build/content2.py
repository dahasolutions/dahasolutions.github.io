"""Second half of the app pages. Same rules as content.py."""

APPS2 = [
    # ------------------------------------------------------------------ Doughbook
    dict(
        slug="doughbook", key="doughbook", name="Doughbook", kind="Recipe costing and orders for home bakers",
        title="Doughbook — Recipe cost calculator and order book for home bakeries",
        desc="Doughbook is a recipe cost calculator, order book and bake planner for cottage bakers, cake makers and cookie "
             "decorators. Know what every bake costs, keep orders in one place, print labels with allergens, send invoices as PDF. "
             "No account; your recipes stay on your phone.",
        h1="From the price of a bag of flour to <em>the price of a cupcake.</em>",
        lead="Doughbook is a recipe cost calculator, order book and bake planner for the home bakery: the cottage baker, the "
             "cake maker, the cookie decorator, the sourdough seller. Built for one person running the whole show from a home "
             "kitchen and a phone.",
        facts="iPhone and Android · No account · Recipes stay on your phone",
        audience="Home bakers and cottage food businesses: cake makers, cookie decorators, sourdough sellers",
        feat_title="Know what every bake costs you",
        features=[
            ("Buy it the way you buy it", "Enter a 5 lb bag, a dozen eggs, a pound of butter. Build recipes in cups or grams; Doughbook does the converting."),
            ("Cost per piece", "What one cupcake, one cookie, one 8-inch cake actually costs — labor and box included."),
            ("A price that pays you back", "A suggested price, and a warning when you are about to sell below your floor."),
            ("Orders in one place", "Who, what, when, deposit paid, balance due — not six chat threads."),
            ("A week that fills itself", "Confirm an order and bake days land on the calendar and ingredients on the shopping list, added up across every order in the bags and cartons you actually buy."),
            ("Paperwork from data you already have", "Quotes, invoices and receipts as PDF. Labels with the ingredient list in the right order and allergens in bold."),
        ],
        how_title="One person, one kitchen, one phone",
        steps=[
            ("Cost a recipe", "Add what you buy once; every recipe that uses it stays up to date."),
            ("Take the order", "Deposit, balance and pickup date in one card, with reminders and a home screen widget for the day."),
            ("Hand over the box", "Send the invoice or receipt the moment the cake goes out the door."),
        ],
        keep_title="Your recipes stay yours",
        keep=[
            "<b>Recipes, orders and customers live on your phone.</b>",
            "<b>No account to create and no ads.</b>",
            "<b>No server that can shut down</b> and take your recipes with it.",
            "<b>Export to CSV or a full backup</b> whenever you like.",
            "<b>Cottage food limit:</b> keep an eye on your yearly sales against your state's cap.",
        ],
        faq=[
            ("How does Doughbook calculate recipe cost?", "You enter ingredients the way you buy them — a 5 lb bag, a dozen eggs — and build recipes in cups or grams. Doughbook converts and works out the cost of one piece, with labor and packaging included."),
            ("Can it suggest what to charge?", "Yes. It suggests a price that covers your costs and warns you when you are about to sell below your floor."),
            ("Does it handle orders and invoices?", "Yes. Orders keep the customer, items, date, deposit and balance, and you can send quotes, invoices and receipts as PDF."),
            ("Can I print ingredient labels?", "Yes. Labels list ingredients in the right order with allergens in bold."),
            ("Do I need an account?", "No. Your recipes, orders and customers live on your phone, and you can export a full backup whenever you like."),
        ],
        cta="Cost your first recipe",
        theme=dict(bg="#FFF7E8", accent="#C9780A", ink="#2A2118", font="slab", radius=14, hero="split", features="cards", weight=700,
                   track="-.01em", strip="bands", strip_colors=["#F6C445", "#FFF1C9", "#F6C445", "#FFF1C9", "#F6C445", "#FFF1C9", "#F6C445", "#FFF1C9", "#F6C445", "#FFF1C9", "#F6C445", "#FFF1C9"]),
    ),
    # ------------------------------------------------------------------ Pitbook
    dict(
        slug="pitbook", key="pitbook", name="Pitbook", kind="Fuel and service log",
        title="Pitbook — Car maintenance log and fuel tracker that stays yours",
        desc="Pitbook is a vehicle maintenance log and fuel tracker for cars, motorcycles, campers and boats. Log a fill-up in "
             "five seconds, get reminders by date or odometer, attach receipts, see fuel economy and cost per mile. No account, works offline.",
        h1="A maintenance log <em>that stays yours.</em>",
        lead="Every service, every fill-up and every receipt lives on your phone. Logging a fill-up takes about five seconds; "
             "after that, Pitbook does the remembering — it tracks what is due by date, by odometer, or both, and always counts "
             "from the last time you actually did the work.",
        facts="iPhone and Android · Works offline · No account",
        audience="Owners who maintain their own cars, motorcycles, campers and boats",
        feat_title="Built for whatever you maintain",
        features=[
            ("Cars, motorcycles, campers, boats", "Each with its own service checklist. Boats and generators can run on engine hours instead of an odometer."),
            ("Petrol, diesel or electric", "An EV logs kWh and skips the oil change entirely."),
            ("Reminders that respect you", "One tap sets up the usual schedule for your kind of vehicle. One daily summary of what is coming due, never a stream of alerts."),
            ("Fuel economy done properly", "Measured between full fill-ups, with partial fills handled. L/100 km, km/L, mpg (US) or mpg (UK) — miles with litres is fine."),
            ("Where the money goes", "Monthly spending, cost by category, cost per mile, and how the price you pay for fuel has moved."),
            ("Receipts and warranty", "Attach receipt photos to any record. Track warranty limits by date or odometer, whichever runs out first."),
        ],
        how_title="Five seconds at the pump",
        steps=[
            ("Add your vehicle", "Enter a VIN and Pitbook checks it and reads back the model year."),
            ("Log as you go", "A fill-up in about five seconds, a service in a few taps. Mark a service done straight from the notification."),
            ("Hand over the history", "A printed service history in PDF — the document that helps a private sale."),
        ],
        keep_title="Your data, always portable",
        keep=[
            "<b>No account.</b> Your records live on your phone and work entirely offline.",
            "<b>Export</b> your records as CSV or JSON whenever you want.",
            "<b>Back up the whole garage</b> to a single file, photos included, and restore it just as easily.",
            "<b>Coming from a spreadsheet?</b> Import the CSV and retype nothing.",
            "<b>Optional lock</b> with Face ID or fingerprint.",
        ],
        faq=[
            ("What vehicles can I track in Pitbook?", "Cars, motorcycles, campers and boats, each with its own service checklist. Petrol, diesel and electric are supported, and boats or generators can use engine hours."),
            ("How do service reminders work?", "Pitbook tracks what is due by date, by odometer, or both, counting from the last time you actually did the work, and sends one daily summary of what is coming due."),
            ("Does it calculate fuel economy?", "Yes, between full fill-ups, with partial fills handled properly, in L/100 km, km/L, mpg (US) or mpg (UK)."),
            ("Can I import my existing log?", "Yes. Import a CSV from your spreadsheet. You can also export your records as CSV or JSON and back up everything to a single file."),
            ("Do I need an account?", "No. There is no account and Pitbook works entirely offline."),
        ],
        cta="Log the last thing you did to it",
        theme=dict(bg="#F5F3F0", accent="#D9661F", ink="#1A1714", font="condensed", radius=4, hero="split", features="rows", weight=800,
                   track=".005em", case="uppercase", h1=(36, 58), h2=38, em="normal", strip="stripes", strip_colors=["#1A1714", "#E8892E"]),
    ),
    # ------------------------------------------------------------------ Moodee
    dict(
        slug="moodee", key="moodee", name="Moodee", kind="Mood tracker and journal",
        title="Moodee — Private mood tracker and mood journal with 10-second check-ins",
        desc="Moodee is a calm, private mood tracker and mood journal. Check in with how you feel in under 10 seconds, add notes, "
             "photos or voice memos, and see patterns by weekday, sleep, stress and energy. No account; everything stays on your device.",
        h1="How are you, really? <em>Ten seconds</em> to check in.",
        lead="Moodee is a calm, private mood tracker and mood journal. Pick one of five moods and, if you like, add a note, a "
             "photo, a voice memo, tags, your stress and energy levels, or last night's sleep. Over time your check-ins become "
             "a picture of how you are really doing.",
        facts="iPhone and Android · Works fully offline · No account",
        audience="Anyone who wants a private mood diary and to see patterns in how they feel",
        feat_title="One required tap, everything else optional",
        features=[
            ("10-second check-ins", "One tap on a mood is enough. Note prompts adapt to how you feel."),
            ("Photos and voice memos", "Attach them to any check-in, along with tags, stress, energy and sleep."),
            ("Calendar and Year in Pixels", "A mood-colored calendar, a whole year in pixels, and a timeline of your entries."),
            ("Reports and insights", "A weekly report, a monthly letter, and insights: mood by weekday and time of day, against sleep, stress and energy, and which tags lift you up or drag you down."),
            ("For heavy days", "Breathing and 5-4-3-2-1 grounding exercises."),
            ("Make it yours", "23 color themes, 4 mood icon sets, a home screen widget for one-tap check-ins, and an app lock."),
        ],
        how_title="A picture that builds itself",
        steps=[
            ("Check in", "One tap from the app or the widget."),
            ("Add what matters", "A line, a photo, a voice memo — or nothing."),
            ("See the pattern", "Weekly reports and insights turn entries into something you can read."),
        ],
        keep_title="Your moods never leave your device",
        keep=[
            "<b>No account, no sign-in, no sync.</b>",
            "<b>Moods, notes, photos and voice memos stay on your device.</b>",
            "<b>Works fully offline.</b>",
            "<b>PDF export and full backup</b> when you want a copy.",
        ],
        note="Moodee is a journal. It is not a medical or mental health service and does not give advice.",
        faq=[
            ("How long does a check-in take?", "Under 10 seconds. Picking one of five moods is the only required tap; everything else is optional."),
            ("Where is my mood data stored?", "On your device. There is no account, no sign-in and no sync; your moods, notes, photos and voice memos never leave it."),
            ("What insights does Moodee show?", "Mood by weekday and by time of day, mood against sleep, stress and energy, and which tags lift you up or drag you down, plus a weekly report and a monthly letter."),
            ("Can I lock the app?", "Yes. Moodee has an app lock."),
            ("Can I export my journal?", "Yes. PDF export and a full backup are built in."),
        ],
        cta="Check in with yourself",
        theme=dict(bg="#F7F1E5", accent="#2F9C83", font="rounded", body="rounded", radius=28, hero="center", features="cards", weight=800,
                   strip="bands", strip_colors=["#E4572E", "#F3A712", "#F7D354", "#76B947", "#2F9C83"]),
    ),
    # ------------------------------------------------------------------ Ladle
    dict(
        slug="ladle", key="ladle", name="Ladle", kind="Recipe box and meal planner",
        title="Ladle — Recipe box, meal planner and grocery list from anything you paste",
        desc="Ladle turns whatever you paste — text, a photo of a page, a share from the browser — into a recipe with real "
             "ingredients and steps, read on your phone. Plan the week, get one grocery list grouped like a store, cook with "
             "several timers. No account, no feed.",
        h1="Paste anything. Get <em>a recipe you can cook from.</em>",
        lead="A recipe you actually cook rarely arrives in a tidy format: a screenshot from a friend, a photo of a page, a wall "
             "of text buried under someone's life story. Ladle takes whatever you paste and turns it into a recipe with real "
             "ingredients and real steps. The reading happens on your phone, so it works in a kitchen with no signal.",
        facts="iPhone and Android · Reads recipes on your phone · No account",
        audience="Home cooks who save recipes from screenshots, photos and web pages and plan meals for the week",
        feat_title="A cookbook that pulls its weight",
        features=[
            ("Paste, snap or share", "Text, a photo, or a share from your browser becomes a recipe with ingredients and steps."),
            ("Read on your phone", "The recipe is parsed on the device. Nothing leaves it, and it works with no signal."),
            ("Plan the week", "Drop recipes onto days and every ingredient lands in one grocery list."),
            ("A list laid out like a store", "Ingredients are grouped the way a store is laid out, so you walk the aisles once."),
            ("Several timers at once", "Cook with more than one timer running. On iPhone they show on the Lock Screen, so you do not unlock with wet hands."),
            ("Shop together", "Share the list with whoever else shops and tick things off from either phone."),
        ],
        how_title="From a screenshot to dinner",
        steps=[
            ("Save it", "Paste the text, snap the page or share the link."),
            ("Plan it", "Pick the days. The grocery list builds itself."),
            ("Cook it", "Step by step, timers running."),
        ],
        keep_title="A cookbook that sits on the shelf and waits",
        keep=[
            "<b>No account, no server, no feed.</b>",
            "<b>Recipes are read on your phone</b> — nothing is sent away to be parsed.",
            "<b>On iPhone, recipes sync across your own devices through iCloud.</b>",
        ],
        faq=[
            ("How do I add a recipe to Ladle?", "Paste text, take a photo of a page, or share a page from your browser. Ladle turns it into a recipe with ingredients and steps."),
            ("Does recipe import need the internet?", "No. The reading happens on your phone, so it works in a kitchen with no signal."),
            ("Does Ladle make a grocery list?", "Yes. Plan the week and every ingredient lands in one grocery list, grouped the way a store is laid out."),
            ("Can two people use the same grocery list?", "Yes. Share the list with whoever else shops and tick things off from either phone."),
            ("Do I need an account?", "No. There is no account, no server and no feed."),
        ],
        cta="Save the next recipe you find",
        theme=dict(bg="#FBF6EF", accent="#3E8E5A", font="serif", radius=22, hero="center", features="rows",
                   strip="gradient", strip_colors=["#F8C8D0", "#FBE3A1", "#BFE3C0", "#B9D8F2"]),
    ),
    # ------------------------------------------------------------------ Chore Jar
    dict(
        slug="chorejar", key="chorejar", name="Chore Jar", kind="Chores and allowance on one family phone",
        title="Chore Jar — Chore chart and allowance tracker on one phone, no accounts for kids",
        desc="Chore Jar is a chore chart and allowance app that runs on a parent's phone. Each kid taps their own PIN, ticks "
             "off chores and watches their jar fill up. Approvals, payday, savings goals and a fairness check between siblings. "
             "No account, no app on kids' devices.",
        h1="Every chore, every kid, <em>one phone.</em>",
        lead="Your kids tap their own PIN on your phone or the family tablet, tick off what they did, and watch their jar fill "
             "up. You approve, the app does the math, and payday comes with a fairness check so nobody can say the other one "
             "got off easy.",
        facts="iPhone, iPad and Android · No account · No app on your kids' devices",
        audience="Parents of children aged about 3 to 12 who want a chore chart and allowance tracker",
        feat_title="A week of chores in five minutes",
        features=[
            ("Kid Mode with a PIN each", "Hand the phone over and it switches to big icons and few words, with no way out except the parent PIN. Picture PINs for kids who do not know numbers yet."),
            ("Age-based templates", "Start from sets for ages 3 to 5, 6 to 8 and 9 to 12, and add a dozen chores at once."),
            ("Schedules that fit real weeks", "Daily, chosen weekdays, a few times a week, once or monthly. Missed chores are marked, never carried over as debt."),
            ("Rotate between siblings", "Assign a chore to one kid, rotate it each week or each day, or leave it open for whoever does it first."),
            ("Approve, pay part, send back", "Review what was done, with an optional photo as proof, and send a note the kid reads in Kid Mode."),
            ("Reward store", "Kids spend what they earned on movie night or fifteen more minutes before bed. You confirm before anything is deducted."),
        ],
        extra=dict(eyebrow="Allowance", title="Allowance that adds itself up",
                   items=[("Money, stars or points", "One Spend jar by default; turn on Save and Give for any kid with a split you choose."),
                          ("Payday", "Adds the weekly allowance plus what each kid earned, whether or not you opened the app that day."),
                          ("Savings goals", "A progress bar the kid can see, and parent-bank interest at a rate you set."),
                          ("Fair between siblings", "See what each kid was assigned, did and earned, and rebalance next week with one tap.")]),
        how_title="Made for kids who cannot read yet, too",
        steps=[
            ("Hand to kids", "They tap their PIN and see morning, evening and anytime chores."),
            ("One tap to finish", "Read-aloud says the chore name; a visual countdown runs for brushing teeth or reading."),
            ("Confetti, then payday", "Streaks and badges at 7, 30 and 100 days, and a weekly recap you can share as a PDF."),
        ],
        keep_title="Nothing leaves your phone",
        keep=[
            "<b>No account.</b>",
            "<b>No app on your kids' devices.</b> Everything runs on yours.",
            "<b>Nothing leaves your phone</b> unless you share a recap or export.",
            "<b>Export everything as CSV</b> for a spreadsheet.",
        ],
        faq=[
            ("Do my kids need their own phone or account?", "No. Chore Jar runs on your phone or the family tablet. Each kid has a PIN, and there is no account and no app on their devices."),
            ("What ages is Chore Jar for?", "Templates cover ages 3 to 5, 6 to 8 and 9 to 12. Picture PINs and read-aloud help kids who cannot read yet."),
            ("Can it track allowance?", "Yes, in money, stars or points, with Spend, Save and Give jars, a weekly payday, savings goals and optional parent-bank interest."),
            ("How does it keep things fair between siblings?", "A fairness view shows what each kid was assigned, did and earned, flags when one is carrying much more than another, and proposes swaps for next week."),
            ("Can kids cheat by marking chores done?", "You approve what they tick off. You can require a photo as proof, pay part, or send a chore back with a note."),
        ],
        cta="Set up this week's chores in five minutes",
        theme=dict(bg="#F1F8FF", accent="#E79A00", ink="#17222E", font="rounded", body="rounded", radius=26, hero="split", features="cards",
                   weight=800, strip="dots", strip_colors=["#F2B632", "#2F86D6", "#F2637E", "#5BB36A", "#8A63D2"]),
    ),
    # ------------------------------------------------------------------ Side Ledger
    dict(
        slug="sideledger", key="sideledger", name="Side Ledger", kind="1099 tax tracker for the self-employed",
        title="Side Ledger — 1099 tax estimator and quarterly tax tracker for gig workers",
        desc="Side Ledger keeps a running estimate of the federal and state taxes you owe on 1099 income while you earn. "
             "Log payouts, receipts and mileage, see the quarterly deadline countdown, export for your accountant. No bank login, no account.",
        h1="Know what you owe the IRS <em>before the bill arrives.</em>",
        lead="Side Ledger keeps a running estimate of your federal and state taxes while you earn. Log a payout, snap a "
             "receipt, add your miles — the number on your dashboard updates on the spot, next to a countdown to the quarterly "
             "deadline. Built for rideshare and delivery drivers, online sellers, creators and freelancers.",
        facts="iPhone, iPad and Android · For US 1099 income · No bank login, no account",
        audience="US gig workers and freelancers with 1099 income: rideshare and delivery drivers, online sellers, creators",
        feat_title="The number that matters, always in sight",
        features=[
            ("A running tax estimate", "Estimated federal and state tax owed, updated every time you log something."),
            ("Quarterly deadlines", "A countdown to every IRS quarterly deadline, with reminders before each one. Mark each payment as paid and watch the number come down."),
            ("See how it is worked out", "A step-by-step breakdown: self-employment tax, income tax, QBI deduction."),
            ("Log it in three taps", "Income, expenses and mileage. Every expense is filed under a Schedule C category, and miles show as dollars deducted."),
            ("Receipts read on your phone", "Snap a receipt and the total, date and merchant are read on the device — offline."),
            ("Ready for your accountant", "Export a clean CSV and a one-page PDF summary."),
        ],
        how_title="Three seconds between rides",
        steps=[
            ("Log the payout", "Or the receipt, or the miles."),
            ("Watch the estimate move", "The dashboard shows what to set aside."),
            ("Pay the quarter", "Mark it paid and start the next one."),
        ],
        keep_title="Your books stay yours",
        keep=[
            "<b>No bank login.</b> You enter what you earned and spent.",
            "<b>No account to create.</b> Income and receipts live on your device.",
            "<b>The estimator works in airplane mode.</b>",
            "<b>On iPhone, a backup goes to your own iCloud</b> — never to us.",
            "<b>Current tax-year figures</b> arrive without waiting for an app update.",
        ],
        note="Side Ledger gives estimates to help you plan. It is not tax advice and it does not file your taxes.",
        faq=[
            ("Who is Side Ledger for?", "Anyone in the US with 1099 income and nobody withholding taxes for them: rideshare and delivery drivers, online sellers, creators and freelancers."),
            ("Does it connect to my bank?", "No. There is no bank login and no account. You log payouts, expenses and mileage yourself, in about three taps each."),
            ("How is the tax estimate calculated?", "From what you log, using built-in federal rates and state taxes, with a step-by-step breakdown of self-employment tax, income tax and the QBI deduction."),
            ("Does it track quarterly estimated taxes?", "Yes. It shows a countdown to every IRS quarterly deadline, reminds you before each one, and lets you mark payments as paid."),
            ("Does Side Ledger file my taxes?", "No. It estimates what you owe and exports a CSV and a one-page PDF summary for you or your accountant."),
        ],
        cta="See your number before the deadline does",
        theme=dict(bg="#FBF4EC", accent="#D95B16", ink="#1D1915", font="sans", radius=12, hero="split", features="ruled", weight=800,
                   track="-.03em", em="normal", strip="bands",
                   strip_colors=["#D95B16", "#D95B16", "#D95B16", "#D95B16", "#D95B16", "#1F6F6B", "#D95B16", "#D95B16"]),
    ),
    # ------------------------------------------------------------------ Zero Owed
    dict(
        slug="zeroowed", key="zeroowed", name="Zero Owed", kind="Debt payoff planner",
        title="Zero Owed — Debt payoff planner with snowball and avalanche, no bank connection",
        desc="Zero Owed is a debt payoff planner. Enter your debts once and see the month you will be debt-free. Compare snowball, "
             "avalanche and your own order, test extra payments, and track what you actually paid. No account, no bank connection, no ads.",
        h1="See the month you will be <em>debt-free.</em>",
        lead="Enter your debts once — credit cards, car loans, student loans, buy now pay later, medical bills. Pick snowball "
             "or avalanche, add what extra you can pay, and watch the payoff date move before you decide anything.",
        facts="iPhone and Android · No bank connection · No account, no ads",
        audience="People paying off credit cards, loans and other debts who want a payoff plan they can check",
        feat_title="A plan you can check",
        features=[
            ("Snowball, avalanche or your own order", "Compare all three side by side: payoff date, total interest, and the difference between them."),
            ("A schedule for every debt", "Month by month, with interest and principal split out, down to the last payment."),
            ("0% promotional rates", "Enter the promo with its end date. The plan switches to the regular rate when it ends."),
            ("Try it before you commit", "Add an extra amount per month or a one-time payment and see how many months sooner you finish and how much interest you save."),
            ("Track what you actually paid", "Tick the payments you made each month. The plan recalculates from your real balances, and a paid-off debt's minimum rolls into the next one."),
            ("The math, written out", "The formulas are shown in How the math works, so you can check any number against your own spreadsheet."),
        ],
        how_title="Watch the date move",
        steps=[
            ("Add your debts", "Balance, APR, minimum payment and due day — or import them from a CSV."),
            ("Pick a strategy", "And an extra amount, if you have one. Pick a target month and get the budget that reaches it."),
            ("Tick off each month", "Reminders on due days, and charts of the plan against what really happened."),
        ],
        keep_title="Your balances stay on your phone",
        keep=[
            "<b>No account. No bank connection. No ads.</b>",
            "<b>Lock the app</b> with Face ID or your passcode, and hide every amount with one switch.",
            "<b>Notifications never show amounts.</b>",
            "<b>Back up to a file you keep</b> and restore it on a new phone.",
            "<b>Export</b> the schedule as a PDF, or your debts and payments as CSV.",
        ],
        note="Zero Owed is a planning tool. It estimates with a monthly interest model; your lender may calculate daily, so your "
             "statement can differ slightly.",
        faq=[
            ("What is the difference between snowball and avalanche?", "Snowball pays the smallest balance first; avalanche pays the highest interest rate first. Zero Owed shows both, plus your own order, side by side with payoff date and total interest."),
            ("Does Zero Owed connect to my bank or credit cards?", "No. There is no bank connection and no account. You enter balances, rates and payments yourself."),
            ("Can I see what extra payments would do?", "Yes. Add an extra monthly amount or a one-time payment and see how many months sooner you finish and how much interest you save."),
            ("Does it handle 0% promotional rates?", "Yes. Enter the promotional rate with its end date and the plan switches to the regular rate when it ends, with a notice 30 days before."),
            ("Can I check the calculations?", "Yes. The formulas are written out in the app, and you can export the full schedule as a PDF or CSV."),
        ],
        cta="Find your debt-free month",
        theme=dict(bg="#EEF8F4", accent="#1E55C9", ink="#13202B", font="sans", radius=16, hero="center", features="rows", weight=800,
                   track="-.03em", strip="bands", strip_colors=["#1E55C9", "#3E6FD6", "#6690E0", "#93B4EA", "#BFD6F2", "#DDEFE9", "#1E9E62"]),
    ),
    # ------------------------------------------------------------------ Line 98 Classic
    dict(
        slug="line98", key="line98", name="Line 98 Classic", kind="The 9×9 ball puzzle",
        title="Line 98 Classic — The classic 9×9 color lines ball puzzle, offline",
        desc="Line 98 Classic is the timeless 9×9 ball puzzle: line up five balls of the same color to clear them. 14 themes, "
             "next-ball preview, three difficulty levels, undo and named saves. Plays fully offline, no login.",
        h1="Five in a row. <em>Keep the board alive.</em>",
        lead="Line 98 Classic is the timeless 9×9 ball puzzle. Tap a ball, tap an empty cell, line up five of the same color "
             "— horizontally, vertically or diagonally — and they shatter. Keep going until the board fills up. Simple to "
             "learn, hard to put down.",
        facts="iPhone and Android · Plays fully offline · No login",
        audience="Fans of the classic Lines / Color Lines puzzle and casual puzzle players",
        feat_eyebrow="Features",
        feat_title="The puzzle you remember, with a few kind additions",
        features=[
            ("See what is coming", "The next three balls and where they will spawn, so you can plan ahead. Hide the preview for a bonus."),
            ("14 themes", "Classic 98, Pixel 8-bit, CRT Arcade, Y2K Chrome, Flat Pastel, Glass, Neon Cyberpunk, Synthwave, Holographic, Claymation, Paper Origami, Wood, Marble, Brutalist."),
            ("14 ball styles", "Matched to the themes, and free to mix and match."),
            ("Progressive scoring", "Longer lines score more — 5, 7, 10, 14, 19 — and crossing lines stack."),
            ("Three difficulty levels", "Easy with 5 colors, Normal with 6, Hard with 7. Change any time."),
            ("Undo and saves", "Undo moves during a game, and keep up to 8 named saves to resume later."),
        ],
        how_title="No daily quests. No FOMO. Just the puzzle.",
        keep_eyebrow="Good to know",
        keep_title="Plays offline, saves on your device",
        keep=[
            "<b>No login and no cloud sync.</b> Your saves live on your device.",
            "<b>Plays fully offline.</b>",
            "<b>Contains ads</b>, which use personalization only with your consent and are skipped when you are offline.",
            "<b>Haptics and sound effects</b> you can turn off any time.",
        ],
        faq=[
            ("How do you play Line 98?", "Move one ball at a time on a 9×9 board. Line up five or more of the same color in a row, column or diagonal to clear them. New balls appear after every move that does not clear a line; the game ends when the board is full."),
            ("Can I play offline?", "Yes. Line 98 Classic plays fully offline."),
            ("Can I undo a move?", "Yes. Undo is available during a game."),
            ("Does it show the next balls?", "Yes. It shows the next three balls and where they will appear. You can hide the preview for a scoring bonus."),
            ("Is there an account or login?", "No. There is no login, and your saved games live on your device."),
        ],
        cta="Start a board",
        theme=dict(bg="#ECECEC", paper="#F7F7F7", accent="#1F4FD8", ink="#111111", font="mono", radius=0, hero="center", features="ruled",
                   weight=700, track="-.02em", case="uppercase", h1=(28, 44), h2=30, em="normal",
                   strip="bands", strip_colors=["#F2C200", "#C62828", "#1F4FD8", "#2E9E44", "#B03AAE", "#7B1E1E", "#1FA9B8"]),
    ),
]
