from game import Board
from game import Game

if __name__ == "__main__":
	board = Board()
	newGame = Game(board)
	newGame.run()