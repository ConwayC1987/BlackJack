# Modules imported to make the game
# os needed to clear the screen
import os
# random needed to shuffle the deck
import random


# Function to clear the screen.
def clear_terminal():
    # Clear for windows and linux
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Game title made using https://patorjk.com/software/taag/#p=display&h=0&f=Big&t=BlackJack
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

# Ranks and suits for the cards in the deck
RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
SUITS = ('♠', '♣', '♦', '♥')
CARD_ASCII = {
    '♠': '♠',
    '♣': '♣',
    '♦': '♦',
    '♥': '♥',
}

# Function to make the card using ASSCI art idea from https://github.com/zsonnen/blackjack/blob/master/visuals.py
def print_card(card):
    rank, suit = card
    # Hearts and Diamonds are red
    if suit in ['\u2665', '\u2666']:
        # Set suit color to red
        suit_color = '\033[31m'
    else:
        # Set suit color to black or red depending on thesuit
        suit_color = '\033[30m'
    cards = [
        '┌───────┐',
        f'│ {rank:<2}    │',
        '│       │',
        f'│   {suit_color}{CARD_ASCII[suit]}\033[0m   │',
        '│       │',
        f'│    {rank:>2} │',
        '└───────┘',
    ]
    return cards

def print_hand_in_row(hand):
    hand_cards = [[] for _ in range(7)]
    for card in hand:
        if len(card) == 7:
            card_cards = card
        else:
            card_cards = print_card(card)
        for i, line in enumerate(card_cards):
            hand_cards[i].append(line)

    for row in hand_cards:
        print(' '.join(row))

# Calculate the value of a hand and have 2 different values for aces, J,Q,K value is 10
def value(hand):
    total = 0
    aces = 0
    for rank, suit in hand:
        if rank == 'A':
            aces += 1
            total += 11
        elif rank in ('K', 'Q', 'J'):
            total += 10
        else:
            total += int(rank)
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

# Create a deck of cards and shuffle them
def create_deck():
    deck = [(rank, suit) for rank in RANKS for suit in SUITS]
    random.shuffle(deck)
    return deck

# Deal a card from the deck
def deal_card(deck):
    return deck.pop()

# Print the dealer card with 1 card hidden using ASSCI art
def print_dealer_hand(hand, hide_first_card):
    if hide_first_card:
        print("\033[34m\nDealer's hand:\033[0m")
        hidden_card_cards = [
            "┌───────┐",
            "│XXXXXXX│",
            "│XXXXXXX│",
            "│XXXXXXX│",
            "│XXXXXXX│",
            "│XXXXXXX│",
            "└───────┘",
        ]
        print_hand_in_row([hidden_card_cards] + hand[1:])
    else:
        print("\033[34m\nDealer's hand:\033[0m")
        print_hand_in_row(hand)

# Function to check the player hand for a blackjack
def check_blackjack(hand):
    if len(hand) == 2 and value(hand) == 21:
        return True
    return False

