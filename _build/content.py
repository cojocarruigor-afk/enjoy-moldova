# Curated content for the prototype. Facts come from moldova.solei.md only (tour pages, price tables, pages).
# Long descriptions are pulled from data/tours_site.json at build time; this file holds the structured, edited parts.

SITE = dict(
    name='Enjoy Moldova',
    legal='Solei Turism',
    phone='(+373 22) 890-900',
    phone_href='tel:+37322890900',
    email='incoming@solei.md',
    address='9 A. Corobceanu str., Chișinău, MD-2004, Republic of Moldova',
    hours='Mon–Fri, 09:00–17:00',
    facebook='https://www.facebook.com/DMCEnjoyMoldova',
    instagram='https://www.instagram.com/enjoymoldova/',
    whatsapp='37300000000',  # ponytail: placeholder until the real WhatsApp number is confirmed
    langs=[('en', 'English'), ('ro', 'Română'), ('ru', 'Русский'), ('de', 'Deutsch'), ('it', 'Italiano'),
           ('es', 'Español'), ('pl', 'Polski'), ('lv', 'Latviešu'), ('lt', 'Lietuvių'), ('nl', 'Nederlands')],
)

CATEGORIES = {
    'multi-day-tours': dict(name='Multi-day tours', short='Multi-day', icon='🗺️', img='/img/cricova.jpg',
                            intro='See the whole country in one trip: wine estates, monasteries, Gagauzia and Transnistria, with hotels, guides and transport arranged.'),
    'day-trips': dict(name='Day trips', short='Day trips', icon='🚐', img='/img/orheiul-vechi.jpg',
                      intro='Short stay in Chișinău? Private day trips with a licensed guide and transport, priced per person by group size.'),
    'wine-tours': dict(name='Wine tours & tastings', short='Wine', icon='🍷', img='/img/milestii-mici.jpg',
                       intro='The world’s biggest wine cellars, historic estates and family wineries. Moldova has the highest density of vineyards in the world.'),
    'culture-heritage': dict(name='Culture & heritage', short='Culture', icon='🏛️', img='/img/capriana.jpg',
                             intro='Cave monasteries, medieval fortresses, Gagauz traditions and the Soviet heritage of Transnistria.'),
    'nature-countryside': dict(name='Nature & countryside', short='Nature', icon='🌿', img='/img/saharna.jpg',
                               intro='Limestone canyons, waterfalls, Codrii forests and village life, far from the city noise.'),
}

TRANSPORT = 'Private transport: car (1–3 travellers), minivan (4–5) or minibus (6–8)'
GUIDE = 'Licensed English-speaking guide (other languages on request)'

