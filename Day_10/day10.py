"""
day10.py

Project: None

Maintainer Ivana Ogando González (you@you.you)
Created @ Wednesday, 12th July 2023 4:23:58 pm

Copyright (c) 2023 Your Company
All Rights Reserved
"""
# %%%%%%%%%% LOOPS %%%%%%%%%%

# While Loop
print("\n>> While Loop")
count = 0
while count < 5:
    print(count)
    count = count + 1  # prints from 0 to 4

print("\n")
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

# Break and Continue - Part 1
print("\n>> Break and Continue - Part 1")

print(" Break")
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

print("\n Continue")
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1

# For Loop
print("\n>> For Loop")
print("For loop with list: ")
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:  # number is temporary name to refer to the list's items
    print(number)  # the numbers will be printed line by line, from 0 to 5

print("\nFor loop with string: ")
language = "Python"
for letter in language:
    print(letter)

print("\n")
for i in range(len(language)):
    print(language[i])

print("\nFor loop with tuple: ")
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

print(
    "\nFor loop with dictionary looping through it to give the key of the dictionary: "
)
person = {
    "first_name": "Ivana",
    "last_name": "Ogando",
    "age": 250,
    "country": "Spain",
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}
for key in person:
    print(key)

print("\n")
for key, value in person.items():
    print(key, value)  # this way we get both keys and values printed out

print("\nLoops in set: ")
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
for company in it_companies:
    print(company)

# Break and Continue - Part 2
print("\n>> Break and Continue - Part 2")
print(" Break")
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        break

print("\n Continue")
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print("Next number should be ", number + 1) if number != 5 else print("loop's end")
print("outside the loop")

# The Range Function
print("\n>> The Range Function")
"""
The range() function is used list of numbers. The range(start, end, step) takes
three parameters: starting, ending and increment. By default it starts from 0
and the increment is 1. The range sequence needs at least 1 argument (end).

# syntax
for iterator in range(start, end, step):
"""
lst = list(range(11))
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(
    range(1, 11)
)  # 2 arguments indicate start and end of sequence, step set to default 1
print(st)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print("\n")
lst = list(range(0, 11, 2))
print(lst)  # [0, 2, 4, 6, 8, 10]
st = set(range(0, 11, 2))
print(st)  # {0, 2, 4, 6, 8, 10}

print("\n")
for number in range(11):
    print(number)  # prints 0 to 10, not including 11

# Nested For Loop
print("\n>> Nested For Loop")
person = {
    "first_name": "Ivana",
    "last_name": "Ogando",
    "age": 250,
    "country": "Spain",
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}
for key in person:
    if key == "skills":
        for skill in person["skills"]:
            print(skill)

# For Else
print("\n>> For Else")
for number in range(11):
    print(number)  # prints 0 to 10, not including 11
else:
    print("The loop stops at", number)

# Pass
print("\n>> Pass")
for number in range(6):
    pass
