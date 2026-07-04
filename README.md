# tools
> Workflow-Dokumentation & Routinen für alle Projekte unter `intelligentresponder-max`  
> Maintainer: André Schwarz / ASGlobal Frankfurt | Stand: Juli 2026

Dieses Repo hat keinen Code — nur Dokumentation. Es ist das Gehirn hinter dem Setup.  
Wenn du (oder Claude) nicht mehr weißt, wie etwas geht: hier nachschauen.

---

## 📁 Dateien in diesem Repo

| Datei | Inhalt |
|---|---|
| `DEPLOY-ROUTINE.md` | `grab`, `deploy`, `clean` — der komplette Push-Workflow von Termux zu GitHub Pages |
| `FRAGE-ROUTINE.md` | Wie du mit Claude arbeitest — Prompt-Struktur, Kontext geben, Iterations-Workflow |
| `RENAME-ROUTINE.md` | Dateien & Ordner umbenennen in Termux, Git-sicher |
| `REPOS-OVERVIEW.md` | Alle aktiven Repos, Zweck, URLs, Status auf einen Blick |

---

## ⚡ Schnellstart (nach langer Pause)

1. **Termux öffnen**
2. `cd ~/storage/shared/<repo-name>` — in das richtige Verzeichnis
3. `grab` — aktuellen Stand holen
4. Änderungen machen
5. `deploy "kurze Commit-Message"` — live pushen

Details: [`DEPLOY-ROUTINE.md`](./DEPLOY-ROUTINE.md)

---

## 🗂️ Aktive Projekte

Vollständige Übersicht → [`REPOS-OVERVIEW.md`](./REPOS-OVERVIEW.md)

Kurzversion:
- **texter-portfolio** — Portfolio-Hub (ASGlobal)
- **bewerbung-copywriter** — Roman Mayer Bewerbung (abgeschlossen)
- **bangla-hilfe** — DE/Bengali Community-Plattform
- **turmhotel** — Gästeportal Turmhotel Frankfurt
- **crown-v10** — Value-Betting-System (Upgrade geplant)
- **Sneaks4seek** — Sneaker-Marketplace

---

## 🧠 Arbeiten mit Claude (Robo Bro)

Kontext am Anfang jeder Session:
```
Ich bin André, Frankfurt. Termux/Android, Coding-Beginner.
Aktuelles Projekt: [Repo-Name]
Ich will: [konkretes Ziel]
```

Vollständige Routine: [`FRAGE-ROUTINE.md`](./FRAGE-ROUTINE.md)

---

## 🔧 Toolchain

Alle Shell-Funktionen leben in `~/.bashrc` auf dem Android-Gerät.  
Nicht in diesem Repo — aber hier dokumentiert.

```bash
grab              # git pull
deploy "msg"      # git add . && git commit -m "msg" && git push
clean             # temporäre Dateien löschen
```

---

## 📌 Wichtige Links

| | |
|---|---|
| GitHub-Account | https://github.com/intelligentresponder-max |
| Portfolio | https://intelligentresponder-max.github.io/texter-portfolio |
| CROWN v10 | https://github.com/intelligentresponder-max/crown-v10 |
