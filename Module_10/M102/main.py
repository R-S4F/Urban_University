# Домашнее задание по теме "Потоки на классах"
from threading import Thread


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        if not isinstance(name, str):
            raise TypeError(f'Атрибут <name> должен являться {str}, а является {type(name)}')
        if not isinstance(power, int):
            raise TypeError(f'Атрибут <power> должен являться {int}, а является {type(power)}')
        self.name = name
        self.power = power

    def run(self):
        days_title = ('день', 'дня', 'дней')
        alies_title = ('воин', 'воина', 'воинов')
        print(f'{self.name}, на нас напали!')
        from time import sleep
        alies = 100
        days = 0
        while alies > 0:
            if alies <= self.power:
                alies = 0
            else:
                alies -= self.power
            days += 1
            sleep(1)
            print(f"{self.name} сражается {self.some_title(days, days_title)},"
                  f" осталось {self.some_title(alies, alies_title)}.")
        print(f'{self.name} одержал победу спустя {self.some_title(days, days_title)}.')

    @staticmethod
    def some_title(count, _tuple):
        if count % 10 == 1 and count != 11:
            return f'{count} {_tuple[0]}'
        elif count % 10 in (2, 3, 4) and count not in range(12, 15):
            return f'{count} {_tuple[1]}'
        else:
            return f'{count} {_tuple[2]}'


first_knight = Knight('Sir Lancelot', 11)
second_knight = Knight("Sir Galahad", 19)
first_knight.start()
second_knight.start()