TOURS = [
    # ---------- multi-day ----------
    dict(slug='culturewineandgastronomytour', title='Culture, Wine & Gastronomy Tour', kind='multi',
         cats=['multi-day-tours', 'wine-tours', 'culture-heritage'], badge='Bestseller', price_from=850,
         summary='Iconic wine estates, the world’s biggest wine cellars, Gagauz traditions, caviar tasting and Soviet heritage, all in one trip.',
         card='Cricova · Mileștii Mici · Purcari · Gagauzia · Transnistria',
         images=['/img/cricova.jpg', '/img/milestii-mici.jpg', '/img/purcari.jpg', '/img/besalma.jpg', '/img/orheiul-vechi.jpg']),
    dict(slug='wine-and-gastronomy', title='Wine & Gastronomy Tour', kind='multi', duration='6 days, 5 nights',
         cats=['multi-day-tours', 'wine-tours'], price_from=800,
         summary='Château Vartely, Cricova, culinary master classes and rural guest houses: Moldova through its food and wine.',
         card='Château Vartely · Cricova · cooking classes',
         images=['/img/placinta-wine.jpg', '/img/comrat-food.jpg', '/img/cricova.jpg', '/img/orheiul-vechi.jpg']),
    dict(slug='countryside-tour', title='Countryside Tour', kind='multi',
         cats=['multi-day-tours', 'nature-countryside'], price_from=780,
         summary='Villages where time moves slowly, crafts, honey and cheese from the producer, Codrii forests and the Țipova and Saharna sanctuaries.',
         card='Villages · Codrii forests · Saharna & Țipova',
         images=['/img/saharna.jpg', '/img/carpet-museum.jpg', '/img/gagauzia-festival.jpg']),
    dict(slug='atasteofmoldova', title='A Taste of Moldova', kind='multi',
         cats=['multi-day-tours', 'culture-heritage', 'wine-tours'], price_from=655,
         summary='Underground wine cities, Mimi Castle, Transnistria, Gagauzia and a medieval fortress on the Dniester: the essentials in one tour.',
         card='Wine cities · Mimi Castle · Gagauzia · Soroca',
         images=['/img/carpet-museum.jpg', '/img/tiraspol.jpg', '/img/soroca.jpg', '/img/besalma.jpg']),

    # ---------- day trips ----------
    dict(slug='wine-tastings', title='Wine Tours & Tastings', kind='day', duration='Flexible',
         cats=['day-trips', 'wine-tours'],
         summary='Choose from 13 wineries, from the world’s biggest cellars to small family estates. Ideal for a short stay.',
         card='13 wineries to choose from',
         highlights=['13 wineries, from giant cellars to family-run estates',
                     'Native grapes: Fetească Albă, Fetească Neagră, Fetească Regală, Rară Neagră, Viorica',
                     '4 wine regions: Codru, Valul lui Traian, Ștefan Vodă and Divin',
                     'National Wine Day: 3–4 October 2026'],
         wineries=['Cricova Wine Cellars', 'Château Vartely', 'Crama Mircești', 'Mileștii Mici Wine Cellars', 'Et Cetera Winery',
                   'KVINT Divines Factory', 'Château Purcari', 'Castel Mimi', 'Asconi Winery', 'Poiana Winery',
                   'Château Cojușna', 'Comrat Wines', 'Carlevana Winery'],
         images=['/img/milestii-mici.jpg', '/img/cricova.jpg', '/img/purcari.jpg']),
    dict(slug='milestii-mici-wine-cellars-and-private-gallery-by-petru-costin',
         title='Mileștii Mici Wine Cellars & Petru Costin Gallery', kind='day', duration='Full day',
         cats=['day-trips', 'wine-tours', 'culture-heritage'], badge='Guinness record',
         summary='Two Guinness record holders in one day: the world’s largest wine collection and a gallery of Soviet-era artefacts, plus Căpriana Monastery.',
         card='1.5 million bottles, 80 m underground',
         highlights=['Petru Costin Gallery: Soviet-era collection and the largest horseshoe collection (Guinness record)',
                     'Mileștii Mici: 200 km of limestone tunnels and about 1.5 million bottles',
                     'Căpriana, the oldest monastery in Moldova, in the Codrii forests'],
         inclusions=[TRANSPORT, GUIDE, 'Entry fee at the Petru Costin Gallery of Collections', 'Cellar tour with a local guide (tasting not included)'],
         extras=['Wine tasting at Mileștii Mici', 'Traditional lunch in Căpriana village'],
         notes=['The gallery is open Wednesday to Sunday.']),
    dict(slug='old-orhei-complex-and-chateau-vartely-winery', title='Old Orhei & Château Vartely', kind='day', duration='Full day',
         cats=['day-trips', 'culture-heritage', 'wine-tours', 'nature-countryside'],
         summary='Moldova’s most important cultural site, nominated for UNESCO, and a wine tasting with views over Orhei.',
         card='Cave monastery, Răut gorge, wine tasting',
         highlights=['Panoramic Belvedere over the Butuceni valley',
                     'Shehr al-Jedid ruins and the ancient hammam',
                     '16th-century rock monastery and a traditional peasant house',
                     'Château Vartely winery tour with 2 wines'],
         inclusions=[TRANSPORT, GUIDE, 'Château Vartely winery tour and tasting of 2 wines', 'Entry fee at Old Orhei'],
         extras=['Lunch at Eco Resort Butuceni or Stone Age Restaurant (Brănești village)']),
    dict(slug='purcari-winery-and-the-medieval-church', title='Purcari Winery & Medieval Church', kind='day', duration='Full day',
         cats=['day-trips', 'wine-tours', 'culture-heritage'],
         summary='Moldova’s oldest wine estate, founded in 1827, and the semi-buried medieval church of Căușeni.',
         card='The oldest wine estate, founded in 1827',
         highlights=['The semi-buried Church of the Assumption in Căușeni and its medieval frescoes',
                     'Château Purcari, at the same latitude as Bordeaux',
                     'Winery tour and tasting of 4 wines',
                     'Legendary blends: Roșu, Alb and Negru de Purcari'],
         inclusions=[TRANSPORT, GUIDE, 'Entry fee at the Căușeni medieval church', 'Winery tour and tasting of 4 wines'],
         extras=['Lunch at the Château Purcari restaurant'],
         notes=['Available Tuesday to Sunday.']),
    dict(slug='cricova-winery-and-orheiul-vechi-tour', title='Cricova Winery & Old Orhei', kind='day', duration='Full day',
         cats=['day-trips', 'wine-tours', 'culture-heritage', 'nature-countryside'],
         summary='The open-air museum of Orheiul Vechi, Curchi Monastery and the underground wine city of Cricova in one day.',
         card='Cave monastery, Curchi, Cricova cellars',
         highlights=['Orheiul Vechi open-air museum and a working cave monastery',
                     '19th-century village architecture in Butuceni',
                     'Curchi Monastery, with Moldova’s tallest church spire (57 m)',
                     'Drive the underground streets of Cricova'],
         images=['/img/tours/cricova-winery-and-orheiul-vechi-tour-1.jpg', '/img/cricova.jpg', '/img/orheiul-vechi.jpg']),
    dict(slug='capriana-monastery', title='Căpriana Monastery & Château Cojușna', kind='day', duration='Full day',
         cats=['day-trips', 'culture-heritage', 'wine-tours'],
         summary='The oldest monastery in Moldova, deep in the Codrii forest, then a French-style château with cellars and a distillery.',
         card='Oldest monastery + château tasting',
         highlights=['Căpriana Monastery, first mentioned in 1420',
                     'Château Cojușna cellars, distillery and wine collection',
                     'Panoramic view from the Cojușna tower',
                     'A 1990 Marsala among the winery’s treasures'],
         inclusions=[TRANSPORT, GUIDE, 'Winery tour and tasting of 2 wines'],
         extras=['Cognac tasting, 5 samples: €17 per person (min. 2 travellers)', 'Lunch at the Château Cojușna restaurant']),
    dict(slug='trip-to-transnistria', title='Transnistria Tour & Mimi Castle', kind='day', duration='Full day',
         cats=['day-trips', 'culture-heritage', 'wine-tours'],
         summary='Soviet-era Tiraspol and the Ottoman fortress of Bender, then a tasting at the restored Castel Mimi.',
         card='Tiraspol, Bender fortress, Castel Mimi',
         highlights=['Tighina (Bender) 16th-century fortress',
                     'Tiraspol: Lenin, a T-34 tank and Soviet-era squares',
                     'Castel Mimi: 5 wines with food pairing',
                     'A castle reopened to the public in 2016'],
         inclusions=[TRANSPORT, GUIDE, 'Entry fee at Tighina fortress', 'Castel Mimi winery tour with tasting of 5 wines and food pairing'],
         extras=['Lunch at a local restaurant in Tiraspol']),
    dict(slug='transnistria-tour', title='Transnistria Tour: Tiraspol & Bender', kind='day', duration='Full day',
         cats=['day-trips', 'culture-heritage'],
         summary='A self-proclaimed republic with its own currency and border guards, where time seems to have stopped in the Soviet era.',
         card='A Soviet time capsule',
         highlights=['Tighina (Bender) fortress, occupied by the Ottomans in 1538',
                     'Tiraspol’s Soviet monuments, theatre and market',
                     'Bender railway station and old cinema from Soviet times',
                     'KVINT cognac or Aquatir caviar tour on request'],
         inclusions=[TRANSPORT, GUIDE, 'Entry fee at Tighina fortress'],
         extras=['Lunch at a local restaurant', 'KVINT cognac tour or Aquatir caviar tour (on request)']),
    dict(slug='gagausia-tour', title='Gagauzia Tour', kind='day', duration='Full day',
         cats=['day-trips', 'culture-heritage'],
         summary='The autonomous region of the Gagauz, an Orthodox people of Turkic origin: museums, food, wine and a UNESCO-listed endangered language.',
         card='Comrat, Besalma, Gagauz food & wine',
         highlights=['Comrat, capital of the autonomous region',
                     'Cara-Ciobanu ethnographic museum in Besalma',
                     'Congaz, “Europe’s largest village”',
                     'Gagauz Sofrasi ethno courtyard'],
         inclusions=[TRANSPORT, GUIDE, 'Entry fees at Besalma museum and the ethno courtyard'],
         extras=['Lunch at Gagauz Sofrasi']),
    dict(slug='soroca-fortress-tour', title='Soroca Fortress & Arta Rustica', kind='day', duration='Full day',
         cats=['day-trips', 'culture-heritage'],
         summary='A 15th-century circular fortress on the Dniester that was never conquered, and a museum of Bessarabian carpets on the way.',
         card='15th-century fortress, carpet museum',
         highlights=['Arta Rustica museum and studio: Bessarabian carpets and working looms',
                     'Circular Soroca Fortress, 37.5 m across with no blind spots',
                     'The legend of the stork and the grapes',
                     'A drive through Soroca’s hilltop Roma quarter'],
         inclusions=[TRANSPORT, GUIDE, 'Entry fees at Soroca fortress and Arta Rustica'],
         extras=['Lunch at a local restaurant']),
    dict(slug='hiking-tour-tipova-saharna', title='Hiking Tour: Țipova & Saharna', kind='day', duration='Full day',
         cats=['day-trips', 'nature-countryside', 'culture-heritage'],
         summary='Cliffside monasteries above the Nistru, 22 cascades in Saharna and a canyon hike to the Țipova waterfalls.',
         card='Canyon hike, cave monastery, waterfalls',
         highlights=['Saharna Holy Trinity Monastery and its 22 cascades',
                     'Țipova, one of the oldest cave monasteries, carved 200 m above the Nistru',
                     'One-way hike to 10–15 m waterfalls in the Țipova canyon',
                     'Legends of Orpheus and Stephen the Great']),
]

