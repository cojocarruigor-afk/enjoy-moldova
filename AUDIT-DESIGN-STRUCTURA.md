# Audit de design și structură: Enjoy Moldova

**Ce am auditat:** prototipul din `Design prototip/` (59 de pagini), pe desktop (1366 px) și pe mobil (375 px).
**Data:** 24.10.2026
**Metode:** critică de design, arhitectura site-ului, accesibilitate (WCAG 2.2 AA), sistem de design, predare către programator, CRO și copy.
**Cum:** am măsurat automat toate paginile (înălțimi, poziția butoanelor și a prețurilor, contrastul fiecărei culori, zonele de atingere, inventarul CSS) și am făcut capturi pe fiecare tip de pagină.

---

## 1. Pe scurt: cele 5 probleme care contează cel mai mult

1. **Pe mobil, pagina de tur ascunde prețul și butonul.** Pagina Purcari are 11 ecrane, iar cardul cu preț și formular apare abia la **ecranul 7** (5454 px). Butonul din bara de jos duce la constructor, nu la turul pe care îl citești.
2. **Homepage-ul e prea lung:** 22 de ecrane pe mobil, cu 11 secțiuni. Trei grile de carduri la rând (tururi de o zi, tururi de mai multe zile, blog) fac pagina monotonă.
3. **Prima imagine e cea mai slabă de pe site:** o poză de 1000 px, neclară și generică. În schimb, broșurile voastre conțin fotografii de calitate de print (8910 px).
4. **Totul e card:** tururi, avantaje, pași, FAQ, legende, „Good to know”, toate cu aceeași rază și umbră. Când totul arată ca un card, nimic nu iese în evidență.
5. **Pe pagina „Wine tours”, tururile apar după 6 ecrane**, pentru că animația de coborâre în pivniță (5 ecrane) stă înaintea listei.

---

## 2. Structura, măsurată

| Pagina | Ecrane pe mobil | Primul buton de acțiune | Primul preț | Verdict |
|---|---|---|---|---|
| Homepage | **22,4** | ecranul 1 ✅ | ecranul 3 | prea lungă |
| Toate tururile | 11 | doar la final (ecranul 9) | ecranul 2 | lipsește un îndemn devreme |
| Wine tours | 13,5 | ecranul 1 | **ecranul 6** ❌ | animația e pusă înaintea produselor |
| Tur Purcari | 10,9 | **ecranul 7** ❌ | ecranul 6 | cea mai gravă problemă de conversie |
| Culture, Wine & Gastronomy | 9,6 | ecranul 6 ❌ | ecranul 5 | la fel |
| Destinații (hartă) | 9,1 | ecranul 7 | n/a | ok |
| Constructorul | 3 | ecranul 1 ✅ | n/a | foarte bine |
| Itinerarii 3/5/7 zile | 10,3 | ecranul 3 | ecranul 3 | ok |
| Contact | 4,3 | ecranul 1 ✅ | n/a | ok |
| About us | 10,3 | ecranul 9 | n/a | perete de text |
| Blog | **28** | ecranul 26 | n/a | 58 de articole pe o pagină |

### Homepage: înainte → după (mobil)
```
ÎNAINTE (22 de ecrane)                  DUPĂ (≈11 ecrane)
─────────────────────────────           ─────────────────────────────
Hero (poză generică 1000px)             Hero (poza voastră + slogan) + 2 butoane
Card „Not sure where to start?”         Card constructor (rămâne)
Categorii (5 carduri mari)              Bestsellers: 3 carduri (2 de o zi + 1 lung)
6 tururi de o zi                        Categorii ca rând de chips cu glisare
Harta                                   Harta (deja originală)
4 tururi de mai multe zile              Coborârea în pivniță (momentul „wow”)
Coborârea în pivniță                    Dovezi: 2001 · premii · 13 crame · recenzii
De ce noi (4 carduri)                   Cum funcționează (3 pași, pe un rând)
Cum funcționează                        FAQ (5 întrebări)
Recenzii (gol)                          CTA final
Blog (3 carduri)                        ─ blogul iese de pe homepage
FAQ (8 întrebări)                         (rămâne doar un link în meniu și subsol)
CTA final
```

