---
name: "upece-oznamy"
description: "Vytvorí HTML týždenných oznamov UPeCe (kalendár, zvonček, oznamy) z textu skopírovaného z Google Docs. Použi, keď používateľ pošle nové oznamy a chce HTML."
---

# Týždenné oznamy UPeCe → HTML

Používateľ vloží text oznamov skopírovaný z Google Docs (tabuľka kalendára sa rozpadne na riadky, potom zvonček a oznamy). Úlohou je vyrobiť HTML presne v tomto šablónovom formáte, uložiť ho ako súbor `oznamy-DD-MM.html` (dátum pondelka) a poslať ho používateľovi. Komunikuj po slovensky, stručne.

## Pravidlá obsahu

- Text oznamov neprepisuj ani neskracuj. Opravuj len zjavné preklepy (napr. „možete“ → „môžete“) a úvodzovky na slovenské „…“. Opravy na konci spomeň jednou vetou.
- Dátumy vo formáte `26. 10.` (s medzerou), sumy `325,10 €` (medzera pred €).
- Ak niečo v texte chýba alebo je nejasné (napr. deň bez času omše), použi rozumný predpoklad a na konci ho spomeň.

### Kalendár
- 7 riadkov, pondelok až nedeľa. Bunka dňa: `26. 10.<br>Pondelok`.
- Liturgický kalendár: text sviatku/spomienky, inak prázdna bunka.
- Svätá omša: `<strong>20:00</strong><br>kaplnka`. Ak nie je omša: `–`. Nedeľa / viac omší: každá na riadok `<strong>10:00</strong> (Veľká Sála)<br>`.
- Akcie v UPeCe: každá akcia v `<strong>…</strong>`, viac akcií oddeľ `<br>`. Poradie slov (čas pred/za názvom) ponechaj podľa textu.
- Nedeľný riadok má `<tr class="sunday">` (texty v ňom netreba obaľovať do strong).

### Zvonček
- `<div class="collection">`, „Zvonček“ a sumy tučne. Ak je aj iná zbierka, pridaj ju do tej istej vety (názov zbierky aj sumu tučne). Ďakovnú vetu prevezmi z textu.

### Oznamy
- Každý oznam = `<div class="notice">` s `<div class="notice-title">` a jedným či viacerými `<p class="notice-text">`.
- Nadpis: názov oznamu + dátum na konci v tvare `13. 11.` (pre termíny/uzávierky „do 4. 11.“), ak ho text v nadpise má alebo ak bol pri tom istom oznamu v minulých týždňoch. Pomlčku pred dátumom („- 4. 11.“) vynechaj.
- Kľúčové dátumy a časy v texte daj do `<strong>`.
- Odseky z pôvodného textu zachovaj ako samostatné `<p class="notice-text">`; dlhý oznam môžeš rozdeliť na logické odseky.
- URL a webové adresy (napr. upcba.sk) sprav ako odkaz `<a href="https://…">…</a>`; odkaz na formulár v tvare `<a href="URL">tohto formulára →</a>`, ak používateľ dodá URL.
- Pred každý blok daj HTML komentár s názvom veľkými písmenami (ako v šablóne).

## Šablóna (CSS kopíruj vždy celé a bez zmien)