PAGES = {
    # new path: (section, title, intro, source slugs in data/pages.json). Old pages are merged into the new menu (11.2026)
    'about-moldova/why-moldova': ('about-moldova', 'Why Moldova?', 'Why travel to Moldova, and the places travellers ask for most.', ['travel-to-moldova', 'top-tours-moldova']),
    'about-moldova/facts': ('about-moldova', 'Facts about Moldova', 'Between Romania and Ukraine, a small country with four seasons, three rivers and a long history.', ['moldova']),
    'about-moldova/chisinau': ('about-moldova', 'Chișinău', 'One of the greenest capitals in Europe, and the starting point of every tour.', ['chisinau']),
    'about-moldova/moldovan-cuisine': ('about-moldova', 'Our cuisine', 'Balkan, Turkish, Slavic and Romanian influences on one table.', ['moldavian-cuisine']),
    'plan-your-trip/general-advice': ('useful-info', 'General advice', 'Money, time, language, getting around, safety and useful numbers.', ['embassies-in-the-republic-of-moldova']),
    'plan-your-trip/passport-visa': ('useful-info', 'Passport & visa', 'Who needs a visa, what your passport needs and what to show at the border.', ['embassies-of-the-republic-of-moldova']),
    'plan-your-trip/customs-border-points': ('useful-info', 'Customs rules & border crossing points', 'The official rules, from the Customs Service and the Border Police.', []),
    'plan-your-trip/festivals-holidays': ('useful-info', 'Festivals & holidays', 'Wine festivals, spring traditions and village feasts through the year.', []),
    'about-us/our-services': ('about-us', 'Our services', 'Everything for your trip to Moldova, from one local team.', []),
    'about-us/transportation': ('about-us', 'Transportation services', 'Any vehicle for your trip, on time and with professional drivers.', []),
}

