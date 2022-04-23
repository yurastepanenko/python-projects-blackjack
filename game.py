import constants
from termcolor import colored, cprint


class Game:
    def __int__(self):
        return Game()

    def main_menu(self):
        while True:
            for key in constants.MAIN_MENU_LIST:
                cprint([key, constants.MAIN_MENU_LIST[key]], 'magenta')
            actions = input('\n Выберите действие ')
            if actions == '0':
                break
