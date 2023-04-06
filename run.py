# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import os
# import random


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
print(f'Welcome {name} to the game. Good luck!')

# Create a while loop 
while True:
    print("1) Play Game")
    print("2) Read The Rules")
    print("3) Exist Game")

    choice = input("Enter menu number please:")
    # Strip method incase the user enters blank spaces
    choice = choice.strip()

    if choice == "1":
        PLAYING = True
        break
    if choice == "2":
        clear_terminal()
        print("""
            \u001b[41;1mTHE RULES ARE:\u001b[0m \n
            1.Aim of JackJack is to get 21 or as close to as possible.\n
            2.Jacks, kings and queens are worth 10. \n
            3.Ace can be either 1 or 11.\n
            4.You get 2 cards face up, dealer will recieve 1 card face down.\n
            5.Choice is to hit or stand until you or the dealer goes bust.\n
            6.You will start with 100 chips and can bet each hand.\n
            7.You will be playing against the computer.""")
    elif choice == "3":
        break
    else:
        print("Invaild Option")
        print("Options are 1, 2 or 3. Please select one.")
        print("No funny business trying to break my code \U0001F607\U0001F600")


# Make a class for the deck
class Deck:
    suits = "Spades Clubs Diamonds Hearts".split()
    symbols = ['\u2663', '\u2660', '\u2665', '\u2666']
    rank = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
    values = ["2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11]

    def shuffle(self):
        random.shuffle(self.cards)

    def _deck(self, decks=1):
        self.length = len(self)
        self.cards = [Card(value, suit) for suit in self.suits for value in self.values] * self.decks

    def join(self):
        return len(self.cards)
    # Idea from len and https://www.pythonmorsels.com/making-the-len-function-work-on-your-python-objects/
    def __len__(self):
        return len(self.cards)
    # The method allows instances of this class to be indexed using square brackets
    def __getitem__(self, position):
        return self.cards[position]
    #
     def __setitem__(self, position, value):
        self.cards[position] = value 
    # Method used to represent a class’s objects as a string
    def __repr__(self):
        return "Deck()\n" + ''.join(f"({card.value}-{card.suit})" for card in self.cards)
    #
    def draw_card(self):
        return self.cards.pop()

    # Reset the deck
    def reset(self):
        self.cards = [Card(value, suit) for suit in self.suits for value in self.values] * self.decks






