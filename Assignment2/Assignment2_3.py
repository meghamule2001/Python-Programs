
#  Write a program which accept one number from user and return its factorial.
# Input : 5 Output : 120

def Factorial(no):
    fact=1
    for i in range(1,no+1):
        fact=(fact*i)
    return fact

def main():
    num=int(input("Enter number : "))
    iret=Factorial(num)
    print("Factorial of {} is : {}".format(num,iret))

if __name__=="__main__":
    main()