# Nested Funcitons

def add(n1: int, n2: int) -> int:
    return n1+n2

def calculator(function, n1: int, n2: int) -> int:
    result = function
    return result

print(type(calculator(add, 1, 1)))