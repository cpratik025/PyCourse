class User():
    def __init__(self,email):
        self.email = email
    #if no params are to be passed then the class needs not to be init
    def signin(self):
        print("Sign In Was Successful")

class Wizard(User):
    def __init__(self,name,power,email):
        User.__init__(self, email)  #intentiating init method of user class into wizerd class same can be achieved using super keyword
        #super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with Power {self.power}")


class Archer(User):
    def __init__(self,name,no_arrows):
        self.name = name
        self.no_arrows = no_arrows

    def attack(self):
        print(f"Attacking with arrows {self.no_arrows}")


wizard1= Wizard('Ram', 100,'marlin@gmail.com')
archer1= Archer('Laxman',30)

print(wizard1)

#introspection helps examine the code and know what the code does

print(dir(wizard1))