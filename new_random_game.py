from random import randint

def randomint(guess, answer):
    if 0 < guess <11:
            if guess == answer:
                print("You have gussed the no correctly")
                return
            else:
                print(f"Gussed no is incorrect, the correct no was {answer}")
                return False
    elif guess >= 11:
        print('Entered Value Exceded the no allowed')
        return False


answer = randint(1, 10)
if __name__ == '__main__':
    while True:
             try:
                guess = int(input("Please guess a no that you want between 1 to 10: "))
                if(randomint(guess,answer)):
                    break
             except ValueError:
               print("Please Enter a Valid No")
               continue



