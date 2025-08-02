print("A simple calculator program")
print("Enter two numbers and a mathematical operation (+, -, *, /)")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
else:
    print("Error: Invalid operation. Please enter +, -, *, or /")
    print("Thank you for using the calculator program!")