# Carlos Leon, Mary Wilson
# This file contains functions for input/output

def print_world(world):
	print("\n   A  B  C  ")
	print(" +---------+")
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

		# print row
		print(row_s)
		index += 1
		print(" +---------+\n")

def print_info(player):
	print("Hello, when the game is shown on the console please be aware that\n")
	b_comment = ""
	w_comment = ""
	if player == 'b':
		b_comment = 'This is you!'
	elif player == 'w':
		w_comment = "This is you!"
	print("* is a black pawn " + b_comment + "\n")
	print("O is a white pawn " + w_comment + "\n\n")

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
	valid = 0

	while(valid != 1):
		print("Please enter a move as Column-Row to Column-Row\n ex) A3 B4 or world to print the world again")
		choice = input(">").lower()
		if choice == 'world':
			print_world(world)
		elif len(choice.strip()) == 5:
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
					# Translate
					try:
						from_col = valid_col.index(from_col)
						to_col = valid_col.index(to_col)
						from_row = valid_row.index(from_row)
						to_row = valid_row.index(to_row)
					except:
						print("That move is not valid.")
						continue
					
					#Validates the input
					valid = validate_move(world, from_col, from_row, to_col, to_row, user)

					if valid == -1: #They tried to move other team
						print("You can't move a pawn you don't control. Try Again.")
					elif valid == 0: #Not valid
						print("That move is not valid.")
						continue
					elif valid == 1: #Valid!!!
						return [from_row, from_col, to_row, to_col]
				else:
					print("Invalid input")
		else:
			print("Invalid input")

	# This should never happen
	return [0,0,0,0]

def print_tie():
	print("A deadlock has been reached\nNo Winner, Tie\n")

def print_victory(player, isUser):
	if player == 'b': player = "Black"
	if player == 'w': player = "White"
	if isUser:
		comment = "the User"
	else:
		comment = "the Computer"
	print("!!!A Winner has been reached!!!\nWinner is " + player + ", " + comment)

#Validates a user input
def validate_move(world, from_col, from_row, to_col, to_row, user):
	#Starts Validation
	#If white
	if (world.board[from_row][from_col]== 'w') and (user == 'w'): 
		if(to_row == from_row -1): #If going one space foward  - covers non-attack moves

			if (to_col == from_col + 1) or (to_col == from_col -1): #Diagonal

				if world.board[to_row][to_col] == 'b': #Can attack opponent
					return 1
				else:
					return 0

			elif (to_col == from_col):
				if world.board[to_row][to_col] == 'e':
					return 1
				else:
					return 0

			else: #Moving multiple diagonals - this is not a knight
				return 0
			
		else: #Moving multiple or no rows
			return 0

	#IF they are black but trying to control white
	elif (world.board[from_row][from_col] == 'w') and (user == 'b'):
		return -1

	#If black
	elif world.board[from_row][from_col] == 'b':
		if(to_row == from_row +1): #If going one space foward  - covers non-attack moves

			if (to_col == from_col + 1) or (to_col == from_col -1): #Diagonal

				if world.board[to_row][to_col] == 'w': #Can attack opponent
					return 1
				else:
					return 0

			elif (to_col == from_col):
				if world.board[to_row][to_col] == 'e':
					return 1
				else:
					return 0

			else: #Moving multiple diagonals - this is not a knight
				return 0
			
		else: #Moving multiple or no rows
			return 0

	#IF they are white but trying to control black
	elif (world.board[from_row][from_col] == 'b') and (user == 'w'):
		return -1

	#If they try moving something not there
	else: #e so invalid 
		return 0

def generating_moves():
	print("Computer is generating moves...")
