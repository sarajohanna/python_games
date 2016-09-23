# Set active player to 1 and print active player

players = [" ", " "]
print "Welcome to this beautiful game of Nim!"
players[0] = raw_input("What shall I call you, player 1? ")
players[1] = raw_input("What shall I call you, player 2? ")
player = players[0]

# Set the initial state, which is the number of objects we start with
state = 21
print "The game starts with {} sticks and the active player can draw 1, 2 or 3 sticks at a time.".format(state)

while (state > 1):
    # Get move from player
    move = input("{}, how many sticks do you want to draw? ".format(player))

    while (move > 3) or (move < 0):
        move = input("Oh no, I told you to draw 1, 2 or 3 sticks. Try again. ")

    # Update the state and show it
    state = state - move
    print "You draw {}, so now there are {} sticks left".format(move, state)

    # Check if player has won or lost
    if (state == 1):
        print "{}, you win the game!".format(player)

    # If the player did not win or lose, swtich players
    if (player == players[0]):
        player = players[1]
    else:
        player = players[0]

print "Game is over, hope you enjoyed it!"
