import csv
from lab_02 import printAllList,addNewElement,deleteElement,updateElement,addcsv,savecsv

list = []

def printAllListtest():
    list.append({"name": "Arnold", "phone": "0689685547", "age": "19", "course": "3"})
    assert printAllList() == "Student name is Arnold, phone is 0689685547, age is 19, course is 3"
    #students_list.clear()

def addNewElementtest():
    addNewElement("Arnold", "0689685547", "19", "3")
    assert list == [{"name": "Arnold", "phone": "0689685547", "age": "19", "course": "3"}]

def deleteElementtest():
    list.append({"name": "Arnold", "phone": "0689685547", "age": "19", "course": "3"})
    deleteElement("John")
    assert list == []

def updateElementtest():
    list.append({"name": "Arnold", "phone": "0689685547", "age": "19", "course": "3"})
    updateElement("Arnold", "Harold", "0961111111", "20", "4")
    assert list == [{"name": "Harold", "phone": "0961111111", "age": "20", "course": "4"}]

def addcsvtest():
    addcsv("lab02.csv")
    assert list == [{"name": "Harold", "phone": "0961111111", "age": "20", "course": "4"}]

def savecsvtest():
    savecsv("lab02.csv")
    with open("lab02.csv", 'r') as file:
        reader = csv.DictReader(file)
        assert list(reader) == [{"name": "Harold", "phone": "0961111111", "age": "20", "course": "4"}]

        