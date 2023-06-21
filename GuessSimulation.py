#number guess simulation

import random

def guess_number():
    r = random.randint(1, 20)
    return r

r = guess_number()
count = 0

while True:
    if count == 3:
        print("too many guesses! You lose.")
        print(f"The number was actually {str(r)}")
        break
    guess = int(input("guess a number between 1 and 20: "))
    if guess < r:
        print("number is too low")
        count = count + 1
    if guess > r:
        print("number is too high")
        count = count + 1
    if guess == r:
        print("You guessed it!")
        print(f"It took you {count + 1} guesses.")
        break


    
