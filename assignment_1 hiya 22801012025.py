# ASSIGNMENT 1


print( "1. Find Area of Rectangle")
# Using sample data
length = 10
width = 6
# Formula for area: length * width
area_of_rectangle = length * width
print(f"The area of the rectangle with length {length} and width {width} is: {area_of_rectangle}")

# EXPECTED OUTPUT:
# 1. Find Area of Rectangle
# The area of the rectangle with length 10 and width 6 is: 60


print(" 2. Find Simple Interest")
# Using sample data
principal = 1000
rate = 6
time = 4
# Formula for Simple Interest: (P * R * T) / 100
simple_interest = (principal * rate * time) / 100
print(f"The simple interest for Principal={principal}, Rate={rate}%, Time={time}yrs is: {simple_interest}")

# EXPECTED OUTPUT:
# 2. Find Simple Interest
# The simple interest for Principal=1000, Rate=6%, Time=4yrs is: 240.0


print(" 3. Convert Temperature from Celsius to Fahrenheit")
# Using sample data
celsius = 37
# Formula: (Celsius * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit")

# EXPECTED OUTPUT:
# 3. Convert Temperature from Celsius to Fahrenheit
# 37 degrees Celsius is equal to 98.6 degrees Fahrenheit



print(" 4. Calculate Average of 3 Numbers")
# Using sample data
num1 = 15
num2 = 20
num3 = 35
# Formula: Sum of all numbers / Total count of numbers
average = (num1 + num2 + num3) / 3
print(f"The average of {num1}, {num2}, and {num3} is: {average}")

# EXPECTED OUTPUT:
# 4. Calculate Average of 3 Numbers
# The average of 15, 20, and 35 is: 23.33



print(" 5. Find Square and Cube of a Number")
# Using sample data
number = 4
# Square is number raised to the power of 2 (**)
square = number ** 2
# Cube is number raised to the power of 3 (**)
cube = number ** 3
print(f"For the number {number}: Square = {square}, Cube = {cube}")

# EXPECTED OUTPUT:
# 5. Find Square and Cube of a Number
# For the number 4: Square = 16, Cube = 64



print(" 6. Swap Two Numbers Without a Third Variable")
# Using sample data
a = 10
b = 20
print(f"Before swapping: a = {a}, b = {b}")

# Swapping logic using addition and subtraction
a = a + b  # a becomes 30 (10 + 20)
b = a - b  # b becomes 10 (30 - 20)
a = a - b  # a becomes 20 (30 - 10)
print(f"After swapping:  a = {a}, b = {b}")

# EXPECTED OUTPUT:
# 6. Swap Two Numbers Without a Third Variable
# Before swapping: a = 10, b = 20
# After swapping:  a = 20, b = 10



print("7. Student Report Program")
try:
    # 1. Take student details using input()
    student_name = input("Enter Student's Name: ")
    student_grade = input("Enter Student's Grade/Class: ")
    
    # 2. Store marks in variables (Converting input strings to floats for math calculation)
    math_marks = float(input("Enter marks for Math (out of 100): "))
    science_marks = float(input("Enter marks for Science (out of 100): "))
    english_marks = float(input("Enter marks for English (out of 100): "))
    
    # 3. Calculate total
    total_marks = math_marks + science_marks + english_marks
    
    # 4. Calculate percentage (Total subjects = 3, Max total = 300)
    percentage = (total_marks / 300) * 100
    
    # Displaying the final report
    print("\n--- FINAL STUDENT REPORT ---")
    print(f"Name: {student_name}")
    print(f"Class: {student_grade}")
    print(f"Math: {math_marks} | Science: {science_marks} | English: {english_marks}")
    print(f"Total Marks: {total_marks} / 300")
    print(f"Percentage: {percentage:.2f}%") # :.2f rounds the percentage to 2 decimal places

except ValueError:
    print("Invalid input! Please enter numerical values for marks.")

# EXPECTED OUTPUT (If you input: Hiya, 12th, 85, 90, 93):
# 7. Student Report Program
# Enter Student's Name: Hiya
# Enter Student's Grade/Class: 12th
# Enter marks for Math (out of 100): 85
# Enter marks for Science (out of 100): 90
# Enter marks for English (out of 100): 93
#
# --- FINAL STUDENT REPORT ---
# Name: Hiya
# Class: 12th
# Math: 85.0 | Science: 90.0 | English: 93.0
# Total Marks: 268.0 / 300
# Percentage: 89.33%