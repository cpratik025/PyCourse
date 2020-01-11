try:
    with open('app/test1.py','r') as myfile:
        print(myfile.readline())
except FileNotFoundError as err:
    print('File Not Found')
    raise err
except IOError as err:
    raise err