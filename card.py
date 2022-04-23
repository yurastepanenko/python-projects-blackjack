from constants import SUITS, RANKS
import itertools


class Card:
    def __init__(self):
        self.suit = None
        self.points = None
        self.picture = None
        self.name = None
        self.deck_position = None


if __name__ == '__main__':
    print(SUITS)
    print(RANKS)
    print(list(itertools.product(RANKS, SUITS)))



