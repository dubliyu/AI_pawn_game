# Carlos Leon, Mary Wilson
# This file is the main file which will run the game

# Import local files
import world
import algo
import stats
import console

# Declare global variables
computer, user, turn = console.get_user()
tracker = stats.tracker(computer, user)

# Init the world
game_world = world.game_world()
console.print_info()

# Start the game loop
while(True):
	# Show the world
	console.print_world()

	# Get the next move
	if turn == computer:
		move = algo.generate_move(game_world, computer, tracker)
		turn = user
	else:
		move = console.get_move(game_world, tracker)
		turn = computer

	# Update the world
	world.update_world(game_world, move)

	# Check for victory
	victory = algo.check_victory(game_world)
	if victory == computer:
		console.print_victory(computer)
	elif victory == user:
		console.print_victory(user)
	elif victory == algo.GAME_TIE:
		console.print_tie()

# Print game Stats
tracker.print_stats()