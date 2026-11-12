from person import Person


class Student(Person):
    def __init__(self, surname, name, age, group):
        super().__init__(surname, name, age)
        self.group = group

    def __str__(self):
        return f"{self.surname} {self.name}, вік: {self.age}, група: {self.group}"

    def show_info(self):
        return str(self)

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))
