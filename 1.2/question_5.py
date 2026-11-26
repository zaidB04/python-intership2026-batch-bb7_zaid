# DigolTech Python Internship 2026
# Section 1.2 - Error Finding & Debugging
# Question 5: List Index Error
#
# Error Identification:
# The list contains four elements with indexes 0 to 3.
# Index 4 does not exist.
#
# Error Type: Runtime Error (IndexError)
#
# Original Incorrect Code:
# fruits = ["Apple", "Banana", "Mango", "Orange"]
# print(fruits[4])
#
# Correction:
# Changed the index from 4 to 3.

fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits[3])

# Expected Output:
# Orange