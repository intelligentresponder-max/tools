# CROWN-AGENT-CHECK.md
> Alle Agenten prüfen, debuggen und erweitern
> Stand: Juli 2026 | André Schwarz / ASGlobal

---

## 🔍 Alle Agenten auf einmal prüfen

```bash
cd ~/crown-v10
grep "^def " agents/*.py
```

Zeigt alle Funktionsnamen in allen Agenten-Dateien.
Wichtig wenn Imports fehlschlagen — so siehst du den echten Funktionsnamen.

---

## 🔧 Import-Fehler fixen

Wenn coordinator.py einen falschen Namen importiert:

```bash
# Prüfen was coordinator erwartet
grep "^from agents" agents/coordinator.py

# Prüfen was wirklich da ist
grep "^def " agents/AGENTNAME.py

# Fix einbauen (Beispiel)
sed -i 's/import FALSCHER_NAME/import ECHTER_NAME as FALSCHER_NAME/' agents/coordinator.py
```

---

## ✅ Automatischer Gesundheitscheck (health_check.sh)

Speichern als `~/crown-v10/health_check.sh`:

```bash
#!/bin/bash
echo "=== CROWN v10 Health Check ==="
echo ""

echo "📁 Agenten-Dateien:"
ls agents/*.py 2>/dev/null || echo "FEHLER: agents/ Ordner nicht gefunden"

echo ""
echo "🔧 Funktionen je Agent:"
grep "^def " agents/*.py

echo ""
echo "🔗 Symlink-Check:"
find . -type l | while read f; do
  if [ ! -e "$f" ]; then
    echo "  KAPUTT: $f -> $(readlink $f)"
  else
    echo "  OK: $f"
  fi
done

echo ""
echo "📦 Python-Import-Test:"
python -c "
import sys
sys.path.insert(0, '.')
agents = ['markets', 'utils', 'config', 'analysis']
for a in agents:
    try:
        __import__(a)
        print(f'  OK: {a}')
    except Exception as e:
        print(f'  FEHLER: {a} — {e}')
"

echo ""
echo "=== Check abgeschlossen ==="
```

Ausführbar machen:
```bash
chmod +x health_check.sh
```

Starten:
```bash
bash health_check.sh
```

---

## 🤖 Aktuelle Agenten (Crown v10)

| Agent | Datei | Haupt-Funktion | Aufgabe |
|---|---|---|---|
| Coordinator | `coordinator.py` | `run_coordinator()` | Steuerung & Routing |
| Odds | `odds_agent.py` | `run_odds_agent()` | Quoten holen & prüfen |
| Value | `value_agent.py` | `run_value_agent()` | EV berechnen, Kelly |
| Stats | `stats_agent.py` | `show_stats()` | Historische Daten |
| Log | `log_agent.py` | `log_bets()` | SQLite-Logging |
| Alert | `alert_agent.py` | `send_value_bets()` | Telegram-Alerts |

---

## 🚀 Empfohlene neue Agenten (Ausbau-Roadmap)

### Sofort sinnvoll:

| Agent | Aufgabe | Warum wichtig |
|---|---|---|
| `result_agent.py` | Ergebnisse automatisch holen & Settlement | Kein manuelles Nachtragen |
| `bankroll_agent.py` | Bankroll tracken, Kelly anpassen | Schutz vor Überinvestment |
| `filter_agent.py` | Spiele vorfiltern nach Liga/Zeit/Mindest-EV | Weniger Rauschen |

### Mittelfristig:

| Agent | Aufgabe | Warum wichtig |
|---|---|---|
| `xg_agent.py` | Live xG überwachen | Live Rules auslösen |
| `lineup_agent.py` | Aufstellungen prüfen vor Wette | Verletzungen = wertlose Quote |
| `report_agent.py` | Tagesreport generieren (PDF/Telegram) | Überblick ohne Terminal |

### Für Kommerzialisierung:

| Agent | Aufgabe | Warum wichtig |
|---|---|---|
| `user_agent.py` | Mehrere User verwalten | Subscription-Modell |
| `webhook_agent.py` | Externe Signale empfangen | n8n / API-Integration |
| `dashboard_agent.py` | Web-Dashboard befüllen | Kunden-Frontend |

---

## 📅 Cronjobs (automatisch starten)

```bash
# Crontab öffnen
crontab -e

# Beispiele:
# Jeden Tag um 10:00 Uhr Crown starten
0 10 * * * cd ~/crown-v10 && python main_auto.py >> ~/crown-v10/cron_v10.log 2>&1

# Jede Stunde Health Check
0 * * * * cd ~/crown-v10 && bash health_check.sh >> ~/crown-v10/health.log 2>&1

# Täglich um Mitternacht GitHub Backup
0 0 * * * cd ~/crown-v10 && bash git_autopush.sh >> ~/crown-v10/backup.log 2>&1
```

Crontab speichern: `Strg+X` → `Y` → Enter

Crontab in Termux aktivieren:
```bash
pkg install cronie -y
crond
```

---

## 💡 Nützliche Einzel-Befehle

```bash
# Alle laufenden Python-Prozesse
ps aux | grep python

# Crown stoppen
pkill python

# Logs live verfolgen
tail -f cron_v10.log

# Letzten 20 Log-Einträge
tail -20 cron_v10.log

# Datenbank-Inhalt prüfen
python -c "import sqlite3; db=sqlite3.connect('data/crown.db'); print(db.execute('SELECT COUNT(*) FROM bets').fetchone())"
```

