"""
day2exercises.py

Project: None

Maintainer Ivana Ogando González (you@you.you)
Created @ Tuesday, 11th July 2023 1:21:18 pm

Copyright (c) 2023 Your Company
All Rights Reserved
"""

# %%%%%%%%%%%%%%% EXERCISE 1 %%%%%%%%%%%%%%%

# Declare a first name variable and assign a value to it
first_name = "Ivana"

# Declare a last name variable and assign a value to it
last_name = "Ogando"

# Declare a full name variable and assign a value to it
full_name = {
    "firstname": "Ivana",
    "lastname": "Ogando",
}

# Declare a country variable and assign a value to it
country = "Spain"

# Declare a city variable and assign a value to it
city = "Vigo"

# Declare an age variable and assign a value to it
age = 23

# Declare a year variable and assign a value to it
year = 2023

# Declare a variable is_married and assign a value to it
is_married = False

# Declare a variable is_true and assign a value to it
is_true = False

# Declare a variable is_light_on and assign a value to it
is_light_on = False

# Declare multiple variable on one line
is_married, is_true, is_light_on = (False, False, False)

# %%%%%%%%%%%%%%% EXERCISE 2 %%%%%%%%%%%%%%%
print(">> EXERCISE 2")

# 1. Check the data type of all your variables using type() built-in function
print("first_name: ", type(first_name))
print("last_name: ", type(last_name))
print("full_name: ", type(full_name))
print("country: ", type(country))
print("city: ", type(city))
print("age: ", type(age))
print("year: ", type(year))
print("is_married: ", type(is_married))
print("is_true: ", type(is_true))
print("is_light_on: ", type(is_light_on))

# 2. Using the len() built-in function, find the length of your first name
print("\n")
len_first_name = len(first_name)
print("Length first_name: ", len_first_name)

# 3. Compare the length of your first name and your last name
len_last_name = len(last_name)
print("Length last_name: ", len_last_name)
print("Length first - last: ", (len_first_name - len_last_name))

# 4. Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

# 4.1. Add num_one and num_two and assign the value to a variable total
print("\n")


def sum(num_one, num_two):
    return num_one + num_two


addition = sum(num_one, num_two)
print("Addition: ", addition)


# 4.2. Subtract num_two from num_one and assign the value to a variable diff
def sub(num_one, num_two):
    return num_one - num_two


diff = sub(num_one, num_two)
print("Subtraction: ", diff)


# 4.3. Multiply num_two and num_one and assign the value to a variable product
def prod(num_one, num_two):
    return num_one * num_two


product = prod(num_one, num_two)
print("Subtraction: ", product)


# 4.4. Divide num_one by num_two and assign the value to a variable division
def div(num_one, num_two):
    return num_one / num_two


division = div(num_one, num_two)
print("Division: ", division)


# 4.5. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
def mod(num_one, num_two):
    return num_one % num_two


remainder = mod(num_one, num_two)
print("Remainder: ", remainder)


# 4.6. Calculate num_one to the power of num_two and assign the value to a variable exp
def power(num_one, num_two):
    return num_one**num_two


exp = power(num_one, num_two)
print("Power result: ", exp)


# 4.7. Find floor division of num_one by num_two and assign the value to a variable floor_division
def floordiv(num_one, num_two):
    return num_one // num_two


floor_division = floordiv(num_one, num_two)
print("Floor division: ", floor_division)

# 5. The radius of a circle is 30 meters.
print("\n")
radius = 30

# 5.1. Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_cirle = (radius**2) * 3.141592

# 5.2. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_cirle = radius * 2 * 3.141592

# 5.3. Take radius as user input and calculate the area.
radius = input("Enter the radius: ")
area_of_cirle = (float(radius)**2) * 3.141592

# 6.Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
country = input("Enter country: ")
age = input("Enter age: ")
