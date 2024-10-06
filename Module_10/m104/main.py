from threading import Thread
import queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        from random import randint
        from time import sleep
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *args):
        self.queue = queue.Queue()
        self.tables = args
        self.full_tables = 0

    def guest_arrival(self, *args):
        for guest in args:
            is_tabled = False

            for table in self.tables:
                if table.guest is None:
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    table.guest = guest
                    self.full_tables += 1
                    is_tabled = True
                    break

            if is_tabled is False:
                self.queue.put(item=guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or self.full_tables:
            for table in self.tables:

                if table.guest is not None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None
                    self.full_tables -= 1

                if not self.queue.empty() and table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}"')
                    self.full_tables += 1

                if table.guest is not None:
                    table.guest.run()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
