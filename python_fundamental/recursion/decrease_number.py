#!/bin/python

# decrease number using recursion

def dec_number(number):
    print(number)
    if number == 0:
        return number
    dec_number(number -1) # decrease the number by 1 ontill number == 0

    #print(number)

dec_number(4)