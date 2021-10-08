currentBalance = 1000
programRunning = True

while programRunning == True:
    userChoice = input("Would you like to Deposit(1), make a Withdrawal(2), or Quit(3)? ")
    if userChoice == "1":
        userDeposit = input("How much would you like to deposit? ")
        userDeposit = int(userDeposit)
        currentBalance = currentBalance + userDeposit
    elif userChoice == "2":
        userWithdraw = input("How much would you like to withdraw? ")
        if int(userWithdraw) > currentBalance:
            print("You don't have enough money for that action!")
        else:
            currentBalance = currentBalance - int(userWithdraw)
    elif userChoice == "3":
        programRunning = False
    else:
        print("Your choice is invalid. Please type 1, 2, or 3 for their respective actions.")
