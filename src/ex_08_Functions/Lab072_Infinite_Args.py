def print_mul_arg(*args):

    for i in args:
        print(i)

print_mul_arg(10, 20, 30, 40, 50)
print_mul_arg("Apple", "Banana", "Cherry")
print_mul_arg(1, "Hello", 3.14, True)
print_mul_arg()  # No arguments passed
print_mul_arg(None, [], {}, (1, 2), {1, 2})
print_mul_arg("SingleArgument")
print_mul_arg(*range(5))  # Unpacking a range object
print_mul_arg(*(x for x in range(3)))  # Unpacking a generator expression
print_mul_arg(*["List", "of", "Strings"])  # Unpacking a list
print_mul_arg(*(i for i in ["A", "B", "C"]))  # Unpacking from a generator expression
print_mul_arg(*[1, 2, 3], *["X", "Y", "Z"])  # Unpacking multiple lists
print_mul_arg(*[i*i for i in range(4)])  # Unpacking a list comprehension
print_mul_arg(*("Tuple", "of", "Values"))  # Unpacking a tuple
print_mul_arg(*{10, 20, 30})  # Unpacking a set
print_mul_arg(*(f"Item {i}" for i in range(3)))  # Unpacking from a generator expression
print_mul_arg(*[None, True, False, 42])  # Unpacking a list with mixed types
print_mul_arg(*["Mixed", 123, 4.56, None])  # Unpacking a list with mixed types
print_mul_arg(*range(1, 6))  # Unpacking a range object from 1 to 5
print_mul_arg(*["A", "B"], *[1, 2])  # Unpacking multiple lists
print_mul_arg(*[i for i in range(3)], *["X", "Y"])  # Unpacking from list comprehension and another list
print_mul_arg(*["End", "of", "Tests"])  # Unpacking a list
print_mul_arg(*[i for i in range(10, 15)])  # Unpacking a list comprehension
print_mul_arg(*("Final", "Test"))  # Unpacking a tuple
print_mul_arg(*[i*2 for i in range(5)])  # Unpacking a list comprehension
print_mul_arg(*["Last", "One"])  # Unpacking a list
print_mul_arg(*[i for i in range(100, 105)])  # Unpacking a list comprehension
print_mul_arg(*("Done",))  # Unpacking a single-element tuple
print_mul_arg(*[i**2 for i in range(6)])  # Unpacking a list comprehension
print_mul_arg(*["Goodbye", "World"])  # Unpacking a list
print_mul_arg(*[i for i in range(200, 205)])  # Unpacking a list comprehension
print_mul_arg(*("The", "End"))  # Unpacking a tuple
print_mul_arg(*[i*3 for i in range(4)])  # Unpacking a list comprehension
print_mul_arg(*["Final", "Final"])  # Unpacking a list
print_mul_arg(*[i for i in range(300, 305)])  # Unpacking a list comprehension
print_mul_arg(*("That's", "All"))  # Unpacking a tuple
print_mul_arg(*[i+1 for i in range(5)])  # Unpacking a list comprehension
print_mul_arg(*["The", "Very", "End"])  # Unpacking a list
print_mul_arg(*[i for i in range(400, 405)])  # Unpacking a list comprehension
print_mul_arg(*("Goodbye",))  # Unpacking a single-element tuple
print_mul_arg(*[i-1 for i in range(5)])  # Unpacking a list comprehension
print_mul_arg(*["See", "You", "Later"])  # Unpacking a list
print_mul_arg(*[i for i in range(500, 505)])  # Unpacking a list comprehension
print_mul_arg(*("Farewell",))  # Unpacking a single-element tuple
print_mul_arg(*[i*4 for i in range(3)])  # Unpacking a list comprehension
print_mul_arg(*["The", "Absolute", "End"])  # Unpacking a list
print_mul_arg(*[i for i in range(600, 605)])  # Unpacking a list comprehension
print_mul_arg(*("Goodnight",))  # Unpacking a single-element tuple
print_mul_arg(*[i//2 for i in range(10)])  # Unpacking


