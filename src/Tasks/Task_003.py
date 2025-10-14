import math

π = 3.14159265
r = float(input("Enter the radius: "))
area = π * pow(r,2)
area51 = math.pi * pow(r,2)

print("Area of the Circle =",area)

# Formatting
print(f"Area of the Circle = {area:.2f}")

print(f"Area of the Circle = {area51:.2f}")