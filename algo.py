# import libs
import math
import world

# Global
GAME_TIE = "TIE"
GAME_BLACK = 'b'
GAME_WHITE  = 'w'
GAME_EMPTY = 'e'
_BASE_WIN = 100
_BASE_LOSS = -100


def generate_move(world, tracker, player):
	# Runs minimax and returns optimal move for algo
	tracker.start_time()
	
	# Get current possible moves
	moveset = get_possible_moves(world, player, tracker)

	# Check the value of each move
	best_move_worth = -math.inf
	best_move = []
	for move in moveset:
		# Create a new world
		new_world = world.game_world()
		new_world.set_world(world, move)

		# Run minimax on new world
		worth_of_move = minimax(new_world, 0, player, False, tracker)

		# Evaluate results
		if worth_of_move > best_move_worth:
			best_move = move 

	# Stop tracking time
	tracker.stop()

	# Return best move
	return best_move

def get_possible_moves(world, player, tracker):
	# Generate all possible current moves
	# Each move is array with 4 values 
	# [from_row, from_col, to_row, to_col]
	moveset = []

	# Get all foward movement moves
	for i in range(len(world)):
		for j in range(len(world[i])):
			if world[i][j] == player:
				# We found a pawn, can it move?
				move = move_forward(world, i, j, player)
				attack = attack_forward(world, i, j, player)
				if move: moveset.append(move)
				if attack: moveset.append(attack)

	# Return found move
	tracker.add_move(len(moveset))
	return moveset

def move_forward(world, i, j, player):
	# Check if a piece can move one space forward
	# black
	if player == GAME_BLACK and (i + 1 > 4 or world[i][j] != GAME_EMPTY):
		return False
	
	# white
	if player == GAME_WHITE and (0 > i - 1 or world[i][j] != GAME_EMPTY):
		return False

	# Return move
	return [i, j, i+1, j]

def attack_forward(world, i, j, player):
	# Check if we can attack a piece
	# white
	if player == GAME_WHITE:
		# Check if upward move is possible
		if 0 > i - 1:
			return False

		# Check two cases
		# left
		if 0 > j - 1 and world[i - 1][j - 1] == GAME_BLACK:
			return [i, j, i-1, j-1]
		# Right
		if j + 1 > 2 and world[i - 1][j + 1] == GAME_BLACK:
			return [i, j, i-1, j+1]

	if player == GAME_BLACK:
		# Check if upward move is possible
		if i + 1 > 4:
			return False

		# Check two cases
		# left
		if 0 > j - 1 and world[i - 1][j - 1] == GAME_WHITE:
			return [i, j, i+1, j-1]
		# Right
		if j + 1 > 2 and world[i - 1][j + 1] == GAME_WHITE:
			return [i, j, i+1, j+1]			

	# Something happened
	return False 

def minimax(world, depth, player, tracker):
	# Run the world to its leafs
	# Note depth
	tracker.check_depth(depth)

	# Evaluate world for victory
	worth = evaluator_func(world, player, isMaxPlayer)

	# Switch on worth
	if worth == GAME_TIE:
		return 0
	elif worth == _BASE_WIN or worth == _BASE_LOSS:
		if isMaxPlayer:
			return worth - depth
		else:
			return worth + depth

	# Get opponent
	if player == GAME_WHITE:
		opponent = GAME_BLACK
	else:
		opponent = GAME_WHITE

	# No victory run minimax again
	if isMaxPlayer:
		# Get our moves
		our_moves = get_possible_moves(world, player, tracker)

		# Call minimax for each move
		best_move_worth = -math.inf
		for move in our_moves:
			# Create a new world
			new_world = world.game_world()
			new_world.set_world(world, move)

			# Run minimax on new world
			worth_of_move = minimax(new_world, , depth + 1, opponent, !isMaxPlayer, tracker)

			# Evaluate results
			if worth_of_move > best_move_worth:
				best_move_worth = worth_of_move 

		# Return the best worth
		return best_move_worth
	else:
		# Get opponent moves
		opp_moves = get_possible_moves(world, opponent)

		# Call minimax for each move
		best_move_worth = math.inf
		for move in opp_moves:
			# Create a new world
			new_world = world.game_world()
			new_world.set_world(world, move)

			# Run minimax on new world
			worth_of_move = minimax(new_world, depth + 1, opponent, !isMaxPlayer, tracker)

			# Evaluate results
			if worth_of_move < best_move_worth:
				best_move_worth = worth_of_move 

		# Return the best worth
		return best_move_worth

def evaluator_func(world, player):
	# Evaluate whether a victory has been had
	s_row = world.board[0]
	t_row = world.board[4]

	# Check white
	if player == GAME_WHITE:
		if s_row[0] == GAME_WHITE or s_row[1] == GAME_WHITE s_row[2] == GAME_WHITE:
			return _BASE_WIN
		if t_row[0] == GAME_BLACK or t_row[1] == GAME_BLACK t_row[2] == GAME_BLACK:
			return _BASE_LOSS

	# Check black
	else:
		if s_row[0] == GAME_WHITE or s_row[1] == GAME_WHITE s_row[2] == GAME_WHITE:
			return _BASE_LOSS
		if t_row[0] == GAME_BLACK or t_row[1] == GAME_BLACK t_row[2] == GAME_BLACK:
			return _BASE_WIN

	# Check if deadlock has happened
	moves = get_possible_moves(world, player)
	if len(moves) == 0:
		return GAME_TIE
	else:
		return 0

def check_victory(world):
	# Run the world through the evaluator function
	worth = evaluator_func(world, GAME_WHITE)
	if worth == _BASE_WIN:
		return GAME_WHITE
	elif worth == _BASE_LOSS:
		return GAME_BLACK
	elif worth == GAME_TIE:
		return GAME_TIE
	else:
		return False 