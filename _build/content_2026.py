# Client materials of 13.11.2026 ("NEW web sait Enjoy Moldova_for Igor" on Drive): MICE, sport travel, wineries 2026,
# programmes for travel agencies and the new day-tour texts. Texts are the client's own, lightly edited.

# ---- Wineries & wine tastings (Wine Tours and Tastings Moldova 2026 PDF). Prices: EUR per person, transport from Chișinău and back included.
WINERIES_2026 = [
    dict(key='cricova', name='Cricova Wine Cellars', days='Mon–Fri', hours='10:00–15:00', from_eur=32,
         text='An underground wine city: drive through more than 60 km of streets named after the wines stored there, such as Cabernet, Fetească, Aligoté and Sauvignon. Cricova keeps historic collections, including Göring’s, and matures classic sparkling wines.',
         options=['Excursion only', 'Excursion + 4 wines & crackers', 'Excursion + 7 wines, cheese plate & dried fruits', 'Excursion + 7 wines & lunch (from 4 people)'],
         note='After 16:00 and at weekends: +5 € per person.', langs='English, German, Italian, Romanian, Russian'),
    dict(key='purcari', name='Château Purcari', days='Mon–Sun', hours='9:00–17:00', from_eur=43,
         text='The oldest winery in Moldova known worldwide. Taste vintage wines like Roșu de Purcari, Alb de Purcari and Negru de Purcari, said to be one of Queen Elizabeth II’s favourites, and the winery’s Ice Wine.',
         options=['Classic wine tour: 3 wines & 1 sparkling wine', 'Exclusive wine tour: 3 wines & 1 sparkling wine'],
         note='', langs='English, Romanian, Russian'),
    dict(key='milestii-mici', name='Mileștii Mici Wine Cellars', days='Mon–Fri', hours='10:00–17:00', from_eur=30,
         text='One of the biggest wine cellars in the world. Its “Golden Collection”, more than 1.5 million bottles, is in the Guinness Book of Records. Riesling, Pinot, Fetească, Codru and Mileștskoe mature in the silence of its galleries.',
         options=['Excursion only', 'Tour & tasting: 3 wines & snack', 'Tour & tasting: 5 wines & European lunch', 'Tour & tasting: 5 wines & traditional lunch'],
         note='After 17:00 and at weekends: +5 € per person.', langs='English, Romanian, Russian'),
    dict(key='castel-mimi', name='Castel Mimi', days='Mon–Fri', hours='10:00–17:00', from_eur=36,
         text='A wine castle with a history going back to Constantin Mimi, who modernised Bessarabian winemaking and planted new European varieties. Its restaurant serves refined dishes made from local products.',
         options=['Classic tour & tasting: 3 wines', 'Iconic tour & tasting: 5 wines with snacks', 'Authentic tour & tasting: 4 wines with lunch',
                  'Authentic tour & tasting: 4 wines with dinner', 'Fusion tour & tasting: 5 wines with dinner'],
         note='At weekends: +5 € per person.', langs='English, Romanian, Russian'),
    dict(key='vartely', name='Château Vartely', days='Tue–Sun', hours='11:00–17:00', from_eur=28,
         text='On the hills of Orhei, a winery making wines to classic European standards, from young vines brought from European growers. Its wines are appreciated at international competitions.',
         options=['Tour & tasting: 2 wines', 'Tour & tasting: 3 wines & snack', 'Tour & tasting: 4 wines & food pairing',
                  'Tour & tasting: 4 sparkling wines', 'Tour & tasting: 6 wines & food pairing'],
         note='', langs='English, Romanian, Russian'),
    dict(key='cojusna', name='Château Cojușna', days='Tue–Sun', hours='11:00–17:00', from_eur=29,
         text='A French-style château with cellars, a distillery and 175,000 bottles in the Galeria Migdal collection. Climb the tower for a panoramic view of the vineyards; among its rarest bottles is a 1990 Marsala.',
         options=['Tour & tasting: 2 wines “Degust”', 'Tour & tasting: 4 authentic wines & cheese plate', 'Tour & tasting: 4 superior wines & cheese plate',
                  'Tour & tasting: 4 divins, cheese & chocolate', 'Tour & tasting: 4 authentic wines & lunch'],
         note='Mondays or extra hours on request: +10 € per person.', langs='English, Romanian, Russian'),
    dict(key='asconi', name='Asconi Winery', days='Mon–Sun', hours='10:00–17:00', from_eur=23,
         text='Modern winemaking with old Moldovan traditions, blending Merlot, Muscat, Chardonnay and Cabernet Sauvignon with Fetească Neagră and Fetească Albă. Guests can take part in the whole process, from the harvest to bottling.',
         options=['Tour & tasting: 3 wines', 'Tour & tasting: 5 wines', 'Tour & tasting: 3 wines & traditional lunch'],
         note='', langs='English, Romanian, Russian'),
]
WINERIES_ON_REQUEST = ['Et Cetera Winery', 'KVINT', 'Comrat Wines', 'Crama Mircești', 'Poiana Winery', 'Carlevana Winery']

