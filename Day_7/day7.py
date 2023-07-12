"""
day7.py

Project: None

Maintainer Ivana Ogando González (you@you.you)
Created @ Wednesday, 12th July 2023 12:42:45 pm

Copyright (c) 2023 Your Company
All Rights Reserved
"""

# %%%%%%%%%% SETS %%%%%%%%%%
"""
Set is a collection of unordered and unindexed distinct elements. In Python set
is used to store unique items, and it is possible to find the union,
intersection, difference, symmetric difference, subset, super set and disjoint
set among sets.
"""

print("\n>> Creating a Set")
# syntax
fruits = {"banana", "orange", "mango", "lemon"}  # set with initial values

print("\n>> Getting Set's Length")
fruits = {"banana", "orange", "mango", "lemon"}
len(fruits)
print("The length of ", fruits, " is: ", len(fruits))

print("\n>> Accessing Items in a Set -> LOOP SECTION")

print("\n>> Checking an Item")
fruits = {"banana", "orange", "mango", "lemon"}
print("Is mango in the fruits?")
print("mango" in fruits)  # True

# syntax
st = {"item1", "item2", "item3", "item4"}
print("Does set st contain item3? ", "item3" in st)  # True

print("\n>> Adding Items to a Set")
print("\nAdd one item using add()")
fruits = {"banana", "orange", "mango", "lemon"}
fruits.add("lime")
print(fruits)

print("\nAdd multiple items using update()")
fruits = {"banana", "orange", "mango", "lemon"}
vegetables = ("tomato", "potato", "cabbage", "onion", "carrot")
fruits.update(vegetables)
print(fruits)

print("\n>> Removing Items from a Set: pop()")
fruits = {"banana", "orange", "mango", "lemon"}
print(fruits)
removed_item = fruits.pop()
print("Now: ", fruits)

print("\n>> Clearing Items in a Set")
fruits = {"banana", "orange", "mango", "lemon"}
print(fruits)
fruits.clear()
print(fruits)  # set()

print("\n>> Deleting a Set")
fruits = {"banana", "orange", "mango", "lemon"}
del fruits

print("\n>> Converting List to Set")
fruits = ["banana", "orange", "mango", "lemon", "orange", "banana"]
fruits = set(fruits)  # {'mango', 'lemon', 'banana', 'orange'}

print("\n>> Joining Sets")
print("\n union()")
fruits = {"banana", "orange", "mango", "lemon"}
vegetables = {"tomato", "potato", "cabbage", "onion", "carrot"}
print(
    fruits.union(vegetables)
)  # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

print("\n update()")
fruits = {"banana", "orange", "mango", "lemon"}
vegetables = {"tomato", "potato", "cabbage", "onion", "carrot"}
fruits.update(vegetables)
print(
    fruits
)  # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

print("\n>> Finding Intersection Items")
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers)  # {0, 2, 4, 6, 8, 10}

python = {"p", "y", "t", "h", "o", "n"}
dragon = {"d", "r", "a", "g", "o", "n"}
python.intersection(dragon)  # {'o', 'n'}

print("\n>> Checking Subset and Super Set")
# Subset: issubset(); Super set: issuperset
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers)  # False, because it is a super set
whole_numbers.issuperset(even_numbers)  # True

python = {"p", "y", "t", "h", "o", "n"}
dragon = {"d", "r", "a", "g", "o", "n"}
python.issubset(dragon)  # False

print("\n>> Checking the Difference Between Two Sets")
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers)  # {1, 3, 5, 7, 9}

python = {"p", "y", "t", "o", "n"}
dragon = {"d", "r", "a", "g", "o", "n"}
python.difference(
    dragon
)  # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
dragon.difference(python)  # {'d', 'r', 'a', 'g'}

print("\n>> Finding Symmetric Difference Between Two Sets")
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers)  # {0, 6, 7, 8, 9, 10}

python = {"p", "y", "t", "h", "o", "n"}
dragon = {"d", "r", "a", "g", "o", "n"}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}

print("\n>> Joining Sets")
even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers)  # True, because no common item

python = {"p", "y", "t", "h", "o", "n"}
dragon = {"d", "r", "a", "g", "o", "n"}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}
