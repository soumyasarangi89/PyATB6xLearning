num = int(input("Enter a number which fact you want to get!"))
fact = 1

if num < 0:
    print("Fact is not defined!")
else:
    for i in range(1, num + 1):
        fact = fact * i
    print("Factorial of :", fact)