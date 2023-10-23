import functions
import operations
import datetime
def main():
    with open("log.txt", "w") as log_file:  
        while True:
            a = float(input("Введіть перше число: "))
            b = float(input("Введіть друге число: "))    
            operation_name = input("Виберіть операцію: ")    
            operation = operations.get_operation(operation_name)   
            result = operation(a, b)
            log_file.write(f"{datetime.datetime.now()} | {a} | {b} | {operation_name} | {result}\n")
            continueorstop = input("Продовжити чи вийти?(y/n): ")
            if continueorstop != "y":
                break

if __name__ == "__main__":
    main()





