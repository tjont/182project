'''
heuristics.py

This file contains heuristics that we assigned to different agents to test them.
'''
import random
from random import randint

class Heuristic:
	def simple(self, gameState, who):

		score = 0

		# for each piece find its position value
		for (x,y) in gameState.getPieces(who):
			score += gameState.pointBoard[x][y]

		# subtract away the opponent's pieces (less for them is better for us)
		score -= len(gameState.getPieces(who*-1))

		# add random element
		score += randint(1,3)

		return score

	def complex(self, gameState, who):
		score = 0
		num_opp_pieces = len(gameState.getPieces(who*-1))
		num_own_pieces = len(gameState.getPieces(who))

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
