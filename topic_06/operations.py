from functions import *
def get_operation(operation_name):
    if operation_name == "+":
        return add
    elif operation_name == "-":
        return min
    elif operation_name == "*":
        return mult
    elif operation_name == "/":
        return div
    else:
        print("Некоректний ввід")

