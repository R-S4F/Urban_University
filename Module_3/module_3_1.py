# Домашняя работа по уроку "Пространство имён"

calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    tuple_ = (len(string), string.upper(), string.lower())
    count_calls()
    return tuple_


def is_contains(string, list_to_search):
    checker = False
    string = string.upper()
    for i in range(0, len(list_to_search)):
        list_to_search[i] = list_to_search[i].upper()
        if string == list_to_search[i]:
            checker = True
            break
    count_calls()
    return checker


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
