class PlayerCharacter:
    #Class Object Attribute is a constant value that does not change
    membership = True
    #This is a special Method, dunder method also known as constructor method.
    def __init__(self,name,age):
        if(self.membership):
            self.name = name #This are attributes Class attributes
            self.age = age
    def run(self):
        print(f'The name is {self.name} and age is {self.age}')

    @classmethod
    def addingThings(cls,num1,num2):
        return num1+num2
    @staticmethod
    def addingThings2(num1,num2):
        return num1+num2

playerName= input("Please Enter a Name for the Character")
playerage = input("Please Enter The Players Age")

player1= PlayerCharacter(playerName,playerage)
player2= PlayerCharacter.addingThings(5,10)
player3 = PlayerCharacter.addingThings2(5,0)
print(player1)
print(player1.name)
print(player1.age)
print(player1.run())
print(player2)
print(player3)
