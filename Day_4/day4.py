"""
day4.py

Project: None

Maintainer Ivana Ogando González (you@you.you)
Created @ Wednesday, 12th July 2023 8:31:12 am

Copyright (c) 2023 Your Company
All Rights Reserved
"""

# %%%%%%%%%%%%%%% STRINGS %%%%%%%%%%%%%%%
print(">> CREATING A STRING")
letter = "P"  # A string can be a single character or a bunch of texts
print(letter)  # P
print(len(letter))  # 1
greeting = "Hello, World!"  # String can be made using a single or double quote
print(greeting)  # Hello, World!
print(len(greeting))  # 13
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)

# For multiline string
print("\n")
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""  # they should be '''
print(multiline_string)

# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

print(">> STRING CONCATENATION")
# String Concatenation
print("\n")
first_name = "Ivana"
last_name = "Ogando"
space = " "
full_name = first_name + space + last_name
print(full_name)  # Ivana Ogando
# Checking the length of a string using len() built-in function
print(len(first_name))  # 5
print(len(last_name))  # 6
print(len(first_name) > len(last_name))  # False
print(len(full_name))  # 12

print("\n")
print(">> ESCAPE SEQUENCES IN STRINGS")
print("I hope everyone is enjoying this.\nAre you ?")  # line break
print("Days\tTopics\tExercises")  # adding tab space or 4 spaces
print("Day 1\t5\t5")
print("Day 2\t6\t20")
print("Day 3\t5\t23")
print("Day 4\t1\t35")
print("This is a backslash  symbol (\\)")  # To write a backslash
print(
    'In every programming language it starts with "Hello, World!"'
)  # to write a double quote inside a single quote

print("\n")
print(">> STRING FORMATTING")

print("Old style: % operator)")
# Strings only
first_name = "Ivana"
last_name = "Ogando"
language = "Python"
formated_string = "I am %s %s. I learn %s" % (first_name, last_name, language)
print(formated_string)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius**2
formated_string = "The area of circle with a radius %d is %.2f." % (
    radius,
    area,
)  # 2 refers the 2 significant digits after the point

python_libraries = ["Django", "Flask", "NumPy", "Matplotlib", "Pandas"]
formated_string = "The following are python libraries:%s" % (python_libraries)
print(
    formated_string
)  # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"

print("\n")
print("New style: str.format")
first_name = "Ivana"
last_name = "Ogando"
language = "Python"
formated_string = "I am %s %s. I learn %s" % (first_name, last_name, language)
print(formated_string)
a = 4
b = 3

print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))  # limit to two digits after decimal
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a**b))

"""output
4 + 3 = 7
4 - 3 = 1
4 * 3 = 12
4 / 3 = 1.33
4 % 3 = 1
4 // 3 = 1
4 ** 3 = 64 """

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius**2
formated_string = "The area of a circle with a radius {} is {:.2f}.".format(
    radius, area
)
print(formated_string)

print("\n")
print("String Interpolation / f-Strings (Python 3.6+)")
a = 4
b = 3
print(f"{a} + {b} = {a +b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")

print("\n")
print(">> PYTHON STRINGS AS SEQUENCES OF CHARACTERS")
print("\n")
print("Unpacking Characters")
language = "Python"
a, b, c, d, e, f = language  # unpacking sequence characters into variables
print(a)  # P
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f)  # n

print("\n")
print("Accessing Characters in Strings by Index")
language = "Python"
first_letter = language[0]
print(first_letter)  # P
second_letter = language[1]
print(second_letter)  # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)  # n

language = "Python"
last_letter = language[-1]
print(last_letter)  # n
second_last = language[-2]
print(second_last)  # o

print("\n")
print("Slicing Python Strings")
language = "Python"
first_three = language[0:3]  # starts at 0 index and up to 3 but not include 3
print(first_three)  # Pyt
last_three = language[3:6]
print(last_three)  # hon
# Another way
last_three = language[-3:]
print(last_three)  # hon
last_three = language[3:]
print(last_three)  # hon

print("\n")
print("Reversing a String")
greeting = "Hello, World!"
print(greeting[::-1])  # !dlroW ,olleH

print("\n")
print("Skipping Characters While Slicing")
language = "Python"
pto = language[0:6:2]  #
print(pto)  # Pto

print("\n")
print(">> STRING METHODS")

print("\n")
print("capitalize()")
challenge = "thirty days of python"
print(challenge)
print(challenge.capitalize())  # 'Thirty days of python'

print("\n")
print("count()")
challenge = "thirty days of python"
print(challenge)
print("y", challenge.count("y"))  # 3
print("y", challenge.count("y", 7, 14))  # 1,
print("th", challenge.count("th"))  # 2`

print("\n")
print("endswith()")
challenge = "thirty days of python"
print(challenge)
print("on", challenge.endswith("on"))  # True
print("tion", challenge.endswith("tion"))  # False

