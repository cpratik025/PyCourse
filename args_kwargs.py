#def super_met(args):
#    return args
# to get n number of values and pass only one parameter in function use *arg
#Persedence Rule: Parameter->*args->Default Parameter->**kwargs
def super_met(*args, **agg):
    #kwargs helps to add key:value pair
    print(args) #this would even work if you remove the * from here as the method has already taken a set of value in the declaration
    print(agg)
    total = 0
    for items in agg.values():
        total = total+items
    return sum(args)+total
print(super_met(1,2,3,4,num1=5, num2=5))

#Persedence Rule: Parameter->*args->Default Parameter->**kwargs

def super_pers(name,*args,age=10,**kargs):
    print(name,*args,age,**kargs)

super_pers(Pratik, 5660, age=15,height=179)
