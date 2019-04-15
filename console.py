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

def get_move(world, tracker, user):
	# vars
	move = []
	valid = False

	while(valid != 1):
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
					#Validates the input
					valid = console.validate_move(world, from_col, from_row, to_col, to_row, user)
					############################## do i need to put console there in same file??? ###########################################

					if valid == -1: #They tried to move other team
						print("You can't move a pawn you don't control. Try Again.")
					else if valid == 0: #Not valid
						print("That move is not valid.")
						continue
					else if valid == 1: #Valid!!!
						return [from_col, from_row, to_col, to_row]


				else:
					print("Invalid input")
		else:
			print("Invalid input")

	# This should never happen
	return [0,0,0,0]

#Validates a user input
def validate_move(world, from_col, from_row, to_col, to_row, user):
#Converting the row / col to grid numbers

	loop = [from_col, from_row, to_col, to_row]

	for i in range (0, len(loop)):
		if loop[i] == 'a':
			loop[i] = 0
		else if loop[i] == 'b':
			loop[i] = 1
		else if loop[i] == 'c':
			loop[i] == 2
		else if loop[i].isnumeric():
			loop[i] == loop[i] - 1
		else:
	
	from_col = loop[0]
	from_row = loop[1]
	to_col = loop[2]
	to_row = loop[3]

	
#Starts Validation
	#If white
	if (world.board[from_col][from_row] == 'w') and (user == 'w'): 
		if(to_row = from_row -1): #If going one space foward  - covers non-attack moves

			if (to_col == from_col + 1) or (to_col == from_col -1): #Diagonal

				if world.board[to_col][to_row] == 'b': #Can attack opponent
					return 1
				else:
					return 0

			else if (to_col == from_col):
				if world.board[to_col][to_row] != 'e':
					return 1
				else:
					return 0

			else: #Moving multiple diagonals - this is not a knight
				return 0
			
		else: #Moving multiple or no rows
			return 0

	#IF they are black but trying to control white
	else if (world.board[from_col][from_row] == 'w') and (user == 'b'):
		return -1

	#If black
	else if world.board[from_col][from_row] == 'b':
		if(to_row = from_row +1): #If going one space foward  - covers non-attack moves

			if (to_col == from_col + 1) or (to_col == from_col -1): #Diagonal

				if world.board[to_col][to_row] == 'w': #Can attack opponent
					return 1
				else:
					return 0

			else if (to_col == from_col):
				if world.board[to_col][to_row] != 'e':
					return 1
				else:
					return 0

			else: #Moving multiple diagonals - this is not a knight
				return 0
			
		else: #Moving multiple or no rows
			return 0

	#IF they are white but trying to control black
	else if (world.board[from_col][from_row] == 'b') and (user == 'w'):
		return -1

	#If they try moving something not there
	else: #e so invalid 
		return 0


