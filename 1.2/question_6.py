# DigolTech Python Internship 2026
# Section 1.2 - Error Finding & Debugging
# Question 6: Function + Return Error
#
# Error Identification:
# The function calculates the square but does not
# return the result.
#
# Error Type: Logical Error
#
# Original Incorrect Code:
# def square(number):
#     result = number * number
#
# print(square(6))
#
# Correction:
# Added return result inside the function.

def square(number):
    result = number * number
    return result

print(square(6))

# Expected Output:
# 36