```html
<style type="text/css">

/* Všetky štýly sú obmedzené na .doc-content, aby neovplyvňovali zvyšok stránky (menu, hlavičku…) */

.doc-content,
.doc-content * {
  box-sizing: border-box;
}

.doc-content {
  max-width: 680px;
  margin: 0 auto;
  padding: 20px 28px 40px 28px;
  background: #ffffff;
  color: #222222;
  font-family: Arial, sans-serif;
  font-size: 10pt;
}

/* =========================
   ZÁKLADNÁ TYPOGRAFIA
   ========================= */

.doc-content p {
  margin: 0;
  color: #222222;
  font-family: Arial, sans-serif;
}

/* =========================
   TABUĽKA
   ========================= */

.doc-content .calendar-wrapper {
  width: 100%;
  margin: 10px 0 22px 0;
  border: 1px solid #d8d2c9;
  border-radius: 10px;
  overflow: hidden;
}

.doc-content .calendar {
  width: 100%;
  border-collapse: collapse;
  table-layout: fixed;
}

.doc-content .calendar th {
  background: #e9e4dd;
  color: #222222;
  font-size: 10pt;
  font-weight: 700;
  text-align: center;
  padding: 11px 7px;
  border-right: 1px solid #d5cfc6;
}

.doc-content .calendar th:last-child {
  border-right: none;
}

.doc-content .calendar td {
  padding: 10px 8px;
  vertical-align: middle;
  border-top: 1px solid #e5e1dc;
  border-right: 1px solid #e5e1dc;
  font-size: 9pt;
  line-height: 1.35;
}

.doc-content .calendar td:last-child {
  border-right: none;
}

.doc-content .calendar .day {
  width: 15%;
  font-weight: 700;
  text-align: center;
}

.doc-content .calendar .liturgy {
  width: 31%;
}

.doc-content .calendar .mass {
  width: 25%;
  text-align: center;
}

.doc-content .calendar .events {
  width: 29%;
  text-align: center;
}

.doc-content .calendar .sunday td {
  background: #f5f2ee;
  font-weight: 700;
}

.doc-content .calendar .sunday .liturgy {
  font-weight: 700;
}

/* =========================
   ZVONČEK
   ========================= */

.doc-content .collection {
  margin: 22px 0 34px 0;
  padding: 15px 18px;
  background: #f5f2ee;
  border-left: 5px solid #e9e4dd;
  border-radius: 5px;
  font-size: 10pt;
  line-height: 1.55;
}

/* =========================
   HLAVNÁ SEKČNÁ HLAVIČKA
   ========================= */

.doc-content .section-title {
  margin: 0 0 22px 0;
  padding: 13px 16px;
  background: #e9e4dd;
  border-radius: 7px;
  font-size: 15pt;
  font-weight: 700;
  line-height: 1.25;
  color: #222222;
}

/* =========================
   OZNAM
   ========================= */

.doc-content .notice {
  margin: 0 0 30px 0;
  padding: 0 0 27px 0;
  border-bottom: 1px solid #ddd8d1;
}

.doc-content .notice:last-child {
  border-bottom: none;
}

.doc-content .notice-title {
  margin: 0 0 9px 0;
  padding-left: 12px;
  border-left: 4px solid #e9e4dd;
  font-size: 13pt;
  font-weight: 700;
  line-height: 1.35;
  color: #222222;
}

.doc-content .notice-text {
  margin: 0;
  font-size: 10pt;
  line-height: 1.62;
  text-align: justify;
}

.doc-content .notice-text + .notice-text {
  margin-top: 10px;
}

/* =========================
   ODKAZY
   ========================= */

.doc-content a {
  color: #222222;
  font-weight: 700;
  text-decoration: underline;
  text-decoration-color: #b9b1a7;
  text-underline-offset: 2px;
}

.doc-content a:hover {
  text-decoration-color: #222222;
}

/* =========================
   MOBIL
   ========================= */

@media screen and (max-width: 600px) {

  .doc-content {
    padding: 12px 12px 30px 12px;
  }

  .doc-content .calendar th,
  .doc-content .calendar td {
    padding: 8px 5px;
    font-size: 8pt;
  }

  .doc-content .section-title {
    font-size: 13pt;
  }

  .doc-content .notice-title {
    font-size: 12pt;
  }

  .doc-content .notice-text {
    font-size: 9.5pt;
    line-height: 1.58;
  }

  .doc-content .collection {
    font-size: 9.5pt;
  }
}

</style>


<div class="doc-content">


<!-- =========================
     LITURGICKÝ KALENDÁR
     ========================= -->

<div class="calendar-wrapper">

<table class="calendar">

<thead>
<tr>
<th class="day">Deň</th>
<th class="liturgy">Liturgický kalendár</th>
<th class="mass">Svätá omša</th>
<th class="events">Akcie v UPeCe</th>
</tr>
</thead>

<tbody>

<tr>
<td class="day">20. 10.<br>Utorok</td>
<td class="liturgy"></td>
<td class="mass"><strong>20:00</strong><br>kaplnka</td>
<td class="events"><strong>6:45 ranná modlitba</strong><br><strong>tance a športy 21:15</strong></td>
</tr>

<!-- … ďalšie dni … -->

<tr class="sunday">
<td class="day">25. 10.<br>Nedeľa</td>
<td class="liturgy">30. nedeľa v Cezročnom období</td>
<td class="mass">
<strong>8:00</strong> (kaplnka)<br>
<strong>10:00</strong> (Veľká Sála)<br>
<strong>22:00</strong> (kaplnka)
</td>
<td class="events"></td>
</tr>

</tbody>
</table>

</div>


<!-- =========================
     ZVONČEK
     ========================= -->

<div class="collection">
<strong>Zvonček</strong> z minulej nedele bol
<strong>740,70 €.</strong>
Pán Boh zaplať za Vašu štedrosť.
</div>


<!-- =========================
     HLAVNÁ SEKČNÁ HLAVIČKA
     ========================= -->

<div class="section-title">
Aktuálne oznamy a akcie v UPeCe
</div>


<!-- =========================
     NIKODÉMOVA NOC
     ========================= -->

<div class="notice">

<div class="notice-title">Nikodémova noc 23. 10.</div>

<p class="notice-text">
Poď na Nikodémovu noc, ktorá sa uskutoční
<strong>23. 10. v UPeCe!</strong>
Program začína o
<strong>20:00</strong>
svätou omšou…
</p>

</div>


<!-- … ďalšie oznamy … -->


</div>
```

## Postup
1. Rozparsuj kalendár (7 dní), zvonček a jednotlivé oznamy.
2. Zostav HTML podľa šablóny (celé CSS + `.doc-content`).
3. Ulož ako `oznamy-DD-MM.html` a pošli súbor používateľovi.
4. Na konci 1–2 vety: čo si opravil alebo predpokladal. Nič viac.