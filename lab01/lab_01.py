## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}

# already sorted list
list = [
    {"name":"Bob", "phone":"0631234567", "age": "18", "course": "2"},
    {"name":"Emma", "phone":"0631234567", "age": "17", "course": "1"},
    {"name":"Jon",  "phone":"0631234567", "age": "19", "course": "3"},
    {"name":"Zak",  "phone":"0631234567", "age": "21", "course": "4"}
]

def printAllList():
    sorted_list = sorted(list, key=lambda x: x["name"])  
    for elem in sorted_list:
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + ", Age is" + elem["age"] + ", Course of university is" + elem["course"]
        print(strForPrint)
    return

def addNewElement():
    name = input("Please enter student name : ")
    phone = input("Please enter student phone : ")
    age = input("Please enter student age : ")
    course = input("Please enter student course : ")
    newItem = {"name": name, "phone": phone, "age": age, "course": course}
    # find insert position

    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        # list.pop(deletePosition)
        del list[deletePosition]
    return


def updateElement():
    name = input("Please enter name to be updated: ")
    for index, student in enumerate(list):
        if name == student["name"]:
            newname = input("Enter new name: ")
            newphone = input("Enter new phone: ")
            newage = input("Enter new age: ")
            newcourse = input("Enter new course: ")
            newElement = {"name": newname, "phone": newphone, "age": newage, "course": newcourse}

            del list[index]
            insertPosition = 0
            for i, elem in enumerate(list):
                if newname > elem["name"]:
                    insertPosition =+ 1
                else:
                    break
            list.insert(insertPosition, newElement)
            print("Element has been updated")
            break
    else:
        print("Student not found")

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")


main()