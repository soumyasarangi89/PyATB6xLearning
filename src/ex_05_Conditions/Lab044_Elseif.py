# Find the positive number is even or odd

num = int(input("Enter a number: ").strip())

if num >= 0:
    if num % 2 == 0:
        print("Its an Even Number")
    else:
        print("Its an Odd Number")
else:
    print("Its a Negative Number")

# You can write short one-liner conditions using ternary operator:
if num >= 0:
    print("Its an Even Number" if num % 2 == 0 else "Its an Odd Number")
else:
    print("Its a Negative Number")