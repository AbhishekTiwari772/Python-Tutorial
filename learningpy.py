#                       THE COMPLETE PYTHON TUTORIAL - 2022 - Beginners Coding by Abhishek

# Variables in Python
# Variables are placeholders to store values temporarily.
# Rules to define variables in Python:
# 1. A variable name must start with a letter or the underscore character.
# 2. A variable name cannot start with a number
# 3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
# 4. Variable names are case-sensitive (name, Name and NAME are three different variables).
# 5. The reserved words(keywords) cannot be used naming the variable.

# Data Types in Python
# Strings, Integers, Float (decimal), boolean(True or False),
# f_name = "Steve"
# age = 64
# l_name = "Harvey"
# is_comedian = True

# Taking input
# name = input("What is your name?\n")
# print("Hey there", name)

# Data Type conversion in Python
# num = 24.9
# print(int(num))
# print(float(num))
# print(str(num))
# print(bool(num))

# Taking integer input
# age = int(input("What is your age?\n"))
# print("You are", age, "years old")

# number = 1
# print(float(number))
# print(str(number))
# print(bool(number))

# A simple sum calculator
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# sum = num1 + num2
# print(sum)

# String Methods
# name = "Ratan Tata"
# print(name.capitalize())
# print(name.endswith("Tata"))
# print(name.upper())
# print(name.lower())
# print(name.isupper())
# print(name.islower())
# print(name.find("Tata"))
# print(name.replace("Ratan", "J.R.D"))
# print('T' in name)
# print(name)

# Arithmetic Operators
# sum = 5 + 2
# difference = 5 - 2
# product = 5 * 2
# quotient = 5 / 2
# quotient_without_decimal = 5 // 2
# remainder = 5 % 2
# print(sum, difference, product, quotient, quotient_without_decimal, remainder)

# Shortcuts in arithmetic
# num = 4
# num += 2 # num = num + 2
# print(num)
# num -= 2 # num = num - 2
# print(num)
# num *= 2 # num = num * 2
# print(num)
# num /= 2 # num = num / 2
# print(num)

# Operator Precedence

# Comparison Operators
# num1 = 12
# num2 = 23
# print(num1 > num2)
# print(num1 < num2)
# print(num1 >= num2)
# print(num1 <= num2)
# print(num1 == num2)
# print(num1 != num2)

# Logical Operators (and, or, not)
# and -> returns True if both conditions are True. If even one is false, returns false.
# print(20 > 30 and 43 < 30) # False
# print(20 < 30 and 43 > 30) # True
# print(20 > 30 and 43 > 30) # False
# or  -> returns True even if one of the conditions is true. If both false, returns false.
# print(20 > 30 or 43 < 30) # False
# print(20 < 30 or 43 < 30) # True
# not -> toggles bool value of the final output
# print(not 20 < 30) # False
# print(not 20 > 30) # True

# if - else statements
# Used to do certain different things, on the basis of conditions

# Eligibility of Driving License (using if and else)
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are an adult\nYou CAN apply for a driving license...")
# else:
#     print("You are NOT an adult\nYou CANNOT apply for a driving license...")

# All in one Calculator
# print("""Welcome to this calculator. Please choose what you want to do. Type...
# 1 for Addition
# 2 for Subtraction
# 3 for Multiplication
# 4 for Division
# 5 for Remainder after division
# """)
# operation = int(input("Operation: "))
#
# if operation == 1:
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     sum = num1 + num2
#     print(sum)
# elif operation == 2:
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     dif = num1 - num2
#     print(dif)
# elif operation == 3:
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     product = num1 * num2
#     print(product)
# elif operation == 4:
#     num1 = int(input("Enter the Dividend: "))
#     num2 = int(input("Enter the Quotient: "))
#     div = num1 / num2
#     print(div)
# elif operation == 5:
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     remain = num1 % num2
#     print(remain)
# else:
#     print("Invalid input!!")

# Range in Python
# print(range(5))

# Loops in Python
# While loop ( print numbers from 1 to 5 )
# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# For loop ( print numbers from 0 to 5 )
# for i in range(6):
#     print(i)

# Lists in Python
# Lists are used to store many values collectively ( complex data type )
# Values in the lists are enclosed within square brackets, each value separated by a comma.
# cars = ["Tata", "Mahindra", "Toyota", "Ford", "Kia"]
# print(cars)
# print(cars[1])
# print(cars[-2])
# print(cars[0:3])

# For loop on lists
# cars = ["Tata", "Mahindra", "Toyota", "Ford", "Kia"]
# for car in cars:
#     print(car)

# List methods/operations
# subjects = ["English", "Hindi", "Maths", "Science"]
# subjects.append("History") # Adds in the end of list
# print(subjects)
# subjects.insert(2, "Sanskrit") # Adds a value on the defined index
# print(subjects)b
# print("Maths" in subjects) # Check for a value in a list (True or False)
# print(len(subjects)) # Returns an integer value representing the length of the list
# subjects.clear()
# print(subjects)

# Break statements in Python ( Stop running the loop on some certain condition )
# subjects = ["English", "Hindi", "Maths", "Science"]
# for subject in subjects:
#     if subject == "Science":
#         break
#     print(subject)

# Continue statements in Python ( Ignore a loop iteration on some certain conditions )
# subjects = ["English", "Hindi", "Maths", "Science"]
# for subject in subjects:
#     if subject == "Maths":
#         continue
#     print(subject)

# Tuple in Python ( unchangable / immutable lists )
# Values in the tuples are enclosed within round brackets (optional), each value separated by a comma.
# subjects = ("English", "Hindi", "Maths", "Science")
# subjects = "English", "Hindi", "Maths", "Science"

# Sets in Python ( Lists with unique values only )
# Values in the Sets are enclosed within curly brackets {}, each value separated by a comma.
# roll_no = {1, 1, 2, 3, 2, 3, 4, 5, 6}
# print(roll_no)

# Dictionary in Python ( Key Value pairs )
# about_me = {
#     "name": "Abhishek Tiwari",
#     "age": 14,
#     "Location": "India"
# }
# print(about_me["age"])

# Packages in Python
# Packages in python are pieces of code written by someone else, which we can use in our code after importing
# import math
# We can also import specific functions from a package by
# from math import sqrt

# Creating your own function
# functions help do a task repeatedly, without writing the code every time.
# def function_name(parameters):
#     # The code goes here
# To call a function...
# function_name(parameters)