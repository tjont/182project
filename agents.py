import random
import copy

class Agent:
	def getAction(self, state):
		raiseNotDefined()

class MinimaxAgent(Agent):
	def getAction(self, gameState):
		current_board = copy.deepcopy(gameState)
		moves = current_board.generateValidMoves(-1)
		max_utility = float(-inf)
		best_move = None
		for move in moves:
			next_state = copy.deepcopy(current_board.generateSuccessorBoard(*move))
			utility = self.alpha_beta(next_state,5,float(-inf),float(inf),1)
			if utility > max_utility:
				max_utility = utility
				best_move = move
		return best_move

	def alpha_beta(self, state, depth, alpha, beta, player):
		moves = state.generateValidMoves(player)

		# if reached depth limit or no more possible moves (endgame)
		if depth is 0 or not len(moves):
			return #heuristic value (TODO)

		if player is -1: # computer: the maximizing player
			pass
		else: # human: the minimizing player
			pass

class AStarAgent(Agent):
	def getAction(self, gameState):
		raiseNotDefined()

class RandomAgent(Agent):
	def getAction(self, state):
		moves = state.generateValidMoves(-1)
		return random.choice(moves)