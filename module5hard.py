# Задание "Свой YouTube"

import time

class UrTube:
    def __init__(self):
        self.users = [] # список зарегистрированных пользователей
        self.videos = [] # список добавленных видео
        self.current_user = None

    def log_in(self, nickname, password):
            for i in self.users:
                if  i.nickname == nickname:
                    if  i.password == hash(password):
                        # print(f'Вход выполнен. Приветствую, {nickname}')
                        self.current_user = i
                        return
                    else:
                        print('Пароль не совпадает')
                        return
            print(f'Пользователь {nickname} не найден')

    def register(self, nickname, password, age):
        # self.log_out()
        for i in self.users:
            if  i.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        self.users.append(User(nickname,password,age))
        # print(f'Зарегистрирован новый пользователь: {nickname}')
        self.log_in(nickname, password)

    def log_out(self):
        # print(f'До свидания, {self.current_user.nickname}. Выход выполнен')
        self.current_user = None

    def add(self, *args):
        for i in args:
            self.videos.append(i)
            # print(f'В базу данных добавили видео "{i.title}"')

    def get_videos(self, search_name):
        result = []
        for i in self.videos:
            if search_name.lower() in i.title.lower():
                result.append(i.title)
        return result

    def watch_video(self, video_name):
        current_video = None
        for i in self.videos:
            if i.title == video_name:
                current_video = i
                break
        if current_video is None:
            print('Видео не найдено')
            return
        elif self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        elif self.current_user.age < 18 and current_video.adult_mode == True:
            print('Вам нет 18 лет, пожалуйста, покиньте страницу')
            return
        else:
            # print(f'Приятного просмотра, {self.current_user}')
            # time.sleep(1)
            for i in range(current_video.time_now, current_video.duration + 1):
                if i < current_video.duration:
                    current_video.time_now += 1
                    print(current_video.time_now, end=' ')
                    time.sleep(1)
                else:
                    print('Конец видео')
                    current_video.time_now = 0
                    # time.sleep(1)

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title # заголовок, строка
        self.duration = duration # продолжительность, секунды
        self.time_now = time_now # секунда остановки
        self.adult_mode = adult_mode # ограничение по возрасту

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname # имя пользователя
        self.password = hash(password) # пароль
        self.age = age # возраст

    def __str__(self):
        """
        При обращении к классу как к строке будет использоваться только имя пользователя
        """
        return f'{self.nickname}'


if __name__ == '__main__':
    # Код для проверки:
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')   # добавили восклицательный знак в конце названия

    # Проверка входа в другой аккаунт
    # ur.log_out()
    # print(ur.current_user)
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)
    # ur.log_in('vasya_pupkin','lolkekcheburek')
    # print(ur.current_user)

# Вывод в консоль:
# ['Лучший язык программирования 2024 года']
# ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
# Войдите в аккаунт, чтобы смотреть видео
# Вам нет 18 лет, пожалуйста покиньте страницу
# 1 2 3 4 5 6 7 8 9 10 Конец видео
# Пользователь vasya_pupkin уже существует
# urban_pythonist
