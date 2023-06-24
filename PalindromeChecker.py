#palindrome checker
import re

word = input("Please enter a word: ")

reversed_word = word[::-1]

if reversed_word == word:
    print("is palindrome.")
else:
    print("not a palindrome")