# CROWN-ARCHITECTURE.md
> Systemdokumentation CROWN v10 — Value-Betting-System
> Stand: Juli 2026 | André Schwarz / ASGlobal
> Repo: https://github.com/intelligentresponder-max/crown-v10

---

## 🏆 Was ist CROWN v10?

CROWN v10 ist ein ausgereiftes Value-Betting-System das auf Android/Termux läuft.  
Es analysiert Fußballspiele automatisch, erkennt Value-Wetten und sendet Alerts via Telegram.  
Entwickelt: März–April 2026. Ziel: Upgrade & kommerzielle Vermarktung.

---

## 🏗️ Architektur-Übersicht

```
┌─────────────────────────────────────────────┐
│              TELEGRAM BOT                   │
│         (Eingang & Ausgang)                 │
└──────────────────┬──────────────────────────┘
                   │
         ┌─────────▼─────────┐
         │  COORDINATOR AGENT │
         │  (Zentrale Steue- │
         │   rung & Routing)  │
         └──┬───┬───┬───┬────┘
            │   │   │   │
     ┌──────┘   │   │   └──────┐
     ▼           ▼   ▼          ▼
┌────────┐ ┌──────┐ ┌──────┐ ┌────────┐
│ ODDS   │ │VALUE │ │ xG   │ │ STATS  │
│ AGENT  │ │AGENT │ │MONIT.│ │ AGENT  │
└────┬───┘ └──┬───┘ └──┬───┘ └───┬────┘
     │        │        │         │
     └────────┴────────┴─────────┘
                   │
         ┌─────────▼─────────┐
         │    LOG AGENT       │
         │  (SQLite-DB)       │
         └─────────┬──────────┘
                   │
         ┌─────────▼─────────┐
         │   ALERT AGENT      │
         │ (Telegram-Output)  │
         └────────────────────┘
```

---

## 🤖 Die 6 Agenten

### 1. Coordinator Agent
- **Rolle:** Dirigent des Systems
- **Aufgabe:** Empfängt Inputs, verteilt Aufgaben an andere Agenten, entscheidet ob ein Alert ausgelöst wird
- **Trigger:** Neues Spiel erkannt, Screenshot eingehend, manueller Start

### 2. Odds Agent
- **Rolle:** Quoten-Wächter
- **Aufgabe:** Ruft aktuelle Quoten ab, erkennt Bewegungen, vergleicht mit Opening Odds
- **Entscheidung:** Ist die Quote noch Value nach Bewegung?

### 3. Value Agent
- **Rolle:** Kern-Kalkulator
- **Aufgabe:** Berechnet Expected Value (EV) auf Basis der Quoten
- **Methode:** Kelly Criterion — 25% fractional Kelly
- **Output:** Empfohlene Stake-Größe & EV in %

### 4. xG Monitor
- **Rolle:** Live-Daten-Tracker
- **Aufgabe:** Überwacht Expected Goals (xG) während des Spiels
- **Trigger für Live Rules:** Wenn xG-Wert einen Schwellenwert erreicht

### 5. Stats Agent
- **Rolle:** Statistik-Basis
- **Aufgabe:** Liefert historische Daten, Team-Form, Head-to-Head
- **Nutzt:** Vorberechnete Wahrscheinlichkeiten als Grundlage für Value Agent

### 6. Log Agent
- **Rolle:** Gedächtnis des Systems
- **Aufgabe:** Schreibt alle Wetten, Ergebnisse, EV-Kalkulationen in SQLite-Datenbank
- **Wichtig für:** Auswertung, Backtesting, Kommerzialisierung

---

## ⚡ Alert Agent

- Letztes Glied in der Kette
- Sendet formatierte Nachrichten via Telegram
- Enthält: Spiel, Markt, Quote, Stake-Empfehlung, EV%, Reasoning
- Nutzt Claude Vision für Screenshot-Analyse (Quoten-Screenshots aus Betting-Apps)

---

## 📋 Live Rules

Live Rules werden während laufender Spiele ausgelöst:

### `BTTS_VALUE_DIP`
- **Bedeutung:** Both Teams To Score — Value Dip
- **Trigger:** Quote für BTTS fällt unter kalkulierten Schwellenwert nach xG-Entwicklung
- **Action:** Alert mit aktueller Quote & Stake-Empfehlung

### `FAVORIT_HZ1`
- **Bedeutung:** Favorit Halbzeit 1
- **Trigger:** Favorit führt noch nicht zur Halbzeit, Quote erhöht sich
- **Action:** Value-Check & Alert wenn EV positiv

### `FAVORIT_HZ2`
- **Bedeutung:** Favorit Halbzeit 2
- **Trigger:** Favorit liegt zurück in HZ2, korrigierte Quote bietet Value
- **Action:** Alert mit erhöhter Stake-Empfehlung (höheres EV)

---

## 🗄️ Datenbank (SQLite)

Tabellen (vereinfacht):

| Tabelle | Inhalt |
|---|---|
| `bets` | Alle platzierten/empfohlenen Wetten |
| `results` | Spielergebnisse & Settlement |
| `odds_history` | Quoten-Bewegungen über Zeit |
| `ev_log` | EV-Kalkulationen je Wette |
| `sessions` | Bot-Sessions & Laufzeiten |

---

## 📱 Telegram Bot

- **Eingang:** Screenshots aus Betting-Apps → Claude Vision analysiert Quoten
- **Ausgang:** Formatierte Alerts mit allen Infos
- **Commands (geplant):** `/status`, `/stats`, `/lastbet`, `/bankroll`

---

## 🔄 Auto GitHub Backup

- System pusht automatisch SQLite-DB & Logs zu GitHub
- Sicherung: täglich oder nach X Wetten
- Verhindert Datenverlust bei Termux-Reset

---

## 🚀 Upgrade-Roadmap (geplant)

| Feature | Priorität |
|---|---|
| Web-Dashboard (Stats & History) | Hoch |
| Mehrere Buchmacher parallel | Hoch |
| Automatisches Settlement | Mittel |
| Subscription-Model (kommerziell) | Hoch |
| iOS-Kompatibilität | Niedrig |
| API für externe Nutzer | Mittel |

---

## 🛠️ Setup (Kurzversion)

```bash
cd ~/storage/shared/repos/crown-v10
pip install -r requirements.txt --break-system-packages
# .env mit Telegram-Token & API-Keys befüllen
python main.py
```

Details → separates `CROWN-SETUP.md` (noch zu erstellen)

---

## 📌 Wichtige Kennzahlen

| Parameter | Wert |
|---|---|
| Kelly Fraction | 25% (fractional) |
| Min. EV für Alert | konfigurierbar (default: +5%) |
| Plattform | Android / Termux |
| Sprache | Python |
| DB | SQLite |
