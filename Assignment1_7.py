
# Write a program which contains one function that accept one number from user and returns
# true if number is divisible by 5 otherwise return false.
# Input : 8 Output : False
# Input : 25 Output : True

def ChkNum(no):
    if no%5==0:
        return True
    else:
        return False

def main():
    n=int(input("Enter Number to be checked : "))
    bret=ChkNum(n)
    if bret==True:
        print("{} is divisible by 5".format(n))
    else:
        print("{} is not divisible by 5".format(n))

if __name__=="__main__":
    main()
