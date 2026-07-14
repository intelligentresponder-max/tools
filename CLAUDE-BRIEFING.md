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

## 🔍 Lessons Learned — RM-apply777 Session 14.07.2026

**Hauptproblem der Session: Paralleles Arbeiten an Repos ohne Sync-Check**
Mehrere Sessions am selben Tag haben unabhängig voneinander an `rm-apply/index.html`
gearbeitet (eine hat "Copywriter→Ghostwriter" + Roman-Mayer-Meta-Tags gebaut, eine andere
parallel dieselben Stellen anders gelöst). Ergebnis: `git push` wurde rejected, weil Remote
schon neuere Commits hatte, die lokal fehlten — inklusive einer komplett neuen Kachel
(Callcenter-Leitfaden), die sonst überschrieben worden wäre.

**Regel ab jetzt: Vor JEDER Änderung an einer bereits mehrfach bearbeiteten Datei:**
```
git fetch origin && git log HEAD..origin/main --oneline
```
Wenn da was steht → NICHT blind pushen. Erst `git diff HEAD..origin/main -- DATEI`
anschauen, dann entscheiden: übernehmen, mergen oder gezielt nur die eigene Änderung
draufsetzen (so wie in dieser Session: Remote-Datei per `curl`/`raw.githubusercontent.com`
ziehen, nur den betroffenen Block per `str_replace` ändern, Rest unangetastet lassen).

**Bei `git reset --hard origin/main`:** Verwirft NICHT nur den Commit-Text, sondern auch
alle Dateien, die nur in diesem verworfenen Commit lagen und noch nicht separat gepusht
wurden (hier: das Hero-Foto ist dabei kurz "verschwunden" und musste danach erneut kopiert
und gepusht werden). Nach jedem `reset --hard` kurz `git status` + `ls` checken, ob was fehlt.

---

## 📋 Proaktiv aufgefallen, noch nicht überall geprüft

- **Telefonnummer-Bug tauchte zweimal auf** (rm-apply UND texter-portfolio hatten beide
  die alte `0163 469 2255` im Footer, obwohl schon früher auf `01525 6044541` korrigiert
  worden war). Empfehlung: bei künftigen Sessions einmal `grep -rn "0163\|163 469"` über
  alle drei Bewerbungs-Repos laufen lassen, um sicherzugehen dass die alte Nummer nirgends
  mehr schlummert (auch `bewerbung-copywriter` nicht separat gecheckt in dieser Session).
- **Privacy-Pattern jetzt auch für Meta-Tags etabliert, nicht nur Dateinamen:** Title,
  meta description, og:title, og:description dürfen "Roman Mayer" nicht enthalten (Google-
  Auffindbarkeit), Fließtext auf der Seite selbst schon (da liest ihn ja Roman Mayer direkt).
  Gilt für alle drei Repos — `bewerbung-copywriter` wurde in dieser Session nicht auf
  Meta-Tags geprüft, sollte nachgeholt werden.
- **Housekeeping-Links waren uneinheitlich** (mal lokale Kopie, mal alte externe URL ohne
  "v3", mal die aktuelle Live-URL). Jetzt einheitlich auf
  `https://intelligentresponder-max.github.io/turmhotel/housekeeping/housekeeping-v3.html`
  in beiden geprüften Repos — `bewerbung-copywriter` noch nicht gecheckt.
