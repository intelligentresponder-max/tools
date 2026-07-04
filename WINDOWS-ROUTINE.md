# WINDOWS-ROUTINE — Arbeiten am PC mit Git Bash

## ⚡ WICHTIG FÜR CLAUDE / KI-AGENTEN

**Wenn André sagt "ich sitze jetzt am PC" oder "bin am Rechner":**
→ SOFORT diese Routine aktivieren und ALLE Empfehlungen umstellen!

Die Termux-Befehle funktionieren am PC NICHT oder anders.
Ab diesem Moment gelten die PC-Regeln unten — bis André sagt
dass er wieder am Handy/Termux ist.

---

## Unterschiede Termux ↔ Git Bash (PC)

| Was | Termux (Android) | Git Bash (Windows PC) |
|---|---|---|
| Download-Ordner | `~/storage/downloads/` | `~/Downloads/` |
| Kopieren | `cp` | `cp` (NICHT `copy` — das ist CMD!) |
| grab-Funktion | ✅ vorhanden | ❌ existiert nicht → manuell `cp` |
| deploy-Funktion | ✅ vorhanden | ❌ existiert nicht → git-Befehle einzeln |
| Screenshot | `screencap -p` | Win+Shift+S (Snipping Tool) |
| Editor | nano | nano oder notepad |
| Pfad-Trenner | `/` | `/` in Git Bash (nicht `\`) |

---

## Standard-Workflow am PC

```bash
# 1. Ins Repo wechseln
cd ~/Documents/GitHub/[REPO]     # Pfad ggf. anpassen — mit ls prüfen!

# 2. Datei aus Downloads holen (grab gibt's hier nicht!)
cp ~/Downloads/[DATEI].html [DATEI].html

# 3. Integrity-Check (Regel aus DEPLOY-ROUTINE)
grep -c "KEYWORD" [DATEI].html

# 4. Push
git add [DATEI].html
git commit -m "Beschreibung"
git push
```

---

## Typische PC-Fallen

1. **`copy` funktioniert nicht** — das ist ein CMD-Befehl. In Git Bash immer `cp`.
2. **Downloads heißt anders** — `~/Downloads/` (großes D), nicht `~/storage/downloads/`
3. **Repo-Pfad unbekannt** — erst `ls ~` und `ls ~/Documents` machen um zu finden wo die Repos liegen
4. **"nothing to commit, working tree clean"** — heißt: die Datei ist identisch mit dem Repo. Meist wurde vom Handy schon gepusht. KEIN Fehler!
5. **Zeilenenden-Warnungen (CRLF/LF)** — kann man ignorieren, git regelt das

---

## Für Claude: Empfehlungen die sich am PC ändern

- ❌ Keine `grab`-Befehle vorschlagen → stattdessen `cp ~/Downloads/...`
- ❌ Keine Termux-Pfade (`~/storage/...`) verwenden
- ❌ Kein `screencap` → Win+Shift+S erwähnen
- ✅ Datei-Upload in den Chat funktioniert am PC identisch (Browser: Büroklammer)
- ✅ Git-Befehle (`pull --rebase`, `checkout --theirs` etc.) sind identisch
- ✅ curl-Checks funktionieren identisch

---

## Zurück am Handy?
Wenn André sagt "bin wieder am Handy" → Termux-Regeln
(DEPLOY-ROUTINE.md) gelten wieder.
