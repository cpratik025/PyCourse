class User():
    #if no params are to be passed then the class needs not to be init
    def signin(self):
        print("Sign In Was Successful")

class Wizard(User):
    def __init__(self,name,power):
        self.name = name
        self.power = power

    def attack():
        print(f"Attacking with Power {self.power}")


class Archer(User):
    def __init__(self,name,no_arrows):
        self.name = name
        self.no_arrows = no_arrows

    def attack():
        print(f"Attacking with arrows {self.no_arrows}")


wizard1= Wizard('Ram', 100)
archer1= Archer('Laxman',30)