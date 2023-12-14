digits = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
operations = ('+', '-', '*', '/', '^')

def isNumber(unit):
    return all(char in digits for char in unit)

def math_operation(operation):
    if operation in ('+', '-'):
        return 0
    elif operation in ('*', '/'):
        return 1
    elif operation == '^':
        return 2

def Rpn(input):
    stack = []
    output = []

    for token in input.split(' '):
        if isNumber(token):
            output.append(token)
            continue

        if token == '(':
            stack.append(token)
            continue

        if token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
            continue

        if token in operations:
            opPriority = math_operation(token)
            while stack and stack[-1] in operations and math_operation(stack[-1]) >= opPriority:
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return output

def RpnRes(rpn):
    stack = []

    for token in rpn:
        if isNumber(token):
            stack.append(token)
        else:
            b = float(stack.pop())
            a = float(stack.pop())
            result = 0

            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a / b
            elif token == '^':
                result = a ** b

            stack.append(result)

    return stack

def main():
    expression = input("Введіть математичний вираз: ")
    rpn = Rpn(expression)
    
    print("Зворотній польський запис:", rpn)
    print("Результат:", RpnRes(rpn))

if __name__ == '__main__':
    main()
