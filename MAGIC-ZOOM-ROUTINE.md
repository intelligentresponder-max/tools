# MAGIC-ZOOM-ROUTINE — Glow + Ken-Burns Video (magic_zoom.py)

## Was macht das Tool?
Wie magix.py PLUS: erstellt ein 9:16 Reels-Video (4 Sek) mit
sanftem Zoom-Effekt auf die leuchtende Stelle. Ideal fuer Instagram/TikTok.

## Zusaetzlich einrichten (einmalig)
pkg install ffmpeg

## Nutzung (interaktiv)
cd ~/tools
python magic_zoom.py ~/storage/downloads/foto.jpg

Fragt zusaetzlich zu magix.py:
3. Wohin zoomen? (auto/mitte/oben/unten/links/rechts)
4. Zoom-Modus? (inout/in/out)

auto = zoomt auf hellste Glow-Stelle = meist der Sneaker/Swoosh

## Nutzung (ohne Fragen)
python magic_zoom.py foto.jpg --farbe weiss --glow volt --fokus auto --modus inout

## Ausgabe
magic-foto.jpg (Standbild)
zoom-foto.mp4 (9:16 Video)

## Parallax-Modus (2.5D Effekt)
python magic_zoom.py foto.jpg --modus parallax

## Merksatz
magic_zoom.py = magix.py + Video. ffmpeg noetig. auto-Fokus findet Sneaker.
