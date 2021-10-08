#Alex Plitt
#PyFighter Alpha 1

class Fighter():
    def punch(self, target):
        print("The fighter punches " + target)
    def kick(self, target):
        print("the fighter kicks " + target)

player1 = Fighter()

player2 = Fighter()

player1.punch("Player 2")

player2.kick("Player 1")
