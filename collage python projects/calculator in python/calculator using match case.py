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

match operator:
    case '+':
        addition(num1, num2)
    case '-':
        substraction(num1, num2)
    case '*':
        multiplication(num1, num2)
    case '/':
        division(num1, num2)
    case _:
        print("Enter a valid operator: ")