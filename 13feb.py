import sys
import Module1

def datatypes():
    no=11
    print(no)
    print(id(no))
    print(type(no))
    print(sys.getsizeof(no))

    f=12.5
    print(sys.getsizeof(f))

    str="Hello"
    print(sys.getsizeof(str))

#Definition of function
def fun():
    print("Inside fun")

def Outer():
    print("Inside Outer")
    def Inner():
        print("Inside Inner")
    Inner()

def mun():
    pass   #when we don't wanted to written any logic inside function then we write pass to avoid error

def main():
    value1=int(input("Enter first number : "))
    value2=int(input("Enter second number : "))
    ret=Module1.Addition(value1,value2);  #function call
    print(ret)
    print("Addition of {} and {} is {} ".format(value1,value2,ret))
    # printf("Addition of %d and %d is %d",value1,value2,value

    Outer()


#starter
if __name__=="__main__":
    main()