# Texts written for the new menu (approved by Igor, 10.11.2026). Sources: the current site, the blog, mfa.gov.md and
# border.gov.md (read 10.11.2026). Anything not found in an official source stays out, in a "de confirmat" box.
PAGE_TEXT = {
    'plan-your-trip/general-advice': '''<h2>Money</h2><p>The currency is the Moldovan leu (MDL). Cards are widely accepted in Chișinău; carry some cash in lei for villages, markets and small wineries. Transnistria has its own currency, so ask us before a trip there.</p>
<h2>Time and language</h2><p>Moldova is on Chișinău time, GMT+2. Romanian is the official language and Russian is widely spoken. Your guide speaks English; other languages on request.</p>
<h2>Getting around</h2><p>Use arranged transfers or app-based taxis. We can organise your airport transfer and private transport for every tour.</p>
<h2>Safety</h2><p>Violent crime against tourists is rare. Keep valuables close in markets and on public transport. Before a trip to Transnistria, read your government’s travel advice. <a href="/plan-your-trip/is-moldova-safe/">Is Moldova safe? →</a></p>
<h2>Emergency and useful numbers</h2>
<table class="info"><tr><td>Emergency: police, fire, ambulance</td><td><a href="tel:112">112</a></td></tr><tr><td>Private emergency medical service</td><td><a href="tel:14112">14112</a></td></tr>
<tr><td>Chișinău International Airport</td><td><a href="tel:+37322525111">(022) 52 51 11</a></td></tr><tr><td>Chișinău railway station</td><td><a href="tel:+37322832733">(022) 83 27 33</a></td></tr>
<tr><td>Customs Service hotline</td><td><a href="tel:+37322279210">(022) 27 92 10</a></td></tr><tr><td>Lost and found office</td><td><a href="tel:+37322223340">(022) 22 33 40</a></td></tr></table>
<div class="todo"><b>De confirmat</b>Numerele vin de pe site-ul vechi: de verificat înainte de lansare.</div>''',
    'plan-your-trip/passport-visa': '''<h2>Who needs a visa</h2><p>Citizens of the European Union, the United Kingdom, the United States, Canada, Israel, Japan, Switzerland and Norway can enter Moldova without a visa. The full list is on the website of the Ministry of Foreign Affairs: <a href="https://www.mfa.gov.md/en/content/visa-regime-foreigners" rel="noopener">Visa regime for foreigners</a>.</p>
<h2>Your passport</h2><p>It must be valid for at least 3 months after the day you leave Moldova, have at least two blank pages and have been issued in the last 10 years.</p>
<h2>At the border</h2><p>You may be asked for the purpose of your trip and proof of your stay: a hotel booking or a booked tour, and a return ticket. Your booking confirmation from us helps.</p>
<h2>Other nationalities</h2><p>Apply for a visa online on the official <a href="https://www.evisa.gov.md/" rel="noopener">E-Visa portal</a>.</p>
<h2>Entering through Transnistria</h2><p>If you arrive from Ukraine through the Transnistrian section of the border, you must declare your entry within 72 hours at a migration office or a Public Services Agency office. We can help you with this.</p>
<p class="small">Official sources: <a href="https://www.mfa.gov.md/en" rel="noopener">mfa.gov.md</a> · <a href="https://www.border.gov.md/" rel="noopener">border.gov.md</a></p>
<div class="todo"><b>De confirmat</b>Câte zile se poate sta fără viză (90 din 180?), dacă cetățenii UE pot intra cu buletinul și dacă e nevoie de asigurare medicală: nu apar în paginile oficiale citite.</div>''',
    'plan-your-trip/customs-border-points': '''<ul class="plus"><li><a href="https://www.customs.gov.md" rel="noopener">Customs Service of Moldova</a>: what you can bring in and take out</li>
<li><a href="https://www.border.gov.md/" rel="noopener">Border Police</a>: border crossing points and rules for foreigners</li></ul>
<h2>In short</h2><ul class="ticks"><li>Cash over €10,000 per person must be declared in writing.</li><li>Objects of cultural value need an authorisation to leave the country.</li></ul>''',
    'plan-your-trip/festivals-holidays': '''<ul class="gtk">
<li><div><b>Mărțișor · 1 March</b>The start of spring: red-and-white tokens worn for luck.</div></li>
<li><div><b>Easter</b>The biggest family holiday, with painted eggs and village traditions.</div></li>
<li><div><b>National Wine Day · first weekend of October, Chișinău</b>Almost every Moldovan winery in one square.</div></li>
<li><div><b>Wine Vernissage</b>Tastings with the winemakers, several editions a year.</div></li>
<li><div><b>Gustar · summer</b>Open-air music and wine festival.</div></li>
<li><div><b>MustFest at Cricova · autumn</b>The grape harvest festival.</div></li>
<li><div><b>Festivals of traditions</b>Duminica Mare, Iprosop (traditional towels), the Carpet Festival in Gagauzia, the Young Craftsman’s Festival, Bostaniada and the Medieval Festival in Soroca.</div></li></ul>
<p><a class="more" href="/blog/category/festivals-traditions/">Festival stories on our blog →</a></p>
<div class="todo"><b>De completat</b>Pozele (le trimiteți voi) și datele exacte pe 2027.</div>''',
    'about-us/our-services': '''<ul class="ticks">
<li><b>Tours and excursions</b> in Moldova, private and with a licensed guide</li>
<li><b>Tailor-made packages</b> for individual travellers (FIT) and groups</li>
<li><b>Combined tours with Romania and city breaks:</b> Bucharest, Iași, Chișinău, Tiraspol</li>
<li><b>Accommodation</b> in Chișinău, across Moldova, in countryside guest houses and in Tiraspol</li>
<li><b>Transport and transfers:</b> airport–hotel–airport, within Moldova and to neighbouring countries</li>
<li><b>Flight tickets</b> (e-tickets)</li>
<li><b>Business travel &amp; MICE</b></li>
<li><b>Events and cultural tourism:</b> wine festival, music festivals, sport events</li>
<li><b>Catering:</b> group meals, wine dinners, tastings</li>
<li><b>Guide services</b> in English and other languages on request</li></ul>''',
    'about-us/transportation': '''<ul class="gtk">
<li><div><b>Cars, including VIP cars</b>For 1–3 travellers.</div></li>
<li><div><b>Minivans</b>For 4–5 travellers.</div></li>
<li><div><b>Minibuses</b>For 6–8 travellers.</div></li>
<li><div><b>Coaches</b>For larger groups.</div></li>
<li><div><b>Rent-a-car</b>On request.</div></li></ul>
<p>Airport transfers, transport for tours across Moldova and transfers to neighbouring countries.</p>
<div class="todo"><b>De completat</b>PDF-ul cu prezentarea mașinilor și capacitatea exactă a autocarelor.</div>''',
}

