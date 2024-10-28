# Задача "Съедобное, несъедобное"

class Animal:
    alive = True # живой
    fed = False # голодный

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True # сытый
        elif food.edible == False:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False # мёртвый

class Plant:
    edible = False # несъедобный

    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Fruit(Plant):
    edible = True # съедобный
    pass

class Flower(Plant):
    pass


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)