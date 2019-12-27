range(100)
#list[range(100)]
#Generators are more efficient as they dont take up huge memory in the system
#it only assigns location to one variable at a time
#For ex a list of range(100) it will first assign a memory to 0 then 1 then 2 and so on instead to assigning location to all 100 items at once
#range() is a Generator
def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result
#Generator fuction prints and allocates memory to iterable one by one instead of creating a complete list and storing it into memory
def generatorfucn():
    for i in range(10):
        #yield pauses the function, it remembers where the fuction was paused
        yield i

g= generatorfucn()
print(next(g)) #index of 0
print(next(g)) #index of 1
next(g) #index of 2 but does not print it but remembers the pointer is at 2
print(next(g)) #index of 3
#for items in generatorfucn():
#    print(items)