import csv
from StudentList import *
from Students import Student

class Utils:
    @staticmethod
    def addFile(file, studentList):
        with open(file, newline='') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                student = Student(row["name"], row["phone"], row["age"], row["course"])
                studentList.addNewStudent(student)
        return studentList

    @staticmethod
    def saveFile(file, studentList):
        try: 
            with open(file, 'w', newline="") as SaveFile:
                fieldnames = ["name", "phone", "age", "course"]
                writer = csv.DictWriter(SaveFile, fieldnames=fieldnames)
                writer.writeheader()
                for student in studentList.students:
                    writer.writerow({"name": student.name, "phone": student.phone, "age": student.age, "course": student.course})
                print("File saved")
        except IOError as e:
            print(f"Error saving data to {file}: {e}")