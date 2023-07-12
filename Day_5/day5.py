"""
day5.py

Project: None

Maintainer Ivana Ogando González (you@you.you)
Created @ Wednesday, 12th July 2023 10:03:36 am

Copyright (c) 2023 Your Company
All Rights Reserved
"""

# %%%%%%%%%% LISTS %%%%%%%%%%

print("\n>> How to Create a List")
fruits = ["banana", "orange", "mango", "lemon"]  # list of fruits
vegetables = ["Tomato", "Potato", "Cabbage", "Onion", "Carrot"]
animal_products = ["milk", "meat", "butter", "yoghurt"]
web_techs = ["HTML", "CSS", "JS", "React", "Redux", "Node", "MongDB"]
countries = ["Finland", "Estonia", "Denmark", "Sweden", "Norway"]

# Print the lists and its length
print("Fruits:", fruits)
print("Number of fruits:", len(fruits))
print("Vegetables:", vegetables)
print("Number of vegetables:", len(vegetables))
print("Animal products:", animal_products)
print("Number of animal products:", len(animal_products))
print("Web technologies:", web_techs)
print("Number of web technologies:", len(web_techs))
print("Countries:", countries)
print("Number of countries:", len(countries))

lst = [
    "Asabeneh",
    250,
    True,
    {"country": "Finland", "city": "Helsinki"},
]  # list containing different data types
print("\n", lst)

print("\n>> Accessing List Items Using Positive Indexing")
fruits = ["banana", "orange", "mango", "lemon"]
first_fruit = fruits[0]  # first item using its index
print(first_fruit)  # banana
second_fruit = fruits[1]
print(second_fruit)  # orange
last_fruit = fruits[3]
print(last_fruit)  # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print("Last fruit: ", last_fruit)

print("\n>> Accessing List Items Using Negative Indexing")
fruits = ["banana", "orange", "mango", "lemon"]
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print("First: ", first_fruit)  # banana
print("Last: ", last_fruit)  # lemon
print("Second last: ", second_last)  # mango

print("\n>> Unpacking List Items")
lst = ["item1", "item2", "item3", "item4", "item5"]
first_item, second_item, third_item, *rest = lst
print(first_item)  # item1
print(second_item)  # item2
print(third_item)  # item3
print(rest)  # ['item4', 'item5']

print("\n")
# First Example
fruits = ["banana", "orange", "mango", "lemon", "lime", "apple"]
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)  # banana
print(second_fruit)  # orange
print(third_fruit)  # mango
print(rest)  # ['lemon','lime','apple']

# Second Example about unpacking list
first, second, third, *rest, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(first)  # 1
print(second)  # 2
print(third)  # 3
print(rest)  # [4,5,6,7,8,9]
print(tenth)  # 10

# Third Example about unpacking list
countries = [
    "Germany",
    "France",
    "Belgium",
    "Sweden",
    "Denmark",
    "Finland",
    "Norway",
    "Iceland",
    "Estonia",
]
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

print("\n>> Slicing Items from a List")
print("\n Positive indexing")
fruits = ["banana", "orange", "mango", "lemon"]
all_fruits = fruits[0:4]  # it returns all the fruits
all_fruits = fruits[0:]  # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3]  # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[
    ::2
]  # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']

print("\n Negative indexing")
fruits = ["banana", "orange", "mango", "lemon"]
all_fruits = fruits[-4:]  # it returns all the fruits
orange_and_mango = fruits[
    -3:-1
]  # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[
    -3:
]  # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
reverse_fruits = fruits[
    ::-1
]  # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']

print("\n>> Modifying Lists")
fruits = ["banana", "orange", "mango", "lemon"]
fruits[0] = "avocado"
print(fruits)  # ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = "apple"
print(fruits)  # ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = "lime"
print(fruits)  # ['avocado', 'apple', 'mango', 'lime']

