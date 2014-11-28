import random
import sys

class Agent:
	def getAction(self, state):
		raiseNotDefined()

class RandomAgent:
	def getAction(self, state):
		moves = state.generateValidMoves(-1)
		return random.choice(moves)

class Game:
	def __init__(self, board, agentType=None):
		self.board = board
		self.gameOver = False
		self.agent = RandomAgent()

	def run(self):
		direct_dict = {'NW':(-1,-1), 'NE':(-1,1), 'SW':(1,-1), 'SE':(1,1)}
		while not self.gameOver:
			print self.board			
			
			moves = self.board.generateValidMoves(1)
			if not len(moves): # if no human moves possible
				print "You lose!"
				sys.exit(0)

			# switch the x and y coordinates to get correct position
			y, x, direction = raw_input("Make move (ex: 0 5 NE): ").split()
			direction = direct_dict[direction]
			
			# change from string to int
			x = int(x)
			y = int(y)

			if ((x,y),direction,1) in moves:
				print "valid move"
				# change board accordingly
				self.board.generateSuccessorBoard((x,y), direction, 1)
			elif ((x,y),direction,2) in moves:
				print "valid move"
				# change board accordingly
				self.board.generateSuccessorBoard((x,y), direction, 2)
			else:
				print "not valid move"
				continue

			if not len(self.board.generateValidMoves(-1)): # if no possible computer moves
				print self.board
				print "You win!"
				sys.exit(0)
				
			# get action
			((x,y), direction, distance) = self.agent.getAction(self.board) 

			# move
			self.board.generateSuccessorBoard((x,y), direction, distance)
