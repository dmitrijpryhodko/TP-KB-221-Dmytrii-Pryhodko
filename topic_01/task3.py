def findD(a, b, c):
    discriminant = b**2 - 4 * a * c
    return discriminant

# Приклад використання:
a = int(input("Please enter start point: "))
b = int(input("Please end point: "))
c = int(input("please enter mult: "))

D = findD(a, b, c)
print(f"Дискримінант рівняння дорівнює {D}")
