# Inbuilt function from module
def Subtraction(no1, no2):
    return no1-no2

def main():
    print("Inside main")
    print("Enter first number : ")
    iValue1 = int(input())

    print("Enter second number : ")
    iValue2 = int(input())

    iRet = Subtraction(iValue1, iValue2)
    print("Subtraction is : ",iRet)

if __name__=="__main__":
    main()
