
while True:
    try:
        age = int(input('Please Input Your Age: '))
        print(age)
        #This raise over rides the call done after
        raise ValueError('Hey Cut it out')
    except ValueError as err:
        print('Invalid Input:Please Enter Age in No'+err)
        #Continue sends the pointer back to start of program if the error is encountered
        continue
    except ZeroDivisionError as err:
        print('Please Enter age higher then zero'+ err)
    else:
        print('Thank You!!!!!!')
        break
    #Finally Runs Regardless of any problems
    finally:
        print('Ok Its Finally Done')

def sumation(num1,num2):
    try:
        return num1/num2
    except (TypeError,ZeroDivisionError) as err:
        print(err)

sumation(4,0) #Will give divide by Zero Error
sumation('a',2) #will give type error