# CLAUDE-BRIEFING.md
> Pflichtlektüre für jede neue Claude-Instanz die mit André Schwarz arbeitet.
> Stand: Juli 2026 | Maintainer: André Schwarz / ASGlobal Frankfurt

---

## 👤 Wer ist André?

- Freelance Copywriter & Digitalisierungsberater, Frankfurt-Preungesheim
- Brand: **ASGlobal** | Nebenjob: Turmhotel Frankfurt (Rezeption)
- GitHub: `intelligentresponder-max`
- Selbstbezeichnung Coding-Level: **Anfänger** — behandle ihn so
- Nennt Claude: **"Robo Bro"** — lockerer Ton ist okay
- Kommuniziert per Stimme auf dem Handy, tippt langsam auf dem Tablet

---

## 📱 Geräte & Umgebungen — WICHTIG

### Handy / Tablet → **Termux (Android)**
- Repos direkt in `~` (z.B. `~/tools`, `~/crown-v10`, `~/texter-portfolio`)
- Downloads: `~/storage/shared/Download` ← **ohne "s"!**
- Samsung hängt manchmal `(1)` oder `-1` an Dateinamen → `copynew` nutzen
- Push-Funktionen in `~/.bashrc`: `deploy`, `grab`, `clean`, `copynew`
- Deploy-Pattern: `cd ~/reponame && deploy "commit message"`
- **Ein Befehl pro Schritt** — nie mehrere auf einmal schicken

### PC → **Git Bash (Windows)**
- Windows-Username: **Holy New**
- Home-Pfad: `C:\Users\Holy New\` = `~/` in Git Bash
- Downloads: `~/Downloads/dateiname`
- Repos müssen ggf. erst geklont werden: `git clone URL foldername`
- Bekannte geklonte Repos: `texter-portfolio` → als `texter` geklont
- Push-Pattern PC:
  ```bash
  cd ~/reponame
  cp ~/Downloads/datei.html .
  git add datei.html
  git commit -m "beschreibung"
  git push
  ```
- LF/CRLF-Warning auf Windows = **harmlos, ignorieren**
- `~` in Git Bash = `/c/Users/Holy New/`

### Signal "Ich bin am PC"
Wenn André sagt **"ich bin am PC"** → sofort auf Git Bash / Windows umschalten.
Andere Pfade, andere Befehle, kein Termux-Syntax.

---

## 📁 Repo-Übersicht

| Repo | Zweck | Gerät |
|---|---|---|
| `tools` | Diese Docs hier | alle |
| `crown-v10` | CROWN Wett-System | Handy/Tablet |
| `turmhotel` | Gästeportal + Housekeeping App | alle |
| `texter-portfolio` | Portfolio André (als `texter` geklont am PC) | alle |
| `bewerbung-copywriter` | Bewerbung Roman Mayer GmbH | alle |
| `sneaks4seek` | Streetwear-Marktplatz | Handy |

---

## 🔧 Arbeitsregeln — PFLICHT

1. **Ein Befehl pro Schritt** — nie Blöcke schicken die André blind eintippt
2. **Erst Verzeichnis prüfen** bevor irgendwas gemacht wird: `pwd`
3. **Vor destruktiven Befehlen** (force-push, reset, rm) explizit warnen
4. **Kein `/tmp` für finale Dateien** — immer direkt ins Ziel-Repo schreiben
5. **Samsung Download-Check:** `ls ~/storage/shared/Download/DATEINAME*` vor jedem `cp`
6. **Nie Funktionsnamen raten** — erst in der Datei nachschauen
7. **LF/CRLF am PC** = harmlos, erwähnen aber nicht aufhalten
8. **Force-Push nur nach expliziter Warnung** — nie einfach so
9. **Pfad-Kontext merken:** Termux vs. Git Bash macht große Unterschiede
10. **Neue Erkenntnisse** → nach spätestens 3 ans tools repo erinnern

---

## 🚨 Lessons Learned (nie wieder)

- **Juli 2026:** Force-Push vom Tablet hat neuere Handy-Version von crown-v10 überschrieben → immer erst vergleichen
- **Symlinks auf Handy:** `markets.py` war ein Symlink der auf Tablet-Pfad zeigte → kaputt auf Handy
- **`/tmp`-Falle:** Claude schreibt Datei nach `/tmp`, aber `git` im Repo merkt nichts → Commit zeigt "nothing to commit"

---

## 🏨 Turmhotel Frankfurt — Kontext

- Inhaberin: Tanja
- Projekte: Gästeportal (GitHub Pages), Housekeeping Manager v3, WhatsApp-Widget
- Hotel-Branding: Grün `#2e6b4f`, Krone-Logo ♔, Fonts: Cormorant Garamond + Jost
- Adresse: Eschersheimer Landstraße 20, 60322 Frankfurt
- Zimmer: 77 (Haupthaus + Nebenhaus)
- Hausdame kommuniziert über WhatsApp-Gruppe (Link = Platzhalter, noch einzutragen)

---

## 💬 Ton

Locker, direkt, "Robo Bro" ist okay.
Bei Risiko-Aktionen: **klar und deutlich warnen**, auch wenn's die Stimmung bremst.
Lieber einmal zu vorsichtig als einmal Force-Push zu viel.

---

## 🚨 Lessons Learned — 12.07.2026 (Turmhotel HSK v3)

- **Escaped-Backtick-Bug:** Ein einziger \` oder \${...} in Template Literals killt das GESAMTE Script lautlos — kein Tab reagiert, alle Zähler bleiben 0. Vor JEDEM Push Pflicht-Check:
  `sed -n '/<script>/,/<\/script>/p' DATEI.html | grep -v '<script>\|</script>' > ~/hk.js && node --check ~/hk.js`
- **git-Desync:** Lokaler Ordner kann veraltet sein trotz "up to date" Meldung (nach Reset/Neuklon). Bei Verdacht: `git fetch origin && git reset --hard origin/main` (verwirft lokale uncommitted Änderungen!)
- **localStorage-Falle:** HSK-Tool speichert nur PRO BROWSER, kein Sync zwischen Geräten/Tabs. Team-Nutzung braucht 1 gemeinsames Gerät ODER Export/Import-Workflow — sonst sieht jeder einen anderen Stand.
- **Datenmodell Turmhotel:** 11–55 (2-stellig) = Vorderhaus = eigentlich HAUPTHAUS (App-Label aktuell falsch vertauscht mit Hinterhaus). 101–510 (3-stellig) = Hinterhaus/Nebenhaus.

## 📌 BACKFALL-Vollständigkeits-Regel
Bei Trigger BACKFALL: nicht nur tools-Repo lesen, sondern bei Bedarf auch
die relevanten Projekt-Repos (turmhotel, sneaks4seek, texter-portfolio,
bewerbung-copywriter, crown-v10) kurz gegenchecken, wenn das Gespräch
dorthin geht — nicht blind auf altes Wissen verlassen.
