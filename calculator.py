# Simple calculator - Tanya Garg

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print("Simple Calculator")
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    op = input("Choose operation (+ - * /): ")
    ops = {"+": add, "-": subtract, "*": multiply, "/": divide}
    if op in ops:
        try:
            print("Result:", ops[op](x, y))
        except ValueError as e:
            print("Error:", e)
    else:
        print("Invalid operation")
