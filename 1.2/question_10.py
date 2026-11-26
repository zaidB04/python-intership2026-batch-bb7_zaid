# DigolTech Python Internship 2026
# Section 1.2 - Error Finding & Debugging
# Question 10: Shopping Cart Debugging
#
# Error Identification:
# The statement total = item[1] replaces the previous
# total with the current item's price.
#
# Error Type: Logical Error
#
# Original Incorrect Code:
#
# cart = [
#     ["Keyboard", 800],
#     ["Mouse", 400],
#     ["USB Cable", 200]
# ]
#
# total = 0
#
# for item in cart:
#     total = item[1]
#
# if total >= 1000:
#     discount = total * 10 / 100
# else:
#     discount = 0
#
# final_amount = total - discount
#
# print("Total:", total)
# print("Discount:", discount)
# print("Final Amount:", final_amount)
#
# Correction:
# Changed total = item[1] to total += item[1].
# This adds all item prices to the total.

cart = [
    ["Keyboard", 800],
    ["Mouse", 400],
    ["USB Cable", 200]
]

total = 0

for item in cart:
    total += item[1]

if total >= 1000:
    discount = total * 10 / 100
else:
    discount = 0

final_amount = total - discount

print("Total:", total)
print("Discount:", discount)
print("Final Amount:", final_amount)

# Expected Output:
# Total: 1400
# Discount: 140.0
# Final Amount: 1260.0