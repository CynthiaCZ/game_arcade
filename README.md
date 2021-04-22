# CLPS0950 final project

## Project Introduction
* This project uses pygame to build a collection of minigames
* The main world is an arcade where the user can choose from games including:
  * Crossing road
  * Snake
  * Rhythm
  * Tetris

## Required python packages
##### These need to be installed for the programs to run
* Pygame/2.0.1
* Pillow/8.2.0

## How to Play
* Once pygame and pillow are installed, it will be necessary to download/pull **all files** in this repository into a single folder for the programs to function. 
* The main world is the file named mainworld_w_animation.py, and this is the main (base) world where you can move your sprite around to choose the various games. Moving your sprite to one of the game blocks will begin that specific game. 
* mainworld_w_animation.py calls the other games which are defined as functions in the separate files crossingroad.py, rhythm_game.py, tetris.py, and snake.py. These files can be used to play each game individually, but it will be necessary to **remove the function call** at the beginning of each of these files to actually have the pygame window open up to play the game. 
