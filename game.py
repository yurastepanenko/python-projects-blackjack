import constants as c
import deck as d
import human_player as hp
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
        '''Считываем информацию об игроке'''
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
        return user_name, user_money

    def create_human_player(self, user_name, user_money):
        player = hp.Human_player(user_name, user_money)
        print(player)
        return player

    def main_menu(self):
        '''Главное меню программы'''
        while True:
            for key in c.MAIN_MENU_LIST:
                cprint([key, c.MAIN_MENU_LIST[key]], 'magenta')
            actions = input('\n Выберите действие ')
            if actions == '0':
                break
            if actions == '1':
                deck = Game.new_deck(self)
                user_name, user_money = Game.get_gamer_info(self)
                Game.create_human_player(self, user_name, user_money)
                #print(deck)

