# DEVICE-RESTORE-ROUTINE.md
> Was tun wenn: neues Gerät, neues Termux, Termux-Reset, oder alles weg
> Stand: Juli 2026 | André Schwarz / ASGlobal

---

## 🧭 Zwei Szenarien

| Szenario | Was tun |
|---|---|
| **Neues Gerät / Termux-Neuinstallation** | → Abschnitt A (Komplett-Setup) |
| **Repos fehlen, aber Termux läuft noch** | → Abschnitt B (Nur Repos holen) |

---

## A) Komplett-Setup auf neuem Gerät

### Schritt 1 — Termux installieren & updaten
```bash
pkg update && pkg upgrade -y
```

### Schritt 2 — Nötige Pakete installieren
```bash
pkg install git openssh python -y
```

### Schritt 3 — SSH-Key erstellen
```bash
ssh-keygen -t ed25519 -C "deine@email.de"
# Enter drücken bis fertig (kein Passwort nötig)
```

### Schritt 4 — SSH-Key zu GitHub hinzufügen
```bash
cat ~/.ssh/id_ed25519.pub
# Den angezeigten Text kopieren
```
Dann: GitHub → Settings → SSH and GPG keys → New SSH key → einfügen → speichern.

### Schritt 5 — Git konfigurieren
```bash
git config --global user.name "intelligentresponder-max"
git config --global user.email "deine@email.de"
```

### Schritt 6 — Storage-Zugriff erlauben
```bash
termux-setup-storage
# Berechtigungsdialog mit "Erlauben" bestätigen
```

### Schritt 7 — Repos holen (→ weiter mit Abschnitt B)

---

## B) Nur Repos holen (Termux läuft, SSH ist eingerichtet)

### Ordner anlegen
```bash
mkdir -p ~/storage/shared/repos
cd ~/storage/shared/repos
```

### Alle Repos auf einmal klonen
```bash
git clone git@github.com:intelligentresponder-max/tools.git
git clone git@github.com:intelligentresponder-max/texter-portfolio.git
git clone git@github.com:intelligentresponder-max/bangla-hilfe.git
git clone git@github.com:intelligentresponder-max/turmhotel.git
git clone git@github.com:intelligentresponder-max/crown-v10.git
git clone git@github.com:intelligentresponder-max/Sneaks4seek.git
git clone git@github.com:intelligentresponder-max/bewerbung-copywriter.git
```

Das war's. Alle Repos sind jetzt lokal verfügbar.

---

## C) bashrc wiederherstellen (grab / deploy / clean)

Nach dem Klonen der Repos:
```bash
cat ~/storage/shared/repos/tools/DEPLOY-ROUTINE.md
```
Die Funktionen aus der Datei manuell in `~/.bashrc` einfügen, dann:
```bash
source ~/.bashrc
```
Ab jetzt funktionieren `grab`, `deploy`, `clean` wieder.

---

## D) Alles auf aktuellem Stand halten (bestehende Repos updaten)

Wenn die Repos schon da sind aber veraltet:
```bash
cd ~/storage/shared/repos/tools && git pull
cd ~/storage/shared/repos/texter-portfolio && git pull
cd ~/storage/shared/repos/bangla-hilfe && git pull
cd ~/storage/shared/repos/turmhotel && git pull
cd ~/storage/shared/repos/crown-v10 && git pull
cd ~/storage/shared/repos/Sneaks4seek && git pull
cd ~/storage/shared/repos/bewerbung-copywriter && git pull
```

Oder als Einzeiler (alle auf einmal):
```bash
for repo in tools texter-portfolio bangla-hilfe turmhotel crown-v10 Sneaks4seek bewerbung-copywriter; do
  echo "--- $repo ---"
  cd ~/storage/shared/repos/$repo && git pull
done
```

---

## ⚠️ Häufige Fehler

| Fehler | Lösung |
|---|---|
| `Permission denied (publickey)` | SSH-Key fehlt auf GitHub → Schritt 3+4 wiederholen |
| `fatal: destination path already exists` | Repo ist schon da → `git pull` statt `git clone` |
| `storage/shared not found` | `termux-setup-storage` nochmal ausführen |
| `git: command not found` | `pkg install git -y` |

---

## 📌 Merke

- `git clone` = erstmalig holen (leeres Verzeichnis)
- `git pull` = vorhandenes Repo aktualisieren
- SSH-Key muss auf GitHub hinterlegt sein — ohne geht nichts
