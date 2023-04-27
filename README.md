# Go Game
Go is a two-player board game that originated in ancient China. The goal of the game is to control more territory on the board than your opponent by placing stones on the intersections of a 19x19 grid.

## This project provides a simple implementation of the Go game using Python. It includes three files:

* go_board.py: This file defines a function for creating a new Go board and a function for displaying the current state of the board.

* go_rules.py: This file defines several functions for checking whether a given move is valid, whether any opponent stones are captured as a result of the move, and for removing any captured stones from the board.

* main.py: This file provides a command-line interface for playing the game of Go. It prompts the players to enter their moves in standard Go board notation (e.g. "a1" for the top-left corner of the board) and uses the functions defined in go_rules.py to check whether the moves are valid and to remove any captured stones. The game ends when both players pass consecutively.

## Usage
To play the game, simply run the main.py file using a Python interpreter. The script will prompt the players to enter their moves and display the current state of the board after each move. If a move is invalid or results in a capture, the script will print an appropriate message.

# Future Improvements
This implementation of the Go game is basic and lacks many of the features that would be needed for a complete Go program. Some possible future improvements include:

* Adding scoring functionality to determine the winner at the end of the game
* Handling more complicated situations, such as ko
* Providing a more user-friendly interface, such as a graphical user interface or a web interface
* Implementing various AI techniques for playing against the computer

## Conclusion
This project provides a simple implementation of the Go game using Python. While it is not a complete or fully-featured Go program, it provides a good starting point for exploring the game of Go.
