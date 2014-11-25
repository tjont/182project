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

	def generateSuccessorBoard(self, pos, direction):
		x, y = pos
		piece = self.state[x][y]
		self.state[x][y] = 0
		if direction == 'NW':
			self.state[x-1][y-1] = piece
		if direction == 'NE':
			self.state[x-1][y+1] = piece
		if direction == 'SE':
			self.state[x+1][y+1] = piece
		if direction == 'SW':
			self.state[x+1][y-1] = piece


class Game:
	# NEED TO ADD agent TYPE
	def __init__(self, board):
		self.board = board
		self.gameOver = False
		#self.agentType = agentType

	def run(self):
		while not self.gameOver:
			print self.board			
			
			x, y = raw_input("Choose piece (format: x y): ").split()
			direction = raw_input("Choose direction (format: NE or NW or SE or SW): ")

			# change the board somehow
			self.board.generateSuccessorBoard((int(x),int(y)), direction)

			# check what agentType we have 
				# make a move based on that agentType









