import random

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
			
			# switch the x and y coordinates to get correct position
			y, x, direction = raw_input("Make move (ex: 0 5 NE): ").split()
			direction = direct_dict[direction]
			moves = self.board.generateValidMoves(1)
			
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

			# get action
			((x,y), direction, distance) = self.agent.getAction(self.board) 

			# move
			self.board.generateSuccessorBoard((x,y), direction, distance)
