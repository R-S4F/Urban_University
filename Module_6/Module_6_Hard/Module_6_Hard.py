# Дополнительное практическое задание по модулю: "Наследование классов."


class Figure:
    SIDES_COUNT = 0

    def __init__(self, color, *sides):

        if self.__is_valid_color(*color):
            self.__color = [*color]
        else:
            self.__color = [0, 0, 0]

        if self.__is_valid_sides(*sides):
            self.set_sides(*sides)
        else:
            self.__sides = [1] * self.SIDES_COUNT

        self.filled = bool()

    def get_sides(self):
        return self.__sides

    def get_color(self):
        return self.__color

    def __len__(self):
        return sum(self.__sides)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = [*new_sides]

    @staticmethod
    def __is_valid_color(r, g, b):
        return (r in range(0, 256) and
                g in range(0, 256) and
                b in range(0, 256))

    def __is_valid_sides(self, *sides):
        if len(sides) == self.SIDES_COUNT:
            for i in [*sides]:
                if not ((i > 0) and isinstance(i, int)):
                    return False
            return True
        else:
            return False


class Circle(Figure):
    SIDES_COUNT = 1

    def __init__(self, color, *sides):
        from math import pi
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * pi)

    def get_square(self):
        from math import pi
        return pi * self.__radius ** 2


class Triangle(Figure):
    SIDES_COUNT = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        from math import sqrt
        p = self.__len__() / 2
        return sqrt(p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2]))


class Cube(Figure):
    SIDES_COUNT = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.set_sides(*([sides][0] * 12))

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
print(cube1.__dict__)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
