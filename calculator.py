# Description: A simple calculator that takes two numbers and an operator as input and returns the result of the operation.

operator = input("Enter an operator(+,-,*,/): ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the secound number: "))

if operator == "+":
    result = num1 + num2
    print(round(result,3))
elif operator == "-":
    result == num1 - num2
    print(round(result,3))
elif operator == "*":
    result = num1 * num2
    print(round(result,3))
elif operator == "/":
    print(round(result,3))

else:
 print(f" {operator} is not an valid operator..")