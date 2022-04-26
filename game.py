import constants as c
import deck as d
import human_player as hp
import bot_player as bp
import dealer_player
import random
from termcolor import colored, cprint


class Game:
    players = []
    count_players = 1
    iterations = 0

    def __int__(self):
        game = Game()
        return Game()

    def new_deck(self):
        """Создаем колоду"""
        deck = d.Deck()
        deck.prepare_deck()
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
                if ((int(count_bots) >= 0) & (
                        int(count_bots) <= c.MAX_COUNT_BOTS)):
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
        """Процесс игры, взятие карт игроком"""
        while True:
            if player.points > 21:
                cprint(c.GAME_MSG['loos'], 'red')
                #print(player)
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
            cprint(f'**********{player.name}**********', 'green')

    def get_bet(self, player):
        """Прием ставок"""
        if player.type == 'd':
            return
        if player.type == 'h':
            if player.get_balance() < 5:
                Game.players.remove(player)
                game_over = f'{player.name} Проиграл. Закончились деньги!'
                cprint(game_over, 'red')

                if player.type == 'h':
                    return 'game_over'
            while True:
                bet = input(c.GAME_MSG['bet'])
                if bet.isdigit():
                    if (int(bet) >= 5) & (int(bet) <= player.get_balance()):
                        player.set_balance(-int(bet))
                        player.bet = int(bet)
                        break
                    elif (int(bet) >= 5) & (int(bet) > player.get_balance()):
                        cprint(f'Ставка не может превышать ваш баланс' \
                               f' = {player.get_balance()}', 'red')
                    else:
                        cprint(f'Ставка не может быть меньше 5', 'red')
                else:
                    cprint(f'Ставка не может быть меньше 5', 'red')
        else:
            if player.get_balance() < 5:
                Game.players.remove(player)
                game_over = f'{player.name} Проиграл. Закончились деньги!'
                cprint(game_over, 'red')
                return

            while True:
                bet = random.randint(5, 20)
                if bet <= player.get_balance():
                    player.set_balance(-int(bet))
                    player.bet = int(bet)
                    break
        cprint(f'Игрок {player} сделал ставку {bet}', 'magenta')

    def check_result(self, dealer):
        """Проверка результатов игры"""
        for _ in Game.players:
            if _ == dealer:
                continue
            elif (_.points > dealer.points) & (_.points <= 21):
                _.set_balance(int(_.bet)*2)
                print(f'Выиграл ставку {_.name}= {int(_.bet)*2} ,'
                      f'баланс = {_.get_balance()}')
            elif (_.points < dealer.points) & (dealer.points > 21):
                _.set_balance(int(_.bet)*2)
                print(f'Выиграл ставку {_.name} = {int(_.bet)*2} ,'
                      f'баланс = {_.get_balance()}')
            elif (_.points < dealer.points) & (dealer.points <= 21):
                dealer.set_balance(int(_.bet)*2)
                print(f'Выиграл ставку Дилер = {int(_.bet) * 2}  ,'
                      f'баланс = {dealer.get_balance()}')
            elif _.points == dealer.points:
                dealer.set_balance(int(_.bet))
                _.set_balance(int(_.bet))
                print(f'Ничья, {_.name} забирает свою ставку = {int(_.bet)} ,'
                      f'баланс = {_.get_balance()}')

            if _.get_balance() < 5:
                Game.players.remove(_)
                game_over = f'{_.name} Проиграл. Закончились деньги!'
                cprint(game_over, 'red')

                if _.type == 'h':
                    return 'game_over'

        cprint(f"=========Закончилась {Game.iterations} раздача========")

    def save_statistic(self):
        with open(c.FILE_NAME, 'a') as text_file:
            for _ in Game.players:
                if _.type == 'h':
                    text_file.write(f'\nИгрок: {_.name}, за игру изменил свой '
                        f'баланс на {_.get_balance() - int(_.start_money)}, '
                                    f'раздач: {Game.iterations} ')

    def show_statistics(self):
        with open(c.FILE_NAME) as text_file:
            for line in text_file:
                print(line, end='\n')


    def main_menu(self):
        """Главное меню программы"""

        while True:
            for key in c.MAIN_MENU_LIST:
                cprint([key, c.MAIN_MENU_LIST[key]], 'magenta')
            actions = input('\n Выберите действие ')
            if actions == '0':
                break
            if actions == '1':

                Game.iterations = 0
                Game.players = []
                Game.count_players = 1
                deck = None
                cprint(c.GAME_MSG['new_game'], 'magenta')

                # Создаем пользователя человека
                user_name, user_money = Game.get_gamer_info(self)
                Game.create_human_player(self, user_name, user_money)

                # Создаем пользователей ботов + дилера
                Game.create_bots_player(self)
                dealer = dealer_player.Dealer_player('Dealer', c.DEALER_SUM)

                while True:
                    # Создали колоду
                    if deck is not None:
                        deck = None
                    deck = Game.new_deck(self)

                    Game.iterations += 1
                    cprint(f"==============={Game.iterations} раздача========")
                    # Сдаем карты игрокам

                    # Сдаем 1 карту Дилеру
                    dealer.cards = []
                    dealer.points = 0
                    #Game.players.append(dealer)
                    dealer.card_draw(deck)


                    for _ in Game.players:
                        # Обнуляем карты и очки перед раздачей
                        if _ != dealer:
                            _.cards = []
                            _.points = 0

                        # Делаем ставки
                        Game.get_bet(self, _)
                        #print(Game.players)
                        _.card_draw(deck)

                        print(_)
                        if _.type == 'h':
                            Game.play_turn(self, deck, _)
                        cprint(f'**********{_.name}**********', 'green')
                    # Сдаем 1 карту Дилеру
                    dealer.card_draw(deck)


                    # Проверка результатов игры
                    cprint(c.GAME_MSG['check_result'], 'magenta')
                    res = Game.check_result(self, dealer)
                    if res == 'game_over':
                        cprint(c.GAME_MSG['game_over'], 'red')
                        break

                    chose = input('Продолжаем игру? 0 - нет ')
                    if chose == '0':
                        Game.save_statistic(self)
                        break

            if actions == '2':
                Game.show_statistics(self)
