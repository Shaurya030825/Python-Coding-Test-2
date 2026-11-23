print("===The Function Calculator===")

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
try:
    a= float(input("Please enter the first number: "))
    b= float(input("Please enter the second number: "))
    op= input("OPeration: (add, subtract, multiply, divide): ")

    if op == "add":
        print("Result:", add(a,b))
    elif op == "subtract":
        print("Result:", subtract(a,b))
    elif op == "multiply":
        print("Result:", multiply(a,b))
    elif op == "divide":
        print("Result:", divide(a,b))
    else:
        print("Unknown operator")
        pass
except ValueError:
    print("Type numbers only")
except ZeroDivisionError:
    print("You cannot divide by zero")
finally:
    print("Thanks for using the calculator")