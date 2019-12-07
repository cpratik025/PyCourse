#augmented assignement Operator
c = 5
c += 5+2
print(c)
#Type Conversion
d= type(str(100))
print(d)
#Escape Sequence \ lets python know anything that comes after \ is a string, \t is for tab spacing,\n is for entering the string in new line
weather = '\t It\'s \n"Kind of" Sunny'
print(weather)
#Formated Strings
name = 'Pratik'
age = 27

print('Hi {}, your age is {} years old'.format(name,age))
print('Hi {1}, your age is {0} years old'.format(name,age))
print('Hi {1}, your age is {0} years old'.format('Vaishali',35))

#Same can be done by fstrings in a cleaner way
print(f'Hi {name}, your age is {age} years old')

#String Indexes
s= 'Me Me Me'
#   01234567
print(s[0])
print(s[1])
print(s[2])
print(s)
#Gets the value from Index 0 to 3, s[Start:Stop]
print(s[0:3])

#Gets the value from Index 0 to 8, s[Start:Stop:Stepover] Stepover skips the variable by the no of value provided for stepover
print(s[0:8:2])
#if negative value is provided the array is readed from the back(This is also called as string slicing
print(s[-1::])
print(s[::-1])
print(s[:-1:])

#String Immutability means once a string is assigned we cannot change or assign it to something else. We can change the value of variable s but cannot change or replace the content of it
#s[1]='8'
print(s)

#Built in function
print(len('Hellooooooooooooooooo'))