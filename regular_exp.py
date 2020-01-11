import re

string = "this is a simple string message by Pratik cHORSIYa, this is not A valid String"


d = re.search('this',string)
#Gives where does the string starts and ends indexes
print(d.span)
#Gives where does a string starts
print(d.start)
print(d.end())
#returns the part of the string where there was a match it returns match object or none
print(d.group())


#compile allows giving a patter
pattern = re.compile('this')
#Finds all the occurance of the mentioned string into string key which are exeact match
a=pattern.findall(string)
print(a)
#Finds the pattern in the string and gives the first match
b=pattern.search(string)
print(b.group())
#Finds the exeact match of the pattern and returns it instead of part of string
c= pattern.fullmatch(string)
print(c)
e = pattern.match(string)
print(e)