import math

π = 3.14159265
r = float(input("Enter the radius: "))
area = π * pow(r,2)
area51 = math.pi * pow(r,2)


# i/p - r - float
# o/p  -> string formatted output of area.


# Logic Building Formula
# || Step 1 ||
# Figure out the inputs and output
# input -> r ->  data type -> float
# pi = 3.14
# power -> pow or ** -> any
# o/p -> String -> float - area , print area

# || Step 2 ||
# rough logic =  area = 3.14 * pow(r,2)


# || Step 3 ||


print("Area of the Circle =",area)

# Formatting
print(f"Area of the Circle = {area:.2f}")

print(f"Area of the Circle = {area51:.2f}")