# ---- Clean URLs. Old WordPress slugs get a 301 redirect (written to REDIRECTS-301.csv and redirects.htaccess) ----
NEW_SLUGS = {  # tour data key (= old slug) → new slug
    'culturewineandgastronomytour': 'culture-wine-gastronomy-tour',
    'wine-and-gastronomy': 'wine-gastronomy-tour',
    'atasteofmoldova': 'a-taste-of-moldova',
    'wine-tastings': 'wine-tours-tastings',
    'milestii-mici-wine-cellars-and-private-gallery-by-petru-costin': 'milestii-mici-petru-costin-gallery',
    'old-orhei-complex-and-chateau-vartely-winery': 'old-orhei-chateau-vartely',
    'purcari-winery-and-the-medieval-church': 'purcari-winery-medieval-church',
    'cricova-winery-and-orheiul-vechi-tour': 'cricova-old-orhei',
    'capriana-monastery': 'capriana-monastery-chateau-cojusna',
    'trip-to-transnistria': 'transnistria-mimi-castle',
    'transnistria-tour': 'transnistria-tiraspol-bender',
    'gagausia-tour': 'gagauzia-tour',
    'soroca-fortress-tour': 'soroca-fortress-arta-rustica',
    'hiking-tour-tipova-saharna': 'tipova-saharna-hiking',
}
PAGE_REDIRECTS = {
    '/about-moldova/moldova/': '/about-moldova/facts/',
    '/about-moldova/moldavian-cuisine/': '/about-moldova/moldovan-cuisine/',
    # old pages merged into the new menu (11.2026)
    '/useful-info/emmergency-calls/': '/plan-your-trip/general-advice/',
    '/useful-info/embassies-in-the-republic-of-moldova/': '/plan-your-trip/general-advice/',
    '/useful-info/embassies-of-the-republic-of-moldova/': '/plan-your-trip/passport-visa/',
    '/useful-info/customs-rules/': '/plan-your-trip/customs-border-points/',
    '/useful-info/border-points/': '/plan-your-trip/customs-border-points/',
    '/about-moldova/travel-to-moldova/': '/about-moldova/why-moldova/',
    '/about-moldova/top-tours-moldova/': '/about-moldova/why-moldova/',
    '/contacts/': '/contact/',
    '/2019/10/19/hello-world/': '/privacy/',
    '/tours-2/': '/',
}