### Pagina de tur pe mobil: înainte → după
```
ÎNAINTE                                  DUPĂ
──────────────────────────               ──────────────────────────
Galerie                                  Galerie cu glisare (o poză + puncte)
Titlu + chips                            Titlu + chips
Rezumat                                  ┌──────────────────────────────┐
Highlights                               │ €158 /pers. pentru 2 · total │  ← NOU, imediat
Prețuri (tabel)                          │ [Get my price]  [WhatsApp]   │
Ce e inclus                              └──────────────────────────────┘
Good to know                             Highlights
Despre tur (text lung)                   Prețuri + ce e inclus
Întrebări                                Good to know
CARD PREȚ + FORMULAR  ← ecranul 7        FORMULAR (mutat aici pe mobil)
Tururi similare                          Despre tur (pliat: „Read more”)
                                         Întrebări · Tururi similare
Bara de jos: „Get a free quote”          Bara de jos: „Get my price” → formularul turului
  → duce la constructor
```

### Alte probleme de structură
- **Categoriile se suprapun.** Culture are 12 tururi, Wine 10, iar în total sunt 15. Pe pagina de categorie lipsește un filtru rapid după durată sau buget.
- **Hub-ul „Plan your trip”:** 4 carduri așezate 3 + 1 (unul singur pe rând) și doar text, fără nicio imagine.
- **Paginile de destinație** refolosesc paragrafe din paginile de tur. Același text pe două pagini e conținut duplicat pentru Google. Le lipsesc informațiile proprii: distanța de Chișinău, cât timp să rezervi, cu ce să combini.
- **Blogul are 58 de articole pe o pagină**, dominate de știri din 2018–2019. Trebuie paginat câte 12, cu cele mai noi 3 ca recomandate.
- **About us:** 10 ecrane de text de pe site-ul vechi, fără oameni, fără poze ale echipei și fără o cronologie (2001 → premii → ITB).

---

## 3. Critica de design, pe tipuri de pagină

**Ce funcționează (păstrăm):**
- harta Moldovei desenată, cu iconițele voastre: originală, de recunoscut;
- coborârea în pivniță: momentul memorabil;
- constructorul cu paharul care se umple;
- bordura tradițională, folosită acum cu măsură;
- tabelul de prețuri transparent și calculatorul de preț.

| Unde | Constatare | Gravitate | Recomandare |
|---|---|---|---|
| Hero | Poza are 1000 px, e neclară și nu spune „Moldova”. Supratitlul roz se pierde pe zonele deschise ale pozei | 🔴 | O poză proprie (vezi capitolul 6), cu un strat închis sub text |
| Homepage | 3 grile de carduri identice la rând | 🟡 | Rămân doar bestsellers; categoriile devin chips; blogul iese de pe homepage |
| Tot site-ul | Același card (rază, umbră, alb) pentru tururi, avantaje, pași, FAQ, legende | 🟡 | Card doar pentru **produse** (tururi). Avantajele și pașii devin rânduri cu iconiță, iar FAQ-ul linii separate de divizoare |
| Constructor, pasul 1 | Emoji (🧳💑🚌) lângă iconițele tradiționale de la pasul 2: două stiluri vizuale | 🟢 | Iconițe tradiționale peste tot (de adăugat: persoană, cuplu, familie, grup) |
| Pagina de tur | Textul „About this tour” e un perete lung de paragrafe | 🟡 | Primele 2 paragrafe vizibile, restul sub „Read more” |
| Galeria de tur | Turul cu 2 poze arată dezechilibrat; pe mobil, pozele 4–5 sunt ascunse | 🟢 | O galerie cu glisare pe mobil |
| Harta | Zona din jurul Chișinăului e foarte aglomerată (10 puncte pe ~80 px) | 🟡 | Un medalion zoom „Chișinău & împrejurimi” sau un buton de zoom pe zonă |
| Paginile de destinație | Imaginea de sus e aceeași cu cea din cardul turului | 🟢 | Poză diferită pe fiecare destinație |
| Brand print ↔ web | Broșurile folosesc panouri închise la culoare, etichete roșii și sloganul *„Country shaped like a bunch of grapes”*. Site-ul e crem | 🟢 | Sloganul în hero sau în subsol, plus 1–2 benzi închise în stilul broșurii (CTA-ul și coborârea sunt deja închise) |

