
# function chaining
# 28 29 16 17 8 9 10 11
# Inbuilt function from module
def Subtraction(no1, no2):
    print("6 : Inside Subtraction")
    return no1 - no2

def SubDecorator(func_name):
    print("10 : Inside SubDecorator")
    def Updator(a,b):
        print("12 : Inside Updator")
        if a<b:    # first parameter is small
            a,b = b,a       # Swaping of numbers
        return func_name(a,b)

    return Updator

def main():
    print("20 : Inside main")
    Sub = SubDecorator(Subtraction)

    print("Enter first number : ")
    value1 = int(input())

    print("Enter second number : ")
    value2 = int(input())
    iRet  = Sub(value1, value2)
    print("Subtraction is : ", iRet)
    print("30 : End of main")

if __name__ == "__main__":
    print("33 : Insider starter")
    main()