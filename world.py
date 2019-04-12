# Carlos Leon, Mary Wilson
# This file defines the game world representation

class game_world:
	# World variables
	board = []

	def __init__(self):
		# 3 x 5 board
		# First row is black
		self.board.append(['b', 'b', 'b'])

		# Next three rows are empty
		self.board.append(['e', 'e', 'e'])
		self.board.append(['e', 'e', 'e'])
		self.board.append(['e', 'e', 'e'])

		# Next row is white
		self.board.append(['w', 'w', 'w'])

	def update_world(move):
		# Not done
		# Move is array of x, y , new_val tuples
		for m in move:
			self.board[m[0]][m[1]] = m[2]



