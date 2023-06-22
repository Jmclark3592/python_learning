#rock paper scissors: Implement the classic game. 
#The user can choose one of the options and the computer randomly selects one. 
#The program then declares a winner based on the game rules.

import random

def game(player1, player2):
    if player1.lower() == 'rock' and player2 == 'scissors':
        print("You win! Rock smashes scissors")
    elif player1.lower() == 'paper' and player2 == 'rock':
        print("You win! Paper covers rock.")
    elif player1.lower == 'scissors' and player2 == 'paper':
        print("You win! Scissors cuts paper.")
    elif player2 == 'rock' and player1.lower() == 'scissors':
        print("You lose! Rock smashes scissors")
    elif player2 == 'paper' and player1.lower() == 'rock':
        print("You lose! Paper covers rock.")
    elif player2 == 'scissors' and player1.lower() == 'paper':
        print("You lose! Scissors cuts paper.")
    else:
        print("You tied.")

options = ['rock', 'paper', 'scissors']

print("you are playing Rock, Paper, Scissors, please select which option you choose... ")
user_select = input()
comp = random.choice(options)
game(user_select, comp)
