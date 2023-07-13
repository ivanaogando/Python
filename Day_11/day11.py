"""
day11.py

Project: None

Maintainer Ivana Ogando González (you@you.you)
Created @ Wednesday, 12th July 2023 8:43:12 pm

Copyright (c) 2023 Your Company
All Rights Reserved
"""
# %%%%%%%%%% FUNCTIONS %%%%%%%%%%

# Declaring and Calling a Function
print("\n>> Declaring and Calling a Function")
"""
--Declaring a function
def function_name():
    codes
    codes
--Calling a function
function_name()
"""

# Function without Parameters
print("\n>> Function without Parameters")


def generate_full_name():
    first_name = "Ivana"
    last_name = "Ogando"
    space = " "
    full_name = first_name + space + last_name
    print(full_name)


generate_full_name()  # calling a function


def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)


add_two_numbers()

# Function Returning a Value - Part 1
print("\n>> Function Returning a Value - Part 1")


def generate_full_name_2():
    first_name = "Ivana"
    last_name = "Ogando"
    space = " "
    full_name = first_name + space + last_name
    return full_name


print(generate_full_name_2())


def add_two_numbers_2():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total


print(add_two_numbers_2())

# Function with Parameters
print("\n>> Function with Parameters")
print("\n Single parameter")


# If our function takes a parameter, we should call our function with an arg.
def greetings(name):
    message = name + ", welcome to Python!"
    return message


print(greetings("Ivana"))


def add_ten(num):
    ten = 10
    return num + ten


print(add_ten(90))


def square_number(x):
    return x * x


print(square_number(2))


def area_of_circle(r):
    PI = 3.14
    area = PI * r**2
    return area


print(area_of_circle(10))


def sum_of_numbers(n):
    total = 0
    for i in range(n + 1):
        total += i
    print(total)


print(sum_of_numbers(10))  # 55
print(sum_of_numbers(100))  # 5050

print("\n Two parameters")


def generate_full_name_3(first_name, last_name):
    space = " "
    full_name = first_name + space + last_name
    return full_name


print("Full Name: ", generate_full_name_3("Ivana", "Ogando"))


def sum_two_numbers_3(num_one, num_two):
    sum = num_one + num_two
    return sum


print("Sum of two numbers: ", sum_two_numbers_3(1, 9))


def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age


print("Age: ", calculate_age(2023, 2000))


def weight_of_object(mass, gravity):
    weight = str(mass * gravity) + " N"  # the value has to be changed to a string first
    return weight


print("Weight of an object in Newtons: ", weight_of_object(100, 9.81))

# Passing Arguments with Key and Value
print("\n>> Passing Arguments with Key and Value")


def print_fullname_4(firstname, lastname):
    space = " "
    full_name = firstname + space + lastname
    print(full_name)


print(print_fullname_4(firstname="Ivana", lastname="Ogando"))


def add_two_numbers_4(num1, num2):
    total = num1 + num2
    print(total)


print(add_two_numbers_4(num2=3, num1=2))  # Order does not matter

# Function Returning a Value - Part 2
print("\n>> Function Returning a Value - Part 2")

print("\n Returning a string:")


def print_name(firstname):
    return firstname


print_name("Ivana")


def print_full_name(firstname, lastname):
    space = " "
    full_name = firstname + space + lastname
    return full_name


print_full_name(firstname="Ivana", lastname="Ogando")

print("\n Returning a number:")


def add_two_numbers_5(num1, num2):
    total = num1 + num2
    return total


print(add_two_numbers_5(2, 3))


def calculate_age_5(current_year, birth_year):
    age = current_year - birth_year
    return age


print("Age: ", calculate_age_5(2023, 2000))

print("\n Returning a boolean:")


def is_even(n):
    if n % 2 == 0:
        print("even")
        return True  # return stops further execution of the function, similar to break
    return False


print(is_even(10))  # True
print(is_even(7))  # False

print("\n Returning a list:")


def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens


print(find_even_numbers(10))


# Function with Default Parameters
print("\n>> Function with Default Parameters")


def greetings_6(name="Peter"):
    message = name + ", welcome to Python!"
    return message


print(greetings_6())
print(greetings_6("Ivana"))


def generate_full_name_6(first_name="ivana", last_name="ogando"):
    space = " "
    full_name = first_name + space + last_name
    return full_name


print(generate_full_name_6())
print(generate_full_name_6("David", "Smith"))


def calculate_age_6(birth_year, current_year=2023):
    age = current_year - birth_year
    return age


print("Age: ", calculate_age_6(2000))


def weight_of_object_6(mass, gravity=9.81):
    weight = str(mass * gravity) + " N"  # the value has to be changed to string first
    return weight


print("Weight of an object in Newtons: ", weight_of_object_6(100))
print("Weight of an object in Newtons: ", weight_of_object_6(100, 1.62))

# Arbitrary Number of Arguments
print("\n>> Arbitrary Number of Arguments")


def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num  # same as total = total + num
    return total


print(sum_all_nums(2, 3, 5))  # 10

# Default and Arbitrary Number of Parameters in Functions
print("\n>> Default and Arbitrary Number of Parameters in Functions")


def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)


print(generate_groups("Team-1", "Ivana", "Brook", "David", "Eyob"))

# Function as a Parameter of Another Function
print("\n>> Function as a Parameter of Another Function")


# You can pass functions around as parameters
def square_number_7(n):
    return n * n


def do_something(f, x):
    return f(x)


print(do_something(square_number_7, 3))  # 27
