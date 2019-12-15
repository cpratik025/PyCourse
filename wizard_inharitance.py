class User():
    def __init__(self,email):
        self.email = email
    #if no params are to be passed then the class needs not to be init
    def signin(self):
        print("Sign In Was Successful")

class Wizard(User):
    def __init__(self,name,power):
        #User.__init__(self, email)  #intentiating init method of user class into wizerd class same can be achieved using super keyword
        #super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with Power {self.power}")


class Archer(User):
    def __init__(self,name,no_arrows):
        self.name = name
        self.no_arrows = no_arrows

    def Arattack(self):
        print(f"Attacking with arrows {self.no_arrows}")

    def run(self):
        print('Ran Really Fast')

class Hybrid(Wizard,Archer):
    def __init__(self,name,power,no_arrows): # as wizard and archar class takes seprate variables we need to define the variables here from both classes
        Archer.__init__(self,name,no_arrows)
        Wizard.__init__(self,name,power)

#wizard1= Wizard('Ram', 100,'marlin@gmail.com')


archer1= Archer('Laxman',30)


hyd = Hybrid('Pratik',50,100)
print(hyd.run())
print(hyd.attack())
print(hyd.Arattack())
#wizard1.attack()
#archer1.attack()
#print(wizard1.email)