# ---- "Good to know" on tour pages (rules use the tour data key) ----
CELLAR_TOURS = {'milestii-mici-wine-cellars-and-private-gallery-by-petru-costin', 'cricova-winery-and-orheiul-vechi-tour', 'wine-tastings',
                'culturewineandgastronomytour', 'wine-and-gastronomy', 'countryside-tour', 'atasteofmoldova'}
TRANSNISTRIA_TOURS = {'transnistria-tour', 'trip-to-transnistria', 'wine-and-gastronomy', 'atasteofmoldova'}
HIKING_TOURS = {'hiking-tour-tipova-saharna'}

# ---- Internal links: content pages → tours that match them ----
RELATED_TOURS = {
    'about-moldova/facts': ['cricova-winery-and-orheiul-vechi-tour', 'old-orhei-complex-and-chateau-vartely-winery', 'purcari-winery-and-the-medieval-church'],
    'about-moldova/chisinau': ['milestii-mici-wine-cellars-and-private-gallery-by-petru-costin', 'old-orhei-complex-and-chateau-vartely-winery', 'capriana-monastery'],
    'about-moldova/moldovan-cuisine': ['gagausia-tour', 'old-orhei-complex-and-chateau-vartely-winery', 'purcari-winery-and-the-medieval-church'],
    'about-moldova/why-moldova': ['cricova-winery-and-orheiul-vechi-tour', 'milestii-mici-wine-cellars-and-private-gallery-by-petru-costin', 'trip-to-transnistria'],
}

# ---- Destination pages: words that find the matching paragraphs in the site's tour descriptions ----
DEST_KEYWORDS = {
    'soroca': ['Soroca'], 'tipova-saharna': ['Tipova', 'Saharna'], 'orheiul-vechi': ['Orhei', 'Butuceni'],
    'capriana': ['Capriana', 'Cojusna', 'Cojușna'], 'cricova': ['Cricova'], 'transnistria': ['Tiraspol', 'Tighina', 'Transnistria'],
    'milestii-mici': ['Mileștii', 'Milestii'], 'castel-mimi': ['Mimi'], 'purcari': ['Purcari', 'Causeni'],
    'gagauzia': ['Comrat', 'Besalma', 'Gagau', 'Congaz'],
}

# Itineraries built from real day trips (prices come from the site's price tables)
ITINERARIES = [
    ('3 days', 'A long weekend: the two Guinness-record highlights near Chișinău.',
     ['milestii-mici-wine-cellars-and-private-gallery-by-petru-costin', 'old-orhei-complex-and-chateau-vartely-winery']),
    ('5 days', 'Wine, monasteries and the Soviet time capsule of Transnistria.',
     ['milestii-mici-wine-cellars-and-private-gallery-by-petru-costin', 'old-orhei-complex-and-chateau-vartely-winery',
      'purcari-winery-and-the-medieval-church', 'trip-to-transnistria']),
    ('7 days', 'The full picture: add Gagauz culture in the south.',
     ['milestii-mici-wine-cellars-and-private-gallery-by-petru-costin', 'old-orhei-complex-and-chateau-vartely-winery',
      'purcari-winery-and-the-medieval-church', 'trip-to-transnistria', 'gagausia-tour']),
]

# ---- Trip builder: interests and how each day trip matches them -------------------------------
INTERESTS = [  # key, label, icon, photo
    ('wine', 'Wine & cellars', '🍷', '/img/milestii-mici.jpg'),
    ('history', 'Monasteries & fortresses', '🏛️', '/img/capriana.jpg'),
    ('soviet', 'Soviet heritage', '🎖️', '/img/tiraspol.jpg'),
    ('nature', 'Nature & hiking', '🌿', '/img/saharna.jpg'),
    ('villages', 'Villages & crafts', '🧺', '/img/carpet-museum.jpg'),
    ('food', 'Food & local cuisine', '🥘', '/img/placinta-wine.jpg'),
]
# slug: (interest tags, overlap group: two tours in the same group are never suggested together)
TRIP_TAGS = {
    'milestii-mici-wine-cellars-and-private-gallery-by-petru-costin': (['wine', 'soviet', 'history'], 'milestii'),
    'cricova-winery-and-orheiul-vechi-tour': (['wine', 'history', 'nature', 'villages'], 'orhei'),
    'old-orhei-complex-and-chateau-vartely-winery': (['history', 'nature', 'wine', 'villages'], 'orhei'),
    'purcari-winery-and-the-medieval-church': (['wine', 'history'], 'purcari'),
    'capriana-monastery': (['history', 'wine', 'nature'], 'capriana'),
    'trip-to-transnistria': (['soviet', 'wine', 'history'], 'transnistria'),
    'transnistria-tour': (['soviet', 'history'], 'transnistria'),
    'gagausia-tour': (['food', 'villages', 'history'], 'gagauzia'),
    'soroca-fortress-tour': (['history', 'villages'], 'soroca'),
    'hiking-tour-tipova-saharna': (['nature', 'history'], 'tipova'),
}
TRIP_ORDER = list(TRIP_TAGS)  # tie-break: most popular first

