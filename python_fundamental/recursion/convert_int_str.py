#!/bin/env python
# convert int to strings

# {}.format 
def rep_cat_form(x, y):
    conv_x_str = "{}".format(x)
    conv_y_str = "{}".format(y)

# str() method
def rep_cat(x, y):
    # Write your code here
    return str(x) * 10 + str(y) * 5

print(rep_cat(3, 4))