# Задача "Записать и запомнить"

def custom_write(file_name, strings):
    strings_positions = {}
    string_number = 0
    file = open(file_name, 'a', encoding='utf-8')
    for i in strings:
        string_number += 1
        first_position = file.tell()
        file.write(f'{i}\n')
        strings_positions[(string_number, first_position)] = i
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