# ---- Illustrated map of Moldova: one folk icon per place, at its real position ----
# key, name, (lat, lon), blurb (facts from the site), image, tour slugs
DESTINATIONS = [
    ('soroca', 'Soroca', (48.156, 28.298), 'A 15th-century circular fortress on the Dniester that was never conquered.', '/img/soroca.jpg',
     ['soroca-fortress-tour', 'atasteofmoldova']),
    ('tipova-saharna', 'Țipova & Saharna', (47.66, 28.98), 'Cliffside monasteries and waterfalls on the Nistru, 120 km from Chișinău.', '/img/saharna.jpg',
     ['hiking-tour-tipova-saharna', 'countryside-tour']),
    ('orheiul-vechi', 'Orheiul Vechi', (47.30, 28.98), 'Cave monasteries in the Răut gorge, 60 km from Chișinău, nominated for UNESCO.', '/img/orheiul-vechi.jpg',
     ['old-orhei-complex-and-chateau-vartely-winery', 'cricova-winery-and-orheiul-vechi-tour', 'wine-and-gastronomy', 'culturewineandgastronomytour']),
    ('capriana', 'Căpriana Monastery', (47.128, 28.509), 'The oldest monastery in Moldova, first mentioned in 1420, deep in the Codrii forests.', '/img/capriana.jpg',
     ['capriana-monastery', 'milestii-mici-wine-cellars-and-private-gallery-by-petru-costin', 'culturewineandgastronomytour']),
    ('cricova', 'Cricova', (47.138, 28.862), 'An underground wine city with 120 km of streets named after wines.', '/img/cricova.jpg',
     ['cricova-winery-and-orheiul-vechi-tour', 'wine-and-gastronomy', 'culturewineandgastronomytour', 'countryside-tour', 'wine-tastings']),
    ('chisinau', 'Chișinău', (47.010, 28.864), 'One of the greenest capitals in Europe, and the starting point of every tour.', '/img/hero-vineyard.jpg',
     []),
    ('transnistria', 'Transnistria', (46.840, 29.630), 'Tiraspol and Bender: a Soviet time capsule with its own border and currency.', '/img/tiraspol.jpg',
     ['transnistria-tour', 'trip-to-transnistria', 'wine-and-gastronomy', 'culturewineandgastronomytour', 'atasteofmoldova']),
    ('milestii-mici', 'Mileștii Mici', (46.920, 28.830), 'A Guinness record: 1.5 million bottles in 200 km of limestone tunnels.', '/img/milestii-mici.jpg',
     ['milestii-mici-wine-cellars-and-private-gallery-by-petru-costin', 'culturewineandgastronomytour', 'wine-tastings']),
    ('castel-mimi', 'Castel Mimi', (46.890, 29.300), 'A restored wine castle, opened to the public in 2016.', '/img/tours/trip-to-transnistria-2.jpg',
     ['trip-to-transnistria', 'atasteofmoldova']),
    ('purcari', 'Purcari', (46.530, 29.850), 'The oldest wine estate (1827) and the semi-buried medieval church of Căușeni.', '/img/purcari.jpg',
     ['purcari-winery-and-the-medieval-church', 'culturewineandgastronomytour']),
    ('gagauzia', 'Gagauzia', (46.300, 28.660), 'Comrat and Besalma: the Gagauz, an Orthodox people of Turkic origin, and their cuisine.', '/img/besalma.jpg',
     ['gagausia-tour', 'wine-and-gastronomy', 'culturewineandgastronomytour', 'atasteofmoldova']),
]

# Approximate road distance from Chișinău, km. Țipova and Orheiul Vechi: from the site; the rest: to check before launch.
DEST_ROAD_KM = {'soroca': 160, 'tipova-saharna': 120, 'orheiul-vechi': 60, 'capriana': 40, 'cricova': 15, 'transnistria': 70,
                'milestii-mici': 20, 'castel-mimi': 40, 'purcari': 115, 'gagauzia': 100}

# Destinations menu (new site menu, 11.2026): every place on the map by type. The client will send the full list with
# descriptions; places without a tour show as "on request". Festivals: list to come from the client.
DEST_TYPE = {
    'wineries': ['cricova', 'milestii-mici', 'castel-mimi', 'purcari', 'vartely', 'cojusna', 'asconi', 'etcetera', 'kvint',
                 'comrat-wines', 'mircesti', 'poiana', 'carlevana'],
    'monasteries': ['capriana', 'curchi', 'orheiul-vechi'],
    'natural-reserves': ['tipova-saharna'],
    'historical-sights': ['soroca', 'transnistria', 'tighina', 'causeni', 'petru-costin'],
    'craftsmanship': ['arta-rustica', 'besalma', 'congaz', 'gagauzia'],
    'festivals': [],
}

