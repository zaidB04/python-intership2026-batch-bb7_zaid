# DigolTech Python Internship 2026
# Section 1.2 - Error Finding & Debugging
# Question 8: Exception Handling
#
# Error Identification:
# 1. ZeroDivisionError is not handled.
# 2. Result is printed outside the try block.
# 3. Result may not exist if an exception occurs.
#
# Error Type: Runtime Error
# (ValueError, ZeroDivisionError and potentially NameError)
#
# Original Incorrect Code:
#
# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     result = a / b
# except ValueError:
#     print("Invalid input")
#
# print("Result:", result)
#
# Correction:
# Added ZeroDivisionError handling.
# Moved the result print statement inside the try block.

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Result:", result)

except ValueError:
    print("Invalid input.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

# Expected Output - Test Case 1:
# Enter first number: 10
# Enter second number: 2
# Result: 5.0
#
# Expected Output - Test Case 2:
# Enter first number: 10
# Enter second number: 0
# Cannot divide by zero.
#
# Expected Output - Test Case 3:
# Enter first number: abc
# Enter second number: 2
# Invalid input.