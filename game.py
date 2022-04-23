import constants
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

    def get_gamer_info(self):
        pass


    def main_menu(self):
        while True:
            for key in constants.MAIN_MENU_LIST:
                cprint([key, constants.MAIN_MENU_LIST[key]], 'magenta')
            actions = input('\n Выберите действие ')
            if actions == '0':
                break
            if actions == '1':
                Game.new_deck(self)

