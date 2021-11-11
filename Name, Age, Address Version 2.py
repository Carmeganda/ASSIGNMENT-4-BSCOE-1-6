# Create a program that will ask for name, age and address. 
# Display those details in the following format.
# Hi, my name is _____. I am ____ years old and I live in _____ .

def getNmAgeAdrss():
    name_ = input("Name: ")
    age_ = int(input("Age: "))
    address_ = input("Adress: ")
    return name_, age_, address_

def display(nameA, ageA, addA):
    print(f"Hi, my name is {nameA}. I am {ageA} years old and I live in {addA}")
 
    # steps
# 1. Ask for name, age, and adress.

name, age, add, = getNmAgeAdrss()

# 2. Display

display( name, age, add)