print("\n>> Checking Items in a List")
fruits = ["banana", "orange", "mango", "lemon"]
does_exist = "banana" in fruits
print(does_exist)  # True
does_exist = "lime" in fruits
print(does_exist)  # False

print("\n>> Adding Items to a List")
fruits = ["banana", "orange", "mango", "lemon"]
fruits.append("apple")
print(fruits)  # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append("lime")  # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)

print("\n>> Inserting Items into a List")
fruits = ["banana", "orange", "mango", "lemon"]
fruits.insert(2, "apple")  # insert apple between orange and mango
print(fruits)  # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, "lime")  # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)

print("\n>> Removing Items from a List")
fruits = ["banana", "orange", "mango", "lemon", "banana"]
fruits.remove("banana")
print(
    fruits
)  # ['orange', 'mango', 'lemon', 'banana'] - this method removes the first item in the list
fruits.remove("lemon")
print(fruits)  # ['orange', 'mango', 'banana']

print("\n>> Removing Items Using Pop")
fruits = ["banana", "orange", "mango", "lemon"]
fruits.pop()
print(fruits)  # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)  # ['orange', 'mango']

print("\n>> Removing Items Using Del")
fruits = ["banana", "orange", "mango", "lemon", "kiwi", "lime"]
print(fruits)
del fruits[0]
print(fruits)  # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)  # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[
    1:3
]  # this deletes items between given indexes, so it does not delete the item with index 3!
print(fruits)  # ['orange', 'lime']

print("\n>> Clearing List Items")
fruits = ["banana", "orange", "mango", "lemon"]
fruits.clear()
print(fruits)  # []

print("\n>> Copying a List")
fruits = ["banana", "orange", "mango", "lemon"]
fruits_copy = fruits.copy()
print(fruits_copy)  # ['banana', 'orange', 'mango', 'lemon']

print("\n>> Joining Lists")
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

fruits = ["banana", "orange", "mango", "lemon"]
vegetables = ["Tomato", "Potato", "Cabbage", "Onion", "Carrot"]
fruits_and_vegetables = fruits + vegetables
print(
    fruits_and_vegetables
)  # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

# Joining using extend() method The extend() method allows to append list in a list. See the example below.
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print("\nNumbers:", num1)  # Numbers: [0, 1, 2, 3, 4, 5, 6]
negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print("Integers:", negative_numbers)  # Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ["banana", "orange", "mango", "lemon"]
vegetables = ["Tomato", "Potato", "Cabbage", "Onion", "Carrot"]
fruits.extend(vegetables)
print(
    "Fruits and vegetables:", fruits
)  # Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

print("\n>> Counting Items in a List")
fruits = ["banana", "orange", "mango", "lemon"]
print(fruits.count("orange"))  # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))  # 3

print("\n>> Finding Index of an Item")
fruits = ["banana", "orange", "mango", "lemon"]
print(fruits.index("orange"))  # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))  # 2, the first occurrence

print("\n>> Reversing a List")
fruits = ["banana", "orange", "mango", "lemon"]
fruits.reverse()
print(fruits)  # ['lemon', 'mango', 'orange', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)  # [24, 25, 24, 26, 25, 24, 19, 22]

print("\n>> Sorting List Items")
fruits = ["banana", "orange", "mango", "lemon"]
fruits.sort()
print(fruits)  # sorted in alphabetical order, ['banana', 'lemon', 'mango', 'orange']
fruits.sort(reverse=True)
print(fruits)  # ['orange', 'mango', 'lemon', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)  # [19, 22, 24, 24, 24, 25, 25, 26]

ages.sort(reverse=True)
print(ages)  # [26, 25, 25, 24, 24, 24, 22, 19]

fruits = ["banana", "orange", "mango", "lemon"]
print("\n", sorted(fruits))  # ['banana', 'lemon', 'mango', 'orange']
# Reverse order
fruits = ["banana", "orange", "mango", "lemon"]
fruits = sorted(fruits, reverse=True)
print(fruits)  # ['orange', 'mango', 'lemon', 'banana']
