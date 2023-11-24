import csv
import sys
import unittest
from io import StringIO

class StudentManagementSystem:
    def __init__(self):
        self.students_list = []

    def FileLoad(self, file):
        with open(file, encoding="utf-8") as file:
            result = csv.DictReader(file)
            return [row for row in result]

    def SaveFile(self, file):
        names = ["name", "phone", "age", "course"]
        try:
            with open(file, "w", newline="", encoding="utf-8") as file:
                ResFile = csv.DictWriter(file, fieldnames=names)
                ResFile.writeheader()
                ResFile.writerows(self.students_list)
            print(f"The data is saved in {file}.")
        except IOError as e:
            print(f"Error saving to {file}: {e}")

    def printAllList(self):
        sorted_list = sorted(self.students_list, key=lambda x: x["name"])
        for elem in sorted_list:
            strForPrint = (
                "Student name is "
                + elem["name"]
                + ",  Phone is "
                + elem["phone"]
                + ", Age is"
                + elem["age"]
                + ", Course of university is"
                + elem["course"]
            )
            print(strForPrint)
        return

    def addNewElement(self, name, phone, age, course):
        newItem = {"name": name, "phone": phone, "age": age, "course": course}
        # find insert position
        insertPosition = 0
        for item in self.students_list:
            if name > item["name"]:
                insertPosition += 1
            else:
                break
        self.students_list.insert(insertPosition, newItem)
        print("New element has been added")
        return

    def deleteElement(self, name):
        deletePosition = -1
        for item in self.students_list:
            if name == item["name"]:
                deletePosition = self.students_list.index(item)
                break
        if deletePosition == -1:
            print("Element was not found")
        else:
            del self.students_list[deletePosition]
        return

    def updateElement(self, name, newname, newphone, newage, newcourse):
        for index, student in enumerate(self.students_list):
            if name == student["name"]:
                newElement = {
                    "name": newname,
                    "phone": newphone,
                    "age": newage,
                    "course": newcourse,
                }
                del self.students_list[index]
                insertPosition = 0
                for i, elem in enumerate(self.students_list):
                    if newname > elem["name"]:
                        insertPosition += 1
                    else:
                        break
                self.students_list.insert(insertPosition, newElement)
                print("Element has been updated")
                break
        else:
            print("Student not found")


class TestStudentManagementSystem(unittest.TestCase):
    def setUp(self):
        self.sms = StudentManagementSystem()

    def test_addNewElement(self):
        self.sms.addNewElement("John", "1234567890", "20", "3")
        self.assertEqual(len(self.sms.students_list), 1)

    def test_deleteElement(self):
        self.sms.addNewElement("John", "1234567890", "20", "3")
        self.sms.deleteElement("John")
        self.assertEqual(len(self.sms.students_list), 0)

    def test_updateElement(self):
        self.sms.addNewElement("John", "1234567890", "20", "3")
        self.sms.updateElement("John", "Jane", "9876543210", "21", "4")
        self.assertEqual(len(self.sms.students_list), 1)
        updated_student = self.sms.students_list[0]
        self.assertEqual(updated_student["name"], "Jane")
        self.assertEqual(updated_student["phone"], "9876543210")
        self.assertEqual(updated_student["age"], "21")
        self.assertEqual(updated_student["course"], "4")


if __name__ == "__main__":
    unittest.main()
