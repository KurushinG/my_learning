# Задание "Слишком древний шифр"
from random import randint

n = randint(3, 20)
list_n = []
rezult = ''
for i in range(1, n):
    list_n.append(i)
print(f'Если в первой вставке выпало {n}')
for i in range(1, n):
    for j in range(i+1, n):
        if n % (i+j) == 0:
            rezult += str(f'{i}{j}')
print(f'Во сторой вставке наужно написать {rezult}')
