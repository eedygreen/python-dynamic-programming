#!/bin/python

# double the list with map()

# map(function, list)
# Note: map() returns an object which can be converted back to list with the function list()

# express function with lambda

num_list = [-2, 8, 3, -1, 7]

double_list = map(lambda n: n * 2, num_list)

# print the list
print(list(double_list))