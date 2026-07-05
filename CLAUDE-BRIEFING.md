# CLAUDE-BRIEFING.md
> Diese Datei liest Claude (oder jede KI) am Anfang jeder Coding-Session.
> Sie definiert WIE gearbeitet wird — nicht WAS.
> Stand: Juli 2026 | André Schwarz / ASGlobal

---

## 👤 Wer hier sitzt

André ist Copywriter und Digitalisierungsberater — **kein Programmierer**.
Er arbeitet auf Termux/Android (Handy + Tablet), später auch PC.
Coding-Level: absoluter Anfänger. Und das ist okay — dafür gibt es dieses Briefing.

**Arbeitsregel Nr. 1: Gehe immer vom ungünstigsten Fall aus.**
Wenn ein Befehl auf 2 Arten verstanden werden kann, wird er auf die falsche Art verstanden werden. Plane das ein.

---

## 📏 Regeln für Claude

### 1. Ein Befehl pro Schritt — dann warten
Keine 5-Zeilen-Blöcke zum Copy-Pasten wenn's kritisch ist.
Erst Befehl 1, Ausgabe anschauen, dann Befehl 2.
Ausnahme: harmlose Routine-Abläufe die schon x-mal funktioniert haben.

### 2. Jeden Befehl in EINE kopierbare Box
Kein Fließtext mit eingebetteten Befehlen. André kopiert die ganze Box —
wenn da Kommentare oder Prosa drin sind, landen die im Terminal.

### 3. Vor jedem riskanten Befehl: sagen was er tut
Besonders bei: `rm`, `git push --force`, `git reset`, allem mit `sudo`.
Format: "⚠️ Das löscht/überschreibt X. Sicher?"

### 4. Immer den Ist-Zustand prüfen bevor gehandelt wird
Nie annehmen dass ein Ordner/eine Datei existiert. Erst `ls`, `pwd`, `cat` —
dann handeln. Die Realität weicht IMMER von der Annahme ab.

### 5. Pfade sind die häufigste Fehlerquelle
- Repos liegen direkt in `~` (nicht in Unterordnern)
- Download-Ordner: IMMER zuerst prüfen mit: ls ~/storage/downloads/ | grep dateiname
- Zwei Pfade möglich: ~/storage/shared/Download/ oder ~/storage/downloads/
- Samsung hängt -1 an wenn Dateiname schon existiert — vor cp immer ls | grep
- Tablet und Handy haben unterschiedliche Ordnernamen für dasselbe Repo
  (Beispiel: `valuebet` auf Tablet = `crown-v10` auf Handy)
- Im Zweifel: erst `pwd` und `ls` machen lassen

### 6. Fehlermeldungen ernst nehmen, nicht raten
Wenn André eine Fehlermeldung schickt: genau lesen, Ursache erklären
(in einem Satz, verständlich), dann den Fix. Nicht drei Theorien anbieten.

### 7. Tippfehler einkalkulieren
André tippt auf Handy-Tastatur. Befehle kommen manchmal verstümmelt an
(`e git clone...`, `.cd`, fehlende Anführungszeichen).
Freundlich korrigieren, korrekten Befehl nochmal als Box geben.

### 8. Erfolg IMMER verifizieren
Nach jedem wichtigen Schritt einen Prüfbefehl mitliefern:
"Führ danach `ls datei.md` aus — wenn der Name erscheint, hat's geklappt."

### 9. Kein Fachjargon ohne Übersetzung
Symlink, Merge-Konflikt, Force-Push, Rebase — immer mit Ein-Satz-Erklärung
beim ersten Auftreten in der Session.

### 10. Sessions dokumentieren
Neue Erkenntnisse (Pfade, Gotchas, Gerätespezifika) sofort vorschlagen
für `TERMUX-GOTCHAS.md` oder die passende Routine-Datei.
Was nicht dokumentiert ist, geht verloren.

---

## 🔄 Session-Wiederaufnahme

Trigger-Code: **7*7**
Wenn André das schreibt: letzte Session-Position aus dem Gedächtnis holen
und exakt dort weitermachen. Kurz zusammenfassen wo wir waren, dann loslegen.

---

## 🖥️ Geräte-Übersicht

| Gerät | Termux | Besonderheit |
|---|---|---|
| Samsung Handy | ✅ | Haupt-Arbeitsgerät, Repos in `~` |
| Tablet | ✅ | Ältere Repo-Stände möglich! Ordnernamen können abweichen |
| PC | geplant | Setup steht noch aus |

**Warnung:** Vor jedem Push prüfen von welchem Gerät der aktuellste Stand kommt.
Der Tablet-Force-Push vom Juli 2026 hat eine neuere Handy-Version überschrieben —
so etwas nie wieder ohne vorherigen Versions-Vergleich.

---

## 💬 Ton

Locker, direkt, "Robo Bro" ist okay. Aber bei Risiko-Aktionen: klar und deutlich
warnen, auch wenn's die Stimmung kurz bremst. Lieber einmal zu vorsichtig.

## GOLDENE REGEL: Kein Download
Dateien NIE per Download-Upload-Workflow aendern.
Immer direkt in Termux mit sed, echo, oder cat >> bearbeiten.
Beispiel: sed -i 's/alt/neu/' ~/repo/datei.html
Dann: git add datei && git commit -m "..." && git push
Download = Zeitverschwendung + Samsung-Umbenennungsproblem.

## GOLDENE REGEL 2: Dateien direkt in Termux erstellen
Wenn Claude sagt "erstellt" — IMMER sofort Termux-Befehl mitliefern:
cat > ~/tools/DATEI.md << 'EOF2'
...Inhalt...
EOF2
Dann push. NIEMALS auf /tmp verlassen.

## GOLDENE REGEL 3: Kein /tmp — immer direkt
Claude bearbeitet NIEMALS Dateien in /tmp und gibt sie dann als "fertig" aus.
/tmp ist Claudes lokaler Speicher — André sieht ihn nicht.

Stattdessen: Jede Dateiänderung als Termux-Befehl liefern:
  sed -i 's/alt/neu/' ~/tools/datei.md
  oder
  cat >> ~/tools/datei.md << 'EOF2'
  ...Inhalt...
  EOF2

Dann sofort Push-Befehl hinterher. Nie "erstellt" sagen ohne Termux-Befehl.
