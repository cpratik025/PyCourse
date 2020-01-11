#open access a file
my_file = open('test.txt')
#read method reads from the file
print(my_file.read())
#this 2 reads wont return nothing as the cursor for open is at the end of the file
print(my_file.read())
print(my_file.read())
#seek method can be used to move the cursor back to the starting of the file
my_file.seek(0)
print(my_file.read())
#readline reads a line at once
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())

my_file.seek(0)
#readlines reads several lines all togather
print(my_file.readlines())
#closes the file
my_file.close()

#another way to open a file is by using with keyword, in this case we do not have to worry about closing a file it closes automatically
with open('test.txt', mode='a') as my_file1: #mode specifies if file can be read mode or write mode
    #r+= gives read and write permission
    #a is append mode which appends the text at the end on the file
    #w is write mode it treats a file as a new and overrides data completly
    my_file1.write('Bas ab han')
    my_file1.readline()