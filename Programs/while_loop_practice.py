#Alex Plitt
#While Loop Practice

import random

magicNumber = random.randint (1, 10)
guesses = 5

#loop for as long as they have guesses remaining
while guesses > 0:
    print("You have " + str(guesses) + " left.")
    #get the user's guess and convert to integer
    userGuess = input("Guess my number: ")
    userGuess = int(userGuess)
    #see if the user's guess is higher, lower, or equal to the magic number
    if userGuess > magicNumber:
        print("You guessed too high!")
    elif userGuess < magicNumber:
        print("You guessed too low!")
    else:
        print("You guessed correctly!")
        #break out of loop if they are correct
        break
    #remove one guess 
    guesses -= 1
