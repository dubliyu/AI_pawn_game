# Carlos Leon, Mary Wilson
# This file defines the game world representation

class game_world:
	def __init__(self):
		# 3 x 5 board
		self.board = []

		# First row is black
		self.board.append(['b', 'b', 'b'])

		# Next three rows are empty
		self.board.append(['e', 'e', 'e'])
		self.board.append(['e', 'e', 'e'])
		self.board.append(['e', 'e', 'e'])

		# Next row is white
		self.board.append(['w', 'w', 'w'])

	def update_world(self, move):
		x = move[0]
		y = move[1]
		x_n = move[2]
		y_n = move[3]
		pawn = self.board[x][y]
		self.board[x][y] = 'e'
		self.board[x_n][y_n] = pawn

	def set_world(self, old_world, move):
		# Set the board
		for row in range(5):
			for col in range(3):
				self.board[row][col] = old_world.board[row][col]

		# Update the world
		x = move[0]
		y = move[1]
		x_n = move[2]
		y_n = move[3]
		pawn = self.board[x][y]
		self.board[x][y] = 'e'
		self.board[x_n][y_n] = pawn




