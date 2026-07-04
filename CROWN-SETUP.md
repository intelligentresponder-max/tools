# CROWN-SETUP.md
> CROWN v10 — Installation & Start auf Android/Termux
> Stand: Juli 2026 | André Schwarz / ASGlobal
> Repo: https://github.com/intelligentresponder-max/crown-v10

---

## Voraussetzungen

- Termux mit Git & SSH (eingerichtet)
- Telegram-Bot-Token (von @BotFather)
- Anthropic API Key (für Claude Vision / Screenshot-Analyse)

---

## Schritt 1 — Repo holen

```bash
cd ~
git clone git@github.com:intelligentresponder-max/crown-v10.git
cd crown-v10
```

Falls schon vorhanden:
```bash
cd ~/crown-v10
git pull
```

---

## Schritt 2 — Abhängigkeiten installieren

```bash
pip install -r requirements.txt --break-system-packages
```

---

## Schritt 3 — Config anpassen

```bash
nano config.py
```

Folgende Werte eintragen/prüfen:
- Telegram Token
- Anthropic API Key
- DB-Pfad
- Kelly Fraction (Standard: 0.25)
- Min EV (Standard: 0.05)

Speichern: `Strg+X` → `Y` → Enter

---

## Schritt 4 — Starten

### Normaler Start:
```bash
python main.py
```

### Auto-Modus (läuft durch):
```bash
python main_auto.py
```

### Alles auf einmal (alle Agenten):
```bash
bash start_all.sh
```

---

## Schritt 5 — Im Hintergrund laufen lassen

```bash
nohup python main_auto.py &
```

Stoppen:
```bash
pkill python
```

Logs prüfen:
```bash
cat nohup.out
```

---

## Wichtige Dateien im Repo

| Datei / Ordner | Funktion |
|---|---|
| `main.py` | Hauptstart — manuell |
| `main_auto.py` | Automatischer Dauerbetrieb |
| `start_all.sh` | Startet alle Komponenten |
| `crown_bot.py` | Telegram-Bot |
| `crown_scanner.py` | Spiele scannen & Value erkennen |
| `agent_pipeline.py` | Agent-Orchestrierung |
| `master_pipeline.py` | Zentrale Pipeline |
| `live_rules/` | Live-Regeln (BTTS_VALUE_DIP etc.) |
| `agents/` | Alle Agenten (coordinator, value, odds...) |
| `core/` | Kern-Logik |
| `config.py` | Konfiguration (Token, Keys, Parameter) |
| `screenshot_analyzer.py` | Claude Vision — Quoten aus Screenshots |
| `stake_calc.py` | Kelly Criterion Kalkulator |
| `live_notifier.py` | Telegram-Alerts |
| `live_importer.py` | Live-Daten importieren |
| `result_checker.py` | Ergebnisse prüfen & Settlement |
| `dashboard_cli.py` | Terminal-Dashboard |
| `git_autopush.sh` | Auto-Backup zu GitHub |
| `data/` | SQLite-Datenbank & Logs |
| `app_data/` | App-Daten & Cache |

---

## Nützliche Einzeltools

```bash
# Quoten-Kalkulator
python stake_calc.py

# Dashboard im Terminal
python dashboard_cli.py

# Ergebnisse manuell importieren
python result_checker.py

# Screenshot analysieren (Claude Vision)
python screenshot_analyzer.py

# Manuelles GitHub-Backup
bash git_autopush.sh
```

---

## ⚠️ Häufige Fehler

| Fehler | Lösung |
|---|---|
| `ModuleNotFoundError` | `pip install -r requirements.txt --break-system-packages` |
| Bot antwortet nicht | Token in `config.py` prüfen |
| `Permission denied (publickey)` | SSH-Key auf GitHub fehlt → `DEVICE-RESTORE-ROUTINE.md` |
| Prozess stirbt bei Termux-Minimize | `nohup python main_auto.py &` verwenden |

---

## Architektur & Live Rules

→ [`CROWN-ARCHITECTURE.md`](./CROWN-ARCHITECTURE.md)
