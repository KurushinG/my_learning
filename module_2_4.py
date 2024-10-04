# Задача "Всё не так уж просто"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    is_prime = True
    if i == 1:
        continue
    for j in numbers:
        if j == 1:
            continue
        elif i == j:
            break
        elif i % j == 0:
            is_prime = False
            break
    if is_prime == True:
        primes.append(i)
    else:
        not_primes.append(i)
print(f' Дан список чисел: {numbers}')
print(f' Из них простые: {primes}')
print(f' Из них составные: {not_primes}')