# ---- Programmes for travel agencies (multi-day brochures, PDF on the page; prices only in the PDF)
AGENCY_PDF = {  # tour data key -> (duration, PDF)
    'culturewineandgastronomytour': ('8 days / 7 nights', '/pdf/culture-wine-gastronomy-8-days.pdf'),
    'wine-and-gastronomy': ('6 days / 5 nights', '/pdf/wine-gastronomy-6-days.pdf'),
    'countryside-tour': ('8 days / 7 nights', '/pdf/countryside-tour-8-days.pdf'),
    'atasteofmoldova': ('7 days / 6 nights', '/pdf/a-taste-of-moldova-7-days.pdf'),
    'atasteofmoldova-5': ('5 days / 4 nights', '/pdf/a-taste-of-moldova-5-days.pdf'),
}
TASTE5_DAYS = [  # from the brochure "A Taste of Moldova Tour, 5 days / 4 nights"
    ('Day 1 · Welcome to Chișinău', 'Arrival, transfer to the hotel and welcome dinner at a traditional city restaurant.'),
    ('Day 2 · Chișinău and Castel Mimi', 'Three-hour city tour and the Archaeology & History Museum, then the wine castle Mimi in Bulboaca: guided tour of the castle and cellars, with a tasting.'),
    ('Day 3 · Curchi, Old Orhei and Cricova', 'Curchi Monastery in the Codrii forests, the Old Orhei reserve with its cave monastery, lunch and a folk programme in Trebujeni, then the underground streets of Cricova.'),
    ('Day 4 · The north: carpets and Soroca fortress', 'The Bessarabian carpet museum and studio Arta Rustica in Clișova Nouă, then Soroca: the medieval fortress on the Dniester and the Roma quarter.'),
    ('Day 5 · Farewell', 'Breakfast and transfer to the airport.'),
]
AGENCY_TOUR_TYPES = ['Cultural tours', 'Rural & eco tourism', 'City breaks', 'Gourmet & wine tours', 'Tailor-made tours', 'Active & adventure tours',
                     'Thematic tours: Jewish, German, Turkish and Soviet heritage', 'Combined tours: Moldova & Romania', 'MICE']

