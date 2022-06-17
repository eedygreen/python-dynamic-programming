#!/bin/python

from audioop import mul


def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def subtract(n1, n2):
    return n1 - n2

def calculate(operator, n1, n2):
    return operator(n1, n2)

print(calculate(add, 3, 4))
print(calculate(multiply, 3, 4))