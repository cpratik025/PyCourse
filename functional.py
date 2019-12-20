#map,zip,reduce and filter
from functools import reduce


mylist=[1,2,3,4]
mylist1=[10,20,30,40]
def multiply_2(li):
    return li*2
print(list(map(multiply_2,[1,2,3])))

def checkodd(it):
    return it %2 != 0
def accumlator(acc,item):
    print(acc,item)
    return item+acc

#reduce takes three parameter function,sequanece,initial
print(reduce(accumlator,mylist,0))
#Zip needs two lists/ittrables and using zip we can zip them togather
print(list(zip(mylist,mylist1))) #return combined value of two list for each item in index i in list is added a tuple

print(list(map(multiply_2,mylist)))
print(mylist )

#Filters out the even no from the odd
print(list(filter(checkodd,mylist)))

#lambda fuction can be used to perform a action that you only want to perform once and dont want
#to code a complete function for it as as example of multiply by 2 function above if we want we
#can assign is using lambda function
print(list(map(lambda item: item*2,mylist)))
#same way it can be used for filter
print(list(filter(lambda item: item %2!=0,mylist)))

print(reduce(lambda acc,item: acc+item,mylist))