# ---- New day-tour texts (Word files, 2026): tour data key -> file in data/tours_2026/, title
DAY_TOURS_2026 = {
    'old-orhei-complex-and-chateau-vartely-winery': 'Old Orhei & Château Vartely',
    'milestii-mici-wine-cellars-and-private-gallery-by-petru-costin': 'Petru Costin Gallery & Mileștii Mici',
    'cricova-winery-and-orheiul-vechi-tour': 'Moldova in a Day: Curchi, Old Orhei & Cricova',
    'trip-to-transnistria': 'Beyond the Dniester: Transnistria & Castel Mimi',
    'transnistria-tour': 'Soviet Transnistria: Bender & Tiraspol',
    'gagausia-tour': 'Gagauzia: Culture, Traditions & Hospitality',
    'hiking-tour-tipova-saharna': 'Țipova Reserve & Fromage Cheese Farm',
    'atv-buket-moldavii': 'ATV Adventure & Buket Moldavii Winery',
    'taste-of-transnistria': 'Flavours of Transnistria: KVINT & Aquatir',
    'codrii-reserve': 'Codrii Reserve: Nature, Honey & Heritage',
    'plaiul-fagului-mircesti': 'Plaiul Fagului & Crama Mircești',
}
NEW_DAY_TOURS = [  # tours that are not on the site yet (images reused until the client sends photos)
    dict(slug='atv-buket-moldavii', kind='day', duration='Full day', cats=['day-trips', 'nature-countryside', 'wine-tours'], min_pax=4,
         summary='An ATV ride through forests and a former quarry with views over the Dniester, then the Buket Moldavii producer in Dubăsari and its tasting.',
         card='Molovata Nouă · Dniester views · Dubăsari', images=['/img/hero-river.jpg', '/img/wine-tasting-table.jpg']),
    dict(slug='taste-of-transnistria', kind='day', duration='Full day', cats=['day-trips', 'culture-heritage'],
         summary='Soviet heritage in Bender and Tiraspol, the Aquatir sturgeon farm and the KVINT distillery with its divins.',
         card='Bender · Tiraspol · Aquatir · KVINT', images=['/img/tiraspol.jpg', '/img/wine-glass-grapes.jpg']),
    dict(slug='codrii-reserve', kind='day', duration='Full day', cats=['day-trips', 'nature-countryside'],
         summary='The ancient Codrii forests with a local guide, the world of bees at Conacul Mierii and the quiet of Hîncu Monastery.',
         card='Codrii Reserve · Conacul Mierii · Hîncu Monastery', images=['/img/capriana.jpg', '/img/monastery-aerial.jpg']),
    dict(slug='plaiul-fagului-mircesti', kind='day', duration='Full day', cats=['day-trips', 'nature-countryside', 'wine-tours'], min_pax=4,
         summary='Forest trails in the Plaiul Fagului reserve, then fine wines, landscapes and local food at Crama Mircești.',
         card='Plaiul Fagului · Crama Mircești', images=['/img/grapes-hands.jpg', '/img/wine-tasting-table.jpg']),
]

