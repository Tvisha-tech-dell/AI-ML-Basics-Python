# Python Functions

# 1. Simple function
def greet():
    print("Hello! Welcome to Python.")


greet()


# 2. Function with parameter
def greet_user(name):
    print("Hello,", name)


greet_user("Tvisha")


# 3. Function with multiple parameters
def add_numbers(a, b):
    return a + b


result = add_numbers(10, 20)
print("\nSum:", result)


# 4. Function to check even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print("10 is", check_even_odd(10))
print("7 is", check_even_odd(7))


# 5. Function to find square
def square(number):
    return number * number


print("\nSquare of 5:", square(5))


# 6. Function with default parameter
def welcome(name="Student"):
    print("Welcome,", name)


welcome()
welcome("Tvisha")


# 7. Function to find maximum
def find_max(a, b):
    if a > b:
        return a
    else:
        return b


print("\nMaximum:", find_max(25, 40))
