def add(a, b):
    return a + b

def min(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a,b):
    if b != 0:
     return a / b
    if b == 0:
        print("На нуль не ділиться")
        return None


while True:
        exit = str(input("Enter 'q' for quit or 'Enter' for continue: "))
        if exit == 'q':
         break

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