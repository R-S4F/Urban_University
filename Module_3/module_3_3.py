# Самостоятельная работа по уроку "Распаковка позиционных параметров".

def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])

values_list = ['str', 1, [1, 2.0]]
values_dict = {'a': 1, 'b': 'str2', 'c': [5, 6]}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [98, 'str3']

print_params(*values_list_2, 42)