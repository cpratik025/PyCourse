
def highest_even(li):
    evens=[]
    for items in li:
        if items % 2 == 0:
            evens.append(items)
    return max(evens)

print(highest_even([1,2,3,4,10,15,20]))
print(highest_even([1,2,3,4,10,15,20,80]))


st= 'helooooooooo'

