
#Addition of two numbers

#import Module1

#import Module1 as AR

#from Module1 import Addition,Substraction

from Module1 import*

# Entry point function
def main():
    print("__name__ from main is : ",__name__)
    value1=int(input("Enter first number : "))
    value2=int(input("Enter second number : "))

    ret1=Addition(value1,value2)
    ret2=Substraction(value1,value2)
    print("Addition is : ",ret1)
    print("Substraction is : ",ret2)

#Code starter
if __name__=="__main__":
    main()

