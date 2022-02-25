# function chaining
# 16 17 10 12 7 8 4 5 12 13 17
# Inbuilt function from module
def Subtraction(no1, no2):
    return no1 - no2

def SubDecorator(fun_name):
    return fun_name(10, 5)

def main():

    iRet = SubDecorator(Subtraction)
    print("Subtraction is : ", iRet)


if __name__ == "__main__":
    main()