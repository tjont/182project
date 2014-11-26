from util import Tuple

class Agent:
	def __init__(self, index=0):
		self.index = index

	def getAction(self, state):
		raiseNotDefined()

class Move:
	"""
	unit tuples for adding to coordinates
	"""
	NW = (-1,-1)
	NE = (-1,1)
	SW = (1,-1)
	SE = (1,1)
	M  = 1
	J  = 2

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

		self.pieces = [(0,5),(2,5),(4,5),(6,5),(1,6),(3,6),(5,6),(7,6),(0,7),(2,7),(4,7),(6,7)]
		self.computer = [(1,0),(3,0),(5,0),(7,0),(0,1),(2,1),(4,1),(6,1),(1,2),(3,2),(5,2),(7,2)]

	def __str__(self):
		""
		representation = {-2: 'X ', -1: 'x ', 0:'_ ', 1:'o ', 2:'O '}
		board = '0 1 2 3 4 5 6 7 \n'
		counter = 0
		for row in self.state:
			for col in row:
				board += representation[col]
			board+= ' ' + str(counter) + ' \n'
			counter += 1
		return board 

	def generateValidMoves(self, who):
		"""
		input: who is 1 if human, -1 if computer
		output: (coordinate, direction, magnitude)
		where magnitude is 1 for no jump and 2 for jump
		"""
		valid_moves = []
		valid_jumps = []
		if who is 1: # human
			pieces_to_choose = self.human
		else: # computer
			pieces_to_choose = self.computer
		for (x,y) in pieces_to_choose:
			current_piece = self.state[x][y]
			# if the piece can move south, figure out possible SE and SW moves
			if abs(current_piece) is 2 or current_piece < 0:
				# for both SE and SW
				for direction in [Move.SE, Move.SW]:
					try:
						nx,ny = Tuple.add((x,y),direction)
						new_square = self.state[nx][ny]
						jx,jy = Tuple.add((nx,ny),direction)
						if not new_square: # if empty square
							valid_moves.append((x,y), direction, Move.M)
						elif -1*who*new_square > 0 and not self.state[jx][jy]: # if can jump over
							valid_jumps.append((x,y), direction, Move.J)
					except IndexError: # ignore move if it would go out of bounds
						pass
			# if the piece can move north, figure out possible NE and NW moves
			if abs(current_piece) is 2 or current_piece > 0:
				# for both NE and NW
				for direction in [Move.NE, Move.NW]:
					try:
						nx,ny = Tuple.add((x,y),direction)
						new_square = self.state[nx][ny]
						jx,jy = Tuple.add((nx,ny),direction)
						if not new_square: # if empty square
							valid_moves.append((x,y),direction, Move.M)
						elif -1*who*new_square > 0 and not self.state[jx][jy]: # if can jump over
							valid_jumps.append((x,y), direction, Move.J)
					except IndexError: # ignore move if it would go out of bounds
						pass
		# if a jump can be made, the person has to jump
		if len(valid_jumps) > 0:
			return valid_jumps
		else:
			return valid_moves

	def generateSuccessorBoard(self, pos, direction, magnitude):
		x, y = pos
		piece = self.state[x][y]
		dist = 1
		if jump:
			dist = 2
		self.state[x][y] = 0
		if direction == 'NW':
			self.state[x-dist][y-dist] = piece
		if direction == 'NE':
			self.state[x-dist][y+dist] = piece
		if direction == 'SE':
			self.state[x+dist][y+dist] = piece
		if direction == 'SW':
			self.state[x+dist][y-dist] = piece


class Game:
	def __init__(self, board, agentType=None):
		self.board = board
		self.gameOver = False
		self.agentType = agentType

	def run(self):
		direct_dict = {'NW':(-1,-1), 'NE':(-1,1), 'SW':(1,-1), 'SE':(1,1)}
		while not self.gameOver:
			print self.board			
			
			x, y = raw_input("Choose piece (format: x y): ").split()
			x = int(x)
			y = int(y)
			direction = direct_dict(raw_input("Choose direction (format: NE or NW or SE or SW): "))
			moves = self.board.generateValidMoves(1)
			# change the board somehow
			if ((x,y),direction,) in moves:
				self.board.generateSuccessorBoard((x,y),direction)
			elif ((x,y),direction,'J') in moves:
				self.board.generateSuccessorBoard((x,y),direction, True)

			# check what agentType we have 
				# make a move based on that agentType









