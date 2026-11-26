# DigolTech Python Internship 2026
# Section 1.2 - Error Finding & Debugging
# Question 7: List Calculation Error
#
# Error Identification:
# The condition checks odd numbers using == 1.
# The program should calculate the sum of even numbers.
#
# Error Type: Logical Error
#
# Original Incorrect Code:
# numbers = [10, 15, 20, 25, 30, 35]
# total = 0
#
# for number in numbers:
#     if number % 2 == 1:
#         total += number
#
# print("Even Sum:", total)
#
# Correction:
# Changed == 1 to == 0.

numbers = [10, 15, 20, 25, 30, 35]

total = 0

for number in numbers:
    if number % 2 == 0:
        total += number

print("Even Sum:", total)

# Expected Output:
# Even Sum: 60