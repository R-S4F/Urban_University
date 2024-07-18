# 2023/09/24 00:00|Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи"

# task 2
immutable_var = 567, 1.0, 'string'
print(f'Immutable tuple: {immutable_var}')

# task 3
# Кортеж является неизменяемым объектом.
# Кортежи поддерживают лишь два вида операций: конкатенацию и умножение
# immutable_var2 = 12.5, 'str'
# print(immutable_var*2)
# print(immutable_var + immutable_var2)

# task 4
mutable_list = [871, 656.9, 'str']
mutable_list.extend('Darling')
mutable_list.append(321)
mutable_list[0] = 1
print(f'Mutable list: {mutable_list}')
