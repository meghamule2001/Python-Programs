
# function chaining
# 32 34 19 21 9 17 11 23 - 27 11-15 5-7 28 29 34
# Inbuilt function from module
def Subtraction(no1, no2):          # 100
    print("6 : Inside Subtraction")
    return no1 - no2

def SubDecorator(func_name):        # 200   func_name = 100
    print("10 : Inside SubDecorator")
    def Updator(a,b):           # 300
        print("12 : Inside Updator")
        if a<b:    # first parameter is small
            a,b = b,a       # Swaping of numbers
        return func_name(a,b)       # return (call 100(10,6)) -> 4

    return Updator          # return 300

def main():             # 400
    print("20 : Inside main")
    Sub = SubDecorator(Subtraction)     # call 200(100) sub contains 300

    print("Enter first number : ")
    value1 = int(input())   # 6

    print("Enter second number : ")
    value2 = int(input())       # 10
    iRet  = Sub(value1, value2)     # call 300(6,10)
    print("Subtraction is : ", iRet)        # subtraction is : 4
    print("30 : End of main")

if __name__ == "__main__":
    print("33 : Insider starter")
    main()                              # call 400