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

	# check if piece is on board
	def onBoard(self, x, y):
		return x >= 0 and x <= 7 and y >= 0 and y <= 7

	def generateValidMoves(self, who):
		valid_moves = []
		valid_jumps = []
		if who is 'computer':
			for (x,y) in self.computer:
				# SE
				# if empty square
				if self.onBoard(x+1,y+1) and self.state[x+1][y+1] == 0:
					valid_moves.append(((x,y),'SE', 'M'))
				# if can jump over
				elif self.onBoard(x+1,y+1) and self.state[x+1][y+1] > 0 and self.onBoard(x+2,y+2) and self.state[x+2][y+2] == 0:
					valid_jumps.append(((x,y),'SE', 'J'))
				
				# SW
				# if an empty square
				if self.onBoard(x+1,y-1) and self.state[x+1][y-1] == 0:
					valid_moves.append(((x,y),'SW', 'M'))
				 # if can jump over
				elif self.onBoard(x+1,y-1) and self.state[x+1][y-1] > 0 and self.onBoard(x+2,y-2) and self.state[x+2][y-2] == 0:
					valid_jumps.append(((x,y),'SW', 'J'))
				
				# if current square contains a king, consider north moves too
				if self.state[x][y] == -2:
					# NE
					# if empty square
					if self.onBoard(x-1,y+1) and self.state[x-1][y+1] == 0:
						valid_moves.append(((x,y),'NE', 'M'))
					# if can jump over
					elif self.onBoard(x-1,y+1) and self.state[x-1][y+1] > 0 and self.onBoard(x-2,y+2) and self.state[x-2][y+2] == 0:
						valid_jumps.append(((x,y),'NE', 'J'))
					# NW
					# if empty square
					if self.onBoard(x-1,y-1) and self.state[x-1][y-1] == 0:
						valid_moves.append(((x,y),'NW', 'M'))
					# if can jump over
					elif self.onBoard(x-1,y-1) and self.state[x-1][y-1] > 0 and self.onBoard(x-2,y-2) and self.state[x-2][y-2] == 0:
						valid_jumps.append(((x,y),'NW', 'J'))
			
			# if a jump can be made, the computer has to jump
			if len(valid_jumps) > 0:
				return valid_jumps
			else:
				return valid_moves
		else: # if human
			for (x,y) in self.human:
				# if current square contains king, consider south moves too
				if self.state[x][y] == 2:
					# SE
					# if empty square
					if self.onBoard(x+1,y+1) and self.state[x+1][y+1] == 0:
						valid_moves.append(((x,y),'SE', 'M'))
					# if can jump over
					elif self.onBoard(x+1,y+1) and self.state[x+1][y+1] < 0 and self.onBoard(x+2,y+2) and self.state[x+2][y+2] == 0:
						valid_jumps.append(((x,y),'SE', 'J'))
					
					# SW
					# if empty square
					if self.onBoard(x+1,y-1) and self.state[x+1][y-1] == 0:
						valid_moves.append(((x,y),'SW', 'M'))
					# if can jump over
					elif self.onBoard(x+1,y-1) and self.state[x+1][y-1] < 0 and self.onBoard(x+2,y-2) and self.state[x+2][y-2] == 0:
						valid_moves.append(((x,y),'SW', 'J'))
				# NE
				# if empty square
				if self.onBoard(x-1,y+1) and self.state[x-1][y+1] == 0:
					valid_moves.append(((x,y),'NE', 'M'))
				# if can jump over
				elif self.onBoard(x-1,y+1) and self.state[x-1][y+1] < 0 and self.onBoard(x-2,y+2) and self.state[x-2][y+2] == 0:
					valid_jumps.append(((x,y),'NE', 'J'))
				# NW
				# if empty square
				if self.onBoard(x-1,y-1) and self.state[x-1][y-1] == 0:
					valid_moves.append(((x,y),'NW', 'M'))				
				# if can jump over
				elif self.onBoard(x-1,y-1) and self.state[x-1][y-1] < 0 and self.onBoard(x-2,y-2) and self.state[x-2][y-2] == 0:
					valid_jumps.append(((x,y),'NW', 'J'))

			# let human make jump or not
			return valid_jumps + valid_moves 

	def generateSuccessorBoard(self, pos, direction, distance, who):
		x, y = pos
		
		# get what type of piece it is -2,-1,0,1,2
		piece = self.state[x][y]
		
		# move piece
		if direction == 'NW':

			# if a single move
			if distance == 'M':
				self.state[x-1][y-1] = piece

				if who == 'human':
					self.human.append((x-1,y-1))
				else:
					self.computer.append((x-1,y-1))

			# if a jump
			else:
				self.state[x-2][y-2] = piece
				self.state[x-1][y-1] = 0

				if who == 'human':
					self.human.append((x-2,y-2))
					self.computer.remove((x-1,y-1))
				else:
					self.computer.append((x-2,y-2))
					self.human.append((x-1,y-1))

		if direction == 'NE':

			# if a single move
			if distance == 'M':
				self.state[x-1][y+1] = piece

				if who == 'human':
					self.human.append((x-1,y+1))
				else:
					self.computer.append((x-1,y+1))

			# if a jump
			else:
				self.state[x-2][y+2] = piece
				self.state[x-1][y+1] = 0

				if who == 'human':
					self.human.append((x-2,y+2))
					self.computer.remove((x-1,y+1))
				else:
					self.computer.append((x-2,y+2))
					self.human.remove((x-1,y+1))
		
		if direction == 'SE':
			
			# in a single move
			if distance == 'M':
				self.state[x+1][y+1] = piece

				if who == 'human':
					self.human.append((x+1,y+1))
				else:
					self.computer.append((x+1,y+1))

			# if a jump
			else:
				self.state[x+2][y+2] = piece
				self.state[x+1][y+1] = 0

				if who == 'human':
					self.human.append((x+2,y+2))
					self.computer.remove((x+1,y+1))
				else:
					self.computer.append((x+2,y+2))
					self.human.remove((x+1,y+1))
		
		if direction == 'SW':

			# if a single move
			if distance == 'M':
				self.state[x+1][y-1] = piece

				if who == 'human':
					self.human.append((x+1,y-1))
				else:
					self.computer.append((x+1,y-1))

			# if a jump
			else:
				self.state[x+2][y-2] = piece
				self.state[x+1][y-1] = 0

				if who == 'human':
					self.human.append((x+2,y-2))
					self.computer.remove((x+1,y-1))
				else:
					self.computer.append((x+2,y-2))
					self.human.remove((x+1,y-1))

		# make original position 0
		self.state[x][y] = 0


		# take original position out of list
		if who == 'human':
			self.human.remove((x,y))
		else:
			self.computer.remove((x,y))




