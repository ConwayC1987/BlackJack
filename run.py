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


def startpg():
    """
    Title using ASCII art
    """
    TITLE = r"""
    ██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗
    ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝
    ██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝ 
    ██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗ 
    ███████║███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗
    ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
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
    print("1) Play Game")
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


# Make a class for the deck
class Deck:
    suits = ['\u2660', '\u2665', '\u2666', '\u2663']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self):
        self.reset_deck()

    # Function to reset the deck
    def reset_deck(self):
        self.deck = [f"{rank}{suit}" for suit in self.suits for rank in self.ranks]
        # Shuffle the deck
        random.shuffle(self.deck)

    # Function to deal a card from the deck
    def deal_card(self):
        return self.deck.pop()

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
            # Hearts and Diamonds are red
            if suit in ['\u2665', '\u2666']:
                # Set suit color to red
                suit_color = '\033[31m'
            else:
                # Set suit color to black
                suit_color = '\033[30m'
            if rank == 'A':
                # ASCII art for Ace
                card_ascii = [
                    f"┌───────┐",
                    f"│A      │",
                    f"│{suit_color}   {suit}   \033[0m│",
                    f"│     A │",
                    f"└───────┘"
                ]
            else:
                # ASCII art for other cards
                card_ascii = [
                    f"┌───────┐",
                    f"│{rank:<2}     │",
                    f"│{suit_color}   {suit}   \033[0m│",
                    f"│     {rank:>2}│",
                    f"└───────┘"
                ]

        return card_ascii


# Class for representing a playing card
class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    # Function for getting the string representation of the card
    def __str__(self):
        if self.rank == 'A':
            return 'A'  # Return 'A' for Ace
        if self.rank == 'J':
            return 'J'
        if self.rank == 'Q':
            return 'Q'
        elif self.rank == 'K':
            return 'K'
        else:
            return self.rank


# Class for the player
class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    # Function that will reset the player's hand.
    def reset_hand(self):
        self.hand = []
        self.score = 0

    # Function to add a card to player's hand
    def add_card(self, card):
        self.hand.append(card)

    # Function for calculating the player's score
    def calculate_score(self, hide_second_card=False):
        self.score = 0
        aces = 0
        for i, card in enumerate(self.hand):
            if hide_second_card and i == 1:
                continue  # Skip hidden card of dealer
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

        # Check for bust (score > 21 with no aces remaining)
        if self.score > 21 and aces == 0:
            self.score -= 10

        return self.score


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

    if not hide_second_card:
        # Print the total score
        score = calculate_score(hand)
        print("Total Score:", score)

        # Check if the score is over 21 and adjust for aces
        aces = sum(card[0] == 'A' for card in hand)
        while score > 21 and aces > 0:
            score -= 10
            aces -= 1


# Function to calculate the total score of a hand
def calculate_score(hand):
    score = 0
    aces = 0
    for card in hand:
        rank = card[0]
        if rank.isdigit():
            score += int(rank)
        elif rank in ['J', 'Q', 'K']:
            score += 10
        elif rank == 'A':
            score += 11
            aces += 1

    while score > 21:
        print("You busted")
        break
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1

    return score


# Function to check if player wants to hit or stay
def ask_hit_or_stand():
    while True:
        choice = input("\nDo you want to Hit or Stay? (h/s) ")
        if choice in ['h', 's']:
            return choice
        else:
            print("Invalid response!")
            print("Press h to hit or s to stay.")


# Play again function for the player
def ask_play_again():
    while True:
        choice = input("\nDo you want to play again? (y/n) ")
        if choice in ['y', 'n']:
            return choice
        else:
            print("Invalid choice! Enter 'y' to play again or 'n' to quit.")


# Main game loop
while True:
    clear_terminal()
    print("_" * 40)

    # Create a deck, dealer and players
    deck = Deck()
    player = Player("Player")
    dealer = Player("Dealer")

    # Add 4 card to the screen
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())

    # Display the initial hands
    display_cards("Your hand is", player.hand)
    display_cards("The Dealer's hand is", dealer.hand, True)

    # Players choice to hit or stand
    while True:
        choice = ask_hit_or_stand()
        if choice == 'h':
            player.add_card(deck.deal_card())
            display_cards("Your hand is", player.hand)
            if calculate_score(player.hand) > 21:
                print("Bust! You Lose")
                break
        else:
            break

    # Dealer's turn
    while dealer.score < 17:
        dealer.add_card(deck.deal_card())
        dealer.calculate_score()
        if dealer.score > 21:
            print("Dealer Bust! You Win")
            break

    # Compare scores and determine the winner
    if player.score <= 21 and dealer.score <= 21:
        if player.score > dealer.score:
            print("You Win!")
        elif player.score < dealer.score:
            print("You Lose!")
        else:
            print("It's a Tie!")
    elif player.score <= 21 and dealer.score > 21:
        print("Dealer Bust! You Win!")
    elif player.score > 21 and dealer.score <= 21:
        print("Bust! You Lose!")
    else:
        print("It's a Tie!")

    # Display the final hands
    display_cards("The Dealer's final hand is", dealer.hand)
    display_cards("Your final hand is", player.hand)

    # Ask if the player wants to play again
    play_again = ask_play_again()
    if play_again == 'n':
        break
print("Thank you for playing! Goodbye!")