import datetime
from operations import CalculatorOperations

def main():
    calc_operations = CalculatorOperations()
    with open("log.txt", "w") as log_file:  
        while True:
            a = float(input("Введіть перше число: "))
            b = float(input("Введіть друге число: "))    
            operation_name = input("Виберіть операцію: ")    
            operation = calc_operations.get_operation(operation_name)
            if operation:
                result = operation(a, b)
                log_file.write(f"{datetime.datetime.now()} | {a} | {b} | {operation_name} | {result}\n")
            continue_or_stop = input("Продовжити чи вийти? (y/n): ")
            if continue_or_stop != "y":
                break

if __name__ == "__main__":
    main()