# tools — Routinen für alle Projekte

**Regel Nr. 1: Jeder Claude/KI-Agent liest dieses Repo BEVOR ein neues Projekt startet.**

## Routinen-Übersicht

| Routine | Wann |
|---|---|
| **DEPLOY-ROUTINE.md** | Datei von Claude → Downloads → Repo → GitHub Pages |
| **FORMULAR-ROUTINE.md** | Neues Formular bauen (5-Sektionen-Standard) |
| **FRAGE-ROUTINE.md** | Checkliste VOR jedem neuen Formular/Projekt |
| **FOTO-ROUTINE.md** | Fotos und Screenshots an Claude übergeben + Glow-Tools |
| **MAGIX-ROUTINE.md** | Bilder mit Volt/Glow-Effekt bearbeiten (magix.py) |
| **MAGIC-ZOOM-ROUTINE.md** | Glow + Ken-Burns Video fuer Reels (magic_zoom.py) |
| **SED-ROUTINE.md** | Dateien direkt in Termux aendern - KEIN Download |
| **KONFLIKT-ROUTINE.md** | git push rejected / Merge-Konflikte lösen |
| **CURL-CHECK-ROUTINE.md** | Live-Deployment ohne Browser verifizieren |
| **WINDOWS-ROUTINE.md** | ⚡ AKTIVIEREN wenn André sagt "bin am PC" |
| **DATEINAME-ROUTINE.md** | index(1).html-Problem & Prefix-Kollisionen |
| **BATCH-ROUTINE.md** | Änderungen sammeln, EIN Push statt sieben |

## Eiserne Regeln (gelten immer)

1. **grab nimmt nur EINE Datei** — immer einzeln aufrufen
2. **Vor grab: alte Versionen aus Downloads löschen** (`rm basename*.html`)
3. **Integrity-Check vor jedem Push**: `grep -c "keyword"` auf INHALT, nie auf Dateinamen
4. **`echo "OK: datei <- quelle"`** vor jedem Push
5. **Branch beachten**: telavendelele = `master`, alle anderen = `main`
6. **Push rejected?** → KONFLIKT-ROUTINE (pull --rebase)
7. **Nach Push: 2 Min warten**, dann CURL-CHECK
8. **Keine Latein-Phrasen** auf Andrés Seiten
9. **Kein Freelance-/Gewerbe-Framing** — André hat kein Gewerbe
10. **André sagt "bin am PC"?** → WINDOWS-ROUTINE aktivieren, Termux-Befehle stoppen

## Repos & Branches

| Repo | Branch | Zweck |
|---|---|---|
| tools | main | Dieses Repo — Routinen |
| bewerbung-copywriter | main | Bewerbung Roman Mayer |
| texter-portfolio | main | Freelance-Portfolio (6 Seiten) |
| telavendelele | **master** | Autos Frankfurt ↔ Comer See |
| Sneaks4seek | main | Sneaker-Plattform |
