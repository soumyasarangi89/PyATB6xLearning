# Problem  Find the Max between 3 numbers

# Logic Building

# User inputs - num1, num2, num3 -> int
# O/p -> int or String with max number .

num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))
num3 = int(input("Enter the num3: "))

if num1 >= num2 and num1 >= num3: # Gretaer is num1
    print("Maximum is ", num1)
elif num2 >= num3 and num2 >= num1:
    print("Maximum is ", num2)
else:
    print("Maximum is ", num3)