# ---- MICE & Business Travel (MICE presentation)
MICE_INTRO = [
    'Founded in 2001, Solei Tourism is an established travel company operating under the brand Enjoy Moldova by Solei Tourism, providing destination management services in the Republic of Moldova.',
    'With over two decades of experience in tourism, business travel and MICE, we offer tailored solutions for international tour operators, corporate clients, event agencies and individual travellers.',
    'Over the years we have built strong relationships with airlines, hotels, transport providers, travel companies and international industry associations, so we can coordinate every service of your event in Moldova.',
    'Our company has been awarded Best Inbound Travel Agency in the Republic of Moldova, most recently at the Moldova Tourism Awards 2024.',
]
MICE_PHILOSOPHY = 'Quality. Integrity. Efficiency. Client Satisfaction.'
MICE_WHY_MOLDOVA = [
    ('f-star', 'A different kind of business destination', 'A welcoming destination where meetings and corporate events can be combined with authentic cultural and gastronomic experiences.'),
    ('f-tower', 'Versatile event venues', 'From modern conference hotels and meeting facilities to atmospheric wineries and countryside locations, for many event formats.'),
    ('f-glass', 'Wine, gastronomy & authentic experiences', 'Winery visits, guided tastings, traditional cuisine, food-and-wine pairings and meetings with local producers.'),
    ('f-bird', 'Business meets culture', 'Cultural discoveries and local traditions that bring people together beyond the meeting room.'),
    ('f-tree', 'Tailor-made group experiences', 'Executive meetings, conferences, incentive trips, team building or corporate celebrations, tailored to your group’s interests and objectives.'),
    ('f-romb', 'Local expertise, one coordinated solution', 'Venues, accommodation, transport, catering and activities coordinated by one local DMC partner.'),
]
MICE_SERVICES = [
    ('Conference venues & meeting facilities', 'Selection and booking of conference venues, meeting rooms and event spaces.'),
    ('Audio-visual & technical support', 'Sound systems, microphones, projectors, screens, lighting and technical assistance.'),
    ('Accommodation', 'Hotel reservations and room allocation for participants.'),
    ('Catering', 'Coffee breaks, business lunches, buffet receptions and gala dinners.'),
    ('Transportation & transfers', 'Airport transfers, hotel-to-venue transport and group logistics.'),
    ('Registration & on-site assistance', 'Participant registration, welcome desk, coordination and on-site support.'),
    ('Interpretation & translation', 'Multilingual interpreters and translation support for international events.'),
    ('Conference materials & branding', 'Name badges, printed materials, signage and branded event elements.'),
    ('Social & networking programmes', 'Welcome receptions, networking dinners and evening entertainment.'),
    ('Pre- and post-conference tours', 'City tours, winery visits and cultural experiences across Moldova.'),
]
MICE_WHY_US = [
    ('Experience you can rely on', 'Established in 2001, with long experience in tourism, business travel and destination management.'),
    ('Local expertise & venue knowledge', 'We know Moldova’s event infrastructure and recommend venues for conferences, seminars, workshops and corporate events, by group size, format and requirements.'),
    ('Reliable technical partners', 'Trusted local suppliers for audio-visual equipment, sound, lighting and presentation technology.'),
    ('One partner for all your needs', 'Venue, accommodation, transport, catering, technical arrangements and social activities through one local point of contact.'),
    ('Tailor-made solutions', 'Every programme is designed around your objectives, schedule, group size and budget.'),
    ('Quality & attention to detail', 'Reliability, punctuality, clear communication and careful coordination at every stage.'),
    ('Beyond the business agenda', 'Wine experiences, gastronomy, cultural discoveries and team building that show the best of Moldova.'),
]
MICE_HOTELS = [
    dict(name='Radisson Blu Leogrand Hotel & Convention Center', stars=5, location='Chișinău city centre', web='https://www.radissonblu.com/hotel-chisinau',
         best='International conferences, forums, gala dinners and high-level business events; a strong choice for multi-day programmes.',
         rooms=143, meeting='6 function rooms (520 m²) + Moldova’s Convention Center (1,200 m², four divisible sections)', space=1720, largest='1,200 m² Convention Center',
         dining=['Apty’s Pub (lobby bar)', 'Ambassador Restaurant (all-day dining)', 'New York Restaurant & Bar (open 24 hours)', 'ZAXI rooftop restaurant (Asian fusion)']),
    dict(name='Courtyard by Marriott Chișinău', stars=4, location='Next to MallDova shopping mall', web='https://www.marriott.com/',
         best='Business meetings, training sessions and small to medium corporate events, with international brand standards.',
         rooms=118, meeting='285 m² of meeting and event space, modern audio-visual equipment', space=285, largest='flexible meeting space',
         dining=['New York Restaurant (06:30–00:00, up to 85 guests)']),
    dict(name='MIMI Hotel & Business Center', stars=4, location='37 Maria Cebotari St, city centre', web='https://mimi-hotels.com/',
         best='Business meetings, training programmes, seminars and institutional events, with rooms, meetings and catering in one place.',
         rooms=108, meeting='6 conference rooms for 10–150 participants: Governor Hall 182 m² (48–150), Pinot Blanc 120 m² (32–100), Glera 87 m² (20–80), Pinot 75 m² (16–60), 9 Muses 30 m² (12–40), Governor S 23 m² (up to 10)',
         space=517, largest='Governor Hall, up to 150 guests',
         dining=['DIVA Restaurant (local and international cuisine)', 'Coffee-break packages and business lunches (buffet or set menus)']),
    dict(name='Bristol Central Park Hotel', stars=4, location='32 Alexandru Pușkin St, by the Central Park', web='https://bristol.md/',
         best='Small and medium corporate groups: seminars, workshops, business meetings and corporate dining in the city centre.',
         rooms=114, meeting='3 halls: Congress (up to 120), Assembly (up to 100), Business (up to 30); theatre, classroom, U-shape and boardroom layouts', space=None, largest='Congress Hall, up to 120 guests',
         dining=['Bristol Central Park Restaurant', 'LUD’s Pub', 'Breakfast with panoramic city views']),
    dict(name='Mercure Chișinău Center Jazz Hotel', stars=4, location='72 Vlaicu Pârcălab St, city centre', web='https://all.accor.com/hotel/B9H0/index.en.shtml',
         best='Small and medium corporate groups looking for a central hotel with a distinctive jazz-inspired atmosphere.',
         rooms=74, meeting='3 meeting rooms; the largest about 150 m², up to 130 participants; business corner with printing', space=None, largest='about 150 m², up to 130 guests',
         dining=['Jazz Restaurant (traditional and seasonal cuisine)', 'Jazz Lobby Bar', 'Breakfast buffet']),
]