---

## 4. Accesibilitate (WCAG 2.2 AA)

**Rezumat:** 9 probleme: 0 critice, 4 majore, 5 minore.

| # | Problemă | Criteriu | Gravitate | Rezolvare |
|---|---|---|---|---|
| 1 | Linkurile de limbă din bara de sus (10 bucăți) sunt mai mici de 44 px | 2.5.8 Mărimea țintei | 🟡 Major | Pe mobil, un singur buton „EN ▾” care deschide lista |
| 2 | Linkurile din subsol au rânduri de ~24 px | 2.5.8 | 🟡 Major | Spațiu între linii de 12 px (zonă de atingere de 44 px) |
| 3 | Întrebările din FAQ au zona de click doar pe text (~26 px) | 2.5.8 | 🟡 Major | Padding pe `summary`, nu pe `details` |
| 4 | Textul de pe hero stă direct pe poză, iar contrastul variază | 1.4.3 Contrast | 🟡 Major | Gradient închis sub text (minim 4,5:1 garantat) |
| 5 | Etichetele „ROMANIA”/„UKRAINE” de pe hartă: 2,2:1 | 1.4.3 | 🟢 Minor | Culoarea `#6b5d59` (5,8:1) |
| 6 | Steaua albă pe auriu (Chișinău): 2,1:1 | 1.4.11 Contrast non-text | 🟢 Minor | Auriu închis `#b97d0e`, sau stea închisă la culoare |
| 7 | Rombul coral de la „trust” | decor | 🟢 Minor | Acceptabil (decorativ) |
| 8 | Punctele hărții au 24–34 px | 2.5.8 | 🟢 Minor | Rezolvat deja prin atingere inteligentă și carusel |
| 9 | Coborârea în pivniță: 5 ecrane de derulare pentru cititoarele de ecran | 2.4.1 | 🟢 Minor | Link „Skip the animation” deasupra ei |

**Trec:** textul principal (14,9:1), textul secundar (5,8–6,3:1), butoanele (9,3:1), linkurile teal (5,1:1), WhatsApp (6,4:1), subsolul (9,8:1). Mai sunt în regulă: etichetele de formular, mesajele de eroare (`role="alert"`), linkul „Skip to content”, `lang="en"`, focusul vizibil, `prefers-reduced-motion` și iconițele marcate `aria-hidden`.

**Neverificat încă:** testul cu un cititor de ecran real (NVDA/VoiceOver) și zoom la 200%.

---

## 5. Sistemul de design

**Scor: 62/100.** Identitatea e bună și coerentă vizual, dar în cod e inconsecventă.

| Categorie | Definite ca variabile | Scrise direct în cod |
|---|---|---|
| Culori | 15 variabile în `:root` | **113** culori scrise direct (34 distincte) |
| Mărimi de text | niciuna | **23** de mărimi în px + `clamp()` |
| Raze de colț | `--r` (14 px) | 10 valori: 4, 8, 10, 12, 14, 16, 50 %, 999 px… |
| Umbre | `--shadow` | 7 umbre diferite |
| Puncte de răspuns | n/a | 980 / 640 / 1100 px |

**Propunere:**
- **Mărimi de text:** 8 trepte: 12 · 14 · 16 · 18 · 22 · 28 · 36 · 48 px, plus un titlu mare cu `clamp()`.
- **Spațiere:** 4 · 8 · 12 · 16 · 24 · 32 · 48 · 72 px.
- **Raze:** 3 valori: `--r-sm` 8 px (chips, inputuri), `--r` 14 px (carduri), rotund (butoane).
- **Umbre:** 2 valori: `--shadow-1` (repaus), `--shadow-2` (hover sau cardul de rezervare).
- **Culori:** 9 variabile de brand (vișiniu, roșu, coral, verde, verde închis, teal, roz, auriu, cerneală) + 3 neutre (crem, alb, linie) + 3 semantice (succes, atenționare, eroare). Toate cele 113 culori scrise direct trec pe variabile.

**Componente** (inventar pentru WordPress):

