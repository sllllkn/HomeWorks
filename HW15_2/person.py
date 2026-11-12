class Person:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.surname} {self.name}, вік: {self.age}"

    def show_info(self):
        return str(self)
