def triangle_type(side1, side2, side3):
    if side1 <= 0 or side2 <= 0 or side3 <= 0:  # Edge Case 01 = Checks for positive lengths
        return "Not a triangle"
    if side1 + side2 <= side3 or side2 + side3 <= side1 or side1 + side3 <= side2: # Edge Case 02 = Triangle inequality theorem
        return "Not a triangle"
    if side1 == side2 == side3:
        return "Equilateral"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return "Isosceles"
    else:
        return "Scalene"

side1=float(input("Enter length of side 1: "))
side2=float(input("Enter length of side 2: "))
side3=float(input("Enter length of side 3: "))

print(triangle_type(side1, side2, side3))


# Verified by AI, added Edge Case 02 with AI suggestion.