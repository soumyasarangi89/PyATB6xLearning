# Create a Program to sum three number from the user input

"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

def sum(num1, num2, num3):
    return num1 + num2 + num3
print("The sum of three number is: ", sum(num1, num2, num3))

"""

def sum_of_three(n1=100, n2=200, n3=300):
    return n1 + n2 + n3

result = sum_of_three(10, 20, 30)
result0 = sum_of_three(10, 20)
result1 = sum_of_three(10)
result2 = sum_of_three()
# result3 = sum_of_three(num1, num2, num3)

print("Sum with all custom args:", result)
print("Sum with two custom args:", result0)
print("Sum with one custom arg:", result1)
print("Sum with all default args:", result2)
# print("Sum from user input:", result3)