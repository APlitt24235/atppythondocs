#Alex Plitt
#Objects/Classes practice

#Creates a class
class Fighter():
    #This is the constructor: it needs the arguement "self"
    def __init__(self):
        #Sets this objects 'hp' property
        self.hp = 20
        #Sets this object's 'name' property
        self.name = "Fighter"
    #Create a punch method with two arguements
    def punch(self, target):
        #Prints this object's name punching the target's name
        print(self.name + " punches " + target.name)
        #This subtracts 3 from the target's HP
        target.hp -= 3

#This creates a Fighter() object called bob
bob = Fighter()
#This changes bob's name property
bob.name = "Bob"
#This creates a Fighter() object called frank
frank = Fighter()
#This changes frank's name property
frank.name = "Frank"

#This makes the bob object use its punch method targetting the frank object
bob.punch(frank)
#This makes the frank object use its punch method targetting the bob object
frank.punch(bob)
#Prints bob's hp property
print(bob.hp)
#Prints frank's hp property
print(frank.hp)


