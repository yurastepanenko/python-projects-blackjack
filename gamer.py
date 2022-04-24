class Gamer:
    MIN_BET = 5
    MAX_BET = 100

    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __str__(self):
        return f'Игрока зовут {self.name}. У него {self.money} денег!'

    def __repr__(self):
        return f'Игрока зовут {self.name}. У него {self.money} денег!(R)'