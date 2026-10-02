# AI-ML-Basics-Python
Beginner-friendly learning repository covering Artificial Intelligence, Machine Learning, Deep Learning, real-world AI applications, and Python programming fundamentals.
Artificial Intelligence, Machine Learning & Python — Learning Notes
1. Introduction to Artificial Intelligence
What is Artificial Intelligence?

Artificial Intelligence (AI) is a field of computer science that focuses on creating systems capable of performing tasks that normally require human intelligence.

These tasks can include:

Learning
Reasoning
Problem solving
Understanding language
Recognizing images
Making predictions
Decision making
Examples of AI
ChatGPT
Google Maps route prediction
Face recognition
Voice assistants
Recommendation systems
Fraud detection
Autonomous vehicles
Medical image analysis
Simple example

When Netflix recommends a movie based on what you previously watched, an AI-based system is being used to make that recommendation.

2. AI vs ML vs Deep Learning

This is one of the most important concepts from your internship requirements.

Artificial Intelligence

AI is the largest concept.

Artificial Intelligence
        │
        └── Machine Learning
                │
                └── Deep Learning
Machine Learning

Machine Learning (ML) is a subset of AI where computers learn patterns from data instead of being explicitly programmed for every situation.

For example:

Instead of programming:

"If temperature > 30°C, predict high electricity consumption."

we can provide historical temperature and electricity data and allow an ML algorithm to learn the relationship.

Deep Learning

Deep Learning is a subset of Machine Learning that uses artificial neural networks with multiple layers.

It is particularly useful for:

Images
Speech
Natural language
Video
Complex patterns
Comparison
AI	Machine Learning	Deep Learning
Broad field	Subset of AI	Subset of ML
Simulates intelligent behavior	Learns from data	Learns using deep neural networks
Can use rules or learning	Primarily data-driven	Usually requires large datasets
Example: expert systems	Spam detection	Image recognition
Easy way to remember

AI = Goal

ML = Method of learning

DL = Advanced ML using neural networks

3. How Machine Learning Works

A basic ML workflow looks like this:

Data
 ↓
Data Preparation
 ↓
Training
 ↓
Model
 ↓
Testing
 ↓
Prediction
Example

Suppose we want to predict whether a student will pass.

We could provide:

Study Hours	Attendance	Result
2	60%	Fail
5	80%	Pass
7	90%	Pass
1	50%	Fail

The ML algorithm learns patterns from this data.

Then we give:

Study Hours = 6
Attendance = 85%

The model may predict:

Pass
4. Types of Machine Learning

There are three major categories.

A. Supervised Learning

The model learns from labeled data.

Example:

Input → Output

House size → House price
Study hours → Exam result
Email → Spam/Not Spam

Common algorithms:

Linear Regression
Logistic Regression
Decision Trees
Random Forest
Support Vector Machines
K-Nearest Neighbors
Two common supervised tasks

Regression

Predicts a numerical value.

Example:

Predict house price = ₹65 lakh

Classification

Predicts a category.

Example:

Email = Spam
B. Unsupervised Learning

The data does not have predefined labels.

The algorithm tries to discover patterns or groups.

Example:

A shopping company has customer data but doesn't know customer categories.

ML can identify groups such as:

Group 1 → Occasional buyers
Group 2 → Frequent buyers
Group 3 → High-value customers

Common technique:

Clustering

Example algorithm:

K-Means Clustering
C. Reinforcement Learning

An agent learns through rewards and penalties.

Action
 ↓
Environment
 ↓
Reward / Penalty
 ↓
Learning

Examples:

Game-playing AI
Robot navigation
Autonomous systems
5. Real-World Applications of AI
Healthcare

AI can assist with:

Medical image analysis
Disease prediction
Drug discovery
Patient monitoring
Finance

AI can be used for:

Fraud detection
Credit risk analysis
Algorithmic trading
Customer support
Transportation

Examples:

Route optimization
Traffic prediction
Driver-assistance systems
Autonomous vehicles
Education

AI can help with:

Personalized learning
Automated assessment
Recommendation systems
Educational chatbots
Manufacturing

AI is used for:

Predictive maintenance
Quality inspection
Robot control
Production optimization
Entertainment

Examples:

Movie recommendations
Music recommendations
Personalized advertisements
Content generation
6. Installing Python

Python is a high-level programming language known for its simple syntax and large ecosystem of libraries.

Check whether Python is installed:

python --version

or:

python --version

A Python program can be executed using:

python filename.py

Example:

print("Hello, World!")

Output:

Hello, World!
7. Python Variables

A variable stores a value.

name = "Tvisha"
age = 20
height = 5.5

Here:

name → "Tvisha"
age → 20
height → 5.5

Python does not require you to explicitly specify the variable's data type.

Example:

x = 10

Python automatically understands that x contains an integer.

8. Python Data Types

Important beginner data types:

Integer

Whole numbers.

age = 20
Float

Decimal numbers.

temperature = 36.5
String

Text.

name = "Tvisha"
Boolean

True or False.

is_student = True
List

Collection of items.

subjects = ["Maths", "Thermodynamics", "SOM"]
Dictionary

Stores data as key-value pairs.

student = {
    "name": "Tvisha",
    "age": 20
}
9. Operators
Arithmetic operators
a + b
a - b
a * b
a / b
a // b
a % b
a ** b

Example:

a = 10
b = 3

print(a + b)
print(a % b)

Output:

13
1

% gives the remainder.

** means exponentiation.

10. Taking User Input

Python's input() function takes input from the user.

name = input("Enter your name: ")

print("Hello", name)

Important:

input() normally returns a string.

If you need an integer:

age = int(input("Enter your age: "))

For decimal values:

height = float(input("Enter your height: "))
11. Conditional Statements

Conditions allow programs to make decisions.

age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")

You can also use elif.

marks = 75

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")
12. Loops

Loops allow us to repeat instructions.

For loop
for i in range(5):
    print(i)

Output:

0
1
2
3
4
While loop
count = 1

while count <= 5:
    print(count)
    count += 1

Output:

1
2
3
4
5
13. Lists

A list stores multiple values.

fruits = ["Apple", "Banana", "Mango"]

Access an item:

print(fruits[0])

Output:

Apple

Remember:

Python indexing starts at 0.

So:

Apple  → 0
Banana → 1
Mango  → 2
Useful list operations
fruits.append("Orange")

Adds an item.

fruits.remove("Banana")

Removes an item.

len(fruits)

Returns the number of items.

14. Functions

A function is a reusable block of code.

def greet():
    print("Hello!")

Call it:

greet()
Function with parameters
def greet(name):
    print("Hello", name)

greet("Tvisha")
Function returning a value
def add(a, b):
    return a + b

result = add(10, 20)

print(result)

Output:

30

Program 1 — Even or Odd
