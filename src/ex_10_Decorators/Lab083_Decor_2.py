def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper


@decorator1
@decorator1
def say_hello():
    print("Hello!")

@decorator2
@decorator1
def greet():
    print("Greetings!")


say_hello()
greet()