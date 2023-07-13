"""
day17.py

Project: None

Maintainer Ivana Ogando González (you@you.you)
Created @ Thursday, 13th July 2023 3:33:35 pm

Copyright (c) 2023 Your Company
All Rights Reserved
"""

# %%%%%%%%%% EXCEPTION HANDLING %%%%%%%%%%
try:
    name = input("\nEnter your name:")
    year_born = input("Year you were born:")
    age = 2023 - year_born
    print(f"\nYou are {name}. And your age is {age}.")
except:
    print("Something went wrong")

try:
    name = input("\nEnter your name:")
    year_born = input("Year you were born:")
    age = 2023 - year_born
    print(f"You are {name}. And your age is {age}.")
except TypeError:
    print("Type error occured")
except ValueError:
    print("Value error occured")
except ZeroDivisionError:
    print("zero division error occured")

try:
    name = input("\nEnter your name:")
    year_born = input("Year you born:")
    age = 2019 - int(year_born)
    print("You are " + name + ". And your age is " + str(age) + ".")
except TypeError:
    print("Type error occur")
except ValueError:
    print("Value error occur")
except ZeroDivisionError:
    print("zero division error occur")
else:
    print("I usually run with the try block")
finally:
    print("I alway run.")

try:
    name = input("\nEnter your name:")
    year_born = input("Year you born:")
    age = 2019 - int(year_born)
    print("You are {name}. And your age is {age}.")
except Exception as e:
    print(e)

# %%%%%%%%%% PACKING AND UNPACKING ARGUMENTS IN PYTHON %%%%%%%%%%
print("\n>> UNPACKING")
print("\n Unpacking lists")


def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e


lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))

numbers = range(2, 7)  # normal call with separate arguments
print("\n", list(numbers))  # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(numbers)  # [2, 3, 4, 5,6]

countries = ["Finland", "Sweden", "Norway", "Denmark", "Iceland"]
fin, sw, nor, *rest = countries
print("\n", fin, sw, nor, rest)  # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)  # 1 [2, 3, 4, 5, 6] 7

print("\n Unpacking dictionaries")


def unpacking_person_info(name, country, city, age):
    return f"{name} lives in {country}, {city}. He is {age} year old."


dct = {"name": "Asabeneh", "country": "Finland", "city": "Helsinki", "age": 250}
print(
    unpacking_person_info(**dct)
)  # Asabeneh lives in Finland, Helsinki. He is 250 years old.

print("\n>> PACKING")

print("\n>> PACKING LISTS")


def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s


print(sum_all(1, 2, 3))  # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7))  # 28

print("\n Packing dictionaries")


def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # Printing dictionary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs


print(packing_person_info(name="Asabeneh", country="Finland", city="Helsinki", age=250))

# %%%%%%%%%% SPREADING IN PYTHON %%%%%%%%%%
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ["Finland", "Sweden", "Norway"]
country_lst_two = ["Denmark", "Iceland"]
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']

# %%%%%%%%%% ENUMERATE %%%%%%%%%%
for index, item in enumerate([20, 30, 40]):
    print(index, item)

for i in enumerate([nordic_countries]):
    print("hi")
    if i == "Finland":
        print("The country {i} has been found at index {index}")
# %%%%%%%%%% ZIP %%%%%%%%%%
fruits = ["banana", "orange", "mango", "lemon", "lime"]
vegetables = ["Tomato", "Potato", "Cabbage", "Onion", "Carrot"]
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({"fruit": f, "veg": v})

print(fruits_and_veges)
