182project
==========

# Encoding the Board
* 8 by 8 board as 2D-array of integers
* Empty spaces are 0
* Positive numbers are human
* Negative numbers are computer
* 1 is regular piece, 2 is promoted piece
* Possible values: -2, -1, 0, 1, 2

## Piece location
We should probably keep track of where each player's pieces are in two separate lists of coordinates so that we don't have to search through 64 spaces to find possible successor moves. This just means more work when it comes to updating the board after a move is taken.

# Generating Successor States

Some general rules I remember about checkers:

* Pieces only move diagonally:
  * By one square if that square is empty
  * By two squares if the square is occupied by other player's piece, which is removed
  * Forwards if the piece is regular
  * Forwards or backwards if the piece is promoted
* Jumping
  * Wikipedia says its mandatory, so that if a player can jump they have to
  * Multiple jumps can happen in a turn, if making one jump leads to another possible jump
* Promoting
  * When a piece reaches the other side of the board, it is promoted and the move ends