| Componentă | Variante | Stări | Notă |
|---|---|---|---|
| Buton | primar, WhatsApp, contur, ghost | hover, focus | ✅ complet |
| Card de tur | cu insignă, cu durată | hover | ✅. Card doar pentru produse |
| Chip | filtru, static | activ, hover | atingerea pe mobil trebuie să aibă 44 px |
| Insignă pe hartă | principală, punct mic, hub | hover, selectat, estompat | ✅ |
| Notă | info, atenționare | n/a | ✅ |
| Tabel de preț | n/a | coloana activă | ✅ |
| Formular de cerere | complet, compact | eroare | ✅ |
| Pas de constructor | n/a | activ | ✅ |
| Rând de avantaj / pas | n/a | n/a | **de creat** (în locul cardurilor) |
| Galerie cu glisare | n/a | n/a | **de creat** |
| Bară fixă „Get my price” | n/a | n/a | **de creat** |

---

## 6. Imagini

**Situația:**
- Homepage-ul încarcă **~4,3 MB de imagini**: fiecare card folosește poze de 1600 px, puse ca fundal CSS și încărcate toate odată.
- Poza din hero are 1000 px.

**Ce aveți deja:**
- **Broșurile de print** (8910×6300 px): `Moldova Tour`, `Wine Testing`, `Grape Harvest`, `Wine Festival`. Conțin fotografii excelente, dar au text pe ele. Se pot decupa: peisajul aerian cu Nistrul, paharele de vin, strugurii în palme, butoaiele.
- `chisinau.jpg` (catedrala, 901 px) și `EDAL1694.jpg` (Arcul de Triumf, 1600 px) se potrivesc pentru Chișinău.

**Ce recomand:**
1. **Acum:** decupez 4–5 cadre din broșuri pentru hero, categorii și Chișinău.
2. **Ideal:** cereți designerului **fotografiile originale** folosite în broșuri. Fără text pe ele, sunt mult mai bune decât decupajele.
3. **Tehnic:**
   - fiecare poză în 3 mărimi (480 / 960 / 1600 px), cu `srcset`;
   - format WebP;
   - cardurile cu `<img loading="lazy">` în loc de fundal CSS;
   - **ținta: homepage-ul sub 1,5 MB.**

---

## 7. Prioritizare (ICE: impact, încredere, ușurință; 1–10 fiecare)

| # | Schimbare | I | C | E | ICE |
|---|---|---|---|---|---|
| 1 | Pagina de tur pe mobil: bloc cu preț + buton sub titlu, formularul mai sus, bara de jos „Get my price” | 9 | 9 | 9 | **9,0** |
| 2 | Wine tours: lista de tururi înaintea coborârii în pivniță | 7 | 9 | 10 | **8,7** |
| 3 | Accesibilitate: FAQ, limbi, subsol, contrastul hărții, steaua | 5 | 9 | 9 | **7,7** |
| 4 | Imagini responsive și WebP (4,3 MB → <1,5 MB) | 7 | 9 | 7 | **7,7** |
| 5 | Hero cu poze proprii (decupaje acum, originale mai târziu) + strat de contrast | 8 | 8 | 7 | **7,7** |
| 6 | Plan your trip: carduri 2×2 cu imagini | 4 | 8 | 9 | **7,0** |
| 7 | Homepage restructurat la ~11 ecrane pe mobil | 8 | 7 | 6 | **7,0** |
| 8 | Blog paginat (12 pe pagină + 3 recomandate) | 5 | 8 | 8 | **7,0** |
| 9 | Mai puține carduri: avantajele, pașii și FAQ ca rânduri | 6 | 6 | 7 | **6,3** |
| 10 | Sistem de design: variabile pentru culori, 8 mărimi de text, 3 raze, 2 umbre | 5 | 9 | 5 | **6,3** |
| 11 | Sloganul din broșuri + o bandă închisă „broșură” | 5 | 6 | 8 | **6,3** |
| 12 | Galerie cu glisare pe pagina de tur (mobil) | 5 | 7 | 6 | **6,0** |
| 13 | Harta: zoom pe zona Chișinăului | 6 | 6 | 5 | **5,7** |
| 14 | Destinații: conținut propriu (distanță, durată, combinații), fără duplicate | 5 | 7 | 5 | **5,7** |
| 15 | About us: cronologie (2001 → premii → ITB) + echipă | 6 | 7 | 4 | **5,7** |

