basket = [1,2,3,4,5]
print(len(basket))
#appends a value at the end of list
basket.append(100)
print(basket)

#insert data at the end or at any position in the list
basket.insert(4,100)
print(basket)
basket.insert(5,200)
print(basket)
basket.insert(6,300)
print(basket)

#insert modifies the list it does not create a new copy of the list

new_list = basket.insert(8,400)
print(basket)
print(new_list)

#extend adds n number of values at the end of a list

new_test_list = [1,2,3,4,5]

new_tst_list = new_test_list.extend([100,200,300])
print(new_test_list)
print(new_tst_list)

#Removes the item for the index is provided if no value is provided it removes from the end
basket.pop()
print(basket)
basket.pop(4)
print(basket)

new_tst_list=basket.pop(5)
print(new_tst_list)
#Removes the value for index value provided without a value it does not remove
basket.remove(2)
print(basket)

#Provides a index of a value in a list,we can also provide for index values to look from
baskets = ['a','b','c','d','e','f','g','d','m','d']
print(baskets.index('b'))
#the below will search for c from index no 0 to 4 in a list
print(baskets.index('c',0,4))


#clear removes all the elements in a list
basket.clear()
print(basket)

#Python Key words
print(baskets.count('d'))

#sort
brackets = [1,4,2,8,3,6,7,15,11]
#brackets.sort()
#instead of sort method we can also make use of sorted key word still the list will be sorted only thing is it produces new array the brackets list will remain the same but the sorted will create a list of itss own instead of changing the main list
print(sorted(brackets))
print(brackets)

#reverse reverses the list
#we do have copy method which copies a list into a new variable
new_brackets = brackets.copy()
print(new_brackets)
new_brackets.reverse()
print(new_brackets)

#Range prints elements till the range is provided
print(list(range(100)))

#join method joins a list of string or no into one string
sentance=''
print(sentance.join(['hi','my','name','is','Pratik']))

sentance=' '
print(sentance.join(['hi','my','name','is','Pratik']))


#list unpcking

a,b, *others = [1,2,3,3,4,5,6,7,8,9]

print(a)
print(b)
print(others)