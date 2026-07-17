# SESSION-ÜBERGABE RM-APPLY777 — 17.07.2026 (Update 2)
> Trigger nächste Session: BACKFALL 7*7 — dieses Dokument zuerst laden, dann tools-Repo (CLAUDE-BRIEFING.md, TERMUX-GOTCHAS.md, DEPLOY-ROUTINE.md).

## 🎯 ZIEL: Bewerbung HEUTE abschicken
André will die Bewerbung bei Roman Mayer GmbH heute fertigstellen und abschicken.
Das ist die oberste Priorität — nicht nachlassen.

## ✅ SEIT LETZTER ÜBERGABE ERLEDIGT
- **Lebenslauf ist jetzt in rm-apply!** Aus `bewerbung-copywriter/lebenslauf.html` übernommen,
  vier "Copywriter"-Stellen bereinigt (Titel-Tag, Meta-Description, Job-Titel bei ASGlobal, Footer),
  Telefonnummer war schon korrekt (01525 6044541). Live geprüft: 0 Treffer für "Copywriter".
  Link: https://intelligentresponder-max.github.io/rm-apply/lebenslauf.html
  ⚠️ Noch NICHT von der Startseite (`index.html`) aus verlinkt — Button/Kachel fehlt noch.
- **Anträge sind bereits vollständig!** `antraege.html` (schon länger in rm-apply) enthält ein
  komplettes Archiv mit 53 einzelnen Anträgen 2016–2025 inkl. Status-Kennzeichnung — deckt alle
  in der Story erwähnten Anträge ab (OF 232/10 → 380/10, OF 406/10, OF 603/10, OF 628/10 etc.).
  Keine weitere Arbeit hier nötig.

## 🚨 KRITISCHER BLOCKER — Anschreiben fehlt noch
**rm-apply hat immer noch KEIN Anschreiben!**
- `anschreiben.html` → 404 in rm-apply, `index.html` verlinkt auf nichts dergleichen
- Existiert nur in `bewerbung-copywriter/index.html` (Anrede "Hallo Roman,", PDF-Download-Button)
- Verstößt aktuell gegen Branding-Regeln: Titel-Tag enthält "Copywriter" UND den Arbeitgebernamen
  "Roman Mayer GmbH" (verboten in crawlbaren SEO-Feldern — Body-Text darf den Namen behalten)

**Nächste Schritte:**
1. `bewerbung-copywriter/index.html` per curl/raw.githubusercontent nach rm-apply als
   `anschreiben.html` holen
2. "Copywriter" → "Texter"/"Ghostwriter" ersetzen
3. Titel-Tag/Meta-Description von Arbeitgebername befreien (Body-Text darf ihn behalten)
4. Telefonnummer gegenchecken (muss 01525 6044541 sein, alte Nummer 0163 469 2255 taucht
   in dieser Session immer wieder auf)
5. **NEU: Passwortschutz einbauen** — André möchte das Anschreiben mit einem einfachen
   Passwort sichern (simple JS-Sperre reicht, kein echtes Backend nötig auf GitHub Pages).
   Passwort wird NICHT öffentlich kommuniziert, sondern separat per E-Mail an Roman mitgeteilt.
   → Mit André klären: welches Passwort genau (Vorschlag stand noch aus)
6. Von `index.html` (Startseite) aus verlinken — Anschreiben UND Lebenslauf brauchen noch
   je einen Button/eine Kachel auf der Startseite
7. Pushen, live prüfen

## 📋 OFFEN — Arbeitsproben-Seite (vereinbart, Umfang erweitert)
Neue Kachel **"Arbeitsproben"** in rm-apply, neue Seite `arbeitsproben.html`,
gespeist aus `bewerbung-copywriter/arbeitsproben.html`.

