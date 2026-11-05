# UX Copy: Enjoy Moldova (site complet)

**Limba de bază:** engleză. Restul limbilor (RO, RU, DE, IT, ES, PL, LV, LT, NL) se traduc din EN.
**Sursa faptelor:** exclusiv site-ul actual moldova.solei.md (tururi, prețuri, incluse, pagini, despre noi).
**Utilizatorul:** turist străin care plănuiește 1–8 zile în Moldova. Nu cunoaște țara, compară agenții și vrea să afle repede ce vede, cât costă și dacă e sigur.

---

## 1. Vocea

| Atribut | Înseamnă | Nu înseamnă |
|---|---|---|
| Local, de încredere | „We're a Chișinău-based team, since 2001” | superlative goale („the best agency ever”) |
| Cald, ospitalier | „We'll meet you on arrival” | familiaritate exagerată, glume |
| Clar, concret | prețuri, durate, ce e inclus | „unforgettable experience” fără detalii |

**Reguli:** propoziții scurte; persoana a 2-a („you”); verbe la începutul butoanelor; cifre cu cifre („6 pax”, „€85”); fără CAPS LOCK în text (site-ul actual are titluri în majuscule, care se transformă în Sentence case).

---

## 2. Termeni consecvenți (glosar)

| Folosim | Nu folosim | Motiv |
|---|---|---|
| **tour** | package, excursion, trip (amestecat) | un singur termen. „Day trip” e acceptat doar pentru categoria de o zi |
| **multi-day tour** / **day trip** | tour package, one day tour | două categorii clare de durată |
| **quote** | offer, price offer, request price | acțiunea principală e cererea unei oferte |
| **per person** | pp, /pers, pax (în text) | „pax” rămâne doar în tabelul de prețuri, ca etichetă de coloană |
| **from €X per person** | price from X EUR/pp | formatul prețului e mereu `from €X per person` |
| **included / not included** | inclusions / supplement | „Optional extras” pentru suplimente |
| **Chișinău, Mileștii Mici, Cojușna, Orheiul Vechi** | Chisinau, Milestii Mici | diacriticele corecte, consecvent |
| **Transnistria** | Pridnestrovie, PMR | numele recunoscut internațional |
| **Gagauzia** | Gagausia, Gagauz Yeri | o singură grafie |

---

## 3. Butoane (CTA)

| Context | Text recomandat | Alternative testabile (A/B) |
|---|---|---|
| CTA principal global (header, hero) | **Get a free quote** | Plan my trip · Get my itinerary |
| WhatsApp | **Chat on WhatsApp** | Ask on WhatsApp · Message us |
| Card de tur | **View tour** | See details · Explore tour |
| Pagina de tur, cardul de rezervare | **Get my price** | Request this tour · Check availability |
| Trimitere formular | **Send my request** | Get my quote · Send request |
| Formular rapid (hero) | **Find my tour** | Show matching tours |
| Blog | **Read article** | Read more |
| Intrare în constructor (homepage, coborârea în pivniță) | **Build my trip** | Plan my trip |
| Trimitere din constructor | **Send me this trip** | Get my quote |
| Final coborâre în pivniță | **Explore wine tours** | Taste it yourself |
| Categorie fără rezultate | **See all tours** | |

**De ce:** fiecare buton spune exact ce se întâmplă după click. „Free” scade frica de cost, iar „my” crește implicarea (verificat des în testele A/B pe formulare de cerere).

---

## 4. Formulare: etichete, ajutor, erori

| Câmp | Etichetă | Text ajutător / placeholder | Eroare |
|---|---|---|---|
| Tur | Which tour? | „Not sure yet” e o opțiune validă | – |
| Dată | Arrival date | Approximate is fine | Please choose a date in the future. |
| Persoane | Travellers | Prices depend on group size | Please enter at least 1 traveller. |
| Nume | Your name | – | Please tell us your name. |
| Email | Email | We'll send your quote here | That email doesn't look right. Check for typos (e.g. name@gmail.com). |
| Mesaj | Anything we should know? (optional) | Interests, hotel level, dietary needs… | – |

**Sub buton:** „Free, no obligation. Office hours: Mon–Fri, 09:00–17:00 (Chișinău time).”
**Trimis cu succes:** titlul „Thank you, your request is in! 🍷”, apoi „We'll email you a tailored itinerary and price. Need it sooner? Call (+373 22) 890-900.”
**Eroare de trimitere:** „We couldn't send your request. Please try again, or email us at incoming@solei.md.”

---

## 5. Prețuri

- Turul de o zi: pe card „from €84 per person”, adică cel mai mic preț din tabel. Pe pagina turului apare tabelul complet 1–6 persoane, cu nota: *Price per person, depends on group size. 7+ travellers: ask for a quote.*
- Turul de mai multe zile: „from €850 per person”, exact ca pe site.
- Turul fără preț pe site: **„Price on request”** + butonul „Get my price”. Nu inventăm prețuri.

---

## 6. Stări goale și mesaje de sistem

| Situație | Text |
|---|---|
| Filtru fără rezultate | **No tours match these filters.** Try another category or see all tours. |
| Pagina 404 | **This page took a wrong turn.** The tour you're looking for may have moved. → See all tours |
| Galerie lipsă | (nu afișăm nimic; nu folosim „No images”) |

---

## 7. Note pentru traducere

- **Lungime:** DE și NL sunt cu ~30% mai lungi decât EN, iar PL, LV și LT cu ~20%. Butoanele au loc pentru minim 22 de caractere.
- **Nume proprii** (Cricova, Mileștii Mici, Castel Mimi, Château Purcari) nu se traduc.
- **Moneda:** € înainte de număr în EN și NL; în DE, IT, ES, PL, LV, LT și RO după număr („850 €”). Preluăm automat din formatul limbii.
- **Formal vs. informal:** DE folosește „Sie”, RU „вы”, PL „Pan/Pani” (sau forma neutră), iar RO „dumneavoastră” doar în formulare, în rest „tu”.
- **„Free quote”:** în DE se traduce „Kostenloses Angebot”, nu „Gratis Zitat”.
- **Transnistria:** în RU se folosește „Приднестровье”, termenul uzual pentru vorbitorii de rusă.
- **Glume și idiomuri:** nu folosim („one glass at a time” se poate păstra doar în EN; în alte limbi traducem sensul).
