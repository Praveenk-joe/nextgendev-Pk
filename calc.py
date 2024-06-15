import math

# Create a function for each calculation

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def square_root(x):
    return math.sqrt(x)

# Prompt the user to select the operation

print("Select an operation to perform: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Modulus")
print("7. Square Root")

# Take input from the user

choice = input("Enter your choice: ")

# Use conditional statements to execute the chosen operation

if choice in ('1', '2', '3', '4', '5', '6'):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))

    elif choice == '5':
        print(num1, "**", num2, "=", power(num1, num2))

    elif choice == '6':
        print(num1, "%", num2, "=", modulus(num1, num2))

elif choice == '7':
    num1 = float(input("Enter the number to find the square root: "))
    print("Square root of ", num1, "is", square_root(num1))

else:
    print("Invalid Input")
