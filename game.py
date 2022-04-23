import constants as c
import deck as d
from termcolor import colored, cprint


class Game:
    def __int__(self):
        return Game()

    def new_deck(self):
        '''Создаем колоду'''
        print('началась новая игра:)')
        deck = d.Deck()
        deck.prepare_deck()
        print(deck.deck_cards[37], deck.deck_cards[39])
        return deck

    def get_gamer_info(self):
        while True:
            user_name = input(c.GAME_MSG['name'])
            if user_name:
                break
        while True:
            user_money = input(c.GAME_MSG['money'])
            if user_money.isdigit():
                if int(user_money) >= 5:
                    break
                else:
                    cprint(c.GAME_MSG['min_money'], 'yellow')

    def main_menu(self):
        while True:
            for key in c.MAIN_MENU_LIST:
                cprint([key, c.MAIN_MENU_LIST[key]], 'magenta')
            actions = input('\n Выберите действие ')
            if actions == '0':
                break
            if actions == '1':
                deck = Game.new_deck(self)
                Game.get_gamer_info(self)
                #print(deck)

