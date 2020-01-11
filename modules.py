from collections import Counter,defaultdict,OrderedDict
import datetime #Helps in using and menipulating date time values
from array import array
#Counter module counts the occurance of a no or string in a list
li=[1,2,3,4,5,6,6,6,7]

sentance = 'Helo How are you helo'
print(Counter(li))
print(Counter(sentance))


#default dict returns a int when a key that does not exist in dictionary is called
dic = defaultdict(int,{'a':1, 'b':2})
dic1 = defaultdict(lambda :5,{'a':1, 'b':2}) #if a non existing fuction is called it would return 5 or what ever is provided to default
dic2 = defaultdict(lambda :'Does Not Exists',{'a':1, 'b':2}) #if a non existing fuction is called it would return 5 or what ever is provided to default
print(dic['a'])
print(dic['c']) #Calling key c would result into 0 as it does not exist in dictionary
print(dic1['c']) #Would return 5 as c does not exists
print(dic2['c']) #Would return string does not exists as c does not exists

#Ordered Dict checks for the order in which the elements are inserted in a dictionary
dictt = OrderedDict()
dictt['a'] = 1
dictt['b'] = 2

dictt2 = OrderedDict()
dictt2['a'] = 1
dictt2['b'] = 2

print(dictt == dictt2) #Would return true as the order of insertion is same for both dictionary


dictt3 = OrderedDict()
dictt3['a'] = 1
dictt3['b'] = 2

dictt4 = OrderedDict()
dictt4['b'] = 2
dictt4['a'] = 1

print(dictt3 == dictt4) #Would return false as the order of insertion is not same for both


print(datetime.time(5,45,6)) #Prints time as 5:45:06
print(datetime.date.today()) #Prints todays date
