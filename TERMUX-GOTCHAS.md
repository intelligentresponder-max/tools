# TERMUX-GOTCHAS.md
> Typische Fallen & Fixes — gesammelt aus echter Nutzung
> Stand: Juli 2026 | André Schwarz / ASGlobal

---

## 📁 Download-Ordner heißt `Download` nicht `Downloads`

**Falsch:**
```bash
cp ~/storage/shared/Downloads/datei.md .
```

**Richtig:**
```bash
cp ~/storage/shared/Download/datei.md .
```

Kein `s` am Ende! Android nennt den Ordner `Download`, Termux zeigt ihn unter `~/storage/shared/Download`.

---

## 📂 Repos liegen direkt in `~`, nicht in Unterordnern

**Falsch:**
```bash
cd ~/storage/shared/repos/tools
```

**Richtig:**
```bash
cd ~/tools
```

Alle Repos sind direkt im Home-Ordner geklont.

---

## 🔧 deploy-Funktion: Syntax beachten

Die `deploy`-Funktion erwartet die Commit-Message in Anführungszeichen:

**Falsch:**
```bash
deploy add CROWN-SETUP.md
```

**Richtig:**
```bash
deploy "add CROWN-SETUP.md"
```

---

## 🐍 Python-Pakete immer mit `--break-system-packages`

**Falsch:**
```bash
pip install flask
```

**Richtig:**
```bash
pip install flask --break-system-packages
pip install -r requirements.txt --break-system-packages
```

Ohne das Flag verweigert Termux die Installation.

---

## 🔑 SSH vs HTTPS bei git clone

`git clone git@github.com:...` funktioniert nur wenn SSH-Key auf GitHub hinterlegt ist.

Falls SSH nicht eingerichtet: HTTPS nutzen:
```bash
git clone https://github.com/intelligentresponder-max/repo-name.git
```

SSH einrichten → `DEVICE-RESTORE-ROUTINE.md` Abschnitt A.

---

## 📂 Python-Skript immer aus dem richtigen Ordner starten

**Falsch** (aus ~ heraus):
```bash
python ~/crown-v10/main.py
```

**Richtig** (erst rein, dann starten):
```bash
cd ~/crown-v10
python main.py
```

Python findet lokale Module (wie `markets.py`) nur wenn du im gleichen Ordner bist.

---

## 💾 Dateien von Claude.ai nach Termux bringen

1. In Claude.ai: Datei herunterladen → landet in Android `Download`-Ordner
2. In Termux:
```bash
cp ~/storage/shared/Download/dateiname.md ~/zielordner/
```

Mehrere auf einmal:
```bash
cd ~/tools
cp ~/storage/shared/Download/DATEI1.md .
cp ~/storage/shared/Download/DATEI2.md .
cp ~/storage/shared/Download/DATEI3.md .
```

