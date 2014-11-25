class Agent:
	def __init__(self, index=0):
		self.index = index

	def getAction(self, state):
		raiseNotDefined()

class Directions:
	NORTHWEST = 'Northwest'
	NORTHEAST = 'Northeast'
	SOUTHWEST = 'Southwest'
	SOUTHEAST = 'Southeast'

class Board:
	def __init__(self):
		self.state = [[0,-1,0,-1,0,-1,0,-1],
				 	  [-1,0,-1,0,-1,0,-1,0],
				 	  [0,-1,0,-1,0,-1,0,-1],
				 	  [0,0,0,0,0,0,0,0],
				      [0,0,0,0,0,0,0,0],
				 	  [1,0,1,0,1,0,1,0],
				 	  [0,1,0,1,0,1,0,1],
				 	  [1,0,1,0,1,0,1,0],
					 ]

	def __str__(self):
		""
		board = ''
		for row in self.state:
			for col in row:
				if col == 1:
					board += 'b '
				if col == 2:
					board += "B "
				if col == -1:
					board += 'w '
				if col == -2:
					board += 'W '
				if col == 0:
					board += 'O '
			board+= '\n'
		return board 

class Game:
	def __init__(self, board, agentType):
		self.board = board
		self.gameOver = False
		self.agentType = agentType

	def run(self):
		while not self.gameOver:
			print self.board			
			
			move = raw_input("Make move: ")

			# change the board somehow

			# check what agentType we have 
				# make a move based on that agentType









