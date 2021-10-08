# Alex Plitt
# Conditional Statements (if/elif/else)

# A statement is one line of code
myPet = input("What is your pet? ")
petColor = input("What color is it? ")

# A conditional statement is a block of code that only runs when the condition is true
if myPet == "dog":
    print("You have a dog!")
elif myPet == "cat":
    print("You have a cat!")
elif myPet == "frog":
    print("You have a frog!")
elif myPet:
    print("You have a " + myPet)
else:
    print("You don't have a pet.")
if myPet and petColor:
    print("Your pet's color is " + petColor)
    
