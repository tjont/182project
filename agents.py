'''
agents.py

This file contains the different types of agents that are used to play checkers.
Minimax, Greedy, Random and Human.
'''
import random
from random import randint
from heuristics import Heuristic
import copy

class Agent:
	def getAction(self, state):
		raiseNotDefined()

class MinimaxAgent(Agent):
	def __init__(self, who):
		self.who = who
		heur = Heuristic()
		self.heuristic = heur.simple

	def getAction(self, gameState):
		moves = gameState.generateValidMoves(self.who)

		if not len(moves):
			return 0

		max_utility = float("-inf")
		best_move = None
		for move in moves:
			next_state = copy.deepcopy(gameState)
			next_state.generateSuccessorBoard(*move)
			utility = self.alpha_beta(next_state,5,float("-inf"),float("inf"),self.who * -1)
			if utility > max_utility:
				max_utility = utility
				best_move = move

		return best_move

	def alpha_beta(self, state, depth, alpha, beta, player):
		moves = state.generateValidMoves(player)

		# if reached depth limit or no more possible moves (endgame)
		if depth is 0 or not len(moves):
			return self.heuristic(state, self.who)

		if player is self.who: # the maximizing player
			low_max_score = float("-inf")
			low_max_state= None
			high_max_score = float("-inf")
			high_max_state = None

			# take only two most promising moves
			for move in moves:
				# make a new board
				next_state = copy.deepcopy(state)
				next_state.generateSuccessorBoard(*move)

				# get score
				score = self.heuristic(next_state, self.who)

				if (score > low_max_score):
					# higher than both top scores
					if (score > high_max_score):
						low_max_score = high_max_score
						low_max_state = high_max_state
						high_max_score = score
						high_max_state = next_state
					# higher than only low_max_score
					else:
						low_max_score = score
						high_max_state = next_state
			
			# for two top states
			for next_state in [low_max_state, high_max_state]:
				# recurse
				if next_state != None:
					alpha = max(alpha, self.alpha_beta(next_state, depth, alpha, beta, 1))

				if beta <= alpha:
					break # prune branches
			return alpha

		else: # human: the minimizing player
			low_min_score = float("inf")
			low_min_state= None
			high_min_score = float("inf")
			high_min_state = None

			# take only two most promising moves
			for move in moves:
				# make a new board
				next_state = copy.deepcopy(state)
				next_state.generateSuccessorBoard(*move)

				# get score
				score = self.heuristic(next_state, self.who*-1)

				if (score < low_min_score):
					# lower than both top scores
					if (score < high_min_score):
						low_min_score = high_min_score
						low_min_state = high_min_state
						high_min_score = score
						high_min_state = next_state
					# lower than only low_max_score
					else:
						low_min_score = score
						high_min_state = next_state

			# for lowest two states
			for next_state in [low_min_state, high_min_state]:
				# recurse
				if next_state != None:
					beta = min(beta, self.alpha_beta(next_state, depth-1, alpha, beta, -1))

				if beta <= alpha:
					break # prune branches 
			return beta
	'''
	def heuristic(self, gameState):
		score = 0
		num_opp_pieces = len(gameState.getPieces(self.who * -1))
		num_own_pieces = len(gameState.getPieces(self.who))

		for (x,y) in gameState.getPieces(self.who):
			# find "safety" value of pieces
			score += gameState.pointBoard[x][y]
			
			# an attacking strategy if near the end
			if (num_opp_pieces < 3 and num_own_pieces > 5):
				# reward for kings that are closer to the other people
				if (abs(gameState.state[x][y]) == 2):
					distance = gameState.distanceToEnemy(self.who, x, y)
					# only try to get far away kings
					if (distance > 3):
						score -= distance

		# subtract number of pieces that are vulnerable
		score -= len(gameState.generateValidMoves(self.who*-1))

		# subtract away the opponents pieces, aka less pieces for them is good for us
		score -= num_opp_pieces

		# add random element
		score += randint(1,3)
		
		return score
	'''

class GreedyAgent(Agent):
	def __init__(self, who):
		self.who = who
		heur = Heuristic()
		self.heuristic = heur.simple

	def getAction(self, gameState):
		# generate valid moves
		moves = gameState.generateValidMoves(self.who)

		if not len(moves):
			return 0

		best_move = None
		best_score = float("-inf")

		for move in moves:
			# get next state
			next_state = copy.deepcopy(gameState)
			next_state.generateSuccessorBoard(*move)
			
			# get the score for that state
			score = self.heuristic(next_state, self.who)

			# check if it is the best score so far
			if (score > best_score):
				best_move = move
				best_score = score

		return best_move
	'''
	def heuristic(self, gameState):

		score = 0
		
		# for each piece find its position value 
		for (x,y) in gameState.getPieces(self.who):
			score += gameState.pointBoard[x][y]

		# subtract away the opponents pieces, aka less pieces for them is good for us
		score -= len(gameState.getPieces(self.who * -1))

		# add random element
		score += randint(1,3)
		
		return score
	'''

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