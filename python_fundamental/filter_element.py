#!/bin/python

num_list = [ 2, 23, 43, 56, 76, 98, 89, 34]

greater_than_60 = filter(lambda n: n > 60, num_list)

print(list(greater_than_60))

greater_than_50 = list(filter(lambda n: n > 50, num_list))

print(greater_than_50)