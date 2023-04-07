# Write your code to expect a terminal of 80 characters wide and 24 rows high
import os
import random


# Function to clear the screen.
def clear_terminal():
    # Clear for windows and linux
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# Make a class for the deck
class Deck():
    # ASCII art for card suits
    suits = ['\u2660', '\u2665', '\u2666', '\u2663']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):    
        self.deck = [(rank, suit) for suit in self.suits for rank in self.ranks]
        # Shuffle the deck        
        random.shuffle(self.deck)

        # Deal cards to dealer and player
        self.dealer_hand = [self.deck.pop(), self.deck.pop()]
        self.player_hand = [self.deck.pop(), self.deck.pop()]

    # Function to create ASCII representation of small cards
    @staticmethod
    def create_small_card_ascii(rank, suit, hidden=False):
        if hidden:
            # ASCII art for hidden card
            card_ascii = [
                f"┌───────┐",
                f"│░░░░░░░│",
                f"│░░░░░░░│",
                f"│░░░░░░░│",
                f"└───────┘"
            ]
        else:
            card_ascii = [
                f"┌───────┐",
                f"│{rank:<2}     │",
                f"│   {suit}   │",
                f"│     {rank:>2}│",
                f"└───────┘"
            ]

        return card_ascii

    # Function to display cards with ASCII representations
    def display_cards(self, title, hand, hide_second_card=False):
        print(f"\n{title}:")
        if hide_second_card:
            # Hide the second card of the hand
            hand_ascii = [self.create_small_card_ascii(card[0], card[1], i == 1) for i, card in enumerate(hand)]
        else:
            hand_ascii = [self.create_small_card_ascii(card[0], card[1]) for card in hand]
        
        card_rows = ["  ".join(lines) for lines in zip(*hand_ascii)]
        for row in card_rows:
            print(row)


def startpg():
    """
    Title using ASCII art
    """
    TITLE = r"""
    ██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗
    ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝
    ██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝ 
    ██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗ 
    ██║  ██║███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗
    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
    """

    # Display the title
    print(TITLE)
    input("\nPress enter to start...")
    

# Call the startpg() function at the beginning of your script
if __name__ == "__main__":
    startpg()

# Get users name.
name = input("\u001b[32mWhat is your name? ")
# Greet the user to the game.
print("\u001b[1mWelcome to \u001b[30mBlack\u001b[31mJack!\u001b[0m")
print(f'Welcome {name} to the game. Good luck!')

# Create a while loop.
while True:
    print("\u001b[42;1m) Play Game")
    print("2) Read The Rules")
    print("3) Exist Game")

    choice = input("Enter menu number please:")
    # Strip method incase the user enters blank spaces
    choice = choice.strip()

    if choice == "1":
        clear_terminal()
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


choice = input("Press enter to start.....")

# Example usage:
# Initialize a new deck
my_deck = Deck()

# Print the dealer's and player's hands with ASCII representations
my_deck.display_cards("Dealer's hand", my_deck.dealer_hand, hide_second_card=True)
my_deck.display_cards("Player's hand", my_deck.player_hand)