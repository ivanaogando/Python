"""
day6.py

Project: None

Maintainer Ivana Ogando González (you@you.you)
Created @ Wednesday, 12th July 2023 12:08:57 pm

Copyright (c) 2023 Your Company
All Rights Reserved
"""

# %%%%%%%%%% TUPLES %%%%%%%%%%
"""
A tuple is a collection of different data types which is ordered and unchangeable (immutable). Tuples are written with round brackets, (). Once a tuple is created, we cannot change its values. We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable). Unlike list, tuple has few methods. Methods related to tuples:

- tuple(): to create an empty tuple
- count(): to count the number of a specified item in a tuple
- index(): to find the index of a specified item in a tuple
  - operator: to join two or more tuples and to create a new tuple
"""

print("\n>> Creating a Tuple")
"""
syntax:                      empty_tuple = ()
using the tuple constructor: empty_tuple = tuple()
"""
# syntax
tpl = ("item1", "item2", "item3")
fruits = ("banana", "orange", "mango", "lemon")

print("\n>> Tuple length")
# syntax
tpl = ("item1", "item2", "item3")
print(tpl, ", length: ", len(tpl))

print("\n>> Accessing Tuple Items")
print("\n Positive indexing")
# Syntax
tpl = ("item1", "item2", "item3")
first_item = tpl[0]
second_item = tpl[1]

fruits = ("banana", "orange", "mango", "lemon")
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

print("\n Negative indexing")
# Syntax
tpl = ("item1", "item2", "item3", "item4")
first_item = tpl[-4]
second_item = tpl[-3]

fruits = ("banana", "orange", "mango", "lemon")
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]

print("\n>> Slicing tuples")
print("\n Range of positive indexes")
# Syntax
tpl = ("item1", "item2", "item3", "item4")
all_items = tpl[0:4]  # all items
all_items = tpl[0:]  # all items
middle_two_items = tpl[1:3]  # does not include item at index 3

fruits = ("banana", "orange", "mango", "lemon")
all_fruits = fruits[0:4]  # all items
all_fruits = fruits[0:]  # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:]

print("\n Range of negative indexes")
# Syntax
tpl = ("item1", "item2", "item3", "item4")
all_items = tpl[-4:]  # all items
middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)

fruits = ("banana", "orange", "mango", "lemon")
all_fruits = fruits[-4:]  # all items
orange_mango = fruits[-3:-1]  # doesn't include item at index 3
orange_to_the_rest = fruits[-3:]

print("\n>> Changing Tuples to Lists")
fruits = ("banana", "orange", "mango", "lemon")
fruits = list(fruits)
fruits[0] = "apple"
print(fruits)  # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)  # ('apple', 'orange', 'mango', 'lemon')

print("\n>> Checking an Item in a Tuple")
# Syntax
tpl = ("item1", "item2", "item3", "item4")
"item2" in tpl  # True

fruits = ("banana", "orange", "mango", "lemon")
print("orange" in fruits)  # True
print("apple" in fruits)  # False

print("\n>> Joining Tuples")
# syntax
tpl1 = ("item1", "item2", "item3")
tpl2 = ("item4", "item5", "item6")
tpl3 = tpl1 + tpl2
print(tpl3)
fruits = ("banana", "orange", "mango", "lemon")
vegetables = ("Tomato", "Potato", "Cabbage", "Onion", "Carrot")
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

print("\n>> Deleting Tuples")
# syntax
tpl1 = ("item1", "item2", "item3")
del tpl1

fruits = ("banana", "orange", "mango", "lemon")
del fruits

