# Дополнительное практическое задание по модулю: "Основные операторы"

def password(w):
    result = str()
    for i in range(1, w):
        for k in range(i+1, n):
            dual = i + k
            if w >= dual and w % dual == 0:
                result += str(i) + str(k)
    return(result)

while True:
    n = int(input('Введите число из первого поля: '))
    if n < 3 or n > 20:
        print('Вы ввели неверное число.\n')
    else:
        break


print(f'Пароль: {password(n)}')

# Постарался воспользоваться знаниями из всех предыдущих тем