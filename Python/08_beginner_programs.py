# Beginner Python Programs

# 1. Add two numbers
a = 10
b = 20

print("1. Sum:", a + b)


# 2. Check even or odd
number = 15

if number % 2 == 0:
    print("2. Even number")
else:
    print("2. Odd number")


# 3. Check positive, negative or zero
number = -10

if number > 0:
    print("3. Positive")
elif number < 0:
    print("3. Negative")
else:
    print("3. Zero")


# 4. Find largest of three numbers
a = 25
b = 40
c = 15

largest = max(a, b, c)

print("4. Largest number:", largest)


# 5. Calculate factorial
number = 5
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("5. Factorial:", factorial)


# 6. Multiplication table
number = 7

print("6. Multiplication table:")

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# 7. Reverse a string
text = "Python"

print("7. Reverse:", text[::-1])


# 8. Count vowels
text = "programming"
vowels = "aeiou"
count = 0

for character in text:
    if character in vowels:
        count += 1

print("8. Number of vowels:", count)


# 9. Check palindrome
word = "madam"

if word == word[::-1]:
    print("9. Palindrome")
else:
    print("9. Not a palindrome")


# 10. Sum of list elements
numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:
    total += number

print("10. Sum of list:", total)


# 11. Find the largest number in a list
numbers = [12, 45, 23, 67, 34]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("11. Largest in list:", largest)


# 12. Simple calculator
a = 20
b = 5
operator = "+"

if operator == "+":
    print("12. Result:", a + b)
elif operator == "-":
    print("12. Result:", a - b)
elif operator == "*":
    print("12. Result:", a * b)
elif operator == "/":
    print("12. Result:", a / b)
else:
    print("12. Invalid operator")
