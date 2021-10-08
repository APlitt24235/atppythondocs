#Alex Plitt
#Naughty/Nice List

cpclass = ["David", "Brandon", "Amari", "Logan Antonio", "Conner", "Jerry",
           "Jimmy", "Allison", "Ryan", "Macarios", "Brandon", "Yan'Luis",
           "Alexander", "Andrew", "Daniel", "Westley", "Mason", "Talon",
           "Everleigh", "Alexander", "Jason", "Abdiel", "Wesley"]

nastudents = []

nistudents = []

for student in cpclass:
    while True:
        userInput = input("Is " + student + " naughty(na) or nice(ni)? ")
        if userInput == "na":
            nastudents.append(student)
            break
        elif userInput == "ni":
            nistudents.append(student)
            break
        else:
            print("You have made an invalid entry.")

print("The following students are on the Nice list: ")

for student in nistudents:
    print(student)

print("The following students are on the Naughty list: ")

for student in nastudents:
    print(student)
