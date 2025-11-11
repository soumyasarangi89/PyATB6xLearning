# Program to count vowels and consonants in user input

def count_vowels_consonants(text):
    # Define what vowels are (both lowercase and uppercase)
    vowels = "aeiouAEIOU"

    # Start counters at 0
    vowel_count = 0
    consonant_count = 0

    # Go through each character in the text
    for char in text:
        if char.isalpha():  # Only check letters (ignore spaces, numbers, etc.)
            if char in vowels:  # If the letter is a vowel
                vowel_count += 1  # Add 1 to vowel counter
            else:  # Otherwise, it's a consonant
                consonant_count += 1  # Add 1 to consonant counter

    # Return both counts
    return vowel_count, consonant_count


# --- Main Program ---
# Ask the user to type something
user_input = input("Enter a string: ")

# Call the function and get the results
vowels, consonants = count_vowels_consonants(user_input)

# Show the results
print("Vowels:", vowels)
print("Consonants:", consonants)