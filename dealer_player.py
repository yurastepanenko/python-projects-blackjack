import gamer
import constants as c
from random import randint


class Dealer_player(gamer.Gamer):
    def __init__(self, Dealer, money):
        super().__init__(Dealer, 1000000)
        self.type = 'd'

    def card_draw(self, deck):
        if self.type == 'd':
            while True:
                print(deck)
                if deck.count_cards == 52:
                    temp_card, point = deck.turn_cards()
                    self.cards.append(temp_card)
                    self.points += point
                    print(f'карты {self.name} = {self.cards}')
                    print(f'сумма карт {self.name} = {self.points}')
                    print(deck)
                    break
                if int(self.points) <= c.DEALER_MAX_POINTS:
                    temp_card, point = deck.turn_cards()
                    self.cards.append(temp_card)
                    self.points += point
                else:
                    # print(f'карты {self.name} = {self.cards}')
                    # print(f'сумма карт {self.name} = {self.points}')
                    # print(deck)
                    break
