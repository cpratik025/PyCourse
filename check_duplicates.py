my_list = ['a','b','c','d','b','c','d','l','m','n','n']
duplicates=[]
for item in my_list:
    if my_list.count(item) > 1:
        if item not in duplicates:
            duplicates.append(item)

print(duplicates)
