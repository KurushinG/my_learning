# Задание "Они все так похожи"
import math

class Figure:
    sides_count = 0 # список сторон (целые числа)
    filled = False # закрашенный (булевый)

    def __init__(self, color, *sides):
        self.__color = list(color)
        self.__sides = []
        if len(sides) == 1:
            for i in range(self.sides_count):
                self.__sides.append(sides[0])
        elif len(sides) != self.sides_count:
            for i in range(self.sides_count):
                self.__sides.append(1)
            # print('стороны назначены по правилам')
        else:
            for i in sides:
                self.__sides.append(i)
            # print('стороны назначены пользователем')
        # print(f'количество заданных сторон: {len(sides)}')
        # print(f'заданные длины сторон: {sides}')
        # print(f'количество сторон фигуры: {len(self.sides)}')
        # print(f'длины сторон фигуры: {self.sides}')

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        flag = True
        rgb = [r, g, b]
        for i in rgb:
            if i < 0 or i > 255:
                flag = False
                break
        return flag

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *new_sides):
        flag = True
        if len(new_sides) != len(self.__sides):
            flag = False
        for i in new_sides:
            if i * 10 % 10 != 0 or i < 0:
                flag = False
                break
        return flag

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            for i in range(self.sides_count):
                self.__sides[i] = new_sides[i]

    def __len__(self): # периметр - сумма длин сторон фигуры
        p = 0
        for i in self.__sides:
            p += i
        return p

class Circle(Figure):
    sides_count = 1  # список сторон (целые числа)

    def get_square(self):
        s = (math.pi * self.get_sides()[0] ** 2)
        return s

class Triangle(Figure):
    sides_count = 3  # список сторон (целые числа)

    def get_square(self):
        p = 0 # плуперитметр
        for i in self.__sides:
            p += i / 2
        s = p ** 0.5
        # формула Герона
        for i in self.__sides:
            s *= (p - i) ** 0.5
        return s

class Cube(Figure):
    sides_count = 12  # список сторон (целые числа)

    def get_volume(self):
        v = self.get_sides()[0] ** 3
        return v

WHITE = (255,255,255)
BLACK = (0,0,0)

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())