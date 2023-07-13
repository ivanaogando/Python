import mymodule
from mymodule import generate_full_name, sum_two_nums
from mymodule import generate_full_name as fullname, sum_two_nums as total
from statistics import *  # importing all the statistics modules
import math


"""
day12.py

Project: None

Maintainer Ivana Ogando González (you@you.you)
Created @ Thursday, 13th July 2023 15:00:08 pm

Copyright (c) 2023 Your Company
All Rights Reserved
"""

# %%%%%%%%%% MODULES %%%%%%%%%%

print("\n>> What is a Module")

print("\n>> Creating a Module")
# In mymodule.py

print("\n>> Importing a Module")
# import mymodule

print(mymodule.generate_full_name("Ivana", "Ogando"))

print("\n>> Import Functions from a Module")
# main.py file
# from mymodule import generate_full_name, sum_two_nums

print(generate_full_name("Ivana", "Ogando"))
print(sum_two_nums(1, 9))


print("\n>> Import Functions from a Module and Renaming")
# main.py file
# from mymodule import (generate_full_name as fullname, sum_two_nums as total)

print(fullname("Ivana", "Ogando"))
print(total(1, 9))

# %%%%%%%%%% IMPORT BUILT-IN MODULES %%%%%%%%%%

print("\n>> OS Module")

print("\n>> Sys Module")
# import sys
# print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
# print("Welcome {}. Enjoy {} challenge!".format(sys.argv[1], sys.argv[2]))

print("\n>> Statistics Module")
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))  # ~22.9
print(median(ages))  # 23
print(mode(ages))  # 20
print(stdev(ages))  # ~2.3

from math import pi

print("\n>> Math Module")
print(math.pi)  # 3.141592653589793, pi constant
print(math.sqrt(2))  # 1.4142135623730951, square root
print(math.pow(2, 3))  # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))  # 10, rounding to the highest
print(math.log10(100))  # 2, logarithm with 10 as base

print(pi)

from math import pi, sqrt, pow, floor, ceil, log10

print(pi)  # 3.141592653589793
print(sqrt(2))  # 1.4142135623730951
print(pow(2, 3))  # 8.0
print(floor(9.81))  # 9
print(ceil(9.81))  # 10
print(math.log10(100))  # 2

from math import *

print(pi)  # 3.141592653589793, pi constant
print(sqrt(2))  # 1.4142135623730951, square root
print(pow(2, 3))  # 8.0, exponential
print(floor(9.81))  # 9, rounding to the lowest
print(ceil(9.81))  # 10, rounding to the highest
print(math.log10(100))  # 2

print("\n>> String Module")
import string

print(string.ascii_letters)  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)  # 0123456789
print(string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

print("\n>> Random Module")
from random import random, randint

print(
    random()
)  # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20))  # it returns a random integer number between [5, 20] inclusive
