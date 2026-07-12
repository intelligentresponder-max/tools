# BACKFALL-ANKER — Stand 12.07.2026

## Regel: CODE-ABILITY-CHECK für ALLE Repos
Vor jedem Fix und nach jedem Schreibvorgang:
1. `git pull` im richtigen Repo (pwd prüfen!)
2. JS-Syntaxcheck:
   sed -n '/<script>/,/<\/script>/p' DATEI.html | grep -v '<script>\|</script>' > ~/check.js && node --check ~/check.js
3. Nur bei "ok" → commit + push

## Lesson Learned 12.07.2026 (Turmhotel HSK v3)
Ein einziger **escapter Backtick** (\`) in Zeile 113 hat das komplette
JS lahmgelegt: showTab() nie definiert → kein Tab reagierte, alle Zähler 0.
Ursache: Heredoc-Escaping beim Schreiben der Datei.
Fix: sed -i 's/\\`/`/g' DATEI.html
Erkennung: grep -c '\\`' DATEI.html

## Offene Punkte Turmhotel
- Gebäude-Labels vertauscht: 11–55 = VORDERHAUS/HAUPTHAUS,
  101–510 = HINTERHAUS/NEBENHAUS (App zeigt es umgekehrt)
- Tagesplan 12.07.: 2 Zimmer ungeklärt (Turck STS → 44 od. 54;
  Von Der Goltz VIH → 202/205/404/405/503/504)
