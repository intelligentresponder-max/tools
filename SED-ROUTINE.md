# SED-ROUTINE — Dateien direkt in Termux aendern (KEIN Download)

## Die Goldene Regel
Text-Dateien (HTML, MD, CSS, JS) werden NIE mehr per Download geaendert.
Claude gibt einen sed-Befehl, André fuehrt ihn aus, dann git push. Fertig.
Download nur noch fuer Binaerdateien: Bilder, PDFs, Videos.

## Standard-Ablauf
1. Claude prueft erst den Ist-Zustand:
   grep -n "SUCHTEXT" ~/repo/datei.html
2. Claude gibt den sed-Befehl:
   sed -i 's/ALTER TEXT/NEUER TEXT/' ~/repo/datei.html
3. Verifizieren:
   grep -n "NEUER TEXT" ~/repo/datei.html
4. Push:
   cd ~/repo && git add datei.html && git commit -m "Fix: ..." && git push

## Regeln fuer Claude beim sed-Bauen
- Vorher IMMER mit grep pruefen ob der Suchtext exakt 1x vorkommt
- Schraegstriche im Text? Anderes Trennzeichen nehmen: sed -i 's|alt/pfad|neu/pfad|'
- Sonderzeichen & wird zu \& im Ersatztext
- Einfache Anfuehrungszeichen im Text? Doppelte aussen nutzen: sed -i "s/dont/do not/"
- Bei langen Texten: nur einen eindeutigen KURZEN Teil ersetzen, nicht den ganzen Absatz
- Mehrzeilige Aenderungen: lieber 2-3 einzelne sed-Befehle als ein komplexer
- Bei grossen Umbauten (ganze Sektionen): python3 heredoc statt sed

## Neue Datei anlegen ohne Download
cat > ~/repo/datei.md << 'ENDE'
Inhalt hier
ENDE

## KRITISCH: Keine Codebloecke in Befehlen
Wenn Claude einen cat-Heredoc-Befehl gibt, darf der Inhalt KEINE
dreifachen Backticks enthalten - die zerbrechen den Chat-Codeblock
und der Befehl kommt unvollstaendig in Termux an.
Stattdessen: Code im Inhalt einruecken (4 Leerzeichen).

## Merksatz
grep pruefen, sed aendern, grep verifizieren, push. Kein Download.
