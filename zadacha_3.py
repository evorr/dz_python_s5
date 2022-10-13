# Создайте программу для игры в ""Крестики-нолики"
import random
def create_grid():
    weight, height = 3,3
    grid = [[1 for x in range (weight)] for y in range (height)]
    k = 1
    for j in range (len(grid)):
        for i in range (len(grid)):
            grid[j][i] = i+k
        k+=3
    return grid

def print_grid(grid):
    for i in range (len(grid)):
        print(grid[i])

def first_move(player1,player2):
    if random.randint(0,1) == 1:
        print(f'Первым делает ход {player1} - X')
        return player1, player2
    else:
        print(f'Первым делает ход {player2} - X')
        return player2, player1


def get_number(player, used_numders):
    if player == 'Computer':
        number_comp = random.randint(1,9)
        if number_comp not in used_numders:
            print('Ходит Computer:')
            return number_comp
        else:
            return get_number(player, used_numders)
    else:
        number_user = int(input('Введите номер клетки: '))
        return number_user

def replace (number, matrix,value):
    for j in range(len(matrix)):
        for i in range(len(matrix)):
            if matrix[j][i] == number:
                matrix[j][i] = value

def check(matrix, used_numb):
    if len(used_numb) == 9:
        return 'end'
    else:
        for j in range(len(matrix)):
            for i in range(len(matrix)):
                if matrix[j][i] == matrix[j][i+1] == matrix[j][i+2]:
                    return 'end'
                elif matrix[j][i] == matrix[j+1][i] == matrix[j+2][i]:
                    return 'end'
                elif matrix[j][i] == matrix[j+1][i+1] == matrix[j+2][i+2]:
                    return 'end'
                elif matrix[j][i+2] == matrix[j + 1][i + 1] == matrix[j + 2][i]:
                    return 'end'
                else:
                    return 'con'

def game (first_player, second_player,start_grid):
    used_numders = []
    stop = ' '
    while stop != 'end':
        number = get_number(first_player,used_numders)
        replace(number, start_grid, value1)
        print_grid(start_grid)
        print()
        used_numders.append(number)
        stop = check(start_grid,used_numders)
        if stop != 'end':
            number = get_number(second_player, used_numders)
            replace(number, start_grid, value2)
            print_grid(start_grid)
            print()
            used_numders.append(number)
            stop = check(start_grid, used_numders)
    print('конец игры')

player = input('Введите ваше имя: ')
bot= 'Computer'
fir_player, sec_player = first_move(player,bot)
value1 = 'X'
value2 = 'O'
st_grid = create_grid()
print_grid(st_grid)
game(fir_player, sec_player, st_grid)