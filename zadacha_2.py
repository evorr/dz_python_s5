# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая
# ход друг после друга. Первый ход определяется жеребьёвкой. За один
# ход можно забрать не более чем 28 конфет. Все конфеты оппонента
# достаются сделавшему последний ход. Сколько конфет нужно взять первому
# игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import random

def first_move(player1,player2):
    if random.randint(0,1) == 1:
        print(f'Первым делает ход {player1}')
        return player1, player2
    else:
        print(f'Первым делает ход {player2}')
        return player2, player1

def check_move(candies, all_candies):
    if all_candies<28:
        if 1<=candies<=all_candies:
            return candies
        else:
            new_count = int(input(f'Возьмите от от 1 до {all_candies} конфет: '))
            return check_move(new_count, all_candies)
    else:
        if 1<=candies<=28:
            return candies
        else:
            new_count = int(input('Возьмите от от 1 до 28 конфет: '))
            return check_move(new_count, all_candies)

def move(player, all_candies, hard_level):
    if player == 'Computer':
        if all_candies <= 28:
            count_b = all_candies
            print(f'Computer взял {count_b} конфет')
            return count_b
        else:
            if hard_level == 2 and 30 <= all_candies <= 57:
                count_b = all_candies - 29
                print(f'Computer взял {count_b} конфет')
                return count_b
            else:
                count_b = random.randint(1,28)
                print(f'Computer взял {count_b} конфет')
                return count_b
    else:
        count_p = int(input(f'{player} Введите количество конфет: '))
        cheсked_count_p = check_move(count_p, all_candies)
        return cheсked_count_p

def game ( all_candy, first_player, second_player, level):
    while all_candy!= 0:
        print(f'на столе {all_candy} конфет')
        all_candy -= move(first_player, all_candy, level)
        print(f'на столе {all_candy} конфет')
        if all_candy == 0:
            print(f'{first_player} выиграл')
        if all_candy >0:
            all_candy -= move(second_player,all_candy, level)
            if all_candy == 0:
                print(f'{second_player} выиграл')

choose = input('Играть против компьютера? введите да  или нет : ')
if choose == 'да' or 'lf':
    game_level = int(input('Выберите уровень сложности 1 - лёгкий или 2 - сложный: '))
    player1 = input('введите ваше имя: ')
    bot = 'Computer'
    first_player, second_player = first_move(player1,bot)
else:
    player1 = input('введите имя первого игрока: ')
    player2 = input('введите имя второго игрока: ')
    first_player, second_player = first_move(player1, player2)

all_candy = 322
game(all_candy,first_player, second_player, game_level)




