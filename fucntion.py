
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