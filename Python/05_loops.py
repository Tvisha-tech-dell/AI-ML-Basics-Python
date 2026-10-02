# Python Loops

# 1. For loop
print("Numbers from 1 to 5:")

for i in range(1, 6):
    print(i)


# 2. While loop
print("\nWhile loop:")

i = 1

while i <= 5:
    print(i)
    i += 1


# 3. Print even numbers
print("\nEven numbers from 1 to 10:")

for i in range(1, 11):
    if i % 2 == 0:
        print(i)


# 4. Sum of numbers
total = 0

for i in range(1, 11):
    total += i

print("\nSum from 1 to 10:", total)


# 5. Multiplication table
number = 5

print("\nMultiplication table of", number)

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# 6. Break statement
print("\nBreak example:")

for i in range(1, 10):
    if i == 5:
        break
    print(i)


# 7. Continue statement
print("\nContinue example:")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)
