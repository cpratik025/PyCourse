def atm():
    currentbal = int(input('Please Enter a Value'))
    withdraw = int(input('Enter the withdrawal Amount'))
    exactfee = 0.50

    if withdraw % 5 == 0:
        newbal = currentbal -(withdraw+exactfee)
        print(newbal)
    else:
        print(currentbal)

atm()