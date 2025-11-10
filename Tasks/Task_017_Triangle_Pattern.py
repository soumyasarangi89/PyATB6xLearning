# Right Triangle Pattern (Left Aligned)
rows = 5  # number of rows

for i in range(1, rows + 1):
    print("*" * i)



# Right Triangle Pattern (Right Aligned)
rows = 5 # number of rows

for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)



# Equilateral Triangle Pattern
rows = 5  # number of rows
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))



# Inverted Right Triangle Pattern (Left Aligned)
rows = 5  # number of rows
for i in range(rows, 0, -1):
    print("*" * i)



# Inverted Right Triangle Pattern (Right Aligned)
rows = 5  # number of rows
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "*" * i)



# Inverted Equilateral Triangle Pattern
rows = 5  # number of rows
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

