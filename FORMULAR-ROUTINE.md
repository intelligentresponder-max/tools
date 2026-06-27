# 📋 Formular-Routine (Onboarding) — TelavendeLele / ASGlobal

> **Zweck:** Standard-Bauplan für künftige Onboarding-Formulare.
> Abgeleitet aus dem Autisti-Formular (Transferfahrer). Jeder Agent baut
> neue Formulare nach diesen 5 Abschnitten — schlank, DSGVO-konform,
> WhatsApp-first.

---

## Die 5 Abschnitte (immer in dieser Reihenfolge)

### 1. Stammdaten & Kontakt (Identifikation)
- **Vollständiger Name** (Vor- + Nachname)
- **Kontaktweg:** Telefonnummer, explizit für **WhatsApp**
- **Wohnort:** Stadt/Region (Nähe zum Einsatzort prüfen, z. B. Raum Frankfurt)

### 2. Rechtliche Voraussetzungen & Qualifikationen
- **Führerschein:** Bestätigung gültige **Klasse B** (bei Fahr-Formularen)
- **Ausweisdokument:** Hinweis auf Notwendigkeit
- **Erfahrung:** Jahr seit Fahrerlaubnis + optional Langstrecken-Erfahrung
- *(Bei anderen Formular-Typen: hier die jeweils nötigen Nachweise/Skills.)*

### 3. Logistische Verfügbarkeit & Einsatzbereitschaft
- **Zeitfenster:** Wochenende / unter der Woche / flexibel / nur bestimmte Zeiträume
- **Art der Dienstleistung:** klar definierte Auswahl
  (z. B. kompletter Transfer DE→Como / nur Fahren / Abholung vor Ort / Zweitfahrer)

### 4. Technischer Workflow & Datenschutz
- **WhatsApp-Integration:** Beim Absenden öffnet sich ein vorausgefüllter
  WhatsApp-Chat mit dem Verantwortlichen (Lele: +39 366 117 8347)
- **QR-Code:** Schneller Einstieg via QR → führt zum Formular oder direkt zu WhatsApp
- **DSGVO:** Expliziter Hinweis — **keine** Speicherung auf der Webseite,
  Übermittlung ausschließlich via WhatsApp

### 5. Bestätigung & Einverständnis
- **Gültigkeitsbestätigung:** Angaben wahrheitsgemäß + gültige Fahrerlaubnis
- **Kontakterlaubnis:** Einverständnis, von TelavendeLele kontaktiert zu werden
- **Technik:** Absende-Button bleibt **deaktiviert**, bis das Consent-Häkchen gesetzt ist

---

## Technische Bau-Regeln (für den Agenten)

1. **Design:** gold `#B8963E`, schwarz `#0D0D0D`, crema `#F5EDD8`,
   Cormorant Garamond (Titel) + Montserrat (Text). Konsistent mit dem Hauptsite.
2. **Kein Backend:** reines HTML/JS. Daten gehen NUR per `wa.me`-Link raus.
3. **WhatsApp-Link-Muster:**
   ```js
   const url = 'https://wa.me/393661178347?text=' + encodeURIComponent(testo);
   window.open(url, '_blank');
   ```
4. **Consent-Gate:** Submit-Button `disabled`, wird erst aktiv wenn Checkbox `checked`.
5. **Pflichtfeld-Check:** mindestens Name + Telefon prüfen, sonst Hinweis anzeigen.
6. **SEO:** Meta description, canonical, Open Graph, `lang`-Attribut korrekt
   (it/de). Seite in `sitemap.xml` eintragen. Interne Tools auf `noindex`.
7. **Mobile-first:** `.row2`-Grid bricht auf einspaltig um (`@media max-width:480px`).
8. **Barrierefreiheit:** sichtbarer Fokus-Ring, `accent-color` für Checkboxen.

---

## Optionale Ausgabe-Formate (auf Wunsch)

- **Formeller Bericht** (PDF) — für interne Doku oder Partner
- **Infografik** (PNG) — Onboarding-Flow visuell, für Schulung/WhatsApp

---

*Erstellt von Robo Bro für André — damit jedes künftige Formular gleich sauber wird. 🌙*
