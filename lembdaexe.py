mylist= [1,2,3,4]
newlist= list(map(lambda item:item**2,mylist))
print(newlist)

a=[(0,2),(4,3),(9,9),(10,-1)]

a.sort(key=lambda x:x[1])
print(a)