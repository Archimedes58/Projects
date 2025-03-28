import random

def random_Number():
    while True:
        try:
            x = int(input("Type in your lower bound: "))
            y = int(input("Type in your upper bound: "))
            if x ==y:
                print("The lower bound cannot be the same as upper bound")
                continue
            else:
                return random.randint(x,y)
        except ValueError:
            print("Your value must be an integer")

def guess_Number():
    choice = random_Number()
    counter = 7
    while counter >0:
        try:
            if counter>1:

                print(f'You have {counter} attempts left!!!')
            else:
                print(f'You have {counter} attempt left!!!!!!!')
            guess = int(input("Guess the right number: "))
            if guess < choice:
                print("Your guess is too low")
                counter = counter - 1
                continue
            
            elif guess > choice:
                print("Your value is too low")
                counter = counter - 1
                continue
            
            else:
                print("Hurrayyyyyy!!!!!!!!, you guessed right!!!")
                break
            
        except ValueError:
            print("Your guess should be an integer")
    print(f"The right number is {choice}")

        


def main():
    guess_Number()

if __name__ == "__main__":
    main()
            


        