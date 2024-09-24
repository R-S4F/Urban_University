# Домашнее задание по теме "Декораторы"

def is_prime(func):
    def wrapper(*args):
        _res = func(*args)
        if _res % 2 == 0 and _res != 2:
            print('Составное')
            return _res
        else:
            xyz = 0
            for _ in range(int(_res**0.5)+1):
                for i in (3, 5, 7, 11):
                    if _res % (i + xyz) == 0 and _res > (i + xyz):
                        print('Составное')
                        return _res
                xyz += 10
            print('Простое')
            return _res
    return wrapper


@is_prime
def sum_three(i1, i2, i3):
    try:
        return i1 + i2 + i3
    except TypeError:
        return 0


result = sum_three(2, 3, 6)
print(result)