# ---- Sport travel (Football presentation, 2026)
SPORT_SINCE = 2009
SPORT_ASSOCIATIONS = ['The Football Association (England)', 'Swedish Football Association', 'German Football Association', 'Swiss Football Association',
                      'Finnish Football Association', 'Hungarian Football Federation', 'Ukrainian Association of Football', 'San Marino Football Federation',
                      'Football Association of Serbia', 'Israel Football Association', 'Hellenic Football Federation (Greece)',
                      'Royal Dutch Football Association (Netherlands)', 'Slovak Football Association', 'Austrian Football Association',
                      'Football Association of Wales', 'Football Association of Ireland', 'Croatian Football Federation', 'Luxembourg Football Federation',
                      'Albanian Football Association', 'Football Federation of Belarus', 'Russian Football Union', 'Polish Football Association',
                      'Football Association of Montenegro']
SPORT_CLUBS = ['Fenerbahçe SK (Turkey)', 'AZ Alkmaar (Netherlands)', 'BSC Young Boys (Switzerland)', 'FC Inter Turku (Finland)', 'GNK Dinamo Zagreb (Croatia)',
               'FC Dinamo București (Romania)', 'FC Dynamo Kyiv (Ukraine)', 'FC Basel (Switzerland)', 'SK Slavia Prague (Czech Republic)', 'FC Twente (Netherlands)',
               'IF Elfsborg (Sweden)', 'FC Copenhagen (Denmark)', 'Tottenham Hotspur (England)', 'PAOK FC (Greece)', 'FC BATE Borisov (Belarus)',
               'FC Zestafoni (Georgia)', 'FK Renova (North Macedonia)', 'FC Lokomotiv Moscow (Russia)', 'Hapoel Be’er Sheva (Israel)', 'Legia Warsaw (Poland)',
               'Odds BK (Norway)', 'MŠK Žilina (Slovakia)', 'FK Kukësi (Albania)', 'Shakhtar Donetsk (Ukraine)', 'Maccabi Haifa (Israel)',
               'KÍ Klaksvík (Faroe Islands)', 'Maccabi Tel Aviv (Israel)', 'FC St. Gallen (Switzerland)']
SPORT_SERVED = [('Professional football teams', 'Clubs and national teams visiting Moldova for international competitions and UEFA away matches.'),
                ('Youth football teams', 'Accommodation and logistics for youth teams in UEFA youth competitions.'),
                ('Beach volleyball teams', 'Accommodation and logistical support for beach volleyball delegations in Chișinău.'),
                ('Other sports delegations', 'Tailor-made arrangements for teams and delegations of other sports.')]
SPORT_SERVICES = ['Airport meet-and-greet and arrival coordination', 'Express Lounge at Chișinău International Airport (extra charge)',
                  'Hotel accommodation and rooming coordination', 'Full-board catering and individually tailored meals',
                  'Dedicated transport for teams and delegations', 'Training facilities and stadium arrangements',
                  'Match-day logistics and on-site coordination', '24/7 assistance throughout the stay']
SPORT_CATERING = ['Full-board meals throughout the stay', 'Individually tailored menus and dietary arrangements', 'Meals served at the hotel',
                  'Packed meals for away trips and excursions', 'Pizza, sandwiches and other quick options when required',
                  'Food delivered to stadiums and training facilities after training']
SPORT_TRANSPORT = ['Modern, comfortable, air-conditioned vehicles', 'Experienced, professional drivers', 'Personal airport meet-and-greet',
                   'Dedicated transport for players, coaching staff and management', 'Transfers between the airport, hotel, stadiums and training grounds',
                   'Every transfer planned around the team’s schedule']
SPORT_TRAINING = ['Booking of training pitches and stadiums', 'Overview of the available training facilities', 'Help choosing venues for the team’s needs',
                  'Coordination of training schedules and venues']
SPORT_COORDINATION = ['A dedicated football team logistics coordinator', 'Personal assistance from arrival to departure', 'Continuous communication with team representatives',
                      'On-site coordination of services', '24/7 availability', 'Overnight presence in Tiraspol when required']
