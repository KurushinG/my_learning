# Задание "Средний балл":
# Школьные учителя устали подсчитывать вручную средний балл каждого ученика,
# поэтому надо автоматизировать этот процесс:
# Написать программу, которая составляет словарь, используя grades и students,
# где ключом будет имя ученика, а значением - его средний балл.

# Исходные данные:
# список оценок для каждого ученика в алфавитном порядке
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# неупорядоченная последовательность имён всех учеников в классе
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# 1. Определение типов исходных множеств
# print('grades', type(grades))
# print('students', type(students))
# print()

# 2. Сортирорвка по алфавиту и формирование списка учеников
students_l=sorted(list(students))
# print(students_l, type(students_l))
# print()

# 3. Формирование списка из средних баллов
# 3.0 Проверка математики
# print(grades[0])
# print('Сумма', sum(grades[0]))
# print('Количество', len(grades[0]))
# print('Среднее', sum(grades[0])/len(grades[0]))
# print()

# 3.1 Поэлементная реализация алгоритма
# grades_a=[]
# grades_a.append(sum(grades[0])/len(grades[0]))
# grades_a.append(sum(grades[1])/len(grades[1]))
# grades_a.append(sum(grades[2])/len(grades[2]))
# grades_a.append(sum(grades[3])/len(grades[3]))
# grades_a.append(sum(grades[4])/len(grades[4]))
# print(grades_a, type(grades_a))
# print()

# 3.2 Реализация алгоритма цикла
# grades_a=[]
# for i in range(len(students_l)): grades_a.append(sum(grades[i])/len(grades[i]))
# print(grades_a, type(grades_a))
# print()

# 4. формирование итого словаря
# rezult=dict(zip(students_l,grades_a))
rezult={}
for i in range(len(students_l)): rezult[students_l[i]]=sum(grades[i])/len(grades[i])
print(rezult)