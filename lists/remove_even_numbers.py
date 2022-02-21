#!/bin/env python3
# Path: python-dynamic-programming/lists/remove_even_numbers.py

# Create a funtion to remove even numbers from a list

'''
step 1: Define a function that takes a list as an argument
step 2: Create a new list
step 3: Iterate through the list
step 4: Filter - If the number is even, remove it from the list
'''

# lets call the function remove_even_numbers

def remove_even_numbers(numbers): # step 1
    my_new_list = []              # step 2
    for element in numbers:       # step 3
        if element % 2 != 0:
            my_new_list.append(element) # step 4
    return my_new_list

print(remove_even_numbers([1,2,3,4,5,6,7,8,9]))


# pythonic way  
'''
define function
return [expression(n) for n in old_list if n % 2 != 0]
'''

def remove_even(given_list: list) -> list:
    return [elements for elements in given_list if elements % 2 !=0]

print(remove_even([11,21,33,44,55,66,77,88,99]))
