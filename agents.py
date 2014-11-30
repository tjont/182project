import random
import copy

class Agent:
	def getAction(self, state):
		raiseNotDefined()

class MinimaxAgent(Agent):
	def __init__(self, who):
		self.who = who

	def getAction(self, gameState):
		moves = gameState.generateValidMoves(self.who)

		if not len(moves):
			return 0

		max_utility = float("-inf")
		best_move = None
		for move in moves:
			next_state = copy.deepcopy(gameState)
			next_state.generateSuccessorBoard(*move)
			utility = self.alpha_beta(next_state,3,float("-inf"),float("inf"),self.who * -1)
			if utility > max_utility:
				max_utility = utility
				best_move = move

		return best_move

	def alpha_beta(self, state, depth, alpha, beta, player):
		moves = state.generateValidMoves(player)

		# if reached depth limit or no more possible moves (endgame)
		if depth is 0 or not len(moves):
			return self.heuristic(state)

		if player is -1: # computer: the maximizing player
			# for each possible move
			for move in moves:
				# make a new board
				next_state = copy.deepcopy(state)
				next_state.generateSuccessorBoard(*move)
				# recurse
				alpha = max(alpha, self.alpha_beta(next_state, depth, alpha, beta, 1))

				if beta <= alpha:
					break # prune branches
			return alpha

		else: # human: the minimizing player
			# for each possible move 
			for move in moves:
				# make a new board
				next_state = copy.deepcopy(state)
				next_state.generateSuccessorBoard(*move)
				# recurse
				beta = min(beta, self.alpha_beta(next_state, depth-1, alpha, beta, -1))

				if beta <= alpha:
					break # prune branches 
			return beta

	def heuristic(self, gameState):

		score = 0
		
		# for each piece find its position value 
		for (x,y) in gameState.getPieces(self.who):
			score += gameState.pointBoard[x][y]

		# subtract away the opponents pieces, aka less pieces for them is good for us
		score -= len(gameState.getPieces(self.who * -1))
		
		return score

class AStarAgent(Agent):
	def getAction(self, gameState):
		raiseNotDefined()

class RandomAgent(Agent):
	def __init__(self, who):
		self.who = who

	def getAction(self, state):
		moves = state.generateValidMoves(self.who)
		
		if not len(moves):
			return 0
		
		return random.choice(moves)

class HumanAgent(Agent):
	def __init__(self, who):
		self.who = who

	def getAction(self, state):
		direct_dict = {'NW':(-1,-1), 'NE':(-1,1), 'SW':(1,-1), 'SE':(1,1)}

		moves = state.generateValidMoves(self.who)

		if not len(moves): # if no human moves possible
			return 0

		# switch the x and y coordinates to get correct position
		y, x, direction = raw_input("Make move (ex: 0 5 NE): ").split()
		direction = direct_dict[direction]
			
		# change from string to int
		x = int(x)
		y = int(y)

		if ((x,y),direction,1) in moves:
			print "valid move"

			return ((x,y), direction, 1)
		elif ((x,y),direction,2) in moves:
			print "valid move"

			return ((x,y), direction, 2)
		else:
			print "not valid move"
			return None