def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


def power(a, b):
    return a ** b

def subtract(a, b):
    return a - b

def modulo(a, b):
    if b == 0:
        return None
    return a % b

if __name__ == "__main__":
    print("Result:",add(2, 3))

    print("Product:",multiply(2, 3))

# TODO: add input from user
