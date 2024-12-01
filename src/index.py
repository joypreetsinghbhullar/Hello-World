print ("Hello World")
print ("It work" * 2)

# This is a variable that sets the price 
price = 10 
price = 20
rating = 4.9
name = "blob"
is_publish = True 
print (price) # Shows what the price of the thing is 

# John Smith Hospital
name = "John Smith"
age = 20 
existing_patient = False 
print (name)
print (age)
print (existing_patient)

# taking in inputs
input_name = input ("What is your name? ")
print ("Hi " + input_name)

# Color and What do they like and should say "USERNAME likes BLUE"

user_input_name = input ("What is your name? ")
favorite_color = input ("What is your favorite color? ")
print (user_input_name + " likes " + favorite_color)

# Ask the year we were born and calculate our age we were born in 
# Key notes
# int() converts value into an integer
# float() converts the value into a float/decimal
# bool() converts string to a boolean value

birth_year = input ("Birth year: ")
print(type(birth_year))
age = 2024 - int(birth_year)
print(type(age))
print (age)

# Askes the user their weight (in pounds), and converts it into kilograms and print it in the terminal

weight_lbs = input("Weight (lbs): ")
weight_kg = int(weight_lbs) * 0.45
print (weight_kg)

# Python course for beginners 
# Key note that you need double quotes to put a aposterphe in a string 

course = "Python's Course for Beginners" 
print(course)

course = 'Python Course for "Beginners"' # You need to use single quotes if you want to put double quotes in your string 
print(course)

course = '''Hello Human,
I hope you like this code
so I will say to you bug hunter,
hello
''' # You need triple quotes to write something in multiple lines (multi line string)

# Get a character and a given index in a string 
new_course = 'Python for Beginners'
print (new_course[0]) # The index of the first character in this string is 0 

# python supports negative index's

new_course = 'Python for Beginners'
print (new_course[-1]) # The index of the last character in this string is 0 and python supports negative indexs 
# Square brackets are utlized to extract a few characters in a string 
# extract all charactes from a value x to y 
new_course = 'Python for Beginners'
print (new_course[0:3]) # will give you charactes starting from 0 to 3 which will be pyt
# Index is character in a string
new_course = 'Python for Beginners'
print (new_course[0:]) # this will extract all characters starting from 0 (p) to the last character
new_course = 'Python for Beginners'
print (new_course[1:]) #excludes the first characters 

name = "blob"
print(name[1:-1])

# Fromatted Strings to dynamically generate text with your variables 
first = 'John'
last = 'Blob'
message = first + ' [' + last + '] is a coder'
print(message) #not a good approach 

# Better version using formatted version
first = 'John'
last = 'Blob'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder' #this is a formatted string
print(message) 
# curly brackets in python represent placeholders or holes, these holes will be filled with the values of a variables
print(msg)

# String Methods 
course_new = 'Python for Beginners'
print(len(course)) # len calculates the given number of characters in a string/general purpose function
print (course_new.upper()) #shows all characters in upercase and . shows methods
print (course_new.lower()) #shows all characters in lowercase and is string only both of them
print (course_new)
print(course_new.find("P")) #find will find the characters number this is case sensitve
print(course_new.find("Beginners")) #will show the starting index
print(course_new.replace('Beginners', "Absolute Beginners")) # This will replace the string with this / case sensitve
print(course_new.replace('P', "J")) # We can also do characters as well

# Check if a string contains a specific word/character
print('Python' in new_course) # This is a boolean expression and will give out true/false # this is case sensitive

# In operator and Find method difference
# The find method returns the index of the character/sequence of characters
# The in operator produces a boolean value, do we have this or not?

# Arithmetic Operations 

# + add a number
# - subtracts a value 
# * multplies a value
# / returns a float
# //  returns an int
# %  returns the remainder of division
# **  exponentiation - x ** y = x to the power of 
# Parenthisis will take priotity 
print (10 % 3)

x = 10 # augmented assignment operator is to write code in short form
x = x + 3
x += 3 # this is an example of a augmented assignment operator / enhanced assignment operator 
print (x)

x = 10 + 3 * 2 # operator presendence or order of operations 
print (x)
x = (10 + 3) * 2 ** 2 #using exponention 

x = (2+3) * 10 -3 
print (x)

# Maths function
x = 2.9
print (round(x)) # rounds it of
print (abs(-2.9)) #absolute will turn it into a positive representation

import math # imports math module

print(math.ceil (2.9)) #rounds it off 
print(math.floor (2.9)) # removes the decimal 

# If statements 
is_hot = True #boolean value
is_cold = False 
if is_hot:
    print("It's a hot day")
    print ("Drink plenty of water")

elif is_cold:
    print ("It's a cold day")
    print ("Wear warm clothes")

else:
   print('Enjoy your day')

# Price of a house example 

house_price = 1000000
good_credit = True

if good_credit:
    down_payment = 0.1 * house_price

else: 
    down_payment = 0.2 * house_price
print (f"Down Payment: ${down_payment}")

# Logical Operations

has_high_income = True 
has_good_credit = True

if has_high_income and has_good_credit: #and operator states if both of these conditions are true than 
    print("Elgible for loan")

# using or operator 
if has_high_income or has_good_credit: #if 1 one this is true than 
    print("Elgible for loan")

# AND: Both condition
# or: Atleast one 
# NOT: tells that this statement does not need to be true 

# Crimnal record 

has_good_credit = True
has_criminal_record = False 

if has_good_credit and not has_criminal_record: 
    print("Eligible for Loan")

# Comparision operations 

# a > b
# a >= b (greater than or equal to)
# a < b
# a <= b
# a == b (equals)
# a != b (not equals) 

temparature = 30 #boolean value

if temparature > 30:
    print("It's a host day")
else: 
    print("It's not a hot day")

# validation message for a name

name = "J"

print(len(name))

if len(name) <3:
    print("Name must be at least 3 characters")
elif len(name) > 50: 
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good")

# Project: Weight Converter 

weight = int(input("Weight: ")) #int converts from a string to a integer 
unit = input('(L)bs or (K)g')
if unit.upper() == "L":
   converted = weight * 0.45
   print (f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")

# Weight converter: Which works now # WARNING: AI GENERATED

weight = int(input("Weight: "))  # int converts from string to an integer
unit = input('(L)bs or (K)g: ')

if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos.")
elif unit.upper() == "K":
    converted = weight / 0.45
    print(f"You are {converted} pounds.")
else:
    print("Invalid input. Please enter 'L' for pounds or 'K' for kilograms.")


# While Loops

i = 1
while 1 <= 5:
    print(i) 
    i = i + 1
print("Done")

# Asterick Example

i = 1
while 1 <= 5:
    print("*" * i) 
    i = i + 1
print("Done")

# Building a guessing game

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
   guess = int(input("Guess:"))
   guess_count +=1
   if guess == secret_number:
       print("You won!")
       break
else:
   print('Sorry you failed') 

# Car Game 




