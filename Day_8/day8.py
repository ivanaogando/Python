"""
day8.py

Project: None

Maintainer Ivana Ogando González (you@you.you)
Created @ Wednesday, 12th July 2023 12:44:21 pm

Copyright (c) 2023 Your Company
All Rights Reserved
"""

# %%%%%%%%%% DAY 8 %%%%%%%%%%

print("\n>> Creating a Dictionary")
person = {
    "first_name": "Ivana",
    "last_name": "Ogando",
    "age": 250,
    "country": "Spain",
    "is_marred": False,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}
print("\n>> Dictionary Length")
print(len(person))  # 7

print("\n>> Accessing Dictionary Items")
person = {
    "first_name": "Ivana",
    "last_name": "Ogando",
    "age": 250,
    "country": "Spain",
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}
print(person["first_name"])
print(person["country"])
print(person["skills"])  # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person["skills"][0])  # JavaScript
print(person["address"]["street"])  # Space street
print("\n")
print(person.get("first_name"))
print(person.get("country"))
print(
    person.get("skills")
)  # ['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get("city"))  # None

print("\n>> Adding Items to a Dictionary")
person = {
    "first_name": "Ivana",
    "last_name": "Ogando",
    "age": 250,
    "country": "Spain",
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}
person["job_title"] = "Instructor"
person["skills"].append("HTML")
print(person)

print("\n>> Modifying Items in a Dictionary")
person = {
    "first_name": "Ivana",
    "last_name": "Ogando",
    "age": 250,
    "country": "Spain",
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}
print(person.get("first_name"))
person["first_name"] = "Anxo"
person["age"] = 252
print(person.get("first_name"), "after change")

print("\n>> Checking Keys in a Dictionary")
# syntax
dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
print("key2" in dct)  # True
print("key5" in dct)  # False

print("\n>> Removing Key and Value Pairs from a Dictionary")
"""
pop(key):  removes the item with the specified key name:
popitem(): removes the last item
del:       removes an item with specified key name
"""
# syntax
dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
dct.pop("key1")  # removes key1 item
dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
dct.popitem()  # removes the last item
del dct["key2"]  # removes key2 item

print("\n")
person = {
    "first_name": "Ivana",
    "last_name": "Ogando",
    "age": 250,
    "country": "Spain",
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}
person.pop("first_name")  # Removes the firstname item
person.popitem()  # Removes the address item
del person["is_married"]  # Removes the is_married item

print("\n>> Changing Dictionary to a List of Items: items()")
# syntax
dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
print(
    dct.items()
)  # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

print("\n>> Clearing a Dictionary: clear()")
# syntax
dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
print(dct.clear())  # None

print("\n>> Deleting a Dictionary")
# syntax
dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
del dct

print("\n>> Copy a Dictionary: copy()")
# syntax
dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
dct_copy = (
    dct.copy()
)  # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

print("\n>> Getting Dictionary Keys as a List: keys()")
# syntax
dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
keys = dct.keys()
print(keys)  # dict_keys(['key1', 'key2', 'key3', 'key4'])

print("\n>> Getting Dictionary Values as a List")
# syntax
dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
values = dct.values()
print(values)  # dict_values(['value1', 'value2', 'value3', 'value4'])
