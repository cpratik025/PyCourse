from random import randint
def randomint():
    while True:
        fixedno = randint(1, 10)

        try:
            userin = int(input("Please guess a no that you want between 1 to 10: "))
            if userin>0 and userin<10:
                if fixedno == userin:
                    print("You have gussed the no correctly")
                    break
                else:
                    print(f"Gussed no is incorrect, the correct no was {fixedno}")
                    continue


        except ValueError:
                print("Please Enter a Valid No")
                continue

randomint()

