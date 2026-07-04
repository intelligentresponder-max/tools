# 🤖 Deploy-Routine für Repo-Coding (André / ASGlobal)

> **Zweck:** Diese Anleitung gibt André jedem Coding-Agenten an den Anfang.
> Sie sorgt dafür, dass Datei-Uploads aufs GitHub-Repo **immer gleich einfach**
> und **fehlerfrei** ablaufen — auch bei 41 Grad und leerem Kopf.

---

## 📋 Kontext für den Agenten (immer mitgeben)

- **Gerät:** Android + Termux. André ist Coding-Anfänger.
- **Befehle:** minimal, einfach, Schritt für Schritt. Immer kopierfertig in einem Block.
- **André kann NICHT:** Dateien von Hand verschieben oder umbenennen.
- **André KANN:** Dateien per Claude-App in den Ordner `Download` herunterladen,
  dann Befehle in Termux einfügen.
- **Push:** läuft über gespeichertes GitHub-Token (kein Passwort nötig).
- **Branch:** Repos nutzen oft `master` (NICHT `main`) — vorher mit
  `git branch` prüfen!

---

## 🔑 Die goldene Regel: IMMER die neueste Datei holen

Die Claude-App lädt neue Versionen als `name-1.html`, `name(2).html` usw. ab.
Ein simples `cp name.html .` würde die **falsche, alte** Version erwischen.
Deshalb IMMER mit `ls -t ... | head -1` die **zuletzt geänderte** Version nehmen
und mit `echo "OK ..."` zur Kontrolle anzeigen, welche Quelle genommen wurde.

---

## 🚀 Standard-Ablauf (5 Schritte)

### Schritt 0 — Einmalig (nur falls Speicher-Zugriff noch nie eingerichtet)
```
termux-setup-storage
```

### Schritt 1 — Ins Repo wechseln & aktuellen Stand holen
```
cd ~/REPONAME && git pull origin master
```

### Schritt 2 — Neueste Dateien aus Download holen
> Der Agent passt die Datei-Namen in den `for`-Schleifen an die jeweilige Aufgabe an.
```
cd ~/REPONAME && D=~/storage/downloads
# HTML-Dateien:
for base in DATEI1 DATEI2; do
  f=$(ls -t "$D/$base"*.html 2>/dev/null | head -1)
  [ -n "$f" ] && cp "$f" "./$base.html" && echo "OK: $base.html <- $(basename "$f")"
done
# Bilder (png):
for img in BILD1 BILD2; do
  f=$(ls -t "$D/$img"*.png 2>/dev/null | head -1)
  [ -n "$f" ] && cp "$f" "./$img.png" && echo "OK: $img.png <- $(basename "$f")"
done
# Einzeldateien (Beispiel sitemap):
f=$(ls -t "$D/sitemap"*.xml 2>/dev/null | head -1)
[ -n "$f" ] && cp "$f" ./sitemap.xml && echo "OK: sitemap.xml <- $(basename "$f")"
```

### Schritt 3 — Inhalt prüfen (vor dem Push!)
> Der Agent baut pro Aufgabe einen kurzen `grep -c`-Check mit einem klaren
> Soll-Wert. WICHTIG: nach dem TEXT suchen, der wirklich in der Datei steht
> (nicht nach `name.html`, wenn der nur 1× vorkommt — sonst Fehlalarm!).
```
grep -c "SUCHBEGRIFF" DATEI.html   # erwarteter Wert: X
```

### Schritt 4 — Hochladen (commit + push)
```
git add . && git commit -m "BESCHREIBUNG" && git push origin master
```

### Schritt 5 — Testen
> 1–2 Minuten warten, dann Live-URL im Browser neu laden (Cache leeren).

---

## ✅ Checkliste für den Agenten (vor "fertig")

