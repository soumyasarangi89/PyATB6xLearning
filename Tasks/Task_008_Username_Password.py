# Check if the user can log in based on correct username and password.
#
# I/p
#
# username = "Admin"
# password = "1234"
#
# O/p
# ✅ Login Successful
#
#
# For the Fail condition Other O/P = ❌ Invalid Credentials

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == 'Admin' and password == "1234":
    print("✅ Login Successful")
else:
    print("❌ Invalid Credentials")