import gamer
import constants as c
from random import randint

class Bot_player(gamer.Gamer):
    def __init__(self, name, money):
        super().__init__(name, money)
        self.type = 'b'

    def card_draw(self, deck):
        if self.type == 'b':
            while True:
                # Для более "человеческого поведения плавающее кол-во очков"
                rand_points = randint(c.BOT_MIN_POINTS, c.BOT_MAX_POINTS)
                if int(self.points) <= rand_points:
                    temp_card, point = deck.turn_cards()
                    self.cards.append(temp_card)
                    self.points += point
                    # print(f'карты {self.name} = {self.cards}')
                    # print(f'сумма карт {self.name} = {self.points}')
                else:
                    break