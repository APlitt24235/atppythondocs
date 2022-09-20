#Alex Plitt
#SQLite 3 Database Browser Doodad
import sqlite3

#Opening a database, and creating a database object from it
database = sqlite3.connect("testdatabase.db")

#Create a cursor "librarian" to browse the databse
cursor = database.cursor()

"""Ask the user for their:
    First name,
    Last name,
    Height in inches,
    Favorite food """
userFirstName = input("What is your first name? ")
userLastName = input("What is your last name? ")
userHeight = input("What is your height in inches? ")
userFavoriteFood = input("What is your favorite food? ")

#Then convert "height" to an integer
userHeight = int(userHeight)

#Make a list of values for the INSERT query
userInfo = [userFirstName, userLastName, userHeight, userFavoriteFood]

#Tell the cursor to execute an INSERT command (google it)
cursor.execute("INSERT INTO classfood (firstname, lastname, height, food) VALUES(?, ?, ?, ?);", userInfo)

#Then run this method to save the changes
database.commit()

#Tell the cursor to run this command and save the results. Use "fetchall()" on the results to convert to list
results = cursor.execute("SELECT * FROM classfood;").fetchall()

#Check the results
print(results)

#Create a for loop, that prints the first name of each result
for result in results:
    print(result[0])

#Tell the cursor to SELECT anything WHERE the first name column is equal to your first name
firstNameResults = cursor.execute("SELECT * FROM classfood WHERE firstname = 'Alex';").fetchall()

#Print your last name using the search results
print(firstNameResults[0][1])

"""
for person in firstNameResults:
    print(person[1])
"""
