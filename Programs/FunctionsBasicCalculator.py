#Alex Plitt
#Functions Basic Calculator

def add(arg1, arg2):
    return arg1 + arg2

def subtract(arg1, arg2):
    return arg1 - arg2

def multiply(arg1, arg2):
    return arg1 * arg2

def divide(arg1, arg2):
    return arg1 / arg2

while True:
    firstNumber = input("What is your first number? ")
    firstNumber = int(firstNumber)
    operator = input("What operator would you like to use? ")
    secondNumber = input("What is your second number? ")
    secondNumber = int(secondNumber)
    if operator == "+":
        print(add(firstNumber, secondNumber))
    elif operator == "-":
        print(subtract(firstNumber, secondNumber))
    elif operator == "*":
        print(multiply(firstNumber, secondNumber))
    elif operator == "/":
        print(divide(firstNumber, secondNumber))
    else:
        print("You have chosen an invalid operator.")
        break
