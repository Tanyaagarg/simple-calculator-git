# Simple calculator - Tanya Garg

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b


if __name__ == "__main__":
    print("Simple Calculator")
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    op = input("Choose operation (+ - * /): ")
    ops = {"+": add, "-": subtract, "*": multiply, "/": divide}
    if op in ops:
        print("Result:", ops[op](x, y))
    else:
        print("Invalid operation")
