a = int(input("Enter a: "))
b = int(input("Enter b: "))
operation = input("Operation: ")

match operation:
    case "+":
        print (a + b)
    case "-":
        print (a - b)
    case "/":
        print (a / b)
    case "*":
        print (a * b)