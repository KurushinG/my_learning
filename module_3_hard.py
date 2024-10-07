# Задание "Раз, два, три, четыре, пять .... Это не всё?"
# подсчёта суммы всех чисел и длин всех строк
summa = 0
def calculate_structure_sum(*args):
    global summa
    for i in args:
        # print(i, type(i))
        if isinstance(i, int):
                # print(f'сумма увеличилась\n'
                #       f'{summa}+{i}={summa + i}')
                summa += i
        elif isinstance(i, str):
                # print(f'сумма увеличилась\n'
                #       f'{summa}+{len(i)}={summa + len(i)}')
                summa += len(i)
        elif isinstance(i, (list, tuple, set)):
                for j in i:
                    calculate_structure_sum(j)
        elif isinstance(i, dict):
                for j, k in i.items():
                    calculate_structure_sum(j, k)
        # print()
    return summa


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
# 1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99

result = calculate_structure_sum(data_structure)
print(result) # 99

