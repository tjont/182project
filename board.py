from util import TupleMath

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

		self.human = [(5,0),(5,2),(5,4),(5,6),(6,1),(6,3),(6,5),(6,7),(7,0),(7,2),(7,4),(7,6)]
		self.computer = [(0,1),(0,3),(0,5),(0,7),(1,0),(1,2),(1,4),(1,6),(2,1),(2,3),(2,5),(2,7)]

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

	def getValue(self,x,y):
		return self.state[x][y]

	def setValue(self,x,y,val):
		self.state[x][y] = val

	def removePiece(self,x,y):
		try:
			self.human.remove((x,y))
		except ValueError:
			try:
				self.computer.remove((x,y))
			except ValueError:
				pass

	def addPiece(self,x,y,who):
		if who > 0:
			self.human.append((x,y))
		else:
			self.computer.append((x,y))

	# check if piece is on board
	def onBoard(self, x, y):
		return x >= 0 and x <= 7 and y >= 0 and y <= 7

	def generateValidMoves(self, who):

		valid_moves = []
		valid_jumps = []
		if who is 1:
			to_choose_from = self.human
		else:
			to_choose_from = self.computer
		for (x,y) in to_choose_from:
			current_piece = self.getValue(x,y)
			# if the piece can move south, figure out SE and SW
			# so, if king or if computer
			if abs(current_piece) is 2 or current_piece < 0:
				for direction in [Move.SW, Move.SE]:
					try:
						nx,ny = TupleMath.add((x,y),direction)
						new_square = self.getValue(nx,ny)
						jx,jy = TupleMath.add((nx,ny),direction)
						if not new_square: # if empty square
							valid_moves.append(((x,y), direction, Move.M))
						elif -1*who*new_square > 0 and not self.getValue(jx,jy): # if can jump over
							valid_jumps.append(((x,y), direction, Move.J))
					except IndexError: # ignore move if it would go out of bounds
						pass
			# if the piece can move north, figure out possible NE and NW moves
			if abs(current_piece) is 2 or current_piece > 0:
				# for both NE and NW
				for direction in [Move.NE, Move.NW]:
					try:
						nx,ny = TupleMath.add((x,y),direction)
						new_square = self.getValue(nx,ny)
						jx,jy = TupleMath.add((nx,ny),direction)
						if not new_square: # if empty square
							valid_moves.append(((x,y),direction, Move.M))
						elif -1*who*new_square > 0 and not self.getValue(jx,jy): # if can jump over
							valid_jumps.append(((x,y), direction, Move.J))
					except IndexError: # ignore move if it would go out of bounds
						pass
		# if a jump can be made, the person has to jump
		if len(valid_jumps) > 0:
			return valid_jumps
		else:
			return valid_moves 

	def generateSuccessorBoard(self, (x,y), direction, magnitude):
		#x, y = pos
		
		# get piece value
		piece = self.getValue(x,y)

		# set current position to be empty and remove from list
		self.setValue(x,y,0)
		self.removePiece(x,y)
		# set position one diagonal away to be empty and remove from list
		nx,ny = TupleMath.add((x,y),direction)
		self.setValue(nx,ny,0)
		self.removePiece(nx,ny)
		# set new position to have the value of the original piece, and add to list
		mx,my = TupleMath.add((x,y),TupleMath.c_multiple(magnitude,direction))
		self.setValue(mx,my,piece)
		self.addPiece(mx,my,piece)
	