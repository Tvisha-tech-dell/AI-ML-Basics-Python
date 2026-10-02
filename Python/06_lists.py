# Python Lists

# Creating a list
fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Fruits:", fruits)

# Accessing elements
print("\nFirst fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Adding an element
fruits.append("Grapes")
print("\nAfter append:", fruits)

# Inserting an element
fruits.insert(1, "Watermelon")
print("After insert:", fruits)

# Removing an element
fruits.remove("Banana")
print("After remove:", fruits)

# Changing an element
fruits[0] = "Pineapple"
print("After changing first element:", fruits)

# List length
print("\nNumber of fruits:", len(fruits))

# Sorting
numbers = [5, 2, 8, 1, 3]

numbers.sort()
print("\nSorted numbers:", numbers)

# Reverse
numbers.reverse()
print("Reversed numbers:", numbers)

# Loop through a list
print("\nFruits one by one:")

for fruit in fruits:
    print(fruit)

# Check if an item exists
if "Mango" in fruits:
    print("\nMango is present in the list.")
