# ✅ Grade Calculator:
# Write a program that calculates and displays the letter grade
# for a given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale

# O: 91-100
# E: 81-90
# A: 71-80
# B: 61-70
# C: 51-60
# D: 33-50
# F: 0-3 2

# Logic Building Formula

# 1 -> User Inputs - score -> int
# 2 ->  O/p -> str -> A, B

score = int(input("Enter Your Score: ").strip())

if 0 > score or score > 100: # Score should be between 0 & 100
    print("❌ Enter a Valid Number ❌")
else:
    if 90 < score <= 100:
        print("You have achieved Grade O, Ranked First Division")
    elif 80 < score <= 90:
        print("You have achieved Grade E, Ranked First Division")
    elif 70 < score <= 80:
        print("You have achieved Grade A, Ranked First Division")
    elif 60 < score <= 70:
        print("You have achieved Grade B, Ranked First Division")
    elif 50 < score <= 60:
        print("You have achieved Grade C, Ranked Second Division")
    elif 33 < score < 50:
        print("You have achieved Grade D, Try to harder, Ranked Third Division")
    else:
        print("Sorry You failed this Semester")