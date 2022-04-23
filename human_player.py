import gamer


class Human_player(gamer.Gamer):
    def __init__(self, name, money):
        super().__init__(name, money)

    # def __str__(self):
    #     return f'Игрока зовут {self.name}. У него {self.money} денег!'

