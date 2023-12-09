from Students import Student

class StudentList():
    def __init__(self) -> None:
        self.students = []

    def __str__(self) -> str:
        string = ''
        for student in self.students:
            string += f'Student name is {student.name}, phone is {student.phone}, age is{student.age}, course is {student.course}'
        return string
    
    def addNewStudent(self, student: Student):
        insertPosition = 0
        for st in self.students:
            if student.name > st.name:
                insertPosition += 1
            else:
                break
        self.students.insert(insertPosition, student)
        print("New element added")

    def deleteStudent(self, student_name):
        deletePosition = -1
        for student in self.students:
            if student.name == student_name:
                deletePosition = self.students.index(student)
                break
        if deletePosition == -1:
            print("Element not found")
        else:
            print("Delete position " + str(deletePosition))
            del self.students[deletePosition]

    def updateStudent(self, studentName, newStudent: Student):
        updatePosition = -1 
        for student in self.students:
            if studentName == student.name:
                updatePosition = self.students.index(student)
                break
        if updatePosition == -1:
            print(f"Student with name {studentName} was updated")
            return
        
        if studentName != newStudent.name:
            del self.students[updatePosition]
            self.addNewStudent(newStudent)
        else:
            self.students[updatePosition].phone = newStudent.phone
            del newStudent