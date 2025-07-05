# in these i have leaned about variables, data types, and basic operations
# and also about the print function
# Variables
name = "John"
age = 30
height = 5.9

# Data Types
print("Name:", name)  # String
print("Age:", age)    # Integer
print("Height:", height)  # Float

# Basic Operations
sum = age + 5
product = age * 2
print("Sum of age and 5:", sum)  # Addition
print("Product of age and 2:", product)  # Multiplication

# Print Function
print("Hello, my name is", name, "and I am", age, "years old.")

# String Formatting
print(f"Hello, my name is {name} and I am {age} years old.")  # f-string formatting

# String Concatenation
print("Hello, my name is " + name + " and I am " + str(age) + " years old.")  # Concatenation with type conversion

# Type Conversion
age_str = str(age)  # Convert integer to string
print("Age as string:", age_str)  # Displaying the converted string

# Type Checking
print("Type of name:", type(name))  # Check type of variable
print("Type of age:", type(age))  # Check type of variable

# Type of height
print("Type of height:", type(height))  # Check type of variable

# Arithmetic Operations
a = 10
b = 5
print("Addition:", a + b)  # Addition
print("Subtraction:", a - b)  # Subtraction
print("Multiplication:", a * b)  # Multiplication
print("Division:", a / b)  # Division
print("Floor Division:", a // b)  # Floor Division
print("Modulus:", a % b)  # Modulus
print("Exponentiation:", a ** b)  # Exponentiation

# Comments
# This is a single-line comment
"""This is a multi-line comment
It can span multiple lines."""
# Variable Naming
# Valid variable names
valid_name = "Valid"
valid_name2 = "Valid2"

# Invalid variable names (uncommenting these will cause errors)
# 1invalid_name = "Invalid"  # Cannot start with a number
# invalid-name = "Invalid"  # Cannot contain hyphens
# invalid name = "Invalid"  # Cannot contain spaces

# Constants
PI = 3.14159  # Constant value for Pi
# Using constants
print("Value of Pi:", PI)  # Displaying the constant value

# also have leaned about that behind the scenes , boolean values are the numbers 0 and 1
# Boolean Values
is_active = True  # Boolean True
is_logged_in = False  # Boolean False

# and also the conversion between boolean and integer is called implicit conversion
# Implicit Conversion
bool_to_int = int(is_active)  # Convert boolean to integer

# type casting
int_to_bool = bool(1)  # Convert integer to boolean
print("Boolean to Integer:", bool_to_int)  # Displaying the converted integer
print("Integer to Boolean:", int_to_bool)  # Displaying the converted boolean

# precision
# Floating Point Precision
pi_value = 3.14159265358979323846  # High precision value of Pi
print("Pi with high precision:", pi_value)  # Displaying high precision value
# Rounding
rounded_pi = round(pi_value, 2)  # Round to 2 decimal places

# decimal and fractional numbers
print("Rounded Pi:", rounded_pi)  # Displaying rounded value
# Decimal and Fractional Numbers
decimal_number = 0.75  # Decimal number
fractional_number = 1/3  # Fractional number
print("Decimal Number:", decimal_number)  # Displaying decimal number

# set precision in decimal numbers
print("Fractional Number:", fractional_number)  # Displaying fractional number
# Setting Precision in Decimal Numbers
import decimal
decimal.getcontext().prec = 4  # Set precision to 4 decimal places
decimal_number_precise = decimal.Decimal('0.123456789')  # High precision decimal number
print("Decimal Number with Precision:", decimal_number_precise)  # Displaying precise decimal number
