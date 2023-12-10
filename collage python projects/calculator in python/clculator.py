def addition (num1,num2):
    result = num1 + num2
    print(result)
def substraction(num1,num2):
    result = num1 - num2
    print(result)
def multiplication(num1,num2):
    result = num1 * num2
    print(result)
def division(num1,num2):
    result = num1 / num2
    print(result)

num1 = int(input("Enter the frist number: "))
num2 = int(input("Enter the second number: "))

operator = input("Choose one (+, -, *, /)")
if operator == '+':
    addition(num1,num2)
if operator == '-':
    substraction(num1,num2)
if operator == '*':
    multiplication(num1, num2)
if operator == '/':
    division(num1,num2)
    