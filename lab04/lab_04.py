operators = {'+', '-', '*', '/', '^'}

def token_list(tokens):
    stack = []
    operatorStack = []

    def math_operators():
        a, b = stack.pop(), stack.pop()
        operator = operatorStack.pop()
        if operator == '+':
            stack.append(b + a)
        elif operator == '-':
            stack.append(b - a)
        elif operator == '*':
            stack.append(b * a)
        elif operator == '/':
            stack.append(int(b / a))
        elif operator == '^':
            stack.append(b ** a)

    for token in tokens:
        if token == '(':
            operatorStack.append(token)
        elif token == ')':
            while operatorStack and operatorStack[-1] != '(':
                math_operators()
            operatorStack.pop()
        elif token in operators:
            while operatorStack and operatorStack[-1] in operators:
                current_operator = operatorStack[-1]
                priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
                if priority.get(token, 0) <= priority.get(current_operator, 0):
                    math_operators()
                else:
                    break

            operatorStack.append(token)
        else:
            stack.append(int(token))

    while operatorStack:
        math_operators()

    return stack.pop()

def main():
    expression = input("Введіть вираз в ЗПЗ: ")
    tokens = expression.split()
    result = token_list(tokens)
    print(result)

if __name__ == "__main__":
    main()