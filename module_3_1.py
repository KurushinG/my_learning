# Задача "Счётчик вызовов"

calls = 0


# подсчитывающая вызовы остальных функций
def count_calls():
    global calls
    calls += 1


# принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре
def string_info(str1):
    count_calls()
    return (len(str1), str1.upper(), str1.lower())


# принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует
def is_contains(str2, list2):
    count_calls()
    for i in range(len(list2)):
        if str2.lower() == list2[i].lower():
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)