#!/bin/python

# fibonacci sequence is the sum of the first two numbers before the number n
# first two numbers are 0 and 1

def fibo(n):
    first_seq = 0
    second_Seq = 1
    
    
    if n < 1:
        return -1
    elif n <= 1:  # first number sequence
        return first_seq
    elif n == 2: # the second number sequence
        return second_seq
    else: 
        return fibo(n - 1) + fibo( n - 2)
