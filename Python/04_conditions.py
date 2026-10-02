# Conditional Statements

# 1. Simple if statement
age = 20

if age >= 18:
    print("You are eligible to vote.")


# 2. if-else
number = 7

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# 3. if-elif-else
marks = 82

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")


# 4. Positive, negative or zero
number = -5

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")


# 5. Largest of two numbers
a = 25
b = 40

if a > b:
    print("A is larger.")
elif b > a:
    print("B is larger.")
else:
    print("Both are equal.")
