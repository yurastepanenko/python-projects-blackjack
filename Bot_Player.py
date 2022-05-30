import Gamer
import Constants as c
from random import randint

class Bot_player(Gamer.Gamer):
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
                    if (int(self.points) > 21):
                        if self.count_A != 0:
                            self.points += self.count_A * 10
                            self.count_A = 0
                        for card in self.cards:
                            if card[0] == 'A' and self.points > 21:
                                self.points -= 10
                                self.count_A += 1
                                print('Пересчитываем туза:)')
                                print(self)
                else:
                    break