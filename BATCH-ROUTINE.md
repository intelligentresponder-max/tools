# BATCH-ROUTINE — Änderungen sammeln, einmal pushen

## Grundregel

**Nicht nach jeder Kleinigkeit deployen!**

Änderungen sammeln (bis ~7 Stück), alle auf einmal umsetzen,
EIN einziger Push. Das spart:
- Zeit (GitHub Pages deployed nur 1x statt 7x)
- Nerven (weniger grab/push-Zyklen)
- Konflikt-Risiko (weniger Pushes = weniger rejected)

---

## Workflow

### 1. Sammeln
Änderungswünsche notieren — im Chat oder als Liste:
```
1. Titel ändern auf X
2. Foto einbauen
3. Satz Y löschen
4. Keywords ergänzen
5. Nav-Link fixen
```

### 2. Alle auf einmal umsetzen lassen
Claude implementiert ALLE Punkte in die Datei(en) —
eine fertige Datei pro Seite, nicht 5 Patches.

### 3. Ein Push für alles
```bash
cd ~/[REPO]
grab [datei1].html
grab [datei2].html
git add [datei1].html [datei2].html
git commit -m "Batch: Titel, Foto, Fix Nav, Keywords, Cleanup"
git push
```

### 4. Ein curl-Check am Ende
```bash
curl -s https://intelligentresponder-max.github.io/[REPO]/[SEITE].html | grep -c "NEUES_KEYWORD"
```

---

## Wann NICHT batchen?

- Kritischer Fix der sofort live muss (z.B. falsche Telefonnummer)
- Wenn eine Änderung erst getestet werden muss bevor die nächste Sinn ergibt

---

## Für Claude / KI-Agenten

Wenn André mehrere Wünsche nacheinander äußert:
→ NICHT nach jedem einzelnen eine Datei liefern.
→ Fragen ob noch mehr kommt, oder sammeln bis er "fertig" sagt.
→ Dann ALLE Änderungen in einem Rutsch in die Datei(en) einbauen.

## Merksatz
> Sammeln → alles einbauen → ein grab pro Datei → ein Push → ein Check.
