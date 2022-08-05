PROJECT GOALS AND MOTIVATION

The content of the folder "game123" implements a 2D Jump & Run style game
in which you play as a dinosaur against an intelligent (guided search using the A star search algorithm), evil pigeon that will hunt the player. After the game, the player can compare his or her score against the scores of his predecessors that have been saved in the scoreboard.csv file and will now be plotted.

The goal of the game is to collect all butterflies, evade the pigeon, or shoot it with your fireballs,
and then reach the goal flag. The goal flag will only unlock, once you have collected all butterflies by running into them. If the evil pigeon catches the dinosaur, you loose the game. You will also get points for collecting butterflies, shooting pigeons and reaching the goal. These points will be the score.

The level consists of a 2D space with platforms on which the player can jump and run. 

Once the game is lost or won the user will get a dialog window that prompts to input your name. This name will then be saved - together with the scores of the player - into the scoreboard.csv
The data in the scoreboard.csv can then (in theory) be used to plot the players scores and name against that of the highest achieved score.

DISCLAIMER:

Unfortunately, we had great trouble with making pygame, numpy, python and matplotlib work together. This has likely to do with the fact, that the newst pygame version is quite old and it comes with its own numpy version. In theory, after the game is finished, a plot will show up with scores. However that code that implements the plotting is commented out. You will see this in the Plot.py file and at the end of the main.py file. This way you still can expierence the game in action, just without the plots. The plotting code is still there, and since we tested in different environments, should plot accordingly.

GAME INSTRUCTIONS

You have to possible control schemas to control the dinosaur. Use either WASD or the arrow keys to move and jump. You can determine the control schema, once you start the game. Either press W or ARROW UP in the start screen. 

Once in the game you can use SPACRE_BAR to shoot fireballs.
Pick up butterflies by moving into them. Same goes for the goal flag.

PROJECT STRUCTURE

The main.py file contains the game logic and the main game loop. This is where all objects of the other classes are instantiated. This is the file you will have to run, to start the game.

The helper.py file contains many helper variables and helper functions that would otherwise clutter up the main.py file. These variables and functions are used throughout many of the other files and classes.
Most prominently, this is where the A Star seach algorithm is implemented. This algorithm is used by the Enemy class (the pigeon) to determine the shortest path to the player and chase him.

// Object classes

The Environment.py is used to instantiate a game environment instance, it manages the objects in the game and the interaction between them.

The Player.py is used to instantiate the player character - the dinosaur. It also handels some of the player inputs (left and right movement)

The Enemy.py is used to instantiate the enemy character - the pigeon.

The Butterfly.py is used to instantiate the butterflies that can be collected by the player.

The Fireball.py is used to instantiate the fireballs that can be shot by the player using the spacebar. Use these fireballs to keep the pigeon off you back!

The Goal.py is used to instatiate the goal flag that must be reached to win the game. However, it will only be reachable once all butterflies have been collected!

The Platform.py is used to instantiate the platfroms that the player can jump on. They cannot be moved through by the player. However, the pigeon will fly over them.

The Grid.py is used to instatiate the grid. This grid is layed over the playing field and seperates it into grid nodes. This is mostly used for setting up the playing field and for determining the search space of the A star algorithm, since the x,y coordinates of the screen would provide a search space way to big. Through the grid the performance is increased greatly. Every object in the game will have a grid position in addition to its x,y position on the screen.

The Plot.py is used to (in theory) plot the players score in bar plots and compare it with the highest score in the scoreboard.csv


PROJECT REQUIREMENTS

To get the pygame package you will need python 3.5, get this with

    $ conda install -c python=3.5

To run the game you will need pygame, get this with:

    $ conda install -c cogsci pygame

You will also need tkinter for the user dialog window, get this with:

    $conda install -c anaconda tk

As stated above, to run the plots you will also need numpy and matplotlib. However it will be hard / impossible to find versions that dont fail / conflict with pygame, since this comes with its own numpy.



