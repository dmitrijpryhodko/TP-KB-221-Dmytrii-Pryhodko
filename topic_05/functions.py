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