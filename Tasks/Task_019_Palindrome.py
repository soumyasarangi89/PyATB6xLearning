# Question - ✅Palidrome of String
#
# 🧩 Example Walkthrough
#
# Let’s take the word "level":
# Forward: "level"
# Backward: "level"
#
# Both are identical → Palindrome ✅

# Now, "hello":
# Forward: "hello"
# Backward: "olleh"
#
# Not the same → Not a palindrome ❌


# Program to check if a string is a palindrome

def is_palindrome(text):
    # Remove spaces and make lowercase for fair comparison
    cleaned_text = text.replace(" ", "").lower()

    # Compare string with its reverse
    return cleaned_text == cleaned_text[::-1]


# --- Main Program ---
user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")