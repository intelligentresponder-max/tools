# DATEINAME-ROUTINE — Nummerierte Duplikate & Prefix-Kollisionen vermeiden

## Problem 1: Android nummeriert Downloads hoch

Wenn `index.html` schon in Downloads liegt und du lädst nochmal
runter, entsteht `index(1).html`, dann `index(2).html` usw.
→ `grab` nimmt dann evtl. die ALTE Datei!

### Lösung A: Vor jedem Download aufräumen
```bash
rm ~/storage/downloads/[BASENAME]*.html 2>/dev/null
echo "Downloads sauber für [BASENAME]"
```

**Beispiel:**
```bash
rm ~/storage/downloads/index*.html 2>/dev/null
rm ~/storage/downloads/lebenslauf*.html 2>/dev/null
```

### Lösung B: Goldene Regel — immer die NEUESTE nehmen
```bash
D=~/storage/downloads
neueste=$(ls -t "$D/index"*.html 2>/dev/null | head -1)
echo "Neueste: $neueste"
cp "$neueste" index.html
echo "OK: index.html <- $neueste"
```

`ls -t` sortiert nach Zeit, `head -1` nimmt die jüngste.
Funktioniert auch mit `index(3).html`.

---

## Problem 2: Prefix-Kollisionen

`whatsapp-katalog.png` und `whatsapp-katalog-de.png` —
das Muster `whatsapp-katalog*` trifft BEIDE!

### Lösung: Suffix-Guard mit grep -v
```bash
# Nur die Datei OHNE -de Suffix:
ls -t "$D/whatsapp-katalog"*.png | grep -v -- '-de' | head -1

# Nur die MIT -de:
ls -t "$D/whatsapp-katalog-de"*.png | head -1
```

Das `--` nach grep -v ist wichtig, sonst denkt grep `-de` sei eine Option.

---

## Problem 3: grab nimmt nur EINE Datei

`grab a.html b.html c.html` → nur `a.html` wird kopiert!

### Lösung: Immer einzeln
```bash
grab index.html
grab lebenslauf.html
grab arbeitsprobe.html
```

---

## Vor jedem Push: Bestätigung

```bash
echo "OK: [DATEI] <- [QUELLE]"
```
Immer diese Zeile ausgeben bevor gepusht wird — dann ist klar
welche Datei wirklich kopiert wurde.

---

## Merksatz
> Erst aufräumen (`rm basename*`), dann laden, dann `ls -t | head -1`,
> dann `echo OK`, dann pushen. grab immer einzeln.
