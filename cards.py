def see_card(card):
    suits = "Spades Clubs Diamonds Hearts".split()
    symbols = ['\u2663', '\u2660', '\u2665', '\u2666']
    suit = dict(zip(suits, symbols))

    r = card.rank
    s = suit[card.suit]

    showCard = [
        '╔════╗',
       f'║ {r:<2} ║',
       f'║ {s:>2} ║',
        '╚════╝']

    return showCard
