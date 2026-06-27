# 📸 Upload-Routine — Bilder &amp; Videos ins Repo (André / ASGlobal)

> **Zweck:** Standard-Ablauf, um Sneaker-Fotos (und kurze Videos) sauber ins
> GitHub-Repo zu bekommen und in Katalog/Galerie einzubinden. Damit es bei
> jeder Temperatur gleich einfach läuft. Gilt für Sneaks4seek und künftige Repos.

---

## Grundprinzip

- Bilder/Videos sind **Binärdateien** → immer über den Download-Ordner + `cp`,
  NIEMALS per Copy-Paste/`cat`.
- Medien kommen in einen eigenen Ordner **`bilder/`** im Repo (Übersicht).
- Dateinamen **klein, ohne Leerzeichen/Umlaute**: `nike-airmax90-43.jpg`,
  nicht `Nike Air Max (43).JPG`.
- Pro Sneaker idealerweise **1 Hauptbild** (+ optional Video).

---

## Schritt-für-Schritt

### 1. Medien vorbereiten (am Handy)
- Fotos/Videos in den **Download-Ordner** legen (oder per Claude-App laden).
- Faustregel Größe: Fotos < 1 MB, Videos < 10 MB (sonst Repo wird träge).

### 2. Bilder-Ordner anlegen (einmalig pro Repo)
```
cd ~/REPONAME && mkdir -p bilder && echo "bilder-Ordner bereit"
```

### 3. Medien aus Download holen (neueste Versionen)
> Namen an die jeweiligen Dateien anpassen.
```
cd ~/REPONAME && D=~/storage/downloads
for n in nike-airmax90-43 adidas-samba-42 jordan1-44; do
  f=$(ls -t "$D/$n"*.jpg "$D/$n"*.jpeg "$D/$n"*.png "$D/$n"*.webp 2>/dev/null | head -1)
  [ -n "$f" ] && cp "$f" "bilder/$n.${f##*.}" && echo "OK: $n <- $(basename "$f")"
done
```

### 4. Videos (optional, gleicher Weg)
```
cd ~/REPONAME && D=~/storage/downloads
for n in nike-airmax90-43-video; do
  f=$(ls -t "$D/$n"*.mp4 "$D/$n"*.webm 2>/dev/null | head -1)
  [ -n "$f" ] && cp "$f" "bilder/$n.${f##*.}" && echo "OK: $n <- $(basename "$f")"
done
```

### 5. Robo Bro baut sie ein
→ André schickt Robo Bro die Liste (Marke, Modell, Größe, Preis, Zustand +
   welcher Dateiname zu welchem Sneaker gehört).
→ Robo Bro ersetzt die Platzhalter-Karten im Katalog durch echte Karten mit
   `background-image:url('bilder/DATEINAME.jpg')`.

### 6. Hochladen
```
git add . && git commit -m "Sneaker-Bilder/Videos hinzugefuegt" && git push origin main
```

---

## Karten-Vorlage (zur Erinnerung, baut Robo Bro ein)

```html
<article class="card">
  <div class="card-img" style="background-image:url('bilder/nike-airmax90-43.jpg');background-size:cover;background-position:center"></div>
  <div class="card-body">
    <span class="status available">Verfügbar</span>
    <div class="brand">Nike</div>
    <h3>Air Max 90</h3>
    <div class="spec">Größe EU 43 · Zustand: Wie neu</div>
    <div class="price">€ 140</div>
    <a class="btn-wa" href="https://wa.me/491634692255?text=...">Anfragen</a>
  </div>
</article>
```

---

## ⚠️ Stolperfallen

1. **Großschreibung der URL:** GitHub Pages ist case-sensitive. Live-URL ist
   `Sneaks4seek` (großes S). Interne Links/Sitemap entsprechend schreiben.
2. **Leerzeichen/Umlaute im Dateinamen** → Bild lädt nicht. Immer klein + Bindestriche.
3. **Zu große Dateien** → Repo wird langsam. Vorher komprimieren.
4. **Marken-Logos:** Nur offizielle **Textbezeichnungen** verwenden
   (z. B. "Nike Air Max"). KEINE Logos/Swoosh einbinden (Markenrecht).
5. **Binär per cat** → kaputt. Immer Download-Ordner + `cp`.

---

*Erstellt von Robo Bro für André — Medien-Upload bei jeder Temperatur einfach. 📸👟*
