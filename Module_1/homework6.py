# 2023/09/25 00:00|Практическое задание по теме: "Словари и множества"

# DICT
my_dict = {'Anton': 2000, 'Diana': 1995, 'Alex': 2003}
print('Dict:', my_dict)
print('Existing value:', my_dict.get('Diana'))
print('Not existing value:',
      my_dict.get('Naruto', 'Хватит смотреть аниме'))
my_dict['Alena'] = 2002
my_dict['Max'] = 2001
print('Deleted Value:', my_dict.pop('Diana'))
print('Modified Dict:', my_dict, '\n\n')

# SET
my_set = {1, 2, 1, 2, 'str', 'str', 'benchmark'}
print('Set:', my_set)
my_set.add('bear')
my_set.add('bunny')
my_set.discard('benchmark')
print('Modified Set:', my_set)
