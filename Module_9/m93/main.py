# Домашнее задание по теме "Генераторные сборки"

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(a)-len(b))
                for a, b in zip(first, second)
                if abs(len(a)-len(b)) != 0)

second_result = (len(first[a]) == len(second[a])
                 for a in range(len(first))
                 if len(first) - len(second) == 0)

print(list(first_result))
print(list(second_result))