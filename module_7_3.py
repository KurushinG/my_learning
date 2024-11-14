# Задача "Найдёт везде"
import re


class WordsFinder:

    def __init__(self, *file_name):
        self.file_names = []
        for i in file_name:
            self.file_names.append(i)

    def get_all_words(self):
        znaki = [',', '.', '=', '!', '?', ';', ':', ' - ']
        all_words = {}
        for name in self.file_names:
            words = []
            with open(name, encoding='utf-8') as file:
                for line in file:
                    # перевёл строку в нижний регистр
                    string = line.lower()
                    # для каждого из вариантов знака пунктуации перезаписываем строчку без него
                    for i in znaki:
                        string = string.replace(i, '')
                    # создаём список слов из строки
                    words += string.split()
            all_words[name] = words
        return all_words

    def find(self, word):
        result = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            pos = 1
            for i in words:
                if i == word:
                    result[name] = pos
                    break
                else:
                    pos += 1
        return result

    def count(self, word):
        result = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            num = 0
            for i in words:
                if word == i:
                    num += 1
            result[name] = num
        return result


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))