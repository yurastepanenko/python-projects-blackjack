import Gamer
from random import randint


class Human_player(Gamer.Gamer):
    def __init__(self, name, money):
        super().__init__(name, money)
        self.type = 'h'
        self.start_money = money

    def card_draw(self, deck):
        if self.type == 'h':
            if len(self.cards) == 0:
                temp_card, point = deck.turn_cards()
                self.cards.append(temp_card)
                self.points += point
                temp_card, point = deck.turn_cards()
                self.cards.append(temp_card)
                self.points += point
            else:
                temp_card, point = deck.turn_cards()
                self.cards.append(temp_card)
                self.points += point





