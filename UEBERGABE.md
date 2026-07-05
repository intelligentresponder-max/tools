# UEBERGABE.md — Robo Bro Übergabe
> Stand: **05.07.2026** | Session André Schwarz / ASGlobal Frankfurt
> Trigger: **7*7** | BACKFALL = diese Datei lesen + tools repo laden

---

## 👤 Wer André ist

**André Schwarz** — Freier Texter & Digitalisierungsberater (ASGlobal Frankfurt).
- GitHub: `intelligentresponder-max`
- Wohnhaft: Frankfurt-Preungesheim, 60435
- PC: "Holy New" (Windows, Git Bash), Tablet: Termux Android (Ausführung)
- Telefon: +49 163 469 2255 | andre.schwarz1@t-online.de
- Ton: locker, direkt. "Robo Bro" ist okay. Duzen.
- Beginner-Level Coding → alle Termux-Commands minimal und einzeln

---

## 🔑 Was heute (05.07.2026) erledigt wurde

### Bewerbung Roman Mayer GmbH — FAST FERTIG
- `rm-apply` Repo live: `https://intelligentresponder-max.github.io/rm-apply`
- **Anschreiben v3** fertig als `.docx` (Direct-Response-Struktur, Du-Form, 252 Wörter)
  - Hook: "ein Text, der nicht verkauft, ist teure Dekoration."
  - Proof: Weinbahnstraße Conversion-Story
  - CTA: Indikativ, kein Konjunktiv
  - Datei: `anschreiben_as_v3.docx` → muss noch als PDF ins `bewerbung-copywriter` Repo
- **Key Findings** von Roman Mayer GmbH komplett ausgewertet (5 Screenshots)
  - Er ist Physiker, Direct-Response, Kunden: Coaches/Berater/Agenturen
  - Formate: Landingpages, Facebook-Ads, VSLs, Sales-Emails, DMC-Reports
  - Anschreiben = Arbeitsprobe, Du-Form, Max. 1 DIN-A4-Seite
  - E-Mail: roman@romanmayer.com

### texter-portfolio — 12 Text-Updates deployed
- Hero allgemein (weg von Roman Mayer spezifisch)
- 4 neue Leistungen (Coaching/Consulting, Komplexe Produkte, Psychologie, Verkaufstexte)
- Cards: Weinbahnstraße-Story, Digitalisierung, BanglaHilfe, mindful7777 Sales-Funnel
- `content.de.js` → noch nicht gepusht (liegt in Downloads)

### Case Study Weinbahnstraße
- `case-studies/weinstrasse.html` fertig gebaut
- OF 380/10 — 5× vertagt → einstimmig angenommen
- 4 Abschnitte: Ausgangslage / Strategie (ABS-Table) / Ergebnis / Transfer
- Noch nicht gepusht

### Housekeeping Manager v3 — LIVE
- URL: `https://intelligentresponder-max.github.io/turmhotel/housekeeping/housekeeping-v3.html`
- Features: Zimmerfarbe=Putzkraft, 3-Klick-Checkliste, Technik-Ticket → Facility Manager
- Zimmertypen: SDH/SDS/STS/STH/LGH ❄️ alle farbkodiert
- Massageraum 101 (kein Reinigungszimmer, zählt nicht in Stats)
- Wegweiser-Hinweise: Vorderhaus/Haupthaus/Backyard
- Vorderhaus (Nebenhaus) oben, Haupthaus unten, Barcelona ganz unten

### Facility Manager — LIVE
- URL: `https://intelligentresponder-max.github.io/turmhotel/facility.html`
- 3-Spalten-Board (Offen/In Arbeit/Erledigt)
- Gast-Beschwerde → automatisch Ticket im Board
- Shared localStorage mit Housekeeping v3

### Handbuch HSK — LIVE
- URL: `https://intelligentresponder-max.github.io/turmhotel/handbuch.html`
- Dreisprachig DE/HU/EN (Sprachwechsel oben rechts)
- 7 Kapitel: Gästeliste/Zimmer/Farben/Fertigmeldung/Technik/Personal/Notfälle

