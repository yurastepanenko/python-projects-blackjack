import constants
from termcolor import colored, cprint


class Game:
    def __int__(self):
        return Game()

    def main_menu(self):
        while True:
            for key in constants.MAIN_MENU_LIST:
                print(key, constants.MAIN_MENU_LIST[key])
            actions = input('Выберите действие ')
            if actions == '0':
                break