**Ordinea propusă:**
- **Etapa A** (1–3, aproximativ o oră): câștig imediat pe conversia de pe mobil.
- **Etapa B** (4–8): imagini și structură.
- **Etapa C** (9–15): rafinare.

---

## ✅ Etapa A implementată (24.10.2026)

| Măsurătoare (mobil, 375 px) | Înainte | După |
|---|---|---|
| Tur Purcari: primul preț + buton | ecranul 7 (5454 px) | **ecranul 1** (882 px) |
| Tur Purcari: formularul de cerere | ecranul 7 (5454 px) | **ecranul 3,5** (2802 px) |
| Tur Culture, Wine & Gastronomy: formularul | ecranul 6 (4450 px) | **ecranul 4** (3466 px) |
| Bara de jos pe paginile de tur | „Get a free quote” → constructor | **„Get my price” → formularul turului** |
| Wine tours: primul tur | ecranul 6 (5153 px) | **ecranul 1** (651 px), cu animația după listă |
| Ținte de atingere sub 24 px (8 pagini testate) | ~30 pe pagină | **0** |
| Butoane și rânduri principale sub 44 px | FAQ, limbi, subsol | **0** |
| Etichetele de țară de pe hartă | 2,2:1 | **6,3:1** |
| Steaua de la Chișinău | 2,1:1 | **3,5:1** (minimul pentru grafice e 3:1) |

**Ce s-a schimbat concret:**
- Pe mobil, sub titlul turului, apare un bloc „Price for 2 travellers · €X”, cu butoanele „Get my price” și WhatsApp.
- Pe mobil, formularul de cerere urcă imediat după „Good to know”, înaintea descrierii lungi.
- Descrierea lungă se pliază după primele 2 paragrafe, sub „Read more about this tour”.
- Pe mobil, limbile stau într-un buton „EN ▾”.
- Pe întrebările din FAQ, linkurile din subsol, firul de navigare și linkurile legale am mărit zona de atingere.
- Hero-ul are un strat mai închis în stânga, plus umbră pe text.
- Am pus un link „Skip the cellar animation” înaintea coborârii în pivniță, vizibil la navigarea cu tastatura.

Desktopul a rămas neschimbat, cu formularul în dreapta, lângă conținut. Am verificat și restul: 57 de pagini, 0 linkuri rupte, 0 pagini cu scroll orizontal pe mobil.

---

## ✅ Etapa B implementată (24.10.2026)

| Măsurătoare | Înainte | După |
|---|---|---|
| Homepage pe mobil | 22,4 ecrane | **12,8 ecrane** |
| Imagini încărcate la deschiderea homepage-ului (mobil / desktop) | ~4,3 MB (toate pozele, de la început) | **313 KB / 390 KB** (restul se încarcă la derulare) |
| Blog pe mobil | 28 de ecrane (58 de articole pe o pagină) | **8,7 ecrane** (12 pe pagină, 5 pagini) |
| Imaginea din hero | 1000 px, generică | **fotografie proprie** (din broșura Moldova Tour), WebP de 1600 px, 960 px pe mobil |
| Plan your trip, „Before you go” | 3 + 1 carduri, fără imagini | **grilă 2×2 cu fotografii** |

**Ce s-a schimbat concret:**
- **Imagini:** fiecare poză din `img/` are acum copii WebP de 480, 960 și 1600 px în `img/r/`. Le generează automat `make_responsive()` la fiecare build. Cardurile și galeriile folosesc `<img srcset loading="lazy">` în loc de fundal CSS.
- **5 fotografii decupate din broșurile voastre:** valea râului la apus (hero), mănăstirea văzută din aer, paharul de vin cu struguri, strugurii în palme și masa de degustare. Am ales nume neutre, pentru că nu știu sigur locația exactă din fiecare fotografie.
- **Homepage**, în ordine:
  1. hero;
  2. constructorul;
  3. 6 bestsellers (pe mobil se glisează orizontal);
  4. categoriile ca chips, cu numărul de tururi;
  5. harta;
  6. coborârea în pivniță (380vh pe mobil);
  7. banda închisă „broșură”, cu sloganul vostru, cifrele și avantajele;
  8. cei 3 pași, fără carduri;
  9. 5 întrebări frecvente;
  10. CTA-ul final.

  Au ieșit de pe homepage: grila de 6 tururi de o zi, grila de 4 tururi de mai multe zile, cardurile „Why us” și blogul.
