#1
student = {'Name': 'Dima', 'Age': 18}
student.update({'Course': 2})
print(student)

#update() - вставляє вказані елементи до словника

#2
student = {'Name': 'Dima', 'Age': 18, 'Surname': 'Pryhod`ko'}
del student['Age']
print(student)

#del() - видаляє елемент із словника

#3
student = {'Name': 'Dima', 'Age': 18, 'Surname': 'Pryhod`ko'}
student.clear()
print(student)

#clear() - видаляє весь словник

#4
student = {'Name': 'Dima', 'Age': 18, 'Surname': 'Pryhod`ko'}
x = student.keys()
print(x)

#keys() - повертає об'єкт представлення

#5
student = {'Name': 'Dima', 'Age': 18, 'Surname': 'Pryhod`ko'}
x = student.values()
print(x)

#values() - повертає дані зі словника

#6
student = {'Name': 'Dima', 'Age': 18, 'Surname': 'Pryhod`ko'}
x = student.items()
print(x)
