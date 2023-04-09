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

    # Function to reset the deck.
    def _init_(self):
        self.reset_deck()

    # Fuction to reset the deck
    def reset_deck(self):
        self.deck = [(rank, suit) for suit in self.suits for rank in self.ranks]
        # Shuffle the deck        
        random.shuffle(self.deck)

    # Function to deal a card from the deck
    def deal_card(self):
        return self.deck.pop()

    # Fuction to deal a cards from the deck.
    @staticmethod
    def make_cards_ascii(rank, suit, hidden=False):
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

        return


# Class for the player
class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    # Fuction that will reset the players hand.
    def reset_hand(self):
        self.hand = []
        self.score = 0

    # Function to add cards to players hand.
    def add_card(self, card):
        self.hand.append(deck)

    # Function for calculating the player's score
    def calculate_score(self):
        self.score = 0
        aces = 0
        for card in self.hand:
            rank = card[0]
            if rank.isdigit():
                self.score += int(rank)
            elif rank in ['J', 'Q', 'K']:
                self.score += 10
            elif rank == 'A':
                self.score += 11
                aces += 1    

        while self.score > 21 and aces > 0:
            self.score -= 10
            aces -= 1


# Function to display cards with ASCII art
def display_cards(title, hand, hide_second_card=False):
    print(f"\n{title}:")
    if hide_second_card:
        # Dealers hidden card
        hand_ascii = [Deck.make_cards_ascii(card[0], card[1], i == 1) for i, card in enumerate(hand)]
    else:
        hand_ascii = [Deck.make_cards_ascii(card[0], card[1]) for card in hand]

    card_rows = [" ".join(lines) for lines in zip(*hand_ascii)]

    # Print the cards in a row
    for row in card_rows:
        print(row)


# Function to check if player wants to hit or stay
def ask_hit_or_stand():
    while True:
        choice = input("\nDo you want to Hit or Stay?")
        if choice in ['h', 's']:
            return choice
        else:
            print("Invalid response!")
            print("Press h for another card or s to stay.")
            print("After you make choice click Enter\u001b[31m\u001b[0m	")


# Play again function for the player
def ask_play_again():
    while True:
        choice = input("\nDo you to play again? (y/n)")
        if choice in ['y', 'n']:
            return choice
        else:
            print("Invalid choice! Please enter 'y' to Play Again or 'n' to Quit.")


# Main game loop
while True:
    clear_terminal()
    print("Good Luck")
    print("_" * 75)

    # Create a deck, dealer and players
    deck = Deck()
    player = Player("Player")
    dealer = Player("Dealer")
    # Add 4 card to the screen
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())

    # Display the hand with 1 of dealer cards hidden
    display_cards("Your hand is", player.hand)
    display_cards("The Dealer hand is", dealer.hand, True)

    # Players choice to hit or stand
    while True:
        choice = ask_hit_or_stand()
        if choice == 'h':
            player.add_card(deck.deal_card())
            display_cards("Your hand is", player.hand)
            player.calculate_score()
            if player.score > 21:
                print("Bust! You Lose")
                break
        else:
            break


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

    option = input("Enter menu number please:")
    # Strip method incase the user enters blank spaces
    option = option.strip()

    if option == "1":
        clear_terminal()
        PLAYING = True
        break
    if option == "2":
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
    elif option == "3":
        break
    else:
        print("Invaild Option")
        print("Options are 1, 2 or 3. Please select one.")
        print("No funny business trying to break my code \U0001F607\U0001F600")


start = input("Press enter to start.....")

# Initialize a new deck
my_deck = Deck()

# Print the dealer's and player's hands with ASCII representations
my_deck.display_cards("Dealer's hand", my_deck.dealer_hand, hide_second_card=True)
my_deck.display_cards("Player's hand", my_deck.player_hand)
# Deal cards to dealer and player
        # self.dealer_hand = [self.deck.pop(), self.deck.pop()]
        # self.player_hand = [self.deck.pop(), self.deck.pop()]