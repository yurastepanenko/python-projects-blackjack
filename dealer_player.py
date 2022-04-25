import gamer
import constants as c


class Dealer_player(gamer.Gamer):
    def __init__(self, Dealer, money):
        super().__init__(Dealer, 1000000)

    def card_draw(self, deck):
        while True:
            # print(self.points)
            # print(c.DEALER_MAX_POINTS)
            # print(int(self.points) <= c.DEALER_MAX_POINTS)
            if int(self.points) <= c.DEALER_MAX_POINTS:
                temp_card, point = deck.turn_cards()
                self.cards.append(temp_card)
                self.points += point
                print(f'карты диллера = {self.cards}')
                print(f'сумма карт диллера = {self.points}')
            else:
                break
