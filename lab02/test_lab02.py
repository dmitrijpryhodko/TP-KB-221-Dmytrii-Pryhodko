from typing import Self
import unittest
import io
import os
import csv
from unittest.mock import patch
from lab_02 import *

class TestScript(unittest.TestCase):
    def setUp(self):
        self.test_file = "lab02.csv"
        self.list = [
            {"name": "Bob", "phone": "1111", "age": "23", "course": "5"},
            {"name": "Emma", "phone": "2222", "age": "19", "course": "3"},
        ]

    def tearDown(self):
        try:
            os.remove(self.test_file)
        except FileNotFoundError:
            pass

    def test_FileLoad(self):
        with open(self.test_file, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["name", "phone", "age", "course"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.list)

        loaded_data = FileLoad(self.test_file)
        self.assertEqual(loaded_data, self.list)

    def test_FileSave(self):
        SaveFile(self.test_file, self.list)
        loaded_data = FileLoad(self.test_file)
        self.assertEqual(loaded_data, self.list)

    def test_printAllList(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            printAllList(self.list)
            output = mock_stdout.getvalue()
            self.assertIn("Emma", output)
            self.assertIn("Bob", output)

    def test_addNewElement(self):
        with patch('builtins.input', side_effect=["Dilan", "3333333", "21", "3"]):
            addNewElement(self.list)
            self.assertEqual(len(self.list), 3)

    def test_deleteElement(self):
        with patch('builtins.input', return_value="Dilan"):
            deleteElement(self.list)
            self.assertEqual(len(self.list), 2)

    def test_updateElement(self):
        with patch('builtins.input', side_effect=["Emma", "Jane", "123456789", "23", "5"]):
            updateElement(self.list)
            self.assertEqual(self.list[1]["name"], "Jane")



if __name__ == "__main__":
    unittest.main()
