# Домашнее задание по теме "Позиционирование в файле".

def custom_write(file_name, strings):
    p1 = open(file_name, 'r+', encoding='utf-8')
    strings_positions = dict()
    for i in strings:
        _index = strings.index(i) + 1
        _byte = p1.tell()
        p1.write(f'{i}\n')
        strings_positions[(_index, _byte)] = i
    p1.close()
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
