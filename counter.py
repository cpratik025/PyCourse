my_list = [1,2,3,4,5,6,7,8,9,10]
counter = 0

for item in my_list:
    counter = counter + item
print(counter)

#range(start,stop)

for item in range(0,100):
    print(item)
#range(start,stop,overlap)

for item in range(0,100,2):
    print(item)

#enumerate() provides with index and value present in that index. Works with set list tuple

for index,item in enumerate(my_list):
    print(index, item)

for index,item in enumerate('hellloooooooooo'):
    print(index, item)

for item, index in enumerate(set(range(0,100,50))):
    print(item, index)

for item, index in enumerate(set(range(100))):
    if item == 50:
        print(f"Index of 50 is :{index}")