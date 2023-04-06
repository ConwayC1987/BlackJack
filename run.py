# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import os
import random


# Function to clear the screen 
def clear_terminal():
    # For windows
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# Page to greet the user to the game.
# Get users name.
print("\u001b[1mWelcome to \u001b[30mBlack\u001b[31mJack!")
name = input("\u001b[32mWhat is your name? ")
print(f'Welcome {name} to game. Good luck!')

