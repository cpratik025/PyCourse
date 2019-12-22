#Higher order function
#If a function takes or returns another function as a parameter or return type then they are called HOF
#Decorator
#Decorator is a function that contains a function in it parameter and then wraps the parameter into a wrap function
#to enhance its ability
#Below we have create a myfuct decorator that has funct as a parameter and that myfuct has another function that enhances the provided function
#When we use @myfuct with hello that hello is passed as a parameter to the myfuct decorator
def myfuct(funct):
    def wrapfunct():
        print('*********')
        funct()
        print('***********')
    return wrapfunct

@myfuct
def hello():
    print('Hello')
@myfuct
def bye():
    print('See you later')

hello()
bye()