class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
students = [
    Student("Dima", 18),
    Student("Tymofii", 19),
    Student("Anastasia", 21),
    Student("Danylo", 24),
    Student("Mykola", 18),
    Student("Anna", 20)
]

parameter = input("Виберіть ключ для сортування (N for name or A for age): ")


if parameter == 'N':
    students = sorted(students, key=lambda x: x.name)
elif parameter == 'A':
    students = sorted(students, key=lambda x: x.age) 

for student in students:
    print(f"Name: {student.name}, Age: {student.age}")
