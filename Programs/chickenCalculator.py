#Alex Plitt
#Minecraft Chicken Cooking Calculator

def coalNeeded(chickens):
    coal = chickens / 8
    return coal
def chickensNeeded(coal):
    chickens = coal * 8
    return chickens
coalOrChickens = input("Do you want to calculate coal needed or chickens needed? ")
if coalOrChickens == "coal":
    chickens = input("How many chickens do you have? ")
    chickens = int(chickens)
    print(coalNeeded(chickens))
elif coalOrChickens == "chickens":
    coal = input("How much coal do you have? ")
    coal = int(coal)
    print(chickensNeeded(coal))
else:
    print("You have made an invalid choice.")
    
