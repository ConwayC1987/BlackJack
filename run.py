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
RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
SUITS = ('♠', '♣', '♦', '♥')
CARD_ASCII = {
    '♠': '♠',
    '♣': '♣',
    '♦': '♦',
    '♥': '♥',
}

def print_card(card):
    rank, suit = card
    color = 'black' if suit in ('♠', '♣') else 'red'
    lines = [
        '┌───────┐',
        f'│ {rank:<2}    │',
        '│       │',
        f'│   \033[31m{CARD_ASCII[suit]}\033[0m   │' if color == 'red' else f'│   {CARD_ASCII[suit]}   │',  # Update color for red suits
        '│       │',
        f'│    {rank:>2} │',
        '└───────┘',
    ]
    print('\n'.join(lines))

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

def create_deck():
    deck = [(rank, suit) for rank in RANKS for suit in SUITS]
    random.shuffle(deck)
    return deck

def deal_card(deck):
    return deck.pop()

def print_dealer_hand(hand, hide_first_card):
    if hide_first_card:
        print("Dealer's hand:")
        print("┌───────┐")
        print("│XXXXXXX│")
        print("│XXXXXXX│")
        print("│XXXXXXX│")
        print("│XXXXXXX│")
        print("│XXXXXXX│")
        print("└───────┘")
        for card in hand[1:]:
            print_card(card)
    else:
        print("\nDealer's hand:")
        for card in hand:
            print_card(card)

def play_game():
    chips = 100

    while chips > 0:
        print(f"Chips: {chips}")
        bet = int(input("Enter bet amount: "))
        if bet > chips:
            print("You don't have enough chips.")
            continue

        deck = create_deck()
        player_hand = [deal_card(deck), deal_card(deck)]
        dealer_hand = [deal_card(deck), deal_card(deck)]

        print_dealer_hand(dealer_hand, hide_first_card=True)

        while True:
            print("\nPlayer's hand:")
            for card in player_hand:
                print_card(card)
            print("Value:", value(player_hand))

            action = input("Enter 'h' to hit or 's' to stand: ").lower()
            if action == 'h':
                player_hand.append(deal_card(deck))
                if value(player_hand) > 21:
                    print("Busted!")
                    for card in player_hand:
                        print_card(card)
                    print("Value:", value(player_hand))
                    print_dealer_hand(dealer_hand, hide_first_card=False)
                    chips -= bet
                    break
            elif action == 's':
                while value(dealer_hand) < 17:
                    dealer_hand.append(deal_card(deck))
                print_dealer_hand(dealer_hand, hide_first_card=False)
                print("Value:", value(dealer_hand))

                if value(dealer_hand) > 21 or value(player_hand) > value(dealer_hand):
                    print("You win!")
                    chips += bet
                elif value(player_hand) == value(dealer_hand):
                    print("It's a draw!")
                else:
                    print("You lose!")
                    chips -= bet
                break

if __name__ == '__main__':
  startpg()
  name = input("What is your name?")
  print("\u001b[1mWelcome to \u001b[30mBlack\u001b[31mJack!\u001b[0m")
  print(f'Welcome {name} to the game. Good luck!')
  while True:
    print("1) Play Game")
    print("2) Read The Rules")
    print("3) Exit Game")

    option = input("Enter menu number please:")
    # Strip method incase the user enters blank spaces
    option = option.strip()

    if option == "1":
        clear_terminal()
        play_game()
        continue
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