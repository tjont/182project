from agents import RandomAgent
from agents import MinimaxAgent
from agents import AStarAgent
from agents import HumanAgent

import sys
import time

class Game:
	def __init__(self, board, agentType1, agentType2):
		self.board = board

		agent_dict = {"RandomAgent":RandomAgent,"MinimaxAgent":MinimaxAgent,"AStarAgent":AStarAgent,"HumanAgent":HumanAgent}
		
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


	def exit(self, who):
		# "who" is the agent who lost
		if who == 1:
			print "Agent 2 wins!"
			print "Number of moves: " + str(len(self.agent2_moves))
			print "Average time per move: " + str(sum(self.agent2_times) / len(self.agent2_times))[:5] + " seconds"
		else:
			print "Agent 1 wins!"
			print "Number of moves: " + str(len(self.agent1_moves))
			print "Average time per move: " + str(sum(self.agent1_times) / len(self.agent1_times))[:5] + " seconds"
		sys.exit(0)


	def run(self):
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




