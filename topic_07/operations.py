from functions import Calculator

class CalculatorOperations:
    def __init__(self):
        self.calculator = Calculator()

    def get_operation(self, operation_name):
        if operation_name == "+":
            return self.calculator.add
        elif operation_name == "-":
            return self.calculator.subtract
        elif operation_name == "*":
            return self.calculator.multiply
        elif operation_name == "/":
            return self.calculator.divide
        else:
            print("Некоректний ввід")
