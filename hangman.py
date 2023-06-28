#hangman: Implement the classic word guessing game. 
#You'll need a list of words and the ability to check if a user's guess is in the chosen word.

import random

possibilities = ['concatenate', 'dictionary', 'database', 'function', 'expression', 'object', 'method', 'immutable', 'parameter', 'variable', 'python']
updated_word = []

hangman_word = random.choice(possibilities)
hangman_letters = list(hangman_word)

guessed_word = ['*'] * len(hangman_word)
count = 0

def check(guess):
    global count
    if guess in hangman_letters:
        for i, letter in enumerate(hangman_letters):
            if letter == guess:
                guessed_word[i] = guess
    else:
        count += 1
    if count >= 6:
        print("sorry too many guesses")
        quit()

while True:
    print(' '.join(guessed_word))
    guess = input("Guess a letter: ")
    check(guess)
    if '*' not in guessed_word:
        print(f"Congrats! You've guessed the word!")
        print(' '.join(guessed_word))
        break
    


