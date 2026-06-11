#NUMBER GUESSING GAME

import random
computer = random.randint(1,100)

while True :
    youchoose = int(input("Enter the number between 1-100 : "))

    if youchoose == computer :
        print("This is fire ! you guess it right")
    elif youchoose > 100 or youchoose < 1 :
        print("you are entering an invalid input")
    elif youchoose > computer :
        print("your guess is wrong ---too high")
    elif youchoose < computer :
        print("your guess is wrong --- too low ")