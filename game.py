import random

class Agent:
	def getAction(self, state):
		raiseNotDefined()

class RandomAgent:
	def getAction(self, state):
		moves = state.generateValidMoves('computer')
		return random.choice(moves)

class Game:
	def __init__(self, board, agentType=None):
		self.board = board
		self.gameOver = False
		self.agent = RandomAgent()

	def run(self):
		while not self.gameOver:
			print self.board			
			
			# switch the x and y coordinates to get correct position
			y, x, direction = raw_input("Make move (ex: 0 5 NE): ").split()
			moves = self.board.generateValidMoves('human')
			
			# change from string to int
			x = int(x)
			y = int(y)

			if ((x,y),direction,'M') in moves:
				print "valid move"
				# change board accordingly
				self.board.generateSuccessorBoard((x,y), direction, 'M', 'human')
			elif ((x,y),direction,'J') in moves:
				print "valid move"
				# change board accordingly
				self.board.generateSuccessorBoard((x,y), direction, 'J', 'human')
			else:
				print "not valid move"
				continue

			# get action
			((x,y), direction, distance) = self.agent.getAction(self.board) 

			# move
			self.board.generateSuccessorBoard((x,y), direction, distance, 'computer')






