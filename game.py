import constants as c
import deck as d
import human_player as hp
import bot_player as bp
import dealer_player
import random
from termcolor import colored, cprint
import main as m


class Game:
    players = []
    count_players = 1
    def __int__(self):
        game = Game()
        return Game()

    def new_deck(self):
        """Создаем колоду"""
        deck = d.Deck()
        deck.prepare_deck()
        #print(deck.deck_cards[37], deck.deck_cards[39])
        return deck

    def get_gamer_info(self):
        """Считываем информацию об игроке"""
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
        """создаем нового игрока"""
        player = hp.Human_player(user_name, user_money)
        Game.players.append(player)
        return player

    def create_bots_player(self):
        """Ввод кол-ва ботов и их создание"""
        while True:
            count_bots = input(c.GAME_MSG['cnt_bots'])
            if count_bots.isdigit():
                if ((int(count_bots) >= 0) & (int(count_bots) <= c.MAX_COUNT_BOTS)):
                    break
            cprint(c.GAME_MSG['err_cnt_bots'], 'red')

        if int(count_bots) == 0:
            return
        for _ in range(int(count_bots)):
            bot_name = random.choice(c.BOT_NAMES)
            c.BOT_NAMES.remove(bot_name)
            bot = bp.Bot_player(bot_name, c.BOT_MONEY)
            print(bot)
            Game.players.append(bot)
            Game.count_players += 1

    def play_turn(self, deck, player):
        while True:
            if player.points > 21:
                cprint(c.GAME_MSG['loos'], 'red')
                print(player)
                break
            elif player.points == 21:
                cprint(c.GAME_MSG['stop'], 'yellow')
                break
            cprint(c.GAME_MSG['new_card'], 'magenta')
            actions = input('\n Выберите действие ')
            if actions == '0':
                break
            elif actions == '1':
                temp_card, point = deck.turn_cards()
                player.cards.append(temp_card)
                player.points += point
            print(player)

    def get_bet(self, player):
        if hasattr(player, 'type'):
            while True:
                bet = input(c.GAME_MSG['bet'])
                if bet.isdigit():
                    if int(bet) >= 5:
                        player.set_balance(-int(bet))
                        break
        else:
            bet = random.randint(5, 20)
        cprint(c.GAME_MSG['get_bet'], 'magenta')



    def main_menu(self):
        """Главное меню программы"""

        while True:
            for key in c.MAIN_MENU_LIST:
                cprint([key, c.MAIN_MENU_LIST[key]], 'magenta')
            actions = input('\n Выберите действие ')
            if actions == '0':
                break
            if actions == '1':
                cprint(c.GAME_MSG['new_game'], 'magenta')
                # Создали колоду
                deck = Game.new_deck(self)

                # Создаем пользователя человека
                user_name, user_money = Game.get_gamer_info(self)
                Game.create_human_player(self, user_name, user_money)

                # Создаем пользователей ботов + дилера
                Game.create_bots_player(self)
                dealer = dealer_player.Dealer_player('Dealer', 1000000)


                # Сдаем карты игрокам
                for _ in Game.players:
                    #Делаем ставки
                    Game.get_bet(self, _)

                    temp_card, point = deck.turn_cards()
                    _.cards.append(temp_card)
                    _.points += point
                    temp_card, point = deck.turn_cards()
                    _.cards.append(temp_card)
                    _.points += point
                    print(_)
                    if hasattr(_, 'type'):
                        Game.play_turn(self, deck, _)


                # Сдаем 1 карту Дилеру
                Game.players.append(dealer)
                temp_card, point = deck.turn_cards()
                dealer.cards.append(temp_card)
                dealer.points += point
                print(dealer)

                # Опрос пользователя после раздачи карт
                # print(Game.players)
                # print(Game.players['h'])
                # if hasattr(_, type):
                #     Game.play_turn(self, deck)





