# Task for Today
# Take 2 input from the user
# Evaluate Quotient & Remainder
from numpy.ma.core import remainder

num1 = float(input("Enter a Number: "))
num2 = float(input("Enter another Number: "))

quotient = num1 // num2
remainder = num1 % num2

print(quotient)
print(remainder)