a = int(input("Enter a: "))
b = int(input("Enter b: "))
operation = input("Operation: ")

def sum(a,b):
    return a + b

def min(a,b):
    return a - b

def div(a,b):
    return a / b

def mult(a,b):
    return a * b

if operation == "+":
    result = sum(a,b)


elif operation == "-":
    result = min(a,b)
    
elif operation == "/":
    result = div(a,b)

elif operation == "*":
    result = mult(a,b)
print(result)