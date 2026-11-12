
class Person:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    def show_info(self):
        return f"Прізвище: {self.surname}, Ім'я: {self.name}, Вік: {self.age}"


class Student(Person):
    def __init__(self, surname, name, age, group):
        super().__init__(surname, name, age)
        self.group = group

    def show_info(self):
        return f"Студент: {self.surname} {self.name}, Вік: {self.age}, Група: {self.group}"


class GroupLimitError(Exception):
    pass


class Group:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        if len(self.students) >= 10:
            raise GroupLimitError("У групі не може бути більше 10 студентів!")
        self.students.append(student)

    def find_student(self, surname):
        for student in self.students:
            if student.surname == surname:
                return student
        return None

    def remove_student(self, surname):
        student = self.find_student(surname)

        if student is not None:
            self.students.remove(student)
            return True

        return False

    def __str__(self):
        result = f"Група: {self.name}\nСписок студентів:\n"

        for student in self.students:
            result += student.show_info() + "\n"

        return result


group = Group("КНТ-215м")

students = [
    Student("Шевченко", "Іван", 20, "КНТ-215м"),
    Student("Петренко", "Олег", 21, "КНТ-215м"),
    Student("Іваненко", "Андрій", 22, "КНТ-215м"),
    Student("Коваленко", "Петро", 20, "КНТ-215м"),
    Student("Бондаренко", "Максим", 21, "КНТ-215м"),
    Student("Мельник", "Дмитро", 22, "КНТ-215м"),
    Student("Ткаченко", "Олександр", 20, "КНТ-215м"),
    Student("Кравченко", "Сергій", 21, "КНТ-215м"),
    Student("Олійник", "Василь", 22, "КНТ-215м"),
    Student("Мороз", "Артем", 20, "КНТ-215м"),
    Student("Лисенко", "Ігор", 21, "КНТ-215м")
]

for student in students:
    try:
        group.add_student(student)
        print(f"Студента {student.surname} додано до групи.")
    except GroupLimitError as error:
        print("Помилка:", error)

print()
print(group)
