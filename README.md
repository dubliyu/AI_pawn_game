# Pawn Game

## Authors
- Carlos Leon
- Mary Wilson

## Description
The pawn game consists of a 3 x 5 chess grid in which both the black and the white player have 3 pawns.
A pawn, like in chess, can only move forward and attack an enemy pawn if its one space diagnol to itself.
We have written a program that recreated the game in the command line in python.
There are two players, the user and the computer. The user is controlled through command line input.
The computer is controlled through a MiniMax algorithm. The AI will generally win.

***

## Playing
##### To run the game
```python
python game.py
```

##### Choose player
The first player is always the white player. You can control if the computer will go first or not.
If the computer goes firsts, then the computer is white and the user are black.
Otherwise, the user is white and the computer is black. A 'y' for yes or 'no' will respond.

##### Making a move
The computer will make their move automatically, but the user can enter their input.
A move requires a from location and a to location seperated by a space.
A location is one of the three columns [A, B, C] and one of the five rows [1, 2, 3, 4, 5]
For example some moves are:
- A5 A4
- B3 C2
- C1 C2

*Note: * Moves are validated, so you will have to try another move if its a wrong move.

##### Finishing the game
When the game finished, certain stats about the game will be printed for you to observe.
Then the game will exit on its own.


## Thank you for playing