- **Blog:** 12 articole pe pagină, cu cele mai noi 3 ca recomandate pe prima pagină. Fiecare categorie are pagina ei, cu numărul de articole: Company news, Wine & wineries, Festivals & traditions, Travel tips.

**Verificare:** 68 de pagini, 155 de fișiere de imagine, 0 linkuri rupte, 0 pagini cu scroll orizontal pe mobil, 0 erori în consolă.

**De făcut, ideal:** fotografiile originale de la designer, fără text, ca să nu mai depindem de decupaje.

---

## ✅ Etapa C implementată (24.10.2026)

| Măsurătoare | Înainte | După |
|---|---|---|
| Culori scrise direct în CSS (în afara variabilelor) | 113 | **6**: doar desenul pivniței și dopul, adică ilustrație, nu interfață |
| Mărimi de text diferite | 35 | **8 fixe** (12 · 14 · 16 · 18 · 22 · 28 · 36 · 48) + 5 fluide pentru titluri |
| Raze de colț | 11 valori | **3** (`--r-sm` 8 · `--r` 14 · `--r-pill`), plus cercurile și dopul desenat |
| Umbre | 5 | **2** (`--shadow-1`, `--shadow-2`) + inelul de selecție `--ring` |
| Spațieri între elemente (`gap`) | 20 de valori | **scara 4 · 8 · 12 · 16 · 24 · 32 · 48 · 72** |
| Galeria de tur pe mobil | 3 din 5 poze vizibile, într-un mozaic | **toate pozele**, una pe tot ecranul, cu glisare și puncte |
| Punctele din zona Chișinăului pe telefon | ~15 px, înghesuite | **~43 px** după „Zoom in on Chișinău” |
| Paginile de destinație | 3 paragrafe copiate din paginile de tur | **0 copiate**: distanță, timp necesar, preț, cu ce se combină, ce e în apropiere |
| Articolele de blog | link spre site-ul vechi | **58 de pagini pe noul design**, la aceeași adresă (`/slug/`) |
| About us pe mobil | 10,3 ecrane de text | **6,2 ecrane**: cronologie, echipă, profilul complet pliat |

**Ce s-a schimbat concret:**
- **Sistem de design (punctul 10):** toate valorile stau acum în `:root`, în `style.css`:
  - culori de brand, neutre și „pe fundal închis” (`--on-dark`, `--peach`);
  - mărimi de text (`--fs-*`), spațiere (`--s1`…`--s8`), raze și umbre.

  Pentru programator: aceste variabile devin paleta globală și tipografia globală din Kadence.
- **Mai puține carduri (9):** cardurile albe rămân doar pentru produse (tururi, articole). Au devenit rânduri cu linie de separare:
  - întrebările frecvente;
  - „Good to know”;
  - „What’s included”;
  - pașii de pe pagina de mulțumire;
  - serviciile de pe pagina Groups & MICE.
- **Sloganul (11):** *Country shaped like a bunch of grapes · Unique terroir · Passion for wine* apare acum și în subsol, pe toate paginile, nu doar în banda „broșură” de pe homepage.
- **Galeria cu glisare (12):** pe telefon, galeria turului e o bandă care se glisează, cu un punct activ care urmărește poza. Pe desktop, mozaicul a rămas la fel.
- **Zoom pe hartă (13):** butonul „Zoom in on Chișinău” mărește zona cu cele mai multe puncte (Chișinău, Cricova, Mileștii Mici, Cojușna, Poiana…).
  - Dacă alegi din listă un loc din afara zonei, harta revine singură la toată țara.
  - Apăsarea pe cel mai apropiat punct funcționează și în modul mărit.
- **Destinații (14):** fiecare pagină are acum:
  - 4 informații: distanța de Chișinău, timpul necesar, prețul de la, câte tururi;
  - „Tururi care merg aici”;
  - „Good to combine with”: destinațiile care apar în aceleași tururi;
  - „Also nearby”: cramele și obiectivele de pe hartă aflate la mai puțin de 30 km.

  Pe mobil, lista cu celelalte destinații a coborât sub conținut.