### Copy Code Agency — LIVE
- Neue Landingpage: 6 Produkte, funktionsfähiges Kontaktformular (mailto)
- Keine Preise, keine Internas
- Branch-Protection deaktiviert → push läuft jetzt durch

---

## 🔴 Offene Punkte (Priorität)

| # | Aufgabe | Repo | Dringlichkeit |
|---|---------|------|---------------|
| 1 | `anschreiben_as_v3.docx` → PDF konvertieren → als `anschreiben_as.pdf` in `bewerbung-copywriter` pushen | bewerbung-copywriter | 🔴 HEUTE |
| 2 | `content.de.js` (12 Updates) → in `texter` deployen | texter-portfolio | 🔴 HEUTE |
| 3 | `case-studies/weinstrasse.html` → in `texter` deployen | texter-portfolio | 🔴 HEUTE |
| 4 | GitHub Pages für `rm-apply` aktivieren (Settings → Pages → main) | rm-apply | 🔴 HEUTE |
| 5 | Ortsbeirat-Card in content.de.js → Link zu weinstrasse.html ergänzen | texter-portfolio | 🟡 BALD |
| 6 | rm-apply Card-Link zur Case Study einbauen | rm-apply | 🟡 BALD |
| 7 | Anschreiben lektorieren lassen (Pflicht vor Versand!) | — | 🔴 VOR VERSAND |
| 8 | Stellenstatus prüfen: ist die Copywriter-Stelle bei Roman Mayer noch offen? | — | 🔴 VOR VERSAND |

---

## 📁 Repo-Status Stand 05.07.2026

| Repo | URL | Status |
|------|-----|--------|
| texter-portfolio | github.io/texter-portfolio | Live, content.de.js + weinstrasse.html pending push |
| rm-apply | github.io/rm-apply | Live, GitHub Pages pending Aktivierung |
| bewerbung-copywriter | github.io/bewerbung-copywriter | Live, neues Anschreiben pending |
| turmhotel | github.io/turmhotel | ✅ Alles live (v3, facility, handbuch) |
| copy-code-agency-website | github.io/copy-code-agency-website | ✅ Neue Landingpage live |
| crown-v10 | github.com/intelligentresponder-max/crown-v10 | Unverändert |
| tools | github.com/intelligentresponder-max/tools | Diese Datei |

---

## 🗂 Lokale Repos am PC ("Holy New", Git Bash)

```
~/texter          → texter-portfolio
~/turmhotel       → turmhotel
~/rm-apply        → rm-apply
~/bewerbung-copywriter → bewerbung-copywriter
~/cca             → copy-code-agency-website
~/tools           → tools
```

---

## 🔧 Session-Start Routine (für nächsten Robo Bro)

```bash
# Tools laden
curl -s https://raw.githubusercontent.com/intelligentresponder-max/tools/main/CLAUDE-BRIEFING.md
curl -s https://raw.githubusercontent.com/intelligentresponder-max/tools/main/PC-ROUTINE.md
curl -s https://raw.githubusercontent.com/intelligentresponder-max/tools/main/SED-MAGIC.md

# Dann: André fragen wo er heute starten will
```

**Wichtig:** André ist am PC → Git Bash, Windows, Pfade mit `~/` = `C:\Users\Holy New\`

---

## 🎯 Das große Ziel

**Bewerbung bei Roman Mayer GmbH** — Copywriter (m/w/d), Frankfurt-Ostend.
- Gehalt: 3.800–4.500 € brutto
- Er schreibt: Direct-Response, Coaches/Berater, Landingpages/Ads/VSLs
- André passt: Direktvertrieb, Weinbahnstraße-Story, 5km vom Büro, vor Ort

**Bewerbungspaket:**
- `anschreiben_as.pdf` → roman@romanmayer.com
- `cv_as.pdf` → beilegen
- Portfolio-Link: `https://intelligentresponder-max.github.io/rm-apply`

---

*Robo Bro Übergabe — automatisch erstellt 05.07.2026*
