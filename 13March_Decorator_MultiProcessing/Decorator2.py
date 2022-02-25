
# function chaining
# 28 29 16 17 8 9 10 11
# Inbuilt function from module
def Subtraction(no1, no2):
    return no1 - no2

def SubDecorator(func_name):
    def Updator(a,b):
        if a<b:    # first parameter is small
            a,b = b,a       # Swaping of numbers
        return func_name(a,b)

    return Updator;

def main():
    Sub = SubDecorator(Subtraction)

    print("Enter first number : ")
    value1 = int(input())

    print("Enter second number : ")
    value2 = int(input())
    iRet  = Sub(value1, value2)
    print("Subtraction is : ", iRet)


if __name__ == "__main__":
    main()