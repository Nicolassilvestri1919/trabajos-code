import math

def calculator():
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Square Root")
    choice = input("Enter choice (1/2/3/4/5): ")
    if choice in ('1', '2', '3', '4'):
        num1, num2 = float(input("Enter first number: ")), float(input("Enter second number: "))
        if choice == '1': print("Answer:", num1 + num2)
        elif choice == '2': print("Answer:", num1 - num2)
        elif choice == '3': print("Answer:", num1 * num2)
        elif choice == '4': print("Answer:", num1 / num2 if num2 != 0 else "Invalid (division by 0)")
    elif choice == '5':
        num = float(input("Enter a number: "))
        print("Answer:", math.sqrt(num) if num >= 0 else "Invalid (Square Root negative number)")
    else: print("Invalid input")

calculator()