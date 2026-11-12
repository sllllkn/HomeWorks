from student import Student
from group import Group
from group_limit_error import GroupLimitError


st1 = Student("Jobs", "Steve", 25, "КНТ-215м")
st2 = Student("Gates", "Bill", 30, "КНТ-215м")
st3 = Student("Musk", "Elon", 28, "КНТ-215м")

gr = Group("КНТ-215м")

gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)

assert gr.find_student("Jobs") == st1
assert gr.find_student("Unknown") is None

print("Пошук студента:")
print(gr.find_student("Jobs"))
print("\nСписок групи:")
print(gr)

gr.remove_student("Gates")

print("\nПісля видалення:")
print(gr)

try:
    for i in range(1, 9):
        gr.add_student(Student(f"Student{i}", f"Name{i}", 20, "КНТ-215м"))
    gr.add_student(Student("Eleventh", "Student", 21, "КНТ-215м"))
except GroupLimitError as error:
    print("\nПомилка:", error)

print("\nУсі перевірки пройдено.")
