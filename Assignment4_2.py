
# Write a program which contains one lambda function which accepts two parameters and return
# its multiplication.
# Input : 4 3 Output : 12
# Input : 6 3 Output : 18

Mult=lambda no1,no2:no1*no2

def main():
    value1=int(input("Enter first number : "))
    value2=int(input("Enter second number : "))

    iret=Mult(value1,value2)
    print("Multiplication of {} and {} is : ".format(value1,value2),iret)

if __name__=="__main__":
    main()