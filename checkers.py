import sys
from game import Game
from board import Board

if __name__ == "__main__":
	board = Board()
	if len(sys.argv) is 3:
		newGame = Game(board, sys.argv[1], sys.argv[2])
		newGame.run()
	elif len(sys.argv) is 4:
		newGame = Game(board, sys.argv[1], sys.argv[2], sys.argv[3])
		newGame.run()
	else:
		print "please format: python checkers.py agent1 agent2"