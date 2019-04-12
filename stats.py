# Carlos Leon, Mary Wilson
# This file contains functions to track the game statistics
# import libs
import time

class tracker:
	# vars
	computer = ''
	user = ''
	elapsed_t = []
	possible_moves = []
	max_depth = 0
	depths = []
	temp_start = 0

	def __init__(self, computer, user):
		self.computer = computer
		self.user = user

	def start_time():
		self.temp_start = time.time()

	def stop_time():
		stop = time.time()
		elapsed_t.append(stop - self.temp_start)

	def check_depth(d):
		if d > self.depth:
			self.depth = d
		depths.append(d)

	def add_move(m):
		self.possible_moves.append(m)

	def print_stats():
		print("-" * 25)
		print("Game Stats:")
		print("Average Time per Move: " + str(sum(elapsed_t) / len(elapsed_t)))
		print("Average number of moves generated: " + str(sum(possible_moves) / len(possible_moves)))
		print("Average depth reached by minimax: "+ str(sum(depths) / len(depths)))
		print("Max depth reached by minimax: " + str(max_depth))
		print("-" * 25)