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

	def validMove(input_move):
		inputs = input_move.split(' ')
		if len(inputs) is not 2:
			return False
		

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

		self.human = [(0,5),(2,5),(4,5),(6,5),(1,6),(3,6),(5,6),(7,6),(0,7),(2,7),(4,7),(6,7)]
		self.computer = [(1,0),(3,0),(5,0),(7,0),(0,1),(2,1),(4,1),(6,1),(1,2),(3,2),(5,2),(7,2)]

	def __str__(self):
		""
		representation = {-2: 'X ', -1: 'x ', 0:'_ ', 1:'o ', 2:'O '}
		board = 'A B C D E F G H \n'
		counter = 1
		for row in self.state:
			for col in row:
				board += representation[col]
			board+= ' ' + str(counter) + ' \n'
			counter += 1
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
	def __init__(self, board, agentType=None):
		self.board = board
		self.gameOver = False
		self.agentType = agentType

	def run(self):
		while not self.gameOver:
			print self.board			
			
			x, y = raw_input("Choose piece (format: x y): ").split()
			direction = raw_input("Choose direction (format: NE or NW or SE or SW): ")
			# change the board somehow
			self.board.generateSuccessorBoard((int(x),int(y)), direction)

			# check what agentType we have 
				# make a move based on that agentType









