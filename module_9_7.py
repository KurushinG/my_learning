def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        k = 0
        for i in range(1, result+1):
            turn = result % i
            if result % i == 0:
                k +=1
                if k > 2:
                    print('Составное')
                    break
        if k == 2:
            print('Простое')
        return result
    return wrapper


@is_prime
def sum_three(a, b, c):
    result = a + b + c
    return result


result = sum_three(2, 3, 6)
print(result)