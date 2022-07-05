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

print(fibo(6))

# define a function
# declare three variables with two constant,
# first sequence is zero
# second sequence is 1
# third variable is to add the two frist variable 
# compare the given number and return the sequence
# repeate

def fib(n):
    first = 0
    second = 1

    if n < 1:
        return -1

    if n == 1:
      return first

    if n == 2:
        return second

    counter = 3

    while counter <= n:
        fib_seq = first + second
        first = second
        second = fib_seq
        counter +=1
    return fib_seq

print(fib(6))