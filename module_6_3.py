# Задача "Мифическое наследование"

class Horse: # лошадь
    x_distance = 0 # пройденный путь

    def __init__(self):
        self.sound = 'Frrr' # звук, который издаёт лошадь
        super().__init__()

    def run(self, dx):
        self.x_distance += dx

class Eagle: # орёл
    y_distance = 0 # пройденный путь

    def __init__(self):
        self.sound = 'I train, eat, sleep, and repeat' # звук, который издаёт орёл
        super().__init__()

    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle): # пегас

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(f'{self.sound}')


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()