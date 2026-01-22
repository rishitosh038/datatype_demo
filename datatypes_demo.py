# -------------------------------
# 1. Variable Declarations
# -------------------------------

# Integer variable
age = 21

# Float variable
height = 5.9

# String variable
name = "Hrishitosh"

# Boolean variable
is_student = True

# -------------------------------
# 2. Printing Data Types
# -------------------------------

print("Data Types of Variables:")
print("age:", age, "| Type:", type(age))
print("height:", height, "| Type:", type(height))
print("name:", name, "| Type:", type(name))
print("is_student:", is_student, "| Type:", type(is_student))

print("-" * 40)

# -------------------------------
# 3. Arithmetic Operations
# -------------------------------

a = 10
b = 3

print("Arithmetic Operations:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)

print("-" * 40)

# -------------------------------
# 4. Type Conversion (Casting)
# -------------------------------

# String numbers
num_str1 = "100"
num_str2 = "25.5"

# Converting string to integer
num_int = int(num_str1)      # "100" → 100

# Converting string to float
num_float = float(num_str2)  # "25.5" → 25.5

print("Type Conversion:")
print("num_int:", num_int, "| Type:", type(num_int))
print("num_float:", num_float, "| Type:", type(num_float))

print("-" * 40)

# -------------------------------
# 5. Handling Invalid Input
# -------------------------------

user_input = "abc"

try:
    converted_number = int(user_input)
    print("Converted Number:", converted_number)
except ValueError:
    print("Error: Invalid input! Cannot convert string to integer.")

print("-" * 40)

# -------------------------------
# 6. String & Number Concatenation
# -------------------------------

marks = 85

# Correct way: convert number to string
result = "Marks obtained: " + str(marks)

print("String Concatenation:")
print(result)

print("-" * 40)

# -------------------------------
# 7. Dynamic Typing Demonstration
# -------------------------------

value = 50
print("Initial value:", value, "| Type:", type(value))

value = "Now I am a string"
print("After reassignment:", value, "| Type:", type(value))

value = 3.14
print("After second reassignment:", value, "| Type:", type(value))

print("-" * 40)

print("End of datatypes_demo.py")
