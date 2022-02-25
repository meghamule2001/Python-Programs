
#  Write a program which accept number from user and return number of digits in that number.
# Input : 5187934 Output : 7

def DigitCnt(no):
    icnt=0
    while no!=0:
        no=no//10
        icnt=icnt+1
    return icnt

def main():
    num=int(input("Enter number : "))
    iret=DigitCnt(num)
    print("Number of digits in {} are : {}".format(num,iret))

if __name__=="__main__":
    main()