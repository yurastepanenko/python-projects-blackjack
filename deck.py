from constants import SUITS, RANKS
import itertools


class Deck:
    def __init__(self):
        self.count_cards = None
        self.deck_cards = []

    def prepare_deck(self):
        self.count_cards = 52
        self.deck_cards = list(itertools.product(RANKS, SUITS))

    def __str__(self):
        return f'Сейчас в колоде {self.count_cards} карт'
#
# if __name__ == '__main__':
#     deck = Deck()
#     deck.prepare_deck()
#     print(deck.deck_cards, deck.count_cards)
#     print(deck.deck_cards[37], deck.deck_cards[39])