# DigolTech Python Internship 2026
# Section 1.2 - Error Finding & Debugging
# Question 9: Student Result Debugging
#
# Error Identification:
# The statement total = mark replaces the previous total
# instead of adding the current mark.
#
# Error Type: Logical Error
#
# Original Incorrect Code:
#
# marks = [80, 75, 90, 65, 70]
# total = 0
#
# for mark in marks:
#     total = mark
#
# percentage = total / 500 * 100
#
# if percentage >= 35:
#     result = "PASS"
# else:
#     result = "FAIL"
#
# print("Total:", total)
# print("Percentage:", percentage)
# print("Result:", result)
#
# Correction:
# Changed total = mark to total += mark.
# Used len(marks) to calculate percentage dynamically
# for different numbers of subjects.

marks = [80, 75, 90, 65, 70]

total = 0

for mark in marks:
    total += mark

percentage = total / (len(marks) * 100) * 100

if percentage >= 35:
    result = "PASS"
else:
    result = "FAIL"

print("Total:", total)
print("Percentage:", percentage)
print("Result:", result)

# Expected Output:
# Total: 380
# Percentage: 76.0
# Result: PASS