def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Division by zero"
    return n1 / n2

def modulo(n1, n2):
    return n1 % n2

def power(n1, n2):
    return n1 ** n2




num1 = int(input("Enter Your First Number :")) 
num2 = int(input("Enter YOur Second Number :"))
operation = input("Enter Your Operation : ")

if operation == "+":
    print("Result:", add(num1, num2))
elif operation == "-":
    print("Result:", subtract(num1, num2))
elif operation == "*":
    print("Result:", multiply(num1, num2))
elif operation == "/":
    print("Result:", divide(num1, num2))
elif operation == "%":
    print("Result:", modulo(num1, num2))
elif operation == "**":
    print("Result:", power(num1, num2))
else:
    print("Invalid Operation !!")