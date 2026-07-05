# SED-MAGIC.md
> ⚡ Proaktiv nutzen! Spart Download-Zyklen und ist in 10 Sekunden erledigt.
> Stand: Juli 2026 | Maintainer: André Schwarz / ASGlobal

---

## 🚨 CLAUDE — BITTE IMMER ZUERST FRAGEN:

> *"Soll ich das per sed/python direkt im Repo fixen? Dauert 10 Sekunden."*

**Wann sed nutzen:** Kleine Fixes, Texttausch, einzelne Zeilen hinzufügen/löschen.
**Wann Download:** Große Umbauarbeiten mit vielen Änderungen (>10 Stellen).

---

## ⚡ Die 7 Magic Commands

### 1. Text ersetzen (einfachster Fall)
```bash
sed -i 's/ALT/NEU/g' datei.html
```
Beispiel: Farbe ändern, URL updaten, Wort ersetzen.

---

### 2. Zeile NACH einem Begriff einfügen
```bash
sed -i '/SUCHBEGRIFF/a NEUE ZEILE HIER' datei.html
```
Beispiel: Nach `</nav>` eine neue Zeile einfügen.

---

### 3. Zeile VOR einem Begriff einfügen
```bash
sed -i '/SUCHBEGRIFF/i NEUE ZEILE HIER' datei.html
```

---

### 4. Zeile löschen die Begriff enthält
```bash
sed -i '/UNERWÜNSCHTER BEGRIFF/d' datei.html
```

---

### 5. Mehrere Dateien gleichzeitig
```bash
sed -i 's/ALT/NEU/g' *.html
```
Oder gezielt:
```bash
for f in index.html willkommen.html checkin.html; do sed -i 's/ALT/NEU/g' $f; done
```

---

### 6. Python — für komplexe mehrzeilige Änderungen
```bash
python3 -c "
f=open('datei.html','r')
c=f.read()
f.close()
c=c.replace('ALTERTTEXT','NEUERTEXT')
f=open('datei.html','w')
f.write(c)
f.close()
print('ok')
"
```
**Wichtig:** Anführungszeichen im Text mit `\"` escapen.

---

### 7. Schnell etwas ans Ende hängen
```bash
echo '<script>/* neuer Code */</script>' >> datei.html
```

---

## 🔄 Nach jedem Fix — immer dieser Abschluss:
```bash
git add -A && git commit -m "fix via sed" && git push
```

---

## 📍 Pfade im Turmhotel-Repo (Referenz)

```bash
~/turmhotel/housekeeping/housekeeping-v3.html   # Housekeeping App
~/turmhotel/index.html                           # Gästeportal
~/turmhotel/willkommen.html                      # Willkommensbuch
~/turmhotel/checkin.html                         # Check-in Anleitung
```

---

## 💡 Typische Anwendungsfälle

| Was | Befehl |
|---|---|
| WhatsApp-Link ersetzen | `sed -i 's/PLATZHALTER_BITTE_ERSETZEN/chat.whatsapp.com\/XXXXX/g' *.html` |
| Farbe ändern | `sed -i 's/#2e6b4f/#1a5c3a/g' datei.html` |
| Bug in JS fixen | `python3 -c "..."` |
| Text in Nav ändern | `sed -i 's/Alter Titel/Neuer Titel/g' datei.html` |
| URL updaten | `sed -i 's/alter-link.html/neuer-link.html/g' *.html` |

---

## ⚠️ Vorsicht bei:
- Sonderzeichen wie `/` im Suchtext → anderes Trennzeichen nutzen: `sed -i 's|ALT|NEU|g'`
- Mehrzeiligen Blöcken → immer `python3` bevorzugen
- Vor riskanten Änderungen: `cp datei.html datei.backup.html`

