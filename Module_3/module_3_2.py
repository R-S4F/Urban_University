# Домашняя работа по уроку "Способы вызова функции"

def send_email(message, recipient, *, sender='university.help@gmail.com'):
    def checker(email):
        domens_for_check = ('.com', '.ru', '.net')
        check = False
        if email == 'university.help@gmail.com':
            check = True
        else:
            for i in domens_for_check:
                if email.replace(i, '') == email[0:len(email) - len(i)]:
                    for k in email[-len(i) - 1::-1]:
                        if k == '@':
                            check = True
                            break
                if check:
                    break
        return check

    # Endline of checker

    if not (checker(sender) and checker(recipient)):
        print(f'Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>')
    else:
        if recipient == sender:
            print("Нельзя отправить письмо самому себе!")
        else:
            if sender == 'university.help@gmail.com':
                print(f"Письмо успешно отправлено с адреса <{sender}> на адрес <{recipient}>.")
            else:
                print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{sender}> на адрес <{recipient}>.")


# Endline of send_email


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
