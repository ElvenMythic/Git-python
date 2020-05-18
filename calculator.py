#import

import time
import winsound

#print instructions

print("This is the Python calculator. To use, type in a number when requested, then enter an operation. Operations include addition (+), subtraction (-), multiplication (*), division (/), and exponents (^).")

time.sleep(2)

#storing operation

print("Enter an operation.")
operation=str(input())

#checking if stored operation is valid
if operation == "+" or operation == "-" or operation == "*" or operation == "/" or operation == "^":

    #storing numbers
    
    print("Enter a number.")
    number1=float(input())
    print("Enter a second number.")
    number2=float(input())

    #checking operation and computing

    print("Calculating...")
    
    if operation == "+":
        result=number1 + number2
        print(number1,"+",number2,"=",result)
    elif operation == "-":
        result=number1 - number2
        print(number1,"*",number2,"=",result)
    elif operation == "*":
        result=number1 * number2
        print(number1,"*",number2,"=",result)
    elif operation == "/":
        result=number1 / number2
        print(number1,"/",number2,"=",result)
    elif operation == "^":
        result=number1 ** number2
        print(number1,"^",number2,"=",result)
    
else:

    #error sequence
    
    print("Error: Invalid operation")
    print("Shutting down...")
    time.sleep(3)
    exit()
