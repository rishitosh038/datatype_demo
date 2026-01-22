## Overview
This project demonstrates the basics of Python variables, data types, type conversion, dynamic typing, and error handling. It is intended for interns and beginners to understand how Python manages data during execution.

## Tools & Technologies
- Python 3
- VS Code / Jupyter Notebook / Google Colab
- Git & GitHub
- Windows OS

## Project Structure
Task_2/
├── datatypes_demo.py
└── README.md

## Concepts Covered

### Variable Declarations
Different types of variables are used:
- Integer (int)
- Float (float)
- String (str)
- Boolean (bool)

Example:
age = 21  
height = 5.9  
name = "Rishitosh"  
is_student = True  

### Data Type Checking
The built-in type() function is used to identify the data type of variables.

### Arithmetic Operations
The script demonstrates:
- Addition
- Subtraction
- Multiplication
- Division
- Floor Division
- Modulus

### Type Conversion
The following conversions are demonstrated:
- String to Integer using int()
- String to Float using float()
- Number to String using str()

Example:
num_int = int("100")  
num_float = float("25.5")  

### Error Handling
Invalid input is handled using try-except to prevent runtime errors.

Example:
try:
    converted_number = int("abc")
except ValueError:
    print("Invalid input")

### String and Number Concatenation
Numbers are converted to strings before concatenation.

Example:
result = "Marks obtained: " + str(marks)

### Dynamic Typing
Python allows variables to change their data type during execution.

Example:
value = 50  
value = "Now I am a string"  
value = 3.14  

## How to Run
1. Clone the repository:
git clone https://github.com/rishitosh038/datatype_demo.git

2. Navigate to the project folder:
cd datatype_demo

3. Run the script:
python datatypes_demo.py

## Learning Outcome
After completing this task, the learner will:
- Understand Python data types
- Perform safe type conversions
- Handle invalid input using error handling
- Explain dynamic typing in interviews
- Use Git and GitHub for project submission

