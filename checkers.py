from game import Game
from board import Board

if __name__ == "__main__":
	board = Board()
	newGame = Game(board)
	newGame.run()