# RENAME-ROUTINE.md

**Zweck:** Heruntergeladene Dateien aus dem Android-Downloads-Ordner sauber
ins Repo bringen — ohne `index (1).html`, `bild(2).webp` & Co. von Hand zu fixen.

Drei Funktionen: **`clean`** (alte Versionen loeschen), **`grab`** (neueste holen),
**`deploy`** (grab + git push in einem).

Funktioniert universell fuer **jede** Datei: HTML, PNG, WEBP, JPG, MP4, PDF, CSS, JS …

---

## EINMAL einrichten (Setup)

Diesen Block **einmal** in Termux einfuegen:

```bash
cat >> ~/.bashrc << 'ROUTINE'

# === ASGlobal Rename-Routine ===
D=~/storage/downloads

# clean <datei> — loescht ALLE alten Versionen aus Downloads (vor dem Download)
clean(){
  local t="$1"; [ -z "$t" ] && { echo "Nutzung: clean <datei>"; return 1; }
  local base="${t%.*}" ext="${t##*.}"
  local n=$(ls "$D/$base"*."$ext" 2>/dev/null | wc -l)
  [ "$n" = "0" ] && { echo "Nichts zu loeschen ($base*.$ext)"; return 0; }
  rm -f "$D/$base"*."$ext" && echo "Geloescht: $n alte $base-Datei(en)"
}

# grab <ziel> — holt die NEUESTE passende Datei aus Downloads ins aktuelle Repo
grab(){
  local target="$1"; [ -z "$target" ] && { echo "Nutzung: grab <datei>"; return 1; }
  local base="${target%.*}" ext="${target##*.}"
  local f=$(ls -t "$D/$base"*."$ext" 2>/dev/null | head -1)
  [ -z "$f" ] && { echo "FEHLER: keine $base*.$ext in Downloads"; return 1; }
  cp "$f" "./$target" && echo "OK: $target  <-  $(basename "$f")"
}

# deploy <datei1> [datei2 ...] — grab + git add/commit/push in einem
deploy(){
  [ -z "$1" ] && { echo "Nutzung: deploy <datei> [weitere ...]"; return 1; }
  for t in "$@"; do grab "$t" || return 1; done
  git add "$@" && git commit -m "update: $*" && git push
}
# === Ende Routine ===
ROUTINE
source ~/.bashrc
echo "Routine aktiv: clean, grab, deploy"
```

---

## DER SAUBERE WORKFLOW (empfohlen)

Damit nie wieder eine falsche `-1`-Version reinrutscht:

**1. VOR dem Download** alte Versionen wegraeumen:
```bash
clean sox.html
```

**2. DANN** die Datei aus der Claude-App runterladen.
Weil Downloads jetzt leer ist, kommt sie garantiert **ohne** `(1)`-Zaehler an.

**3. Ins Repo + live:**
```bash
cd ~/sneaks4seek && deploy sox.html
```

---

## clean — warum das der Schluessel ist

Das `-1`-Problem entsteht **nur**, weil Android beim erneuten Download eine
Datei nicht ueberschreibt, sondern `datei (1).html` anlegt. `grab` nimmt zwar
immer die zeitlich neueste — aber wenn du sichergehen willst, dass es **gar
keine** Verwechslung gibt, loeschst du vorher mit `clean` alle alten Versionen.

Dann liegt nach dem Download **genau eine** Datei da. Kein Zaehler, kein Raetsel.

---

## BEFEHLE im Detail

### Eine Datei deployen (haeufigster Fall)
```bash
cd ~/sneaks4seek
clean sox.html      # vorher saubermachen
# ... sox.html runterladen ...
deploy sox.html
```

### Mehrere Dateien auf einmal
```bash
clean a.html; clean b.html; clean c.html
# ... alle runterladen ...
deploy a.html b.html c.html
```

### Nur kopieren, NICHT pushen
```bash
grab katalog.html
```

### Bilder & Videos gehen genauso
```bash
clean combo.mp4
deploy combo.mp4
```

---

## Wichtig

- **Branch:** `git push` nutzt automatisch den richtigen Branch.
  Bei "rejected" → erst `git pull --no-edit && git push`
  (einmalig vorher: `git config --global pull.rebase false`)
- **Login:** Beim Push fragt Termux nach Username + Token (PAT). Das gibst nur du ein.
- **Ordnernamen klein:** Repos liegen lokal klein, z.B. `~/sneaks4seek`.
  Die Live-URL bleibt trotzdem mit grossem S — das ist normal.
- **Prefix-Falle:** Wenn `bild.png` und `bild-de.png` existieren, gezielt:
  `grab bild-de.png` greift nur die `-de`-Variante.

---

## Spickzettel

| Was | Befehl |
|---|---|
| Alte Versionen loeschen | `clean datei.html` |
| Eine Datei live | `deploy datei.html` |
| Mehrere live | `deploy a.html b.html` |
| Nur reinkopieren | `grab datei.html` |
| Push abgelehnt? | `git pull --no-edit && git push` |
