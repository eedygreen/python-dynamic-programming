#!/bin/python3

'''
String concatenation
f string - This is prefferable because its straight forward and simple
+
.format
'''


answ = input("enter the name of your best friend: ")

digit = " Dude"

# Example of f string
def stringJoiner(data):
    con_cat = f"{data} is the real {digit}!"
    return con_cat

print(stringJoiner(answ))