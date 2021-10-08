#Alex Plitt
#Functions Practice


#IDLE will turn functions purple
#Functions will always have parenthesis at the end
#You will never see parenthesis without a function or equation
print("This is a function!")

#You can "call" functions by using their name and passing them their required arguments
print("I am calling the print function. This sentance is the argument.")

#You can write your own functions with the def keyword
def printHello():
    print("This print is in the printHello() function.")
    print("Hello!")

#You can define arguments that the function requires
def add(a, b):
    print("This function adds two arguments.")
    print(a + b)

#You can pass "arguments" to a function when calling
add(5, 7)

#Functions can have return values
def subtract(a, b):
    print("This function subtracts two arguments, then it returns the answer.")
    c = a - b
    return c

#This won't print anything:
subtract(7, 5)

#You must print the return value
print(subtract(7, 5))
