# MAGIX-ROUTINE — Bilder mit Glow-Effekt bearbeiten (magix.py)

## Was macht das Tool?
Waehlt eine Farbe im Bild aus (z.B. weisse Sox/Sneaker) und laesst
sie leuchten: Volt, Gold, Cyan, Pink usw. Hintergrund wird abgedunkelt.
Ergebnis: magic-bild.jpg

## Einmalig einrichten
pip install pillow numpy --break-system-packages

## Nutzung (interaktiv)
cd ~/tools
python magix.py ~/storage/downloads/foto.jpg

Das Tool fragt:
1. Welche Farbe soll leuchten? (weiss/schwarz/rot/blau/gruen/gelb)
2. Welche Glow-Farbe? (volt/gold/cyan/pink/weiss/rot/gruen)

## Nutzung (ohne Fragen)
python magix.py foto.jpg --farbe weiss --glow volt

## Mehrere Bilder auf einmal
python magix.py *.jpg

## Ausgabe
magic-foto.jpg (im selben Ordner wie das Original)

## Merksatz
pip install pillow numpy — python magix.py bild.jpg — fertig.
