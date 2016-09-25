import getpass

# Define what should be printed out, hangman image
#   +---+
#   |   |
#   |   O
#   |  /|\
#   |  / \
#   |
# =====

h10 = "  +---+\n  |   |\n  |   O\n  |  /|\ \n  |  / \ \n  |\n====="
h9 = "  +---+\n  |   |\n  |   O\n  |  /|\ \n  |  / \n  |\n====="
h8 = "  +---+\n  |   |\n  |   O\n  |  /|\ \n  |\n  |\n====="
h7 = "  +---+\n  |   |\n  |   O\n  |  /|\n  |\n  |\n====="
h6 = "  +---+\n  |   |\n  |   O\n  |   |\n  |\n  |\n====="
h5 = "  +---+\n  |   |\n  |   O\n  |\n  |\n  |\n====="
h4 = "  +---+\n  |   |\n  |\n  |\n  |\n  |\n====="
h3 = "  +---+\n  |\n  |\n  |\n  |\n  |\n====="
h2 = "  |\n  |\n  |\n  |\n  |\n====="
h1 = "====="

# Put the cases in a list to later print out each case for the incorrect guess
image_list = [h10, h9, h8, h7, h6, h5, h4, h3, h2, h1]

# Give some instructions to the players and ask their names
print "\n\n"
print "Welcome to this awesome game of hangman!"
print "One of you will type a word, and the other one will guess the letters."
print "You can make {} mistakes.\n".format(len(image_list))
players = [" ", " "]
players[0] = raw_input("Who wants to give me a word? ")
players[1] = raw_input("Nice, so who is going to do the guessing? ")
print "\n"

# Ask player 1 for a word, create a list with the characters in the word.
word = list(getpass.getpass("{}, give me a word!\nWhat you type won't show on the screen, let's keep it secret! ".format(players[0])).upper())
print "\n"

# Write out the empty spaces as a list, this needs to be a new list
empty_word = ["_"] * len(word)
print empty_word, "\n"

# Create a list to fill with the incorrect guesses
error_list = []

# Contiue the loop untill player have guessed wrong 11 times
count = len(image_list)
while count > 0:
    # Ask player 2 for a character and check if it is in the word.
    # If it is, add it to the empty list
    guess = raw_input("Give me a guess {}! ".format(players[1])).upper()
    print "\n"

    for pos, char in enumerate(word):
        if char == guess:
            empty_word[pos] = guess

    # If char not in word, append to error list, print hangman and count -1
    if not (guess in word):
        error_list.append(guess)
        print image_list[(count - 1)]
        count -= 1

    # Print the count, the "empty" word and the error list
    print "Guesses left: {}".format(count)
    print "Word: {}".format(empty_word)
    print "Used letters: {}".format(error_list)
    print "\n\n\n"
    # If the "empty" word equals the real word, the player has won!
    if word == empty_word:
        print "You won the game {}!!".format(players[1])
        break

    # If the player has guessed wrong 11 times, the player loses
    if count == 0:
        print "You've used all your guessess. Better luck next time {}!".format(players[1])
