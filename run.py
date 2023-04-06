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