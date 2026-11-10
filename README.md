# Adventurer I

Small game developed with Python and Pygame. The main program is `aventurier_1.py`.

## Prerequisites

- Python 3
- `pip` (provided with most Python installations)

## Installation and launch

Open a terminal in the project directory, the one containing `aventurier_1.py`, then run:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install pygame
python aventurier_1.py
```

The game window opens. To quit, close the window or use its close button.

At each new terminal session, activate the virtual environment again before launching the game:

```bash
source .venv/bin/activate
python aventurier_1.py
```

On Windows, the equivalent activation and launch commands are:

```powershell
.venv\Scripts\Activate.ps1
python aventurier_1.py
```

## Controls

- `D` : avancer
- `A`, `Z` ou `E` : attaquer
- `Espace` : sauter

## Game Files

Launch the script from the project directory and keep the folders `Background/`, `Images/`, `Musics/`, `Sounds/` and `Sprites/`, as well as `animated_sprites.py`, in their location. The game uses these relative paths to load its images, animations, and sounds.
