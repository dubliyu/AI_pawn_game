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
	memoized_size = 0

	def __init__(self, computer, user):
		self.computer = computer
		self.user = user

	def start_time(self):
		self.temp_start = time.time()

	def stop_time(self):
		stop = time.time()
		self.elapsed_t.append(stop - self.temp_start)

	def check_depth(self, d):
		if d > self.max_depth:
			self.max_depth = d
		self.depths.append(d)

	def add_move(self, m):
		self.possible_moves.append(m)

	def add_size(self, s):
		if s > self.memoized_size:
			self.memoized_size = s

	def print_stats(self):
		print("-" * 25)
		print("Game Stats:")
		print("Average Time per Move: " + str(sum(self.elapsed_t) / len(self.elapsed_t)))
		print("Average number of moves generated: " + str(sum(self.possible_moves) / len(self.possible_moves)))
		print("Average depth reached by minimax: "+ str(sum(self.depths) / len(self.depths)))
		print("Max depth reached by minimax: " + str(self.max_depth))
		print("End size of memoizing hash table: " + str(self.memoized_size))
		print("-" * 25)