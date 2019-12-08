
#Positional Arguments, data will be displayed as per the position of argument
#Positional Argument practice is a better one
def say_something(name):
        print(f'The name provided is {name}')


def say_something1():
    name = input('Please enter a name')
    print(f'The name provided is {name}')

say_something('Pratik')

say_something1()

#Keyword Arguments, arguments and parameters are provided in the method itself

say_something(name = 'Prratik')

def say_nothing():
    a = int(input("Please Enter a value"))
    b = int(input("Please Enter a value"))
    op= input("Please enter a operation")
    if op == '+':
        c= a+b
        print(f"The summation of value is {c}")
    elif op == '-':
        c = a - b
        print(f"The subtraction of value is {c}")
    elif op == '/':
        c = a/b
        print(f"The value of division {c}")
    elif op == '*':
        c = a * b
        print(f"The Multiplication of the values is {c}")
    else:
        print("The operation is incorrect")

say_nothing()