# Function to play the game
def play_game():
    # Give the player 100 chips to start the game
    chips = 100
    # If the player chips are all gone the game is over
    while chips > 0:
        # Tell the player their chip count
        print(f"Chips: {chips}")
        # Player has to enter their bet
        bet_input = input("\033[32mEnter bet amount:\033[0m")
        # Error handling: Check if user input is a valid integer
        try:
            # Attempt to convert bet_input to an integer
            bet = int(bet_input)
        except ValueError:
            # Display an error message if bet_input is not a valid integer
            print("Error: Please enter a valid bet amount.")
            continue
        # If the player does not have enough chips
        if bet > chips:
            print("\033[31mYou don't have enough chips.\033[0m")
            continue

        # Create a deck, dealer and player
        deck = create_deck()
        player_hand = [deal_card(deck), deal_card(deck)]
        dealer_hand = [deal_card(deck), deal_card(deck)]
        # Print the dealer cards hiding 1
        print_dealer_hand(dealer_hand, hide_first_card=True)

        # Tell the player their hand total
        while True:
            print(f'\033[94m{name} hand is:\033[0m')
            # Print the player hand in a row
            print_hand_in_row(player_hand)
            # Print the hands value
            print("\033[31mCard value total:\033[0m", value(player_hand))

            # Check for blackjack for player and dealer
            if check_blackjack(player_hand):
                print("You have blackjack!")
                print_dealer_hand(dealer_hand, hide_first_card=False)
                print("You Win!")
                chips += bet
                continue

            # Ask the player if they want to hit or stand
            action = input("\033[94mEnter 'h' to hit or 's' to stand:\033[0m ").lower()
            # If h is selected then add a card
            if action == 'h':
                player_hand.append(deal_card(deck))
                # If player goes over 21 then they are busted
                if value(player_hand) > 21:
                    print("\033[31mBusted!")
                    print("You lose!\033[0m")
                    print_hand_in_row(player_hand)
                    print("\033[31mCard value total:\033[0m", value(player_hand))
                    # Show the dealer cards if the player goes bust
                    print_dealer_hand(dealer_hand, hide_first_card=False)
                    # Chip total will change if player busts
                    chips -= bet
                    break       
            # If player decides to stand
            elif action == 's':
                # When the dealer card is less than the player they get more cards
                while value(dealer_hand) < value(player_hand):
                    dealer_hand.append(deal_card(deck))
                print_dealer_hand(dealer_hand, hide_first_card=False)
                print("Card value total", value(dealer_hand))

                # Check if the dealer has blackjack
                if check_blackjack(dealer_hand):
                    # If the dealer has blackjack
                    print("Dealer has blackjack!")
                    print_dealer_hand(dealer_hand, hide_first_card=False)
                    print("Dealer wins!")
                    chips -= bet
                    break

                # Check if the player has blackjack and the dealer have blackjack
                if check_blackjack(player_hand):
                    print("Player and dealer both have blackjack!")
                    print_dealer_hand(dealer_hand, hide_first_card=False)
                    print("It's a draw!")
                    continue

                # If statement for if the dealer goes bust or who total is closer to 21 deciding the winner
                if value(dealer_hand) > 21 or value(player_hand) > value(dealer_hand):
                    print("You win!")
                    chips += bet
                elif value(player_hand) == value(dealer_hand):
                    print("It's a draw!")
                else:
                    print("You lose!")
                    chips -= bet
                break


# Print the title welcome the player give them an option list of play game, rules or exist the game
if __name__ == '__main__':
    startpg()
    # Get the players name
    name = input("\033[96mWhat is your name?\033[0m")
    print("\u001b[1mWelcome to \u001b[30mBlack\u001b[31mJack!\u001b[0m")
    print(f'\033[96mWelcome {name} to the game. Good luck!\033[0m')
    # Options
    while True:
        print("\033[34m\033[1m1) Play Game")
        print("2) Read The Rules")
        print("3) Exit Game\033[0m\033[21m")

        # Ask the player to select on of the options
        option = input("Enter menu number please:")
        # Strip method incase the user enters blank spaces
        option = option.strip()

        # Option to play the game if they enter 1
        if option == "1":
            clear_terminal()
            play_game()
            continue
        # Game Rules if they enter 2
        if option == "2":
            clear_terminal()
            print("""
                \u001b[41;1mTHE RULES ARE:\u001b[0m \n
                1.Aim of JackJack is to get 21 or as close to as possible.\n
                2.Jacks, kings and queens are worth 10. \n
                3.Ace can be either 1 or 11.\n
                4.You get 2 cards showing dealer will recieve 1 card face down.\n
                5.Choice is to hit or stand until you or the dealer goes bust.\n
                6.You will start with 100 chips and can bet each hand.\n
                7.You will be playing against the computer.""")
        # Option to quit the game
        elif option == "3":
            break
        # Error handling
        else:
            print("Invaild Option")
            print("Options are 1, 2 or 3. Please select one.")
            print("No funny business don't break my code \U0001F607\U0001F600")