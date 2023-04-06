# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import os
#import random


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

# Create a while loop 
while True:
    print("1) Play Game")
    print("2) Read The Rules")
    print("3) Exist Game")

    choice = input("Enter menu number please:")

    choice = choice.strip()

    if (choice == "1"):
        PLAYING = True
        break
    elif (choice == "2"):
        clear_terminal()
        print("""
            \u001b[41;1mThe rules are:\u001b[0m
            1.Aim of JackJack is to get 21 or as close to as possible\n
            2.Jacks, kings and queens are worth 10 \n
            3.Ace can be either 1 or 11\n
            4.You get 2 cards face up, dealer will recieve 1 card face down\n
            5.The choice is to hit or stand until you or the dealer goes bust\n
            6.You will start with 100 chips and can bet each hand\n
            7.You will be playing against the computer""")
    elif (choice == "3"):
        break


