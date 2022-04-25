class Gamer:
    MIN_BET = 5
    MAX_BET = 100

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.cards = []
        self.points = 0

    def __str__(self):
        return f'Игрока зовут {self.name}. У него {self.money} денег! ' \
               f'У него есть карты: {self.cards}' \
               f'Сумма карт = {self.points}\n'

    def __repr__(self):
        return f'Игрока зовут {self.name}. У него {self.money} денег!(R) ' \
               f'У него есть карты: {self.cards}'\
               f'Сумма карт = {self.points}\n'
