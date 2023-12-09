from StudentList import *
from Utils import *
from Students import Student

def main():
    studentList = StudentList()
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print, S save, L load, X exit ] ")      
        match chouse.lower():
            case "C"|"c":
                print("New element will be created:")
                student = Student(input("Enter name: "), input("Enter phone: "), input("Enter age: "), input("Enter course: "))
                studentList.addNewStudent(student)
            case "U"|"u":
                print("Existing element will be updated")
                name = input("Enter student name to be updated: ")
                newStudent = Student(input("Enter new name: "), input("Enter new phone: "), input("Enter new age: "), input("Enter new course: "))
                studentList.updateStudent(name, newStudent)
            case "D"|"d":
                print("Element will be deleted")
                name = input("Enter student name to delete: ")
                studentList.deleteStudent(name)
            case "P"|"p":
                print("List will be printed")
                print(studentList)
            case "X"|"x":
                print("Exit()")
                break
            case "L"|"l":
                file = input("Enter CSV file name: ")
                studentList = Utils.addFile(file, studentList)
            case "S"|"s":
                file = input("Enter CSV file name: ")
                Utils.saveFile(file, studentList)

if __name__ == "__main__":
    main()