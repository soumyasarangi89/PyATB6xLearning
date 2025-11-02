def sum_three_numbers(a=1, b=2, c=3):
    return a + b + c

result1 = sum_three_numbers()
print(result1)

result2 = sum_three_numbers(10)
print(result2)

result3 = sum_three_numbers(10, 20)
print(result3)

result4 = sum_three_numbers(10, 20, 30)
print(result4)

result5 = sum_three_numbers(c=30)
print(result5)

result6 = sum_three_numbers(b=20, c=30)
print(result6)