- [ ] Branch geprüft (`master` vs `main`)?
- [ ] Repo VOR dem Bauen frisch geklont/gepullt (aktueller Stand)?
- [ ] `ls -t | head -1` für JEDE Datei genutzt (neueste Version)?
- [ ] `echo "OK <- ..."` zeigt, welche Quelldatei genommen wurde?
- [ ] Prüf-`grep` sucht nach echtem Datei-INHALT, nicht nach `.html`-Endung?
- [ ] Bei gemeinsamen Präfixen (`name` / `name-de`) das kürzere mit `grep -v -- '-suffix'` abgesichert?
- [ ] Soll-Wert beim Prüf-`grep` klar genannt?
- [ ] Alle Befehle in EINEM kopierfertigen Block?
- [ ] Mehrsprachige/SEO-Dateien (sitemap, robots) mitgedacht?

---

## ⚠️ Stolperfallen (aus Erfahrung)

1. **Falsche Datei-Version** → langwierige Fehlersuche.
   Lösung: immer `ls -t | head -1`.
2. **`grep`-Fehlalarm** → nach `.html`-Endung gesucht, die nur 1× vorkommt.
   Lösung: nach Inhalts-Stichwort suchen (z.B. Name, Slogan).
3. **`main` statt `master`** → Push schlägt fehl.
   Lösung: `git branch` checken.
4. **Binärdateien (PDF/PNG)** lassen sich NICHT per `cat`/Copy-Paste einfügen.
   Lösung: immer über Download-Ordner + `cp`.
5. **Riesige `cat`-Blöcke** (>5000 Zeichen) sind am Handy unzumutbar.
   Lösung: Download-Methode statt Inline-`cat`.
6. **Präfix-Überschneidung bei Dateinamen** (⚠️ NEU, real passiert!)
   `ls -t "whatsapp-katalog"*.png` greift AUCH `whatsapp-katalog-de.png`,
   weil das Sternchen alles nach dem Präfix matcht. Folge: die kürzer
   benannte Datei (z.B. die italienische) wird mit der längeren (`-de`)
   überschrieben.
   **Lösung A** — Suffix gezielt ausschließen:
   ```
   f=$(ls -t "$D/whatsapp-katalog"*.png | grep -v -- '-de' | head -1)
   ```
   **Lösung B** — exakten Namen matchen statt Wildcard, wenn keine
   Versionsnummern erwartet werden:
   ```
   f=$(ls -t "$D/whatsapp-katalog".png "$D/whatsapp-katalog"\(*\).png 2>/dev/null | head -1)
   ```
   **Merkregel:** Wenn zwei Dateien dasselbe Präfix teilen (`name` und
   `name-de`, `index` und `index2`), IMMER das kürzere mit `grep -v`
   gegen das längere Suffix absichern.

---

*Erstellt von Robo Bro für André — damit Repo-Deploys bei jeder Temperatur einfach bleiben. 🥤*

---
## Learnings 04.07.2026

### Jekyll immer von Anfang an deaktivieren
touch .nojekyll && git add .nojekyll && git commit -m 'Jekyll deaktivieren' && git push

### Build-Fehler debuggen
Neue Dateien geben 404 aber alte Seite läuft? Actions-Tab checken:
github.com/intelligentresponder-max/REPO/actions
Rotes X = Build fehlgeschlagen, Fehlermeldung anklicken und lesen.
'Deployment failed, try again later' = GitHub-Fehler, kein Code-Fehler. Einfach warten + nochmal pushen.

### Google Search Console Verifizierung
1. HTML-Datei runterladen
2. cp /storage/emulated/0/Download/google*.html ~/REPO/
3. git add . && git commit -m 'Google Verifizierung' && git push
4. 3-5 Min warten, dann VERIFY druecken
5. Datei NIE loeschen - sonst verliert man die Verifizierung

### Sicherheit
Interne Docs nie im oeffentlichen Repo lassen. .gitignore nutzen oder: git rm --cached DATEINAME

### Push rejected - fetch first
Fehler: 'Updates were rejected because the remote contains work you do not have locally'
Loesung: immer erst pullen, dann pushen:
git pull --rebase && git push
Laeuft durch ohne Fehler? Fertig. Kommt CONFLICT? Stopp und Hilfe holen.
