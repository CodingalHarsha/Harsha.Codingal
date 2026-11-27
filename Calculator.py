print("*****Calculator*****")

def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b

try:
    print("Enter which opertation you want to do: 1. Add, 2. Subtract, 3. Multiply, 4. Divide")
    operation = input("Enter your choice:")

    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))

    if operation == "1":
        result = add(num1, num2)
        print(result)
    elif operation == "2":
        result = sub(num1, num2)
        print(result)
    elif operation == "3":
        result = mul(num1, num2)
        print(result)
    elif operation == "4":
        result = div(num1, num2)
        print(result)
    else:
        print("Please choose a valid option.")

except ValueError:
    print("Please choose valid numbers.")
except ZeroDivisionError:
    print("Numbers cannot be divided by 0.")