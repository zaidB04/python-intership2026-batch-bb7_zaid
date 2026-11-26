# DigolTech Python Internship 2026
# Section 1.2 - Error Finding & Debugging
# Question 3: Loop Error
#
# Error Identification:
# range(1, 10) excludes 10 because the ending value
# in range() is not included.
#
# Error Type: Logical Error
#
# Original Incorrect Code:
# for i in range(1, 10):
#     print(i)
#
# Correction:
# Changed the ending value from 10 to 11.

for i in range(1, 11):
    print(i)

# Expected Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10