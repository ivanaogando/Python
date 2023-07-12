"""
day3exercises.py

Project: None

Maintainer Ivana Ogando González (you@you.you)
Created @ Tuesday, 11th July 2023 3:49:49 pm

Copyright (c) 2023 Your Company
All Rights Reserved
"""

# 1 Declare your age as integer variable
age = 23

# 2 Declare your height as a float variable
height = 155

# 3 Declare a variable that store a complex number
complex_number = 1 + 1j

# 4 Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = input("Enter the base: ")
height = input("Enter the height: ")
area = float(base) * float(height) * 0.5
print("The area of the triangle is ", area)


# 5 Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = input("Enter the a: ")
b = input("Enter the b: ")
c = input("Enter the c: ")
perimeter = float(a) + float(b) + float(c)
print("The perimeter of the triangle is ", perimeter)


# 6 Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

length = input("Enter the length: ")
width = input("Enter the width: ")
area = float(length) * float(width)
perimeter = 2 * (float(length) + float(width))
print("The area of the triangle is ", area)
print("The perimeter of the triangle is ", perimeter)

# 12 Find the length of 'python' and 'dragon' and make a falsy comparison statement.
len_phyton = len("phyton")
len_dragon = len("dragon")
print(len_phyton < len_dragon)

# 13 Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("on" in "phyton")
print("on" in "dragon")

# 16 Find the length of the text python and convert the value to float and convert it to string
len_text = len("python")
len_float = float(len_text)
len_string = str(len_float)

# 18 Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print('2.7 is 7 // 3:', 2.7 == (7 // 3))

# 21 Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = input("Enter the hours: ")
rate = input("Enter the rate per hour: ")
earning = float(hours) * float(rate)
print("The weekly earning is ", earning)
