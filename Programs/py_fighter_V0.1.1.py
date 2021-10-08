#Alex Plitt
#PyFighter V0.1

import random

player1HP = 20
player2HP = 20
player1ATK = 5
player2ATK = 5
player1DEF = 5
player2DEF = 5
player_turn = 1
game_playing = True

def punch(ATK, DEF):
    hit_score = random.randint(1, 10) + ATK + 1
    damage = 3 - 1
    if hit_score > 5 + DEF:
        if player_turn == 1:
            global player2HP
            player2HP = player2HP - damage
        elif player_turn == 2:
            global player1HP
            player1HP = player1HP - damage
        return True
def kick(ATK, DEF):
    hit_score = random.randint(1, 10) + ATK - 1
    damage = 3 + 1
    if hit_score > 5 + DEF:
        if player_turn == 1:
            global player2HP
            player2HP = player2HP - damage
        elif player_turn == 2:
            global player1HP
            player1HP = player1HP - damage

while game_playing == True:
    if player_turn == 1:
        currentATK = player1ATK
        currentDEF = player2DEF
        currentHP = player2HP
    if player_turn == 2:
        currentATK = player2ATK
        currentDEF = player1DEF
        currentHP = player1HP
    player_choice = input("Do you want to punch or kick? ")
    if player_choice == "punch":
        if punch(currentATK, currentDEF) == True:
            print("The attack hit! The target's HP is now " + str(currentHP)+ ".")
        else:
            print("The attack missed!")
        if player_turn == 1:
            player_turn = 2
        elif player_turn == 2:
            player_turn = 1
    elif player_choice == "kick":
        if kick(currentATK, currentDEF) == True:
            print("The attack hit! The target's HP is now " + str(currentHP) + ".")
        else:
            print("The attack missed!")
        if player_turn == 1:
            player_turn = 2
        elif player_turn == 2:
            player_turn = 1
    else:
        print("Pick a valid attack option!")
    if currentHP <= 0:
        print("Player " + player_turn + " wins!")
        game_playing = False
        
    
