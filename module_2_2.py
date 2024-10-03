# Задача "Все ли равны?"
print('Введите первое число: ')
first=int(input())
print('Введите второе число: ')
second=int(input())
print('Введите третье число: ')
third=int(input())
if first==second and first==third:
    print(3)
elif first==second or first==third or second==third:
    print(2)
else:
    print(0)