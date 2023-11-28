import csv
import sys


def FileLoad(file):
	with open(file, encoding="utf-8") as file:
		result = csv.DictReader(file)
		return [row for row in result]

def SaveFile(file, list):
	names = ["name", "phone", "age", "course"]
	try:
		with open(file, "w", newline="", encoding="utf-8") as file:
			ResFile = csv.DictWriter(file, fieldnames=names)
			ResFile.writeheader()
			ResFile.writerows(list)
		print(f"The data is saved in {file}.")
	except IOError as e:
		print(f"Error saving to {file}: {e}")

def printAllList(list):
    sorted_list = sorted(list, key=lambda x: x["name"])  
    for elem in sorted_list:
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + ", Age is" + elem["age"] + ", Course of university is" + elem["course"]
        print(strForPrint)
    return

def addNewElement(list):
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

def deleteElement(list):
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


def updateElement(list):
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

            



list = [ ]
AFile = None

def main():
	global AFile

	if len(sys.argv) > 1:
		try:
			file = sys.argv[1]
			list.extend(FileLoad(file))
			print("Data loaded successfully.")
			AFile = file
		except IOError as e:
			print("File upload error.")
	else:
		print("No CSV file specified in the command line arguments.")


def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print, S save, L load, X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement(list)
                printAllList(list)
            case "U" | "u":
                print("Existing element will be updated")
                updateElement(list)
            case "D" | "d":
                print("Element will be deleted")
                deleteElement(list)
            case "P" | "p":
                print("List will be printed")
                printAllList(list)
            case "X" | "x":
                print("Exit()")
                break
            case "L":
                try:
                        file = input("Enter the name of the CSV file from which you want to download data: ")
                        list.extend(FileLoad(file))
                        print("Data loaded successfully.")
                        AFile = file
                except IOError as e:
                        print("File upload error.")
            case "S":
                    file = input("Enter a name for the CSV file to save the data to: ")
                    SaveFile(file, list)
            case "X":
                    print("Exit")
                    break
            case _:
                    print("Wrong choice")
                    
if __name__ == "__main__":
	main()



