# CURL-CHECK-ROUTINE — Live-Deployment ohne Browser verifizieren

## Wann benutzen?
Nach jedem `git push` — um zu prüfen ob GitHub Pages die Änderung
wirklich live geschaltet hat. Kein Browser nötig, direkt in Termux.

⏱ GitHub Pages braucht 1-2 Minuten nach dem Push. Nicht sofort checken.

---

## Content-Check — ist meine Änderung live?

```bash
curl -s https://intelligentresponder-max.github.io/[REPO]/[SEITE].html | grep -c "KEYWORD"
```

**Beispiel:**
```bash
curl -s https://intelligentresponder-max.github.io/bewerbung-copywriter/lebenslauf.html | grep -c "Front Office"
```

- Ergebnis `1` oder höher → ✅ Änderung ist live
- Ergebnis `0` → ⏳ warten und nochmal, oder Push prüfen

**WICHTIG:** Immer auf INHALT prüfen (ein Wort das NEU ist),
nie auf den Dateinamen. Der Dateiname ist immer gleich.

---

## Asset-Check — ist die Datei (Bild/PDF) erreichbar?

```bash
curl -s -o /dev/null -w "%{http_code}\n" https://intelligentresponder-max.github.io/[REPO]/[DATEI]
```

**Beispiel:**
```bash
curl -s -o /dev/null -w "%{http_code}\n" https://intelligentresponder-max.github.io/bewerbung-copywriter/andre_portrait.jpg
```

- `200` → ✅ Datei ist live und erreichbar
- `404` → ❌ Datei fehlt (Push vergessen? Dateiname falsch?)

---

## Mehrere Seiten in einem Rutsch

```bash
for s in index.html lebenslauf.html arbeitsprobe.html; do
  echo "$s: $(curl -s -o /dev/null -w '%{http_code}' https://intelligentresponder-max.github.io/bewerbung-copywriter/$s)"
done
```

---

## Merksatz
> Push → 2 Minuten warten → curl mit grep auf NEUES Keyword → Zahl ≥ 1 = live
