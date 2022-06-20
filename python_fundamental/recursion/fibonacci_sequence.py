#!/bin/python

# fibonacci sequence is the sum of the first two numbers before the number n
# first two numbers are 0 and 1

def fibo(n):
    if n <= 1:  # first number sequence
        return 0
    elif n == 2: # the second number sequence
        return 1
    else: 
        return fibo(n - 1) + fibo( n - 2)

print(fibo(3))