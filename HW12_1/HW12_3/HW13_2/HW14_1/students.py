
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


class Group:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
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


student1 = Student("Шевченко", "Іван", 20, "КНТ-215м")
student2 = Student("Петренко", "Олег", 21, "КНТ-215м")
student3 = Student("Іваненко", "Андрій", 22, "КНТ-215м")

group = Group("КНТ-215м")

group.add_student(student1)
group.add_student(student2)
group.add_student(student3)

print(group)

found_student = group.find_student("Петренко")

if found_student is not None:
    print("Знайдено студента:")
    print(found_student.show_info())
else:
    print("Студента не знайдено")

group.remove_student("Петренко")

print("\nПісля видалення студента:")
print(group)
