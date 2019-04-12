# Carlos Leon, Mary Wilson
# This file contains functions for input/output

def print_world(world):
	print("   A  B  C  ")
	print(" +-----------+")
	index = 1
	row_s = ""
	for row in world.board:
		row_s = str(index) + "| "
		for i in row:
			# Add character
			if i == 'e': row_s += ' '
			if i == 'b': row_s += '*'
			if i == 'w': row_s += 'O'

			# Add spacing
			row_s += " | "
		row_s = row_s[:-1]
		print(row_s)
		index += 1
	print(" +-----------+")

def print_info():
	print("Hello, when the game is shown on the console please be aware that")
	print("* is a black pawn")
	print("O is a white pawn\n\n")

def get_user():
	# vars
	computer = ""
	user = ""
	turn = ""

	# dynamic input
	print("Welcome to the pawn game!")
	print("The white and black player compete to make their pawns get to other side")
	print("The White player always goes first")
	comp_first = 'a'
	while(comp_first != 'y' and comp_first != 'n'):
		comp_first = input("Will the computer go first? (Y/N) >")
		comp_first = comp_first.lower()
		if comp_first == 'y':
			computer = 'w'
			user = 'b'
			turn = 'w'
		elif comp_first == 'n':
			computer = 'b'
			user = 'w'
			turn = 'w'
	# Return
	return computer, user, turn

def get_move(world, tracker):
	# vars
	move = []
	valid = False

	while(not valid):
		print("Please enter a move as Column-Row to Column-Row\n ex) A3 B4 or world to print the world again")
		choice = input(">").lower()
		if choice == 'world':
			print_world()
		elif len(choice.strip()) == 4:
			l = choice.split()
			if len(l) != 2:
				print("Invalid input")
			else:
				# Get variables
				from_col = l[0][0]
				from_row = l[0][1]
				to_col = l[1][0]
				to_row = l[1][1]

				# Note what is valid
				valid_col = ['a', 'b', 'c']
				valid_row = ['1', '2', '3', '4', '5']

				# Check for validity
				if from_col in valid_col and to_col in valid_col and to_row in valid_row and from_row in valid_row:
					# TODO
					# perform logic validation here
					#valid = world.validate_move(from_col, from_row, to_col, to_row)
					# Place into move
					valid = True
				else:
					print("Invalid input")
		else:
			print("Invalid input")

	# Return move
	return [0 , 0 , 1 , 0]



