import math


class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Сторони прямокутника повинні бути додатними")

        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return math.isclose(self.area(), other.area())

    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() < other.area()

    def __gt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() > other.area()

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented

        new_area = self.area() + other.area()
        scale = math.sqrt(new_area / self.area())

        return Rectangle(
            self.width * scale,
            self.height * scale
        )

    def __mul__(self, number):
        if not isinstance(number, (int, float)) or number <= 0:
            raise ValueError("Множник повинен бути додатним числом")

        scale = math.sqrt(number)

        return Rectangle(
            self.width * scale,
            self.height * scale
        )

    def __rmul__(self, number):
        return self.__mul__(number)

    def __str__(self):
        return (
            f"Прямокутник: ширина = {self.width:.2f}, "
            f"висота = {self.height:.2f}, "
            f"площа = {self.area():.2f}"
        )


rect1 = Rectangle(2, 4)
rect2 = Rectangle(3, 6)

print("Перший прямокутник:")
print(rect1)

print("\nДругий прямокутник:")
print(rect2)

print("\nПорівняння прямокутників:")
print("Площі рівні:", rect1 == rect2)
print("Перший менший за другий:", rect1 < rect2)
print("Перший більший за другий:", rect1 > rect2)

rect3 = rect1 + rect2

print("\nРезультат додавання:")
print(rect3)

rect4 = rect1 * 3

print("\nРезультат множення на 3:")
print(rect4)

rect5 = 2 * rect1

print("\nРезультат множення на 2:")
print(rect5)