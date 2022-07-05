#!/bin/env python

# define a function to take in list as a n argument
# define a varibale to count the specified numbers
# iterate the list
# compare the element in the list
# return the amount of the counts
def list_iterator(n):
    counter_num = 0
    for num in n:
        if num > 5:
            counter_num += 1
    return counter_num

print(list_iterator([12, 2, 4, 56, 23, 32, 24, 11, 9]))