SPORT_TIRASPOL = ['Maccabi Tel Aviv & Maccabi Haifa (Israel)', 'FC St. Gallen (Switzerland)', 'Shakhtar Donetsk (Ukraine)', 'Dundalk FC (Ireland)',
                  'IF Elfsborg (Sweden)', 'NK Olimpija Ljubljana (Slovenia)', 'Zira FC (Azerbaijan)', 'KÍ Klaksvík (Faroe Islands)']
SPORT_WHY = [('Football logistics experience', 'Extensive practical experience with international football teams and delegations.'),
             ('Individual approach', 'Arrangements adapted to each team’s requirements and schedule.'),
             ('One point of contact', 'All local services coordinated through one dedicated partner.'),
             ('Carefully selected providers', 'Reliable hotels, transport companies and service partners.'),
             ('Flexible catering', 'Meals organised around the team’s schedule, preferences and dietary needs.'),
             ('Training facility coordination', 'Help selecting and booking suitable training venues.'),
             ('Local expertise', 'Operational knowledge of Chișinău, Orhei, Tiraspol and other destinations in Moldova.'),
             ('24/7 assistance', 'Continuous support throughout the team’s stay.')]


# ---- Day by day for the agency programmes (read from the 2026 brochures): (title, meals, what happens)
PROGRAMME_FACTS = {  # group size, board, best season
    'a-taste-of-moldova-5-days': ('From 5 people', 'Half board', None),
    'atasteofmoldova': ('5–15 people', 'Half board', None),
    'culturewineandgastronomytour': ('5–15 people', 'Full board', None),
    'countryside-tour': ('5–15 people', 'Half board', 'April – early October'),
    'wine-and-gastronomy': ('From 5 people', 'Full board', None),
}
PROGRAMME_DAYS = {
    'a-taste-of-moldova-5-days': [
        ('Welcome to Chișinău', 'D', 'Arrival, transfer to the hotel and a welcome dinner at a traditional city restaurant.'),
        ('Chișinău and the wine castle Mimi', 'B/L', 'A three-hour city tour and the Archaeology & History Museum, lunch at a city café, then Castel Mimi in Bulboaca: the castle, the cellars and a tasting.'),
        ('Curchi Monastery, Old Orhei and Cricova', 'B/L', 'Curchi Monastery in the Codrii forests, the Old Orhei reserve and its cave monastery, lunch at a family guest house in Trebujeni, then the underground streets of Cricova and a tasting.'),
        ('The north: carpets and Soroca fortress', 'B/L', 'The Bessarabian carpet museum and studio Arta Rustica in Clișova Nouă, lunch in Soroca, the medieval fortress on the Dniester and the Roma quarter.'),
        ('Farewell to Moldova', 'B', 'Breakfast and transfer to the airport.')],
    'atasteofmoldova': [
        ('Welcome to Chișinău', 'D', 'Arrival, transfer to the hotel and a welcome dinner at a traditional city restaurant.'),
        ('Chișinău and the wine castle Mimi', 'B/L', 'A three-hour city tour and the Archaeology & History Museum, then Castel Mimi in Bulboaca: guided tour of the castle and cellars with a tasting.'),
        ('Curchi, Old Orhei and Cricova', 'B/L', 'Curchi Monastery, the Old Orhei reserve, the cave monastery and Butuceni village, lunch at a family guest house (folk programme on request), then the Cricova cellars and a tasting.'),
        ('Gagauzia, the south of Moldova', 'B/L', 'A walking tour of Comrat, a Gagauz lunch at the Gagauz Sofrasi ethno yard in Congaz, the Besalma museum and a folk performance.'),
        ('The north: carpets and a medieval fortress', 'B/L', 'Arta Rustica in Clișova Nouă, Soroca fortress (first mentioned in 1499) and the Roma quarter.'),
        ('A day in Transnistria', 'B/L', 'Tiraspol sightseeing, the KVINT divin factory and tasting, a Soviet-style lunch, the green market and the Tighina fortress in Bender.'),
        ('Farewell to Moldova', 'B', 'Check-out and transfer to the airport.')],
    'culturewineandgastronomytour': [
        ('Arrival in Chișinău', 'D', 'Transfer to the hotel and a first taste of Moldovan wine at the INVINO oenotheque.'),
        ('Chișinău and the wine kingdom of Cricova', 'B/L/D', 'A three-hour city tour, the Archaeology & History Museum, lunch at La Plăcinte, then the Cricova tunnels with a tasting and dinner.'),
        ('Old Orhei, Curchi Monastery and Château Vartely', 'B/L/D', 'The Old Orhei open-air museum and Butuceni village, lunch at a guest house, a talk with a monk at Curchi, then Château Vartely’s light show in the cellar and dinner at the winery.'),
        ('Back to the USSR: Transnistria', 'B/L/D', 'The Tighina fortress, the KVINT divin factory with tasting and lunch, Tiraspol sightseeing and the Aquatir sturgeon farm with caviar tasting.'),
        ('Gagauzia, the south of Moldova', 'B/L/D', 'Comrat, a cooking class in Congaz with Gagauz lunch, the Besalma museum and the Comrat winery with dinner.'),
        ('Two Guinness records and Château Cojușna', 'B/L/D', 'The Mileștii Mici galleries and the Petru Costin collections, lunch in the Codrii forests, Căpriana Monastery and a tasting at Château Cojușna.'),
        ('Château Purcari and the medieval church', 'B/L/D', 'A tasting and lunch at Château Purcari, the semi-buried church of Căușeni, free time and a farewell dinner in Chișinău.'),
        ('Departure', 'B', 'Check-out and transfer to the airport.')],
    'countryside-tour': [
        ('Arrival and Chișinău', 'D', 'Transfer to the hotel, a sightseeing tour of the city centre and a welcome dinner.'),
        ('Murano glass, Cricova and Curchi', 'B/D', 'A Murano glass masterclass, the Cricova wine cellars, Curchi Monastery, and a countryside dinner and night in a guest house in Butuceni or Trebujeni.'),
        ('Old Orhei and a cooking class', 'B/L', 'A full day in Old Orhei: the cave monastery, a two-hour hike in the Răut valley, lunch in the countryside and a plăcintă cooking class.'),
        ('Arta Rustica and the legends of the north', 'B/L', 'The carpet studio Arta Rustica, then Soroca: the fortress, the Candle of Gratitude and the Roma quarter. Night in Soroca.'),
        ('Saharna Monastery and a cheese farm', 'B/D', 'Saharna and its 22 waterfalls, cheese tasting at the Fromage farm in Horodiște, a sarmale masterclass and dinner at Hanul Hanganu in Lalova.'),
        ('Țipova canyon and the legend of wine', 'B/L', 'The Țipova cave monastery, a one-hour hike to the waterfalls, lunch in Țipova, then a tour and tasting at Château Vartely.'),
        ('Codrii forests, the House of Honey and Căpriana', 'B/L', 'The nature museum of the Codrii reserve, honey tasting and lunch at Conacul Mierii, then Căpriana, the oldest monastery in Moldova.'),
        ('Departure', 'B', 'Check-out and transfer to the airport.')],
    'wine-and-gastronomy': [
        ('Arrival in Chișinău', 'D', 'Transfer to the hotel and a first taste of Moldovan wine at the INVINO oenotheque.'),
        ('Chișinău and the wine kingdom of Cricova', 'B/L/D', 'A three-hour city tour, lunch at La Plăcinte, then the Cricova tunnels with a tasting and dinner.'),
        ('Old Orhei, Curchi Monastery and Château Vartely', 'B/L/D', 'Old Orhei and Butuceni, lunch at a guest house, Curchi Monastery, then Château Vartely with its light show and dinner at the winery.'),
        ('Back to the USSR: Transnistria', 'B/L/D', 'The Tighina fortress, the KVINT factory with a tasting and lunch, Tiraspol sightseeing and the Aquatir sturgeon farm with caviar tasting.'),
        ('Gagauzia, the south of Moldova', 'B/L/D', 'Comrat, the Besalma museum, a cooking class in Congaz and the Comrat-Vin winery with dinner.'),
        ('Farewell to Moldova', 'B', 'Free time for shopping and transfer to the airport.')],
}
