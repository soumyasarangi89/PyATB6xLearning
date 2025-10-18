# Write a program to take a user age and
# let him know if he can go the club.
# 21


# Logic Building Formula

# Step 01
# i/p = age, int
# o/p = String

name = input("Enter your name ")
age = int(input("\nEnter your Age ").strip())


# Step 02 Rough Logic
# age -> print go
# age -> print can't go

# Step 03 Write Logic

if age <= 0 or age > 130:
    print(name + " Enter a valid age")
else:
    if age >= 21:
        print("Hi " + name + "! You are eligible for joining us on the Trip")
    else:
        print("Hey " + name + "! I am sorry to inform you that, You are under age to join us in this trip")

# Step 4.  Check for the edge cases.
# We should consider edge cases such as:
# Negative ages or extremely high values -> program will break.
# Non-numeric input - ABC
# Age which is valid. > 130

# Step 5.  Optimize the code.
# Handle all the edges.