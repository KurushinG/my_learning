# Функции
# Ввывод поля
def draw_area():
    for i in area:
        print(*i)
    print()

# Ход игрока
def turn():
    raw = int(input('Введите номер строки (1, 2, 3): ')) - 1
    col = int(input('Введите номер столбца (1, 2, 3): ')) - 1
    return raw, col

# Проверка условия победы
def win_approve():
    rezult = False
    # проверка равенства строк
    if   area[0][0] == area[0][1] == area[0][2] != '*':
        rezult = True
    elif area[1][0] == area[1][1] == area[1][2] != '*':
        rezult = True
    elif area[2][0] == area[2][1] == area[2][2] != '*':
        rezult = True
    # проверка равенстрва столбцов
    elif area[0][0] == area[1][0] == area[2][0] != '*':
        rezult = True
    elif area[0][1] == area[1][1] == area[2][1] != '*':
        rezult = True
    elif area[0][2] == area[1][2] == area[2][2] != '*':
        rezult = True
    # проверка равенства диагоналей
    elif area[0][0] == area[1][1] == area[2][2] != '*':
        rezult = True
    elif area[2][0] == area[1][1] == area[0][2] != '*':
        rezult = True
    return rezult

print('Добро пожаловать в игру "крестики-Нолики"')
print('-----------------------------------------')
area = [ ['*','*','*'], ['*','*','*'], ['*','*','*'] ]
draw_area()
winner = {'X': 'Крестиков', 'O': 'Ноликов'}
mark = 'O'
rezult = False
# while rezult == False:
#     if mark == 'X':
#         mark = 'O'
#     else:
#         mark = 'X'
#     raw, col = turn()
#     if area[raw][col] != '*':
#         print(f'Здесь уже стоит {area[raw][col]}. Пожалуйста, выберите другое место')
#         raw, col = turn()
#     area[raw][col] = mark
#     draw_area()
#     rezult = win_approve()
# print(f'Игра закончилось победой {winner[mark]}')
for i in range(9):
    if mark == 'X':
        mark = 'O'
    else:
        mark = 'X'
    print(f'Ход {winner[mark]}')
    raw, col = turn()
    if area[raw][col] != '*':
        print(f'Здесь уже стоит {area[raw][col]}. Пожалуйста, выберите другое место')
        raw, col = turn()
    area[raw][col] = mark
    draw_area()
    rezult = win_approve()
    if rezult == True:
        print(f'Игра закончилось победой {winner[mark]}')
        break
if rezult == False:
    print(f'Игра закончилось вничью')

