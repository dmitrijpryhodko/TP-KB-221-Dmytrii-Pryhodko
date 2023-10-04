#1
students1 = ["Emma", "Jon", "Bob"]          #студенти першої групи
students2 = ["Stiven", "Jake", "Lara"]      #студенти другогї групи

students1.extend(students2)
print(students1)
#extend() - додає вказані елементи списку у кінець поточного списку

#2
students1 = ["Emma", "Jon", "Bob"]        
students1.append("Tailer")
print(students1)

#append() - додає елемент до списку

#3
students1 = ["Emma", "Jon", "Bob"]          
students1.insert(1, "Tailer")
print(students1)

#insert() - додає елемент до списку за індексом

#4
fruits = ["apple", "orange", "lemon", "cherry"]
fruits.remove("orange")
print(fruits)

#remove() - видаляє елемент з списку

#5
fruits = ["apple", "orange", "lemon", "cherry"]
fruits.clear()
print(fruits)

#clear() - повністю видаляє список

#6
def myFunc(e):
    return len (e)
animals = ["bird", "tiger", "cat", "leo"]
animals.sort(key=myFunc)
print(animals)
animals.sort(reverse= True, key=myFunc)
print(animals)

#sort() - сортує список. у нашому випадку сортування відбулося за довжиною і в оберненому порядку

#7
fruits = ["apple", "orange", "lemon", "cherry"]
fruits.reverse()
print(fruits)

#reverse() - розвертає список

#8
fruits = ["apple", "orange", "lemon", "cherry"]
a = fruits.copy()
print(fruits)
print(a)




