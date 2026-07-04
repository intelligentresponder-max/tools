# CROWN-START-ROUTINE.md
> Checkliste vor jedem CROWN v10 Start
> Stand: Juli 2026 | André Schwarz / ASGlobal

---

## ✅ Pre-Start Checkliste

### 1. Richtiger Ordner
```bash
cd ~/crown-v10
pwd
# muss zeigen: /data/data/com.termux/files/home/crown-v10
```

### 2. Repo aktuell?
```bash
git pull
```

### 3. Symlink-Check — keine gebrochenen Links
```bash
find . -type l | while read f; do
  if [ ! -e "$f" ]; then
    echo "KAPUTT: $f -> $(readlink $f)"
  else
    echo "OK: $f"
  fi
done
```
Wenn `KAPUTT` erscheint: Datei fehlt (z.B. noch auf Tablet) → erst `git pull` oder vom Tablet pushen.

### 4. Python-Module prüfen
```bash
pip install -r requirements.txt --break-system-packages 2>&1 | tail -3
```

### 5. Config prüfen
```bash
head -20 config.py
```
Token & API Keys vorhanden?

### 6. Teststart
```bash
python main.py
```

---

## 🚨 Häufige Fehler & Fix

| Fehler | Ursache | Fix |
|---|---|---|
| `No module named 'markets'` | Symlink kaputt — Datei auf anderem Gerät | Vom Tablet pushen, dann `git pull` |
| `No module named 'xyz'` | requirements nicht installiert | `pip install -r requirements.txt --break-system-packages` |
| Bot antwortet nicht | Token falsch | `config.py` prüfen |
| Prozess stirbt | Termux minimiert | `nohup python main_auto.py &` |

---

## 📱 Dateien vom Tablet holen

Wenn Symlinks kaputt sind (Dateien noch auf Tablet):

**Auf dem Tablet:**
```bash
cd ~/crown-v10
# oder wo valuebet liegt:
cd ~/valuebet
cp *.py ~/crown-v10/
cd ~/crown-v10
git add .
git commit -m "add missing source files"
git push
```

**Dann auf Handy:**
```bash
cd ~/crown-v10
git pull
```

---

## 🚀 Start-Befehle

```bash
# Normal
python main.py

# Auto-Dauerbetrieb
nohup python main_auto.py &

# Alles auf einmal
bash start_all.sh

# Logs verfolgen
cat nohup.out
```
