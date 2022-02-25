
# Write a program which accept one number for user and check whether number is prime or not.
# Input : 5 Output : It is Prime Number

def ChkPrime(no):
    if no>1:
        for i in range(2,no):
            if no%i==0:
                return False
            else:
                return True
    else:
        return False

def main():
    num=int(input("Enter Number : "))
    bret=ChkPrime(num)
    if bret==True:
        print("{} is Prime Number".format(num))
    else:
        print("{} is not Prime Number".format(num))

if __name__=="__main__":
    main()
