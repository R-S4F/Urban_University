# Домашнее задание по теме "Доступ к свойствам родителя. Переопределение свойств."

class Vehicle:
    __COLOR_VARIANTS = [
        'blue',
        'red',
        'green',
        'black',
        'white'
    ]

    for i in __COLOR_VARIANTS:
        __COLOR_VARIANTS[__COLOR_VARIANTS.index(i)] = i.upper()

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color.upper()

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}', end='\n\n')

    def set_color(self, new_color):
        if new_color.upper() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}', end='\n\n')


class Sedan(Vehicle):
    def __init__(self, owner, model, engine_power, color):
        super().__init__(owner, model, engine_power, color)
        self.__PASSENGERS_LIMIT = 5

    def get_passengers_limit(self):
        return self.__PASSENGERS_LIMIT


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'


vehicle1.print_info()


