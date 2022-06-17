#!/bin/python
def calculate(operator, n1, n2):
    return operator(n1, n2)

def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def subtract(n1, n2):
    return n1 - n2

print(calculate(add, 3, 4))
print(calculate(multiply, 3, 4))

# use lambda to simplify the function
# add func = lambda n1, n2: n1 + n2
# ...
add_num  = calculate(lambda n1, n2: n1 + n2, 3, 4)
mult_num = calculate(lambda n1, n2: n1 * n2, 3, 4)

print(add_num)
print(mult_num)
