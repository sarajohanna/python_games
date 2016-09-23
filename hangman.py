
# Define the two players
players = [" ", " "]
players[0] = raw_input("Who wants to give me a word? ")
players[1] = raw_input("Nice, so who is going to do the guessing? ")

# Ask player 1 for a word and create a list with the characters in the word
word = list(raw_input("{}, give me a word, capital letters please! ".format(players[0])))

print word

# Write out the empty spaces as a list, this needs to be a new list
empty_word = ["_"] * len(word)
print empty_word

error_list = []
count = 0

while count < 12:
    guess = raw_input("Give me a guess, {} ".format(players[1]))
    # Ask player 2 for a character and check if it is in the word.
    # If it is, add it to the empty list, if not, add to the error list.
    for pos, char in enumerate(word):
        if char == guess:
            empty_word[pos] = guess
        else:
            error_list.append(guess)

    # count += 1
    print empty_word
    print error_list

print word

# character in the "empty" list. If it is not, put it in a
# "error list". If player two guesses wrong 11 times, he/she
# loses.
