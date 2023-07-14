"""
day21.py

Project: None

Maintainer Ivana Ogando González (you@you.you)
Created @ Wednesday, 12th July 2023 3:30:08 pm

Copyright (c) 2023 Your Company
All Rights Reserved
"""
# %%%%%%%%%% CLASSES AND OBJECTS %%%%%%%%%%

# Creating a Class
print("\n>> Creating a Class")


class Person:
    pass


print(Person)

# Creating an Object
print("\n>> Creating an Object")
p = Person()
print(p)

# Class Constructor
print("\n>> Class Constructor")


class Person1:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city


p = Person1("Ivana", "Ogando", 23, "Spain", "Vigo")
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)

# Object Methods
print("\n>> Object Methods")


class Person2:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f"{self.firstname} {self.lastname} is {self.age} years old. She lives in {self.city}, {self.country}"


p = Person2("Ivana", "Ogando", 23, "Spain", "Vigo")
print(p.person_info())

# Object Default Methods
print("\n>> Object Default Methods")


class Person3:
    def __init__(
        self,
        firstname="Ivana",
        lastname="Ogando",
        age=23,
        country="Spain",
        city="Vigo",
    ):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f"{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}."


p1 = Person3()
print(p1.person_info())
p2 = Person3("John", "Doe", 30, "Nomanland", "Noman city")
print(p2.person_info())

# Method to Modify Class Default Values
print("\n>> Method to Modify Class Default Values")


class Person4:
    def __init__(
        self,
        firstname="Ivana",
        lastname="Ogando",
        age=23,
        country="Spain",
        city="Vigo",
    ):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        return f"{self.firstname} {self.lastname} is {self.age} years old. She lives in {self.city}, {self.country}."

    def add_skill(self, skill):
        self.skills.append(skill)


p1 = Person4()
print(p1.person_info())
p1.add_skill("HTML")
p1.add_skill("CSS")
p1.add_skill("JavaScript")
p2 = Person4("John", "Doe", 30, "Nomanland", "Noman city")
print(p2.person_info())
print(p1.skills)
print(p2.skills)

# Inheritance
print("\n>> Inheritance")


class Student(Person4):
    pass


s1 = Student("Eyob", "Yetayeh", 30, "Finland", "Helsinki")
s2 = Student("Lidiya", "Teklemariam", 28, "Finland", "Espoo")
print(s1.person_info())
s1.add_skill("JavaScript")
s1.add_skill("React")
s1.add_skill("Python")
print(s1.skills)

print(s2.person_info())
s2.add_skill("Organizing")
s2.add_skill("Marketing")
s2.add_skill("Digital Marketing")
print(s2.skills)


# Overriding parent method
print("\n>> Overriding parent method")


class Student(Person4):
    def __init__(
        self,
        firstname="Ivana",
        lastname="Ogando",
        age=23,
        country="Spain",
        city="Vigo",
        gender="female",
    ):
        self.gender = gender
        super().__init__(firstname, lastname, age, country, city)

    def person_info(self):
        gender = "He" if self.gender == "male" else "She"
        return f"{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}."


s1 = Student("Eyob", "Yetayeh", 30, "Finland", "Helsinki", "male")
s2 = Student("Lidiya", "Teklemariam", 28, "Finland", "Espoo", "female")
print(s1.person_info())
s1.add_skill("JavaScript")
s1.add_skill("React")
s1.add_skill("Python")
print(s1.skills)

print(s2.person_info())
s2.add_skill("Organizing")
s2.add_skill("Marketing")
s2.add_skill("Digital Marketing")
print(s2.skills)
