#while condition:
#   do something
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]
for item in picture:
    for items in item:
        if(items):
            #end is a parameter provided to print as to define what you want to do after a char is printed
            #by default it take new line by here we specify not to create a new line
            print('*', end="")
        else:
            print(" ", end="")
    print('')