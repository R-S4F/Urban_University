# Домашняя работа по уроку "Способы вызова функции"

def checker(email):
    domains_for_check = ('com', 'ru', 'net')
    if email == 'university.help@gmail.com':
        return True
    elif (email.split('.')[-1] in domains_for_check) and '@' in email:
        return True
    return False


def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if not (checker(sender) and checker(recipient)):
        print(f'Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>')
        return

    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        return

    if sender == 'university.help@gmail.com':
        print(f"Письмо успешно отправлено с адреса <{sender}> на адрес <{recipient}>.")
        return

    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{sender}> на адрес <{recipient}>.")
        return


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
