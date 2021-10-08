#Lump
#Random Dice Generator
#For Dungeons & Dragons and other nerd stuff

#Imports the random module
import random

#Sets the variables named diceAmount, diceSides, modifier, programRunning, and result to an imputted value
diceAmount = 0
diceSides = 0
modifier = 0
programRunning = True
result = 0

#Puts the variable programRunning into a loop, which is active as long as the value is true
while programRunning:
    diceAmount = input("How many dice are you rolling? ")
    if diceAmount == "0":
        break
    else:
        diceSides = input("How many sides does your dice have? ")
        modifier = input("What should I add to the total result? ")
        loops = int(diceAmount)
    #Puts the variable loops into a while loop, which is active as long as loops is greater than 0
        while loops > 0:
            loops -= 1
            result += random.randint(1, int(diceSides))
        result += int(modifier)
        print(result)
