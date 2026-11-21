print("===The Function Calculator===")
num1= int(input("Enter the first number: "))
num2= int(input("Enter the second number: "))
function=int(input("Choose which function you want to use:"))
if function== "addition":
    print(num1 + num2)
elif function=="subtraction":
    print(num1 - num2)
elif function== "multiplication":
    print(num1 * num2)
else:
    print(num1/num2)
    