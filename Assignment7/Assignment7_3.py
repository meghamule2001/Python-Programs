
# Write a program which contains one class named as Numbers.
# Arithmetic class contains one instance variables as Value.
# Inside init method initialise that instance variables to the value which is accepted from user.
# There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(),
# Factors().
# ChkPrime() method will returns true if number is prime otherwise return false.
# ChkPerfect() method will returns true if number is perfect otherwise return false.
# Factors() method will display all factors of instance variable.
# SumFactors() method will return addition of all factors. Use this method in any another method
# as a helper method if required.
# After designing the above class call all instance methods by creating multiple objects.

class Numbers:
    def __init__(self,i):
        self.Value = i

    def ChkPrime(self):
        i=0
        if self.Value>1:
            for i in range(2,(self.Value//2)+1):
                if (self.Value%i) != 0:
                    return True
                else:
                    return False
        else:
            return False

    def ChkPerfect(self):
        if self.SumFactors() == self.Value:
            return True

    def SumFactors(self):
        i=0
        iSum = 0
        for i in range(1,(self.Value//2)+1):
            if (self.Value%i) == 0:
                iSum = iSum+i

        return iSum

    def Factors(self):
        i=0
        for i in range(1,(self.Value//2)+1):
            if (self.Value%i) == 0:
                print(i)

def main():
    print("Enter number : ")
    iValue = int(input())

    obj = Numbers(iValue)

    bRet = obj.ChkPrime()
    if(bRet == True):
        print("{} is prime number".format(iValue))
    else:
        print("{} is not prime number".format(iValue))

    bRet = obj.ChkPerfect()
    if (bRet == True):
        print("{} is perfect number".format(iValue))
    else:
        print("{} is not perfect number".format(iValue))

    iRet = obj.SumFactors()
    print("Sum of factors : ",iRet)

    print("Factors of {} ".format(iValue))
    obj.Factors()

if __name__=="__main__":
    main()