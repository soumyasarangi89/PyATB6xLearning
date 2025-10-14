user_age = int(input("Enter your Age: "))

if user_age >= 18:
    print("Yes you are eligible for Goa Trip")
else:
    print("No you are underage for Goa Trip")


print("Yes you are eligible for Goa Trip" if user_age >= 18 else "No you are underage for Goa Trip")