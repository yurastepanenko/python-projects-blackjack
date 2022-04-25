class Gamer:
    MIN_BET = 5
    MAX_BET = 100

    def __init__(self, name, money):
        self.name = name
        self.__money = money
        self.cards = []
        self.points = 0
        self.bet = 0

    def __str__(self):
        return f'Игрока зовут {self.name}. У него {self.__money} денег! ' \
               f'У него есть карты: {self.cards}' \
               f'Сумма карт = {self.points}\n'

    def __repr__(self):
        return f'Игрока зовут {self.name}. У него {self.__money} денег!(R) ' \
               f'У него есть карты: {self.cards}'\
               f'Сумма карт = {self.points}\n'

    def get_balance(self):
        return int(self.__money)

    def set_balance(self, money):
        self.__money = int(self.__money) + int(money)
