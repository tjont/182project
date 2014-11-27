class Agent:
	def __init__(self, index=0):
		self.index = index

	def getAction(self, state):
		raiseNotDefined()

class Move:
	NORTHWEST = 'Northwest'
	NORTHEAST = 'Northeast'
	SOUTHWEST = 'Southwest'
	SOUTHEAST = 'Southeast'

class Game:
	def __init__(self, board, agentType=None):
		self.board = board
		self.gameOver = False
		self.agentType = agentType

	def run(self):
		while not self.gameOver:
			print self.board			
			
			x, y = raw_input("Choose piece (format: x y): ").split()
			direction = raw_input("Choose direction (format: NE or NW or SE or SW): ")
			moves = self.board.generateValidMoves('human')
			if ((x,y),direction,'M') in moves or ((x,y),direction,'J') in moves:
				print "valid move"
			# change the board somehow
			self.board.generateSuccessorBoard((int(x),int(y)), direction)

			# check what agentType we have 
				# make a move based on that agentType









