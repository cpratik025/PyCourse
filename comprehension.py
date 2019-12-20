#can be implemented on list,set,dictionary
mylist = []
for char in 'hello':
    mylist.append(char)
print(mylist)
#format is list -=[param for param in iterable]
mylist1= [char for char in 'hello']
print(mylist1)
mylist2=[item for item in range(0,100)]
mylist3=[item*2 for item in range(0,100)]
print(mylist2)
print(mylist3)