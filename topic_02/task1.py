import math

def findD(a, b, c):
    discriminant = b**2 - 4 * a * c
    return discriminant

def find_roots(a, b, c):
    discriminant = findD (a, b, c)
    
    if discriminant > 0:
        # Два різних корені
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    elif discriminant == 0:
        # Один подвійний корінь
        root1 = -b / (2*a)
        return (root1,)
    else:
        # Немає дійсних коренів
        return None
    
a = int(input("Введіть значення a: "))
b = int(input("Введіть значення b: "))
c = int(input("Введіть значення c: ")) 
roots = find_roots(a, b, c)
if roots:
    if len(roots) == 2:
        print(f"Два корені: {roots[0]} та {roots[1]}")
    else:
        print(f"Один подвійний корінь: {roots[0]}")
else:
    print("Немає дійсних коренів")