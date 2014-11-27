from util import Tuple

class Agent:
	def __init__(self, index=0):
		self.index = index

	def getAction(self, state):
		raiseNotDefined()

class Move:
	"""
	unit tuples for adding to coordinates
	unit scalars for jumps or regular moves
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
	
	def getValue(coordinate):
		x,y = coordinate
		return self.state[x][y]
	
	def setValue(coordinate, value):
		x,y = coordinate
		self.state[x][y] = value
	
	def removePiece(coordinate):
		try:
			self.pieces.remove(coordinate)
		except ValueError:
			try:
				self.computer.remove(coordinate)
			except ValueError:
				pass
	def addPiece(coordinate, who):
		if who > 0:
			self.pieces.append(coordinate)
		else:
			self.computer.append(coordinate)

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
		for coord in pieces_to_choose:
			current_piece = self.getValue(coord)
			# if the piece can move south, figure out possible SE and SW moves
			if abs(current_piece) is 2 or current_piece < 0:
				# for both SE and SW
				for direction in [Move.SE, Move.SW]:
					try:
						new_coord = Tuple.add(coord,direction)
						new_square = self.getValue(new_coord)
						jump_coord = Tuple.add(new_coord,direction)
						if not new_square: # if empty square
							valid_moves.append(coord, direction, Move.M)
						elif -1*who*new_square > 0 and not self.getValue(jump_coord): # if can jump over
							valid_jumps.append(coord, direction, Move.J)
					except IndexError: # ignore move if it would go out of bounds
						pass
			# if the piece can move north, figure out possible NE and NW moves
			if abs(current_piece) is 2 or current_piece > 0:
				# for both NE and NW
				for direction in [Move.NE, Move.NW]:
					try:
						new_coord = Tuple.add(coord,direction)
						new_square = self.getValue(new_coord)
						jump_coord = Tuple.add(new_coord,direction)
						if not new_square: # if empty square
							valid_moves.append(coord,direction, Move.M)
						elif -1*who*new_square > 0 and not self.getValue(jump_coord): # if can jump over
							valid_jumps.append(coord, direction, Move.J)
					except IndexError: # ignore move if it would go out of bounds
						pass
		# if a jump can be made, the person has to jump
		if len(valid_jumps) > 0:
			return valid_jumps
		else:
			return valid_moves

	def generateSuccessorBoard(self, pos, direction, magnitude):
		"""
		pos is current piece position
		direction is tuple indicating unit to add to get new direction
		magnitude is 1 or 2: 1 for no jump, 2 for jump
		"""
		# get piece value
		piece = self.getValue(pos)

		# set current position to be empty and remove from list
		self.setValue(pos,0)
		self.removePiece(pos)
		# set position one diagonal away to be empty and remove from list
		one_diagonal = Tuple.add(pos,direction)
		self.setValue(one_diagonal,0)
		self.removePiece(one_diagonal)
		# set new position to have the value of the original piece, add back to list
		new_pos = Tuple.add(pos,Tuple.c_multiple(magnitude,direction))
		self.setValue(new_pos,piece)
		self.addPiece(new_pos,piece)




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









