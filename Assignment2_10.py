
# Write a program which accept number from user and return addition of digits in that number.
# Input : 5187934 Output : 37

def AddDigits(n):
    icnt=0
    sum=0
    while n!=0:
        mod=n%10
        sum=sum+mod
        n=n//10
        icnt=icnt+1
    return sum

def main():
    num=int(input("Enter Number : "))
    iret=AddDigits(num)
    print("Addition of digits of {} is : {}".format(num,int(iret)))

if __name__=="__main__":
    main()
