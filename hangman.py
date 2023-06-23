#hangman: Implement the classic word guessing game. 
#You'll need a list of words and the ability to check if a user's guess is in the chosen word.

import random

possibilities = ['concatenate', 'dictionary', 'database', 'function', 'expression', 'object', 'method', 'immutable', 'parameter', 'variable', 'python']
updated_word = []

hangman_word = random.choice(possibilities)
hangman_letters = list(hangman_word)
length = len(hangman_letters)
length_in_asterisk = '* ' * length
updated_word = length_in_asterisk
guessed_word = list(updated_word) #word stored as asterisks
count = 0




def check(guess):
    if guess in hangman_letters:
        for letter in range(len(hangman_letters)):