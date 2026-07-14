# UEBERGABE_RM-APPLY777.md — Bewerbung Roman Mayer GmbH
> Stand: 14.07.2026 | Trigger: **RM-apply777**
> Bei Trigger: diese Datei lesen, danach mit offenen Punkten unten weitermachen.

---

## 🎯 Ziel
André bewirbt sich als Copywriter bei **Roman Mayer GmbH** (Marketing-Agentur,
Copywriting für Coaches/Berater/Personenmarken, karriere.romanmayer.com).
Repo-Name bewusst ohne Klarnamen im Titel: **`rm-apply`** (Datenschutz-Entscheidung,
siehe unten).

---

## ✅ Was heute (14.07.2026) erledigt wurde

### `rm-apply` — eigenes Bewerbungs-Repo
- Live-Repo: `https://github.com/intelligentresponder-max/rm-apply`
- Vermutliche GitHub-Pages-URL: `https://intelligentresponder-max.github.io/rm-apply/`
  (noch nicht verifiziert ob Pages aktiviert ist — bei Bedarf in Settings → Pages prüfen)
- Design/Layout-Struktur bewusst an Roman Mayers eigener Karriere-Seite orientiert
  (Layout-Muster übernommen, NICHT Texte/Fotos/Wortmarke):
  - Voller Hero mit Foto (Split-Layout: Text links, Portrait rechts)
  - Helle "Über mich"-Zwischenzone mit Stat-Reihe (60+ Anträge · 77 Zimmer · 30 Sprachen)
  - Vorteile-Zeilen-Layout ("Was ich mitbringe")
  - Card-Footer mit Button-Stil ("Ansehen →") mirrort ihre Job-Karten
- Hero-Foto: `andre-hero.webp` (aus Selfie-Auswahl, mit `cwebp -q 82` optimiert, 900px breit, 64 KB)
- Telavendelele (Auto-Verkaufstexte Italien) ergänzt: kleine Zeile im Hero + eigene Karte
  unter "Ausgewählte Arbeiten"
- `.claude/agents/Robo Bro.agent.md`: "Roman Mayer" aus der öffentlichen SEO-Keyword-Liste
  entfernt (Datenschutz — Name soll nicht in Meta-Tags auftauchen)

### Datenschutz-Bereinigung — Klarname raus aus öffentlichen Dateinamen
- `bewerbung-copywriter/Anschreiben_Andre_Schwarz_Roman_Mayer.pdf`
  → `Anschreiben_Andre_Schwarz.pdf` (+ 2 Links in `index.html` mit angepasst)
- `texter-portfolio/Andre_Schwarz_Bewerbung_RomanMayer_v2.pdf`
  → `Andre_Schwarz_Bewerbung_v2.pdf`
- ⚠️ Downloads-Ordner auf dem Handy bewusst NICHT angefasst (privat, kein Risiko)

### "Projekt anfragen"-Buttons entfernt (beide Repos)
Grund: André bewirbt sich exklusiv bei einem Unternehmen — generische
"Jetzt buchen"-CTAs wirken wie automatisch generierter Freelancer-Sales-Text.
- `texter-portfolio` + `bewerbung-copywriter`: `willkommensbuch.html`, `crown-valuebet.html`,
  `content.de.js` (dort ungenutzt, aber sicherheitshalber mit bereinigt)
- Übrig bleibt jeweils nur "Mehr Arbeitsproben"

### Willkommensbuch-Showcase — Ansprache umgestellt
- Vorher: adressierte Hotelbesitzer/Geschäftsführung ("Ihr Haus verdient klare Worte")
- Jetzt: adressiert Roman Mayer als zukünftigen Chef ("Genau diese Sorgfalt bringe ich
  zu Roman Mayer")
- ⚠️ **OFFEN:** Zitat-Sektion mit DE/EN-Beispielzeile ist aktuell nur **nachempfunden**,
  nicht das echte Original — André fand die Reaktion "nicht gelungen" und will
  **echte Zitate** aus dem tatsächlichen Willkommensbuch (2-3 Stellen)
- ⚠️ **OFFEN:** "+15 weitere" Sprachen-Chip soll durch die **vollständige Liste aller
  30+ Sprachen** ersetzt werden — André besteht darauf, nichts zu verstecken

### Texter-portfolio — alter Fehlversuch verworfen
- Commit `2dc7350` (RomanMayer-Branding im Titel, komplett anderes Navy/Gold-Design,
  neue `lebenslauf.html`) wurde per `git reset --hard origin/main` verworfen
- Bleibt nur lokal im Reflog auf Andrés Handy, nicht gepusht, kein Risiko

---

## 🔴 Wichtigster offener Punkt für die nächste Session

**André hat das echte Willkommensbuch gefunden**, kann es aber in diesem Chat nicht
hochladen. Nächste Schritte, sobald der Trigger **RM-apply777** kommt:

1. Nachfragen, wie er den Text bereitstellen will (Foto, Copy-Paste, Datei-Upload
   in neuem Chat, etc.)
2. Echte Zitate (2-3 Stellen) für die Willkommensbuch-Showcase-Seite einbauen
   → ersetzt die aktuelle "nachempfundene" Platzhalter-Zitat-Sektion in
   `texter-portfolio/willkommensbuch.html` UND `bewerbung-copywriter/willkommensbuch.html`
3. Vollständige Sprachenliste (alle 30+, nicht "+15 weitere") in beiden Dateien einbauen

---

## 📋 Weiterhin offen (aus früheren Sessions, noch nicht angefasst)

- Handschriftliche Korrekturen aus dem 143-Block-Korrektur-PDF
  (`Korrektur_KOMPLETT_Portfolio_PdG_12-07.pdf`) — bisher nur Workflow besprochen
  (Block-Nummer + Diktat), noch keine einzige Korrektur verarbeitet
- Foto auf `bewerbung-copywriter` weiterhin als "zu dunkel" gemeldet — noch nicht behoben
- `rm-apply` sollte laut ursprünglichem Plan noch weitere Unterseiten bekommen:
  `willkommensbuch.html`, `antraege.html`, `crown-valuebet.html`,
  Wahlprogramm-PDF (aktuell verlinkt `rm-apply` extern auf `texter-portfolio`,
  nicht lokal kopiert)

---

## 🔧 Technischer Kontext (Kurzfassung, Details siehe CLAUDE-BRIEFING.md)
- André: Coding-Anfänger, Termux (Handy/Tablet) + Git Bash (PC "Holy New")
- Ein Befehl pro Schritt, nie Blöcke blind einfügen lassen
- Kein Push-Zugriff für Claude — André kopiert Dateien aus Downloads selbst und pusht
- Bei Datei-Konflikten (`git pull --rebase`): erst `--stat` prüfen bevor irgendwas
  gemerged wird, im Zweifel `git rebase --abort` und nachfragen
