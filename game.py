from agents import RandomAgent
from agents import MinimaxAgent
from agents import AStarAgent
from agents import HumanAgent

import sys

class Game:
	def __init__(self, board, agentType1, agentType2):
		self.board = board

		agent_dict = {"RandomAgent":RandomAgent,"MinimaxAgent":MinimaxAgent,"AStarAgent":AStarAgent,"HumanAgent":HumanAgent}
		
		agent_class1 = agent_dict[agentType1]
		agent_class2 = agent_dict[agentType2]
		
		self.agent1 = agent_class1(1)
		self.agent2 = agent_class2(-1)

	def run(self):
		agent1_moves = []
		agent2_moves = []

		def exit():
			print "Agent 1 took " + str(len(agent1_moves)) + "moves"
			print "Agent 2 took " + str(len(agent2_moves)) + "moves"
			sys.exit(0)

		while True:
			print self.board			

			while True:
				# get action Agent 1						
				action = self.agent1.getAction(self.board) 

				# deals with invalid moves
				if action != None:
					if action == -1:
						exit()

					agent1_moves.append(action)
					((x,y), direction, distance) = action
					self.board.generateSuccessorBoard((x,y), direction, distance)
					break


			print self.board

			while True:
				# get action Agent 2
				action = self.agent2.getAction(self.board)
				
				# deals with invalid moves
				if action != None:
					if action == -1:
						exit()

					agent2_moves.append(action)
					((x,y), direction, distance) = action
					self.board.generateSuccessorBoard((x,y), direction, distance)
					break