**Bereits recherchiert, bereit zum Übertragen:**
1. **Copy Code Agency** — live: `intelligentresponder-max.github.io/copy-code-agency-website/`.
   Kollaboration mit Fullstack-Entwickler Tomasz Szafrański ("Code trifft Copy").
   André-Anteil: Conversion Copy & Brand (Landingpages, SEO-Copy, E-Mail-Sequenzen),
   plus Mitarbeit an KI-Lebenslauf-Optimizer, Value-Bet-Dashboard (baut auf CROWN v10 auf),
   IT-Recruiting-Plattform DE/PL. Entwurf für Kartentext steht bereit, noch nicht eingefügt.
   ⚠️ Team-Sektion der Quellseite selbst nennt André dort noch "Copywriter" — nur relevant,
   falls man mehr als die Kurzfassung übernimmt.
2. **mindful7777** — live: `intelligentresponder-max.github.io/mindful7777/` (Wellness/Selbsthypnose, GEO-optimiert)
3. **Frankfurt Energie Online** — live: `frankfurt-energie.online` (Conversion-Landingpage für TELESON AG)
4. **Recruiting-Texte in 8 Sprachen** — PDF, liegt in bewerbung-copywriter als `recruiting-8-sprachen.pdf` → muss mitkopiert werden
5. **KfW-Businessplan** — PDF, liegt in bewerbung-copywriter als `KfW_Businessplan_Nachbarschaftshilfe.pdf` → muss mitkopiert werden

**Bereits als eigene Kacheln vorhanden — NICHT doppelt aufnehmen:**
Wahlprogramm, Anträge, CROWN v10 (crown-valuebet.html), BanglaHilfe

## ✅ WAS DAVOR SCHON FERTIG WURDE (17.07.2026)
- `index.html` komplett wiederhergestellt (war durch zwei fehlerhafte Commits auf 3 von 6 Kacheln
  geschrumpft + hatte eine Tool-Fehlermeldung als Klartext im HTML) → alle 6 Original-Kacheln
  wieder da: Digitalisierung, Callcenter, Willkommensbuch, Housekeeping, Wahlprogramm, Anträge, Tech
- `antraege.html`, `crown-valuebet.html`, `Wahlprogramm-Freie-Waehler-Frankfurt-2026.pdf` aus
  texter-portfolio nach rm-apply umgezogen, alle Links lokalisiert
- "Vollständiges Portfolio"-Button (externer Link auf texter-portfolio) entfernt — kompletter
  Inhalt von texter-portfolio steckt jetzt in rm-apply, kein Cross-Link mehr nötig
- Neue Kachel BanglaHilfe hinzugefügt (Behördenkommunikation, DE/Bengali, live verlinkt)
- Hero-Foto (`andre-hero.webp`) neu zugeschnitten (Arm + unruhiger Hintergrund raus, enger auf
  Kopf/Schultern) — Varianten als PNG/JPG geliefert, aber **noch nicht ins Repo gepusht**,
  André muss das finale Bild noch hochladen

## 🔧 KONTEXT & REGELN (Kurzfassung, Details im tools-Repo)
- André: Frankfurt, Coding-Anfänger, aktuell am Handy/Termux (Signal "ich bin am PC" = Git Bash/Windows wechseln)
- **Ein Befehl pro Schritt**, nie Blöcke zum Blind-Einfügen
- Branding: kein "Copywriter" irgendwo, kein Arbeitgebername in Title/Meta/OG-Tags (Body-Text ok)
- Sneaks4seek darf NIEMALS in Bewerbungskontext auftauchen
- STAFF-Repo ist komplett separates Projekt, nie mit rm-apply verknüpfen
- Alle Portfolio-Aussagen brauchen einen verifizierbaren Link
- Telefonnummer überall: 01525 6044541 (alte falsche Nummer: 0163 469 2255 — Vorsicht, taucht immer wieder auf)
- Vor jedem Edit an mehrfach bearbeiteten Dateien: `git fetch origin && git log HEAD..origin/main --oneline`
- Graphify (uv tool graphifyy) läuft nur auf dem PC, nicht auf Termux (Kompilierfehler bei tree-sitter-Paketen)

## 📍 Live-Links
- Repo: https://github.com/intelligentresponder-max/rm-apply
- Live: https://intelligentresponder-max.github.io/rm-apply
- Lebenslauf: https://intelligentresponder-max.github.io/rm-apply/lebenslauf.html
