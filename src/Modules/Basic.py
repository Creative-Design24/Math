def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    c = round(a/b)
    r = a - (b * c)
    return [c, r]


def empowerment(a, b):
    return a ** b
