
# Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
# for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
# parameters as number and perform the operation. Write on python program which call all the
# functions from Arithmetic module by accepting the parameters from user.

import Assignment2_1_Arithmatic as AR

def main():
    a=int(input("Enter first number : "))
    b=int(input("Enter second number : "))

    iret=AR.Add(a,b)
    print("Addition of {} and {} is : {}".format(a,b,iret))

    iret=AR.Sub(a,b)
    print("Subtraction of {} and {} is : {}".format(a,b,iret))

    iret=AR.Mult(a,b)
    print("Multiplication of {} and {} is : {}".format(a,b,iret))

    ret=AR.Div(a,b)
    print("Division of {} and {} is : {}".format(a,b,ret))

if __name__=="__main__":
    main()