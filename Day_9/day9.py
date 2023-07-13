"""
day9.py

Project: None

Maintainer Ivana Ogando González (you@you.you)
Created @ Wednesday, 12th July 2023 14:03:04 pm

Copyright (c) 2023 Your Company
All Rights Reserved
"""
# %%%%%%%%%% CONDITIONALS %%%%%%%%%%

# If
print("\n>> If Condition ")
a = 3
if a > 0:
    print("A is a positive number")  # A is a positive number

# If-else
print("\n>> If Else")
a = 3
if a < 0:
    print("A is a negative number")
else:
    print("A is a positive number")

# If-Elif-Else
print("\n>> If Elif Else")
a = 0
if a > 0:
    print("A is a positive number")
elif a < 0:
    print("A is a negative number")
else:
    print("A is zero")

# Short Hand
print("\n>> Short Hand")
a = 3
print("A is positive") if a > 0 else print(
    "A is negative"
)  # first condition met, 'A is positive' will be printed

# Nested Conditions
print("\n>> Nested Conditions")
a = 0
if a > 0:
    if a % 2 == 0:
        print("A is a positive and even integer")
    else:
        print("A is a positive number")
elif a == 0:
    print("A is zero")
else:
    print("A is a negative number")

# If Condition and Logical Operators
print("\n>> If Condition and Logical Operators")
a = 0
if a > 0 and a % 2 == 0:
    print("A is an even and positive integer")
elif a > 0 and a % 2 != 0:
    print("A is a positive integer")
elif a == 0:
    print("A is zero")
else:
    print("A is negative")

# If and Or Logical Operators
print("\n>> If and Or Logical Operators")
user = "James"
access_level = 3
if user == "admin" or access_level >= 4:
    print("Access granted!")
else:
    print("Access denied!")
