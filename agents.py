import random

class Agent:
	def getAction(self, state):
		raiseNotDefined()

class MinimaxAgent(Agent):
	def getAction(self, gameState):
		pass

class RandomAgent(Agent):
	def getAction(self, state):
		moves = state.generateValidMoves(-1)
		return random.choice(moves)