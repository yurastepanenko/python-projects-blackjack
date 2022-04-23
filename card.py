from constants import SUITS, RANKS
import itertools


class Card:
    def __init__(self):
        suit = None
        points = None
        picture = None
        name = None
        deck_position = None


if __name__ == '__main__':
    print(SUITS)
    print(RANKS)
    print(list(itertools.product(RANKS, SUITS)))



