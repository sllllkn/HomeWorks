
class Counter:
    def __init__(self, minimum=0, maximum=100, initial=0):
        if minimum > maximum:
            raise ValueError("Мінімум не може бути більшим за максимум")

        if initial < minimum or initial > maximum:
            raise ValueError("Початкове значення виходить за межі лічильника")

        self.minimum = minimum
        self.maximum = maximum
        self.value = initial

    def set_maximum(self, maximum):
        if maximum < self.minimum:
            raise ValueError("Максимум не може бути меншим за мінімум")
        if maximum < self.value:
            raise ValueError("Максимум не може бути меншим за поточне значення")
        self.maximum = maximum

    def set_minimum(self, minimum):
        if minimum > self.maximum:
            raise ValueError("Мінімум не може бути більшим за максимум")
        if minimum > self.value:
            raise ValueError("Мінімум не може бути більшим за поточне значення")
        self.minimum = minimum

    def set_initial(self, initial):
        if initial < self.minimum or initial > self.maximum:
            raise ValueError("Початкове значення виходить за межі лічильника")
        self.value = initial

    def step_up(self):
        if self.value >= self.maximum:
            raise ValueError("Досягнуто максимуму")
        self.value += 1

    def step_down(self):
        if self.value <= self.minimum:
            raise ValueError("Досягнуто мінімуму")
        self.value -= 1

    def get_value(self):
        return self.value


counter = Counter(minimum=0, maximum=5, initial=2)

print("Початкове значення:", counter.get_value())

counter.step_up()
counter.step_up()
print("Після збільшення:", counter.get_value())

counter.step_down()
print("Після зменшення:", counter.get_value())

counter.set_initial(5)
print("Поточне значення:", counter.get_value())

try:
    counter.step_up()
except ValueError as error:
    print("Помилка:", error)

counter.set_initial(0)

try:
    counter.step_down()
except ValueError as error:
    print("Помилка:", error)
