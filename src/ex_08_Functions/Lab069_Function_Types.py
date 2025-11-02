# User Defined
# 1. Non-Returning Function
# 2. Returning Function
# 3. Parameterized Function
# 4. Non-Parameterized Function

import math

# Built in Function
result = max(10, 20, 30, 40)
print(result)

# 1. Non-Returning Function
def greet():
    print("Hello, welcome to the program!")
greet()


def greet_by_name(name):
    return f"Hello, {name}!"

greet_by_name("Soumya")  # Function called but return value not used


def say_hello_default_args(naam="Guest"):
    print("Hello !", naam.upper())

say_hello_default_args()  # Function called with default argument
say_hello_default_args("Alice")  # Function called with custom argument

def multiple_args(name1="Soumya", name2="Sarangi"):
       print(f"Hello {name1} and {name2}!")

multiple_args()  # Both default arguments
multiple_args("Bob")  # One custom, one default
multiple_args("Charlie", "Dave")  # Both custom arguments



# 2. Returning Function

