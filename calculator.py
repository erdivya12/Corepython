def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y == 0:
        return "Error! Division by zero!"
    else:
        return x / y
def calculator():
    print("select operation:")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("divide")
    choice = input("Enter choice(1,2,3,4):")

    num1 = float(input("Enter first number"))
    num2 = float(input("Enter second number"))

    if choice == '1':
        print("result:", add(num1, num2))
    elif choice == '2':
        print("result:", subtract(num1, num2))
    elif choice == '3':
        print("result:", multiply(num1,num2))
    elif choice == '4':
        print("result:",divide(num1,num2))
    else:
        print("invlid password")
calculator()