#!/bin/env python

# check if the bracket are balance

# define a function
# define a check variable
# iterate through if the open bracket is found increase by 1
# if an enclosed bracket is found decreas by 1

def balance_checker(brackets):
    check_bracket = 0
    for bracket in brackets:
        if bracket == '[':
            check_bracket += 1
        elif bracket == ']':
            check_bracket -= 1
        if check_bracket < 0:
            break
    return check_bracket == 0

print(balance_checker('[]'))