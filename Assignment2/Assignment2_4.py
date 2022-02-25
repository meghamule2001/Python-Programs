
# Write a program which accept one number form user and return addition of its factors.
# Input : 12 Output : 16 (1+2+3+4+6)

def AddFactors(no):
    sum=0
    for i in range(1,no):
        if no%i==0:
            sum=sum+i
    return sum

def main():
    num=int(input("Enter Number : "))
    iret=AddFactors(num)
    print("Addition of factors of {} is : {}".format(num,iret))

if __name__=="__main__":
    main()