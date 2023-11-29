# python is a scripting language
# a function is a group of code that can be called.

# Execute the script - python [filename.py]

# Hello World
from typing import ClassVar


print("Hello World")


# Declaring variable
# int apples = 20
# string apples ="20"
# float = 2.0
### in python you don't need to clear an int, string, float, etc.
## i.e apples = 20 ==> int 
## apples = "20" ==> string

apples = 20
print(apples)

apples = 8
print(apples)

# The variable declared as an int
apples = 9
# you cannot declare an in and put it with a string, so you need
# str() 
print("I have " + str(apples) + " apples")

#google - print - diiferent ways of print function
print(f"I have {apples} apples")

planet = "jupiter"
print(planet)

# Everytime you see a dot after the object, its a function.
# convert the value into the uppercase
print(planet.upper())
print(planet.find("t"))
print(planet.replace("i", "y"))



x = 3
y = 5

total = x + y
print(total) 

def greeting(name):
    print("Hello, " + name)
greeting("Himat Varsani")
   
# Operator - comparation - returns a boolean    
a = 5
b = 9

c = a > b
print (c)

d = a == b
print(d)

# Algorithm - Pseudo code
# If statement = condition
# if something is true then
#   do something
# else
#   do something else
# end if

if a == b:
    print("They are equal")
    if a > 5:
        print("A is greater than 5")
    elif a == 5:
        print("They are the same")
    else:
        print("A is smaller than 5")
else:
    print("They are not equal")

#List - list index starts with 0
list_var = ["Hello", "World"]

# Dictionaries
dictionary_var = {
    # Key: Value - Key needs to be unique
    "name": "Himat",
    "surname": "Varsani"
}

print(list_var)
print(list_var[1])
print(dictionary_var)
print(dictionary_var["name"])


# Dictionaries
student = {
    # Key: Value - Key needs to be unique
    "st_01": {
        "name": "Alice", 
        "dob": "01/01/01"
    },
      "st_02": {
        "name": "Bob", 
        "dob": "02/02/02"
    }
}

print(student["st_01"])
print(student["st_01"]["dob"])
print(student.keys())
print(student.values())
print(student["st_01"].keys())

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("model")
print(x)

# For each loop
students = {
       # Key: Value - Key needs to be unique
    "st_01": {
        "name": "Alice", 
        "dob": "01/01/01"
    },
      "st_02": {
        "name": "Bob", 
        "dob": "02/02/02"
    },
        "st_03": {
        "name": "Steve", 
        "dob": "03/03/03"
    }
}

for st in students:
    print(st)
print("End of program")

for st in students.keys():
    print(st)
print("End of program")

# This will return the tuple
# tuple_var = ("item1", "item2", "item3")
#                 0        1        2
for st in students.items():
    print(st)
    print(st[0])
    print(st[1]["name"])
print("End of program")


# Function - define a function - def my_function():
# return -- optional
def my_function():
    print("Hello World")

my_function()

def my_function(a, b):
    c = a + b
    print(c)

my_function(1, 5)
my_function(10, 2)
my_function(4, 7)
my_function(11, 1000)
my_function(234334, 34434)


def my_function(a, b):
    return a + b
print(my_function(1,5))

def my_function(a, b):
    if a > b:
        c = a - b
    else:
        c = b - a
    return c
print(my_function(98, 54))

def my_function(list):
    a = list[0]
    for i in list:
        if a > i:
            return i
    return 0

apples = [56, 1, 2, 4, 5]
print(my_function(apples))
