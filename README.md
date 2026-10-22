# Aventurier I

Petit jeu développé avec Python et Pygame. Le programme principal est `aventurier_1.py`.

## Prérequis

- Python 3
- `pip` (fourni avec la plupart des installations Python)

## Installation et lancement

Ouvrez un terminal dans le dossier du projet, celui qui contient `aventurier_1.py`, puis exécutez :

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install pygame
python aventurier_1.py
```

La fenêtre du jeu s’ouvre. Pour quitter, fermez la fenêtre ou utilisez son bouton de fermeture.

À chaque nouvelle session de terminal, activez de nouveau l’environnement virtuel avant de lancer le jeu :

```bash
source .venv/bin/activate
python aventurier_1.py
```

Sur Windows, les commandes équivalentes d’activation et de lancement sont :

```powershell
.venv\Scripts\Activate.ps1
python aventurier_1.py
```

## Commandes

- `D` : avancer
- `A`, `Z` ou `E` : attaquer
- `Espace` : sauter

## Fichiers du jeu

Lancez le script depuis le dossier du projet et gardez les dossiers `Background/`, `Images/`, `Musics/`, `Sounds/` et `Sprites/`, ainsi que `animated_sprites.py`, à leur emplacement. Le jeu utilise ces chemins relatifs pour charger ses images, animations et sons.