- **About us (15):** cronologie în 5 pași, fiecare cu link spre articolul vostru care o povestește:
  1. 2001: fondarea;
  2. 2016: diplomele de gradul I;
  3. 2018: ITB Berlin, MITT și COTTM;
  4. 2023: ITB Berlin;
  5. 2024: Moldova Tourism Awards, locul 1 la turism receptor.

  Urmează secțiunea de echipă, cu 4 locuri marcate „de completat”. Textul complet de pe site-ul vechi a rămas, pliat sub „Read our full company profile”.
- **Articolele de blog (cerut pe parcurs):**
  - Conținutul s-a descărcat de pe site cu `_build/scrape_posts.py` și a fost curățat de stilurile vechi.
  - Fiecare articol are: hero cu poza lui, categoria și data, textul, pozele într-o grilă, video-urile YouTube, 3 tururi legate de locurile din text, 3 articole din aceeași categorie, schema `BlogPosting` și breadcrumbs.
  - Link-urile spre paginile vechi de tur duc acum la paginile noi.
  - 23 de poze și PDF-uri care dau 404 chiar pe site-ul actual nu mai apar.

**Verificare:**
- 128 de pagini + 404, la 375 px lățime.
- 0 link-uri interne rupte, 0 pagini cu scroll orizontal, 0 erori JavaScript.
- Câte un singur H1 pe fiecare pagină.
- 0 zone de atingere sub 24 px. Am exclus kitul de design (pagină internă, noindex) și butoanele radio ascunse din constructor, unde se apasă pe cardul mare.

**De completat de voi:**
- **Distanțele pe drum:** Țipova (120 km) și Orheiul Vechi (60 km) vin de pe site. Celelalte 8 sunt aproximative și trebuie verificate în `DEST_ROAD_KM`, în `content.py`.
- **Echipa:** fotografie, nume, rol și limbi vorbite, pentru 3–6 oameni.
- **Textele paginilor de destinație:** sunt acum unice, dar scurte (165–324 de cuvinte). Câte 150–300 de cuvinte scrise de voi (ce vezi, când e cel mai frumos, un sfat de ghid) le-ar face mai bune pentru Google.
- **Articolul „Events and Festivals 2023”** nu are text nici pe site-ul actual.
- **Articolul în română** („Târgul de turism al României”) e pe un site în engleză: trebuie tradus sau mutat pe versiunea RO.

---

## 8. Note pentru programator (WordPress + Kadence)

| Element din prototip | În WordPress |
|---|---|
| Variabile `:root` (culori, fonturi, `--fs-*`, `--s*`, `--r*`, `--shadow-*`) | Paleta globală Kadence (9 culori) + tipografie globală (Fraunces / Inter, cele 8 mărimi) + spațierea globală |
| Articolele de blog | Rămân articole WordPress la aceeași adresă `/slug/`, deci nu e nevoie de redirecționări. Șablonul de articol din Kadence reproduce structura: hero, text, grilă de poze, 3 tururi, 3 articole |
| Card de tur | Șablon de card în Kadence (Query Loop) pe un tip de conținut „Tour”, cu câmpuri: preț pentru 2, preț minim, durată, insignă |
| Tabel de preț + calculator | Câmpuri repetabile (1–6 persoane) + un script mic (~30 de linii din `site.js`) |
| Harta, coborârea în pivniță, constructorul | Blocuri HTML personalizate sau un mini-plugin, cu SVG-ul și JS-ul din prototip, neschimbate |
| Iconițele tradiționale | Fișierele SVG din `motive/`, încărcate ca iconițe personalizate |
| Bordura | O clasă CSS `.ornament`, pusă ca separator |
| Animații | Respectă `prefers-reduced-motion`. Durate: 0,3 s pentru hover, 0,9 s pentru paharul care se umple, 1,8 s pentru desenarea hărții |
| Puncte de răspuns | ≤1100 px: meniul de mobil · ≤980 px: o coloană · ≤640 px: telefon |

---

## 9. Ce n-am verificat
- Lighthouse (viteză, LCP), înainte și după: îl rulez după etapa A, cum scrie în plan.
- Test cu un cititor de ecran real și zoom la 200%.
- Fișierele originale ale fotografiilor: am văzut doar broșurile machetate.
