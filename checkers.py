import sys
from game import Game
from board import Board

if __name__ == "__main__":
	board = Board()
	if len(sys.argv) is 2:
		agent = sys.argv[1]
		newGame = Game(board, agent)
	else:
		newGame = Game(board)
	newGame.run()