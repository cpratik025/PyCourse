class Toy:
    def __init__(self,color,age):
        self.color=color
        self.age=age
    def info(self):
        print(f'The Toy color is {self.color} and age is {self.age}')
    #dunder method can be modified based on a class
    def __str__(self):
        return f'{self.color}'
actionfig = Toy('Red',25)

print(actionfig.info())
#__str__ is a dunder method can be used to perform specific operation
print(actionfig.__str__())