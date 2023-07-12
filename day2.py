"""
day2.py

Project: None

Maintainer Ivana Ogando González (you@you.you)
Created @ Tuesday, 11th July 2023 12:37:10 pm

Copyright (c) 2023 Your Company
All Rights Reserved
"""
# %%%%%%%%%%%%%%% VARIABLES %%%%%%%%%%%%%%%

# Variables in Python
first_name = "Ivana"
last_name = "Ogando"
country = "Spain"
city = "Vigo"
age = 250
is_married = True
skills = ["HTML", "CSS", "JS", "React", "Python"]
person_info = {
    "firstname": "Ivana",
    "lastname": "Ogando",
    "country": "Spain",
    "city": "Vigo",
}

print("Hello, World!")  # The text Hello, World! is an argument
print("Hello", ",", "World", "!")  # it can take multiple arguments
print(len("Hello, World!"))  # it takes only one argument

# Printing the values stored in the variables
print("\n >> VALUES STORED IN VARIABLES")
print("First name:", first_name)
print("First name length:", len(first_name))
print("Last name: ", last_name)
print("Last name length: ", len(last_name))
print("Country: ", country)
print("City: ", city)
print("Age: ", age)
print("Married: ", is_married)
print("Skills: ", skills)
print("Person information: ", person_info)

# Declaring multiple variable in a line

first_name, last_name, country, age, is_married = (
    "Ivana",
    "Ogando",
    "Spain",
    250,
    True,
)
print("\n >> MULTIPLE VARIABLES IN A LINE")
print(first_name, last_name, country, age, is_married)
print("First name:", first_name)
print("Last name: ", last_name)
print("Country: ", country)
print("Age: ", age)
print("Married: ", is_married)
print("\n")
first_name = input("What is your name: ")
age = input("How old are you? ")
print("\n")
print(first_name)
print(age)

# %%%%%%%%%%%%%%% DATA TYPES %%%%%%%%%%%%%%%

# Different python data types
# Let's declare variables with various data types

first_name = "Ivana"  # str
last_name = "Ogando"  # str
country = "Spain"  # str
city = "Vigo"  # str
age = 250  # int, it is not my real age, don't worry about it

# Printing out types
print("\n >> TYPES")
print(type("Ogando"))  # str
print(type(first_name))  # str
print(type(10))  # int
print(type(3.14))  # float
print(type(1 + 1j))  # complex
print(type(True))  # bool
print(type([1, 2, 3, 4]))  # list
print(type({"name": "Ivana", "age": 250, "is_married": 250}))  # dict
print(type((1, 2)))  # tuple
print(type(zip([1, 2], [3, 4])))  # set

# Casting
print("\n >> CASTING")

# int to float
num_int = 10
print("num_int:", num_int)  # 10
num_float = float(num_int)
print("num_float:", num_float)  # 10.0

# float to int
gravity = 9.81
print("Gravity in float:", int(gravity))  # 9

# int to str
num_int = 10
print("num_int:", num_int)  # 10
num_str = str(num_int)
print("num_str:", num_str)  # '10'

# str to int or float
num_str = 10.6
print("num_int:", int(num_str))  # 10
print("num_float:", float(num_str))  # 10.6

# str to list
first_name = "Ivana"
print(first_name)  # 'Ivana'
first_name_to_list = list(first_name)
print(first_name_to_list)  # ['I', 'v', 'a', 'n', 'a']


