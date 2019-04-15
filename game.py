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
stop_loop = False

# Init the world
game_world = world.game_world()
console.print_info(user)

# Start the game loop
while(stop_loop == False):
	# Show the world
	console.print_world(game_world)

	# Get the next move
	if turn == computer:
		move = algo.generate_move(game_world, computer, tracker)
		turn = user
	else:
		move = console.get_move(game_world, tracker, user)
		turn = computer

	# Update the world
	game_world.update_world(move)

	# Check for victory
	victory = algo.check_victory(game_world, tracker)
	if victory == computer:
		console.print_victory(computer, False)
		stop_loop = True
	elif victory == user:
		console.print_victory(user, True)
		stop_loop = True
	elif victory == algo.GAME_TIE:
		console.print_tie()
		stop_loop = True

# Print game Stats
tracker.print_stats()