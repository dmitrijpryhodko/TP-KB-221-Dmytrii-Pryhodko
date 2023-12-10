import unittest
from unittest.mock import patch
from io import StringIO
from lab_03 import *
import os
from Utils import Utils
from StudentList import *
from Students import *

class Tests(unittest.TestCase):
    def test_Student(self):
        student = Student("Bob", "061234567", 20, "3")
        self.assertEqual(student.name, "Bob")
        self.assertEqual(student.phone, "061234567")
        self.assertEqual(student.age, 20)
        self.assertEqual(student.course, "3")

    def setUp(self):
        self.studentList = StudentList()
        self.student1 = Student("Bob", "061234567", 20, "3")
        self.student2 = Student("Zak", "061234567", 21, "3")

    def test_addNewStudent(self):
        self.studentList.addNewStudent(self.student1)
        self.assertEqual(len(self.studentList.students), 1)
        self.assertEqual(self.studentList.students[0].name, "Bob")

        self.studentList.addNewStudent(self.student2)
        self.assertEqual(len(self.studentList.students), 2)
        self.assertEqual(self.studentList.students[1].name, "Zak")

    def test_deleteStudent(self):
        self.studentList.addNewStudent(self.student1)
        self.studentList.addNewStudent(self.student2)

        self.studentList.deleteStudent("Bob")
        self.assertEqual(len(self.studentList.students), 1)
        self.assertEqual(self.studentList.students[0].name, "Zak")

        self.studentList.deleteStudent("John")
        self.assertEqual(len(self.studentList.students), 1)

    def test_updateStudent(self):
        self.studentList.addNewStudent(self.student1)
        self.studentList.addNewStudent(self.student2)

        newStudent = Student("Dilan", "061234567", 20, "3")
        self.studentList.updateStudent("Dilan", newStudent)

        self.assertEqual(len(self.studentList.students), 2)
        self.assertEqual(self.studentList.students[0].phone, "061234567")
        self.assertEqual(self.studentList.students[0].course, "3")

        nonExistingStudent = Student("John", "061234567", 18, "2")
        self.studentList.updateStudent("John", nonExistingStudent)

        self.assertEqual(len(self.studentList.students), 2)

    def test_loadFile(self):
        self.testFile = "unittests.csv"
        self.studentList = StudentList()
        with open(self.testFile, "w") as file:
            file.write("name,phone,age,course\nBob,061234567,20,3")
        Utils.addFile(self.testFile, self.studentList)
        self.assertEqual(len(self.studentList.students), 1)

    def test_saveFile(self):
        self.testFile = "unittests.csv"
        self.studentList = StudentList()
        student = Student("Bob", "061234567", 20, "3")
        self.studentList.addNewStudent(student)
        Utils.saveFile(self.testFile, self.studentList)
        self.assertTrue(os.path.exists(self.testFile))


if __name__ == '__main__':
    unittest.main()