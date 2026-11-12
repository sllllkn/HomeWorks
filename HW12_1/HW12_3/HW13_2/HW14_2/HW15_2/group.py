from group_limit_error import GroupLimitError


class Group:
    def __init__(self, name):
        self.name = name
        self.group = set()

    def add_student(self, student):
        if student not in self.group and len(self.group) >= 10:
            raise GroupLimitError("У групі не може бути більше 10 студентів")
        self.group.add(student)

    def find_student(self, surname):
        for student in self.group:
            if student.surname == surname:
                return student
        return None

    def remove_student(self, surname):
        student = self.find_student(surname)
        if student is not None:
            self.group.remove(student)
            return True
        return False

    def __str__(self):
        students = sorted(self.group, key=lambda student: (student.surname, student.name))
        result = f"Група: {self.name}\n"
        result += "\n".join(str(student) for student in students)
        return result
