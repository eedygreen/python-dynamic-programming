#!/bin/python3

# find two numbers in a list that sum up to a given number

"""
Step 1: Define a function that takes a list and a number as arguments
Step 2: Create a new list
Step 3: Iterate through the list to get first_list 
        Step : and iterate through the list to get a second_list
Step 4: add elements of the first list to the second list and check if the sum is equal to the given number
Step 5: return the matching elements
"""

def find_numbers(list, numbers):
    for a in range(len(list)):
        for b in range(len(list)):
            if list[a] + list[b] == numbers and a != b:
                return [list[a], list[b]]

print(find_numbers([1,2,3,4,5,6,7,8,9], 2))

