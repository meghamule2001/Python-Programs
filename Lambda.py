
# name=lambda parameters:body

# named function
def Addition(no1,no2):
    return no1+no2

# lambda function
Sum = lambda no1,no2 : no1+no2

def fun(name):
    ret=name(10,20)
    print("Value from fun is : ",ret)

def main():
    value1 = int(input("Enter first number : "))
    value2 = int(input("Enter second number : "))

    ret=Addition(value1,value2)
    print("Addition is : ",ret)

    ret=Sum(value1,value2)
    print("Addition with lambda is : ",ret)

    fun(Sum)
    fun(Addition)

if __name__=="__main__":
    main()
