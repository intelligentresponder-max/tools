# Geraet-Routine: Wo bin ich gerade?

Claude fragt beim Start IMMER zuerst:
1. Handy, Tablet oder PC?
2. Welches Repo bearbeiten wir?
3. Ist das Repo auf diesem Geraet geklont?

## Repo noch nicht da?
git clone https://github.com/intelligentresponder-max/REPO.git ~/REPO

## Termux Speicherzugriff
termux-setup-storage

## Git Email einmalig setzen
git config --global user.email "intelligentresponder-max@users.noreply.github.com"

## Vor jedem Push
git pull --rebase && git push

## Push rejected
git stash && git pull --rebase && git stash pop && git add . && git commit -m "msg" && git push

## Unstaged Changes
git stash && git pull --rebase && git stash pop

## Jekyll deaktivieren (einmalig pro Repo)
touch .nojekyll && git add .nojekyll && git commit -m "Jekyll deaktivieren" && git push

## Build schlaegt fehl?
github.com/intelligentresponder-max/REPO/actions
Rotes X = Build-Log lesen. "Deployment failed, try again later" = GitHub-Fehler, warten + nochmal pushen.

## Google Search Console
1. HTML-Datei runterladen
2. cp /storage/emulated/0/Download/google*.html ~/REPO/
3. git add . && git commit -m "Google Verifizierung" && git push
4. 5 Min warten, VERIFY druecken
5. Datei NIE loeschen!

## Sicherheit
Interne Docs nie im oeffentlichen Repo: git rm --cached DATEINAME
