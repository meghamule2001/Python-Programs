
#Addition of two numbers

#Definition
def Addition(no1,no2):
    ans=no1+no2
    return ans


#Definition of substraction
def Substraction(no1,no2):
    ans=no1-no2
    return ans

# Entry point function
def main():
    value1=int(input("Enter first number"))
    value2=int(input("Enter second number"))

    ret1=Addition(value1,value2)
    ret2=Substraction(value1,value2)
    print("Addition is : ",ret1)
    print("Substraction is : ",ret2)



#Code starter
if __name__=="__main__":
    main()