# Main destinations by kind, for the map filter
DEST_KIND = {'cricova': 'winery', 'milestii-mici': 'winery', 'castel-mimi': 'winery', 'purcari': 'winery'}  # the rest are sights

# Smaller points on the map: the wineries from our tasting list and the sights named in the tours.
# Coordinates: OpenStreetMap (Nominatim), 24 Oct 2026. Texts: facts from moldova.solei.md only.
WINE_LIST = 'One of the 13 wineries in our wine tours & tastings programme. Ask us for a tasting.'
POIS = [
    # key, name, kind, (lat, lon), icon, text, tour slugs
    ('vartely', 'Château Vartely', 'winery', (47.368, 28.827), 'f-glass',
     'On a hill above Orhei, with a view over the town and its vineyards. Wines made to classic European standards.',
     ['old-orhei-complex-and-chateau-vartely-winery', 'wine-and-gastronomy', 'culturewineandgastronomytour']),
    ('cojusna', 'Château Cojușna', 'winery', (47.094, 28.669), 'f-glass',
     'A French-style château with cellars, a distillery and a tower with a panoramic view of the vineyards.', ['capriana-monastery', 'culturewineandgastronomytour']),
    ('asconi', 'Asconi Winery', 'winery', (46.824, 29.034), 'f-glass', WINE_LIST, ['wine-tastings']),
    ('etcetera', 'Et Cetera Winery', 'winery', (46.450, 29.988), 'f-glass', WINE_LIST, ['wine-tastings']),
    ('kvint', 'KVINT', 'winery', (46.837, 29.611), 'f-bottle', 'The divines (brandy) factory in Tiraspol. A cognac tour is available on request.', ['transnistria-tour', 'wine-tastings']),
    ('comrat-wines', 'Comrat Wines', 'winery', (46.301, 28.656), 'f-glass', 'The oldest winery in the south of Moldova.', ['gagausia-tour', 'wine-tastings']),
    ('mircesti', 'Crama Mircești', 'winery', (47.403, 28.000), 'f-glass', WINE_LIST, ['wine-tastings']),
    ('poiana', 'Poiana Winery', 'winery', (47.014, 28.546), 'f-glass', WINE_LIST, ['wine-tastings']),
    ('carlevana', 'Carlevana Winery', 'winery', (46.891, 29.242), 'f-glass', WINE_LIST, ['wine-tastings']),
    ('curchi', 'Curchi Monastery', 'sight', (47.336, 28.655), 'f-church',
     'One of Moldova’s most beautiful monasteries, with the country’s tallest church spire: 57 m.', ['cricova-winery-and-orheiul-vechi-tour']),
    ('causeni', 'Căușeni Medieval Church', 'sight', (46.650, 29.407), 'f-church',
     'The semi-buried Church of the Assumption, with the last stage of medieval fresco painting in Moldova.', ['purcari-winery-and-the-medieval-church']),
    ('tighina', 'Tighina (Bender) Fortress', 'sight', (46.837, 29.487), 'f-fortress',
     'A fortress on the Dniester first built by the princes of Moldavia, occupied by the Ottomans in 1538.', ['transnistria-tour', 'trip-to-transnistria']),
    ('arta-rustica', 'Arta Rustica', 'sight', (47.494, 28.634), 'f-flower',
     'Museum and studio of the Bessarabian carpet in Clișova Nouă, with looms that still work.', ['soroca-fortress-tour']),
    ('besalma', 'Besalma Museum', 'sight', (46.173, 28.649), 'f-tulip',
     'The Cara-Ciobanu museum of Gagauz history and ethnography, founded in 1966.', ['gagausia-tour']),
    ('congaz', 'Congaz', 'sight', (46.108, 28.602), 'f-bowl',
     '“Europe’s largest village”, home of the Gagauz Sofrasi ethno courtyard and its food.', ['gagausia-tour']),
    ('petru-costin', 'Petru Costin Gallery', 'sight', (46.944, 28.777), 'f-hook',
     'Soviet-era artefacts, flags and monuments, plus the largest horseshoe collection: a Guinness record.', ['milestii-mici-wine-cellars-and-private-gallery-by-petru-costin']),
]

BLOG_CATS = [  # first match wins
    ('Company news', ['award', 'diploma', 'anniversary', 'itb', 'mitt', 'cottm', 'targul', 'târgul', 'fair', 'conference', 'netflix']),
    ('Wine & wineries', ['wine', 'cricova', 'mimi', 'milest', 'asconi', 'vernissage', 'vin', 'mustfest']),
    ('Festivals & traditions', ['festival', 'easter', 'christmas', 'new year', 'martisor', 'mărţişor', 'valentine', 'women', 'flag', 'duminica', 'iprosop', 'craftsman', 'gustar', 'bostaniada', 'pottery', 'events', 'rose', 'picnic', 'carpet']),
    ('Travel tips', ['']),
]