print("\n")
print("expandtabs()")
challenge = "thirty\tdays\tof\tpython"
print(challenge)
print(challenge.expandtabs())  # 'thirty  days    of      python'
print(challenge.expandtabs(10))  # 'thirty    days      of        python'

print("\n")
print("find()")
challenge = "thirty days of python"
print(challenge)
print("y", challenge.find("y"))  # 5
print("th", challenge.find("th"))  # 0

print("\n")
print("rfind()")
challenge = "thirty days of python"
print("y", challenge.rfind("y"))  # 16
print("th", challenge.rfind("th"))  # 17

print("\n")
print("format()")
first_name = "Ivana"
last_name = "Ogando"
age = 250
job = "teacher"
country = "Finland"
sentence = "I am {} {}. I am a {}. I am {} years old. I live in {}.".format(
    first_name, last_name, age, job, country
)
print(sentence)

radius = 10
pi = 3.14
area = pi * radius**2
result = "The area of a circle with radius {} is {}".format(str(radius), str(area))
print(result)

print("\n")
print("index()")
challenge = "thirty days of python"
sub_string = "da"
print(challenge.index(sub_string))  # 7

print("\n")
print("rindex()")
challenge = "thirty days of python"
sub_string = "da"
print(challenge.rindex(sub_string))  # 8

print("\n")
print("isalnum()")
challenge = "ThirtyDaysPython"
print(challenge, challenge.isalnum())  # True

challenge = "30DaysPython"
print(challenge, challenge.isalnum())  # True

challenge = "thirty days of python"
print(challenge, challenge.isalnum())  # False, space is not an alphanumeric character

challenge = "thirty days of python 2019"
print(challenge, challenge.isalnum())  # False

print("\n")
print("isalpha()")
challenge = "thirty days of python"
print(challenge, challenge.isalpha())  # False, space is once again excluded
challenge = "ThirtyDaysPython"
print(challenge, challenge.isalpha())  # True
num = "123"
print(num, num.isalpha())  # False

print("\n")
print("isdecimal()")
challenge = "thirty days of python"
print(challenge, challenge.isdecimal())  # False
challenge = "123"
print(challenge, challenge.isdecimal())  # True
challenge = "12 3"
print(challenge, challenge.isdecimal())  # False, space not allowed

print("\n")
print("isdigit()")
challenge = "Thirty"
print(challenge, challenge.isdigit())  # False
challenge = "30"
print(challenge, challenge.isdigit())  # True
challenge = "\u00B2"
print(challenge, challenge.isdigit())  # True

print("\n")
print("isnumeric()")
num = "10"
print(num, num.isnumeric())  # True
num = "\u00BD"  # ½
print(num, num.isnumeric())  # True
num = "10.5"
print(num, num.isnumeric())  # False

print("\n")
print("isidentifier()")
challenge = "30DaysOfPython"
print(challenge, challenge.isidentifier())  # False, it starts with a number
challenge = "thirty_days_of_python"
print(challenge, challenge.isidentifier())  # True

print("\n")
print("islower()")
challenge = "thirty days of python"
print(challenge, challenge.islower())  # True
challenge = "Thirty days of python"
print(challenge, challenge.islower())  # False

print("\n")
print("isupper()")
challenge = "thirty days of python"
print(challenge, challenge.isupper())  #  False
challenge = "THIRTY DAYS OF PYTHON"
print(challenge, challenge.isupper())  # True

print("\n")
print("join()")
web_tech = ["HTML", "CSS", "JavaScript", "React"]
result = " ".join(web_tech)
print(result)  # 'HTML CSS JavaScript React'

web_tech = ["HTML", "CSS", "JavaScript", "React"]
result = "# ".join(web_tech)
print(result)  # 'HTML# CSS# JavaScript# React'

print("\n")
print("strip()")
challenge = "thirty days of pythoonnn"
print(challenge, challenge.strip("noth"))  # 'irty days of py'

print("\n")
print("replace()")
challenge = "thirty days of python"
print(challenge, challenge.replace("python", "coding"))  # 'thirty days of coding'

print("\n")
print("split()")
challenge = "thirty days of python"
print(challenge, challenge.split())  # ['thirty', 'days', 'of', 'python']
challenge = "thirty, days, of, python"
print(challenge, challenge.split(", "))  # ['thirty', 'days', 'of', 'python']

print("\n")
print("title()")
challenge = "thirty days of python"
print(challenge, challenge.title())  # Thirty Days Of Python

print("\n")
print("swapcase()")
challenge = "thirty days of python"
print(challenge, challenge.swapcase())  # THIRTY DAYS OF PYTHON
challenge = "Thirty Days Of Python"
print(challenge, challenge.swapcase())  # tHIRTY dAYS oF pYTHON

print("\n")
print("startswith()")
challenge = "thirty days of python"
print(challenge, challenge.startswith("thirty"))  # True

challenge = "30 days of python"
print(challenge, challenge.startswith("thirty"))  # False
