#!/bin/python3

'''
String concatenation
f string - This is prefferable because its straight forward and simple
+
.format
'''

# answ = input("enter the name of your best friend: ")

# digit = " Dude"

# # Example of f string
# def stringJoiner(data):
#     con_cat = f"{data} is the real {digit}!"
#     return con_cat

# print(stringJoiner(answ))


'''
Steps
1. define an input variable to allow users to add their friend's name

2. Write a function that accept the users's input and add it to predefined strings

3. print the result
'''

# 1
user_name = input("Please, enter your friend's name here: ")

#2, use f string
def joinName( data ):
    join_names = f"Your friend, {user_name} is lucky to have you. {user_name} is a nice buddy!"
    return join_names

print(joinName(user_name))