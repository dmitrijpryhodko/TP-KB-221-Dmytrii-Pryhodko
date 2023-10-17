def add(a, b):
    return a + b

def min(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Ділення на нуль неможливе")
        return None

while True:
    exit = str(input("Enter 'q' for quit or 'Enter' for continue: "))
    if exit == 'q':
        break

    try:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        operation = input("Operation (+, -, *, /): ")
        
    
    
        if operation == "+":
            result = add(a, b)
        elif operation == "-":
            result = min(a, b)
        elif operation == "/":
            result = div(a, b)
        elif operation == "*":
            result = mult(a, b)
        else:
            print("Невідома операція")
            continue

        print("Результат:", result)
    except ValueError:
        print("Ви ввели щось не те")
        
