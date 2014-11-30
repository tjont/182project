import sys
from game import Game
from board import Board

if __name__ == "__main__":
	board = Board()
	if len(sys.argv) is 3:
		agent1 = sys.argv[1]
		agent2 = sys.argv[2]
		newGame = Game(board, agent1, agent2)
		newGame.run()
	else:
		print "please format: python checkers.py agent1 agent2"