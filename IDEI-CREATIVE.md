# Idei creative: site dinamic, original, memorabil

Principiu: fiecare efect **spune ceva despre Moldova** sau **ajută la conversie**. Fără animații de decor.
Reguli tehnice pentru toate:
- respectăm `prefers-reduced-motion`;
- conținutul rămâne text real, citibil de Google;
- încărcăm efectele doar când apar pe ecran;
- Lighthouse pe mobil rămâne peste 85;
- totul se poate muta în WordPress ca blocuri.

---

## ⭐ Top 3: semnătura site-ului (recomand să începem cu ele)

### 1. „Coborâre în pivniță”: scroll de la suprafață la −80 m
Pe homepage și pe pagina de vin, scroll-ul te duce **în subteran**:
- cerul și podgoria se întunecă treptat în piatră de calcar și apoi în rafturi cu sticle;
- un **indicator de adâncime** pe margine: 0 m → −30 m → −80 m;
- la fiecare nivel apare câte un fapt real: „200 km of tunnels”, „12–14°C all year”, „1.5 million bottles, a Guinness record”;
- la final apare butonul: **„Taste it yourself → Wine tours”**.

**De ce:** nimeni din turismul moldovenesc nu are așa ceva. Transformă cea mai mare atracție a țării într-o experiență de pe site, iar oamenii o țin minte și o trimit mai departe.
**Tehnic:** CSS cu animații legate de scroll, plus fallback simplu. Nu cere poze noi (am deja Cricova și Mileștii Mici).

### 2. Harta Moldovei în formă de ciorchine de struguri
Site-ul vostru spune deja că Moldova „is shaped like a grape”. O transformăm în **elementul vizual al brandului**:
- harta interactivă e un ciorchine, iar fiecare **bobiță e o destinație**: Cricova, Orheiul Vechi, Soroca, Purcari, Gagauzia, Transnistria…;
- la hover sau tap, bobița se „coace” (se colorează) și arată poza, distanța de Chișinău („45 min”) și tururile care o includ;
- ciorchinele apare și ca iconiță, pe pagina 404 și ca animație de încărcare.

**De ce:** e original și ușor de recunoscut, e geografie reală (nu o hartă Google generică) și duce direct în noile pagini de destinație.
**Tehnic:** un singur SVG, fără bibliotecă externă.

### 3. Constructor „Build your Moldova trip” cu paharul care se umple
Înlocuiește formularul lung. Pașii sunt carduri vizuale cu poze, nu câmpuri de completat:
1. **Who’s coming?** Couple · Family · Friends · Group
2. **What makes you curious?** Wine · Monasteries · Soviet past · Village life · Food · Nature (poți alege mai multe)
3. **How many days?** un slider de 1–8 zile
4. Apare imediat un **itinerariu propus** din tururile reale, cu **preț estimat** calculat din tabelele de preț existente.
5. „Send me this trip” → cererea pleacă **cu itinerariul deja completat**.

Bara de progres e un **pahar de vin care se umple** la fiecare pas. Când trimiți, primești o animație scurtă de dop care sare și „Noroc!”.

**De ce:** clientul își construiește singur călătoria și o prețuiește mai mult (efectul IKEA). Paharul care se umple îl împinge să termine. Voi primiți cereri complete, nu „hello, how much?”.

---

## Dinamic: site-ul se schimbă singur

| Idee | Ce face | Ce cere |
|---|---|---|
| **„Moldova right now”** | Un widget mic în header sau hero: ora în Chișinău, vremea de azi (API gratuit open-meteo, fără cheie) și sezonul: „🍇 Harvest season · 23°C”. | nimic |
| **Homepage-ul se schimbă cu anotimpul** | Poza mare și mesajul se schimbă automat: **cules** (sep–oct), **Wine Vernissage** (iarna), **Mărțișor** (1 martie), **vară pe Nistru**. | câte o poză pe sezon |
| **Countdown la evenimente reale** | „National Wine Day in 12 days: 3–4 Oct 2026 → Join our Wine Day tour”. Urgență reală, nu falsă. | data evenimentelor |
| **Salut în limba vizitatorului** | Titlul începe cu „Witamy / Willkommen / Benvenuti” după limba browserului, iar recenziile din țara lui sunt puse primele. | recenzii |
| **Cifre animate** | „1.5M bottles” se numără de la 0 când apare pe ecran. | nimic |
| **Ziua turului ca o cronologie** | Pe pagina de tur, ziua e o linie orizontală: **08:30 pickup → 10:00 Căușeni → 12:30 Purcari → 18:00 back**, cu poze care apar la scroll. | orele aproximative |

---

## Original: elemente pe care nu le are nimeni

| Idee | Descriere |
|---|---|
| **Covorul basarabean ca sistem vizual** | Banda ornamentală (deja în prototip) devine un sistem întreg: motive de covor ca separatoare care „se țes” la scroll, colțuri brodate pe carduri și **un motiv diferit pentru fiecare categorie** (vin, mănăstiri, sat). |
| **Quiz: „Which Moldovan wine are you?”** | 5 întrebări amuzante → rezultatul: *Fetească Neagră*, *Rară Neagră*, *Negru de Purcari*, *Ice Wine*… Primești un card frumos de distribuit pe Instagram și turul recomandat. Se răspândește singur, iar emailul se cere la final. |
| **Modul „underground” pe paginile de vin** | Paginile despre crame trec automat pe temă întunecată, culoarea pivniței, cu lumină caldă de lumânare pe carduri. Paginile de sat și natură rămân luminoase. |
| **„Meet your guide” cu un salut audio** | Card de ghid: poză, nume, „my favourite wine”, plus **un salut audio de 10 secunde**. Construiește încrederea înainte de călătorie, iar nimeni din piață nu are așa ceva. *(cere ghizii)* |
| **Carte poștală după cerere** | Pe pagina de mulțumire se generează o **carte poștală** cu numele clientului și turul ales („Greetings from Orheiul Vechi, Anna!”), descărcabilă și de distribuit. |
| **Pagina 404 creativă** | „You’ve wandered 80 m underground and got lost in the tunnels.” Cu ciorchinele animat și „Back to the surface →”. |

---

## Ordinea de implementare recomandată

1. **Top 3** (coborârea în pivniță, ciorchinele, constructorul de călătorie): cel mai mare impact vizual și pe conversie
2. **Widgetul „Moldova right now” + countdown la evenimente**: rapid și dinamic
3. **Quiz-ul de vin**: pentru social media și strângerea de emailuri
4. **Sistemul vizual de covor + modul underground**
5. Ce cere materiale de la voi: ghizii audio, pozele de sezon, cartea poștală cu poze proprii

Fiecare idee se măsoară în GA4: cât e folosită și câte cereri aduce. Ce nu aduce cereri, se scoate.
