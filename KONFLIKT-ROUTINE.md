# KONFLIKT-ROUTINE — Git Push abgelehnt / Merge-Konflikte lösen

## Wann benutzen?
Wenn `git push` diese Fehlermeldung zeigt:
```
! [rejected]  main -> main (fetch first)
error: failed to push some refs
```

Ursache: Auf GitHub liegt ein Commit den du lokal nicht hast
(z.B. vom anderen Gerät gepusht oder per GitHub-Webeditor geändert).

---

## Standard-Lösung (kein Konflikt)

```bash
git pull --rebase origin main
git push
```

Fertig in 90% der Fälle.

---

## Wenn CONFLICT erscheint

```
CONFLICT (content): Merge conflict in [datei]
```

**Entscheidung: Welche Version gewinnt?**

### Fall A: MEINE lokale Version soll gewinnen (Standard bei frischen Claude-Dateien)
```bash
git checkout --theirs [datei]
git add [datei]
git rebase --continue
git push
```

⚠️ Bei rebase ist `--theirs` = DEINE lokale Änderung (verwirrend aber so ist git).

### Fall B: Die GitHub-Version soll gewinnen
```bash
git checkout --ours [datei]
git add [datei]
git rebase --continue
git push
```

---

## Wenn der Commit-Editor aufgeht (nano)

Es erscheint ein Textfenster mit der Commit-Message:
```
Ctrl+X → Y → Enter
```
Danach läuft der Rebase automatisch weiter.

---

## Notausgang — alles abbrechen und von vorn

```bash
git rebase --abort
```
Stellt den Zustand vor dem Pull wieder her. Nichts geht verloren.

---

## Merksatz
> Push abgelehnt? → `pull --rebase` → bei Konflikt `checkout --theirs` → `add` → `rebase --continue` → `push`

## Branch beachten!
- `telavendelele` → **master**
- alle anderen Repos → **main**
