# Задача "Матрица воплоти"

def get_matrix(n, m, value):
    # n - количество строк
    # m - количество столбцов
    # value - значения
    matrix=[]
    for i in range(n):
        matrix_j=[]
        for j in range(m):
            matrix_j.append(value)
        matrix.append(matrix_j)
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

print('Введи количество строк матрицы')
n=int(input())
print('Введи количество строк матрицы')
m=int(input())
print('Введи количество строк матрицы')
value=int(input())
print('Ваша матрица:')
matrix=get_matrix(n, m, value)
print(matrix)