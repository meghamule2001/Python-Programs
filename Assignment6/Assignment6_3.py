
#  Write a program which contains one class named as Arithmetic.
# Arithmetic class contains three instance variables as Value1 ,Value2.
# Inside init method initialise all instance variables to 0.
# There are three instance methods inside class as Accept(), Addition(), Subtraction(),
# Multiplication(), Division().
# Accept method will accept value of Value1 and Value2 from user.
# Addition() method will perform addition of Value1 ,Value2 and return result.
# Subtraction() method will perform subtraction of Value1 ,Value2 and return result.
# Multiplication() method will perform multiplication of Value1 ,Value2 and return result.
# Division() method will perform division of Value1 ,Value2 and return result.
# After designing the above class call all instance methods by creating multiple objects.

class Arithmatic:

    def __init__(self):
        self.Value1=0
        self.Value2=0

    def __del__(self):
        print("Deallocating the memory of object")
        del self.Value1
        del self.Value2

    def Accept(self):
        print("Enter first number : ")
        self.Value1=int(input())

        print("Enter second number : ")
        self.Value2=int(input())

    def Addition(self):
        iSum=(self.Value1+self.Value2)
        return iSum

    def Subtraction(self):
        iSub=(self.Value1-self.Value2)
        return iSub

    def Multiplication(self):
        iMult=(self.Value1*self.Value2)
        return iMult

    def Division(self):
        iDiv=(self.Value1//self.Value2)
        return iDiv

def main():
    obj1=Arithmatic()
    obj2=Arithmatic()

    iRet1=obj1.Accept()

    iRet1=obj1.Addition()
    print("Addition is : ",iRet1)

    iRet1=obj1.Subtraction()
    print("Subtraction is : ", iRet1)

    iRet1=obj1.Multiplication()
    print("Multiplication is : ",iRet1)

    iRet1=obj1.Division()
    print("Division is : ",iRet1)
    print("\r")

    iRet2=obj2.Accept()

    iRet2=obj2.Addition()
    print("Addition is : ",iRet2)

    iRet2=obj2.Subtraction()
    print("Subtraction is : ", iRet2)

    iRet2=obj2.Multiplication()
    print("Multiplication is : ",iRet2)

    iRet2=obj2.Division()
    print("Division is : ",iRet2)

if __name__=="__main__":
    main()