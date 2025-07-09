num1 = float(input("Enter first num: "))
op = input("Enter operator: ")
num2 = float(input("Enter second num: "))

#num1 and num2 are strings - we have to manually convert
#result = num1 + num2
#result = int(num1) + int(num2) -- error if user enters decimal number

if op == "+":
    print( num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid operator")
