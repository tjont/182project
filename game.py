"""
game.py

Control flow of program. In charge of alternating player turns and running
the desired number of simulations. As well as printing board state and 
relevant statistics.
"""

from agents import RandomAgent
from agents import MinimaxAgent
from agents import GreedyAgent
from agents import HumanAgent
from board import Board

import sys
import time

class Game:
	def __init__(self, board, agentType1, agentType2, simulations=1):
		self.board = board

		# number of times to simulate
		self.simulations = int(simulations)

		agent_dict = {"RandomAgent":RandomAgent,"MinimaxAgent":MinimaxAgent,"GreedyAgent":GreedyAgent,"HumanAgent":HumanAgent}
		
		agent_class1 = agent_dict[agentType1]
		agent_class2 = agent_dict[agentType2]
		
		self.agent1 = agent_class1(1)
		self.agent2 = agent_class2(-1)

		# list of all moves
		self.agent1_moves = []
		self.agent2_moves = []
		
		# list of how long it took an agent to make a move for each move
		self.agent1_times = []
		self.agent2_times = []
	
		# totals
		self.agent1_wins = 0 
		self.agent2_wins = 0

	def exit(self, who):
		# "who" is the agent who lost
		if who == 1:
			self.agent2_wins += 1
		else:
			self.agent1_wins += 1
		
		print ('Agent 1: {:d} moves, {:f} avg time per move'.format(len(self.agent1_moves), (sum(self.agent1_times) / len(self.agent1_times))))
		print ('Agent 2: {:d} moves, {:f} avg time per move'.format(len(self.agent2_moves), (sum(self.agent2_times) / len(self.agent2_times))))
		
		if self.simulations >= 1:
			# reset all the single game statistics
			self.agent1_moves = []
			self.agent2_moves = []
			self.agent1_times = []
			self.agent2_times = []

			# reset the board
			self.board = Board()

			self.run()

		else:
			print "================ TOTALS ================"
			print "Agent 1 won " + str(self.agent1_wins) + "/" + str(self.agent1_wins + self.agent2_wins)
			print "Agent 2 won " + str(self.agent2_wins) + "/" + str(self.agent1_wins + self.agent2_wins)
			sys.exit(0)


	def run(self):
		# log this game
		self.simulations -= 1
		
		while True:
			print "Agent 1's (O) turn "
			print self.board			

			while True:
				# get action Agent 1
				start_time = time.time() 						
				action = self.agent1.getAction(self.board) 
				end_time = time.time()

				# record how long it takes
				self.agent1_times.append(end_time-start_time)

				# deals with invalid moves
				if action != None:
					# this player lost
					if action == 0:
						self.exit(1)

					self.agent1_moves.append(action)
					((x,y), direction, distance) = action
					self.board.generateSuccessorBoard((x,y), direction, distance)
					break

			print "Agent 2's (X) turn "
			print self.board

			while True:
				# get action Agent 2
				start_time = time.time()
				action = self.agent2.getAction(self.board)
				end_time = time.time()

				# record how long it takes
				self.agent2_times.append(end_time-start_time)
				
				# deals with invalid moves
				if action != None:
					if action == 0:
						self.exit(-1)

					self.agent2_moves.append(action)
					((x,y), direction, distance) = action
					self.board.generateSuccessorBoard((x,y), direction, distance)
					break




