from functions import*

def userdata():
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    operation = input("Виберіть операцію: ")
    return a, operation, b

def completeoperation(a, operation, b):
    if operation == '+':
        return add(a, b)
    elif operation == '-':
        return min(a, b)
    elif operation == '*':
        return mult(a, b)
    elif operation == '/':
        return div(a, b)
    else:
        return "Невідома операція"
