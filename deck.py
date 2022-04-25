from constants import SUITS, RANKS
import itertools
import random


class Deck:
    def __init__(self):
        self.count_cards = None
        self.deck_cards = []

    def prepare_deck(self):
        self.count_cards = 52
        self.deck_cards = list(itertools.product(RANKS, SUITS))

    def __str__(self):
        return f'Сейчас в колоде {self.count_cards} карт'

    def turn_cards(self):
        """Выдать карту"""
        temp_card = random.choice(self.deck_cards)
        #print(temp_card)
        self.deck_cards.remove(temp_card)
        self.count_cards -= 1

        if temp_card[0].isdigit() == True:
            point = int(temp_card[0])
            #print(point)
        elif temp_card[0] in ('J', 'Q', 'K'):
            point = 10
            #print(point)
        elif temp_card[0] in ('A'):
            point = 11
            #print(point)
        return temp_card, point

# if __name__ == '__main__':
#     deck = Deck()
#     deck.prepare_deck()
#     # print(deck.deck_cards, deck.count_cards)
#     # print(deck.deck_cards[37], deck.deck_cards[39])
#     temp = deck.turn_cards()
#     print(temp[0])
#     if temp[0].isdigit() == True:
#         point = int(temp[0])
#         print(point)
#     elif temp[0] in ('J', 'Q', 'K'):
#         point = 10
#         print(point)
#     elif temp[0] in ('A'):
#         point = 11
#         print(point)
