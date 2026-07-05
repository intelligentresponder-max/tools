# PC-ROUTINE.md
> Git Bash auf Windows — Arbeitsroutine für André Schwarz
> Stand: Juli 2026

---

## 🖥️ Setup

- **OS:** Windows (PC "Holy New")
- **Shell:** Git Bash (MINGW64)
- **Username:** `Holy New`
- **Home:** `C:\Users\Holy New\` = `~/` in Git Bash
- **Downloads:** `~/Downloads/`

---

## 📁 Repos am PC (Stand Juli 2026)

| Repo | Lokaler Ordner | Geklont? |
|---|---|---|
| `texter-portfolio` | `~/texter` | ✓ ja |
| `bewerbung-copywriter` | noch offen | prüfen |
| `turmhotel` | noch offen | prüfen |
| `crown-v10` | noch offen | nicht nötig am PC |
| `tools` | noch offen | empfohlen |

---

## ⚡ Standard-Workflow am PC

### Datei aus Claude-Download ins Repo pushen:
```bash
cd ~/reponame
cp ~/Downloads/dateiname.html .
git add dateiname.html
git commit -m "was wurde geändert"
git push
```

### Repo erstmalig klonen (wenn noch nicht vorhanden):
```bash
cd ~
git clone https://github.com/intelligentresponder-max/REPONAME.git LOKALER-ORDNERNAME
```
Beispiel texter-portfolio:
```bash
git clone https://github.com/intelligentresponder-max/texter-portfolio.git texter
```

### Mehrere Dateien auf einmal:
```bash
cd ~/reponame
cp ~/Downloads/datei1.html .
cp ~/Downloads/datei2.html .
git add datei1.html datei2.html
git commit -m "update"
git push
```

### Aktuellen Stand holen (vor dem Arbeiten):
```bash
cd ~/reponame
git pull
```

---

## ⚠️ PC-spezifische Hinweise

- **LF/CRLF Warning** beim Commit = harmlos, einfach ignorieren
- **Leerzeichen im Pfad:** `Holy New` hat ein Leerzeichen → in Skripten mit Anführungszeichen: `"~/Downloads/meine datei.html"`
- **Kein Termux hier:** `deploy`, `grab`, `copynew` gibt es am PC nicht
- **Kein `~/storage/`:** Downloads liegen direkt in `~/Downloads/`
- **GitHub Pages:** nach Push ~1-2 Min warten bis Änderung live ist

---

## 🔄 Sync-Check (wenn unsicher ob aktuell)

```bash
cd ~/reponame
git status
git log --oneline -5
```

---

## 📋 Repos prüfen (welche sind am PC geklont?)

```bash
ls ~
```
Zeigt alle Ordner in Home — geklonte Repos sind dabei.

