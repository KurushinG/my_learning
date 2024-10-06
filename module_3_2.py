# Задача "Рассылка писем"

# проверка корректности адреса
def adress_error(adress):
    is_error = False
    if '@' not in adress:
        is_error = True
    elif adress[-4:] != '.com':
        if adress[-4:] != '.net':
            if adress[-3:] != '.ru':
                is_error = True
    return is_error


def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    if adress_error(recipient) == True or adress_error(sender) == True:
        return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender is recipient:
        return print(f'Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        return print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        return print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')