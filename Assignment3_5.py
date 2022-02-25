
# Write a program which accept N numbers from user and store it into List. Return addition of all
# prime numbers from that List. Main python file accepts N numbers from user and pass each
# number to ChkPrime() function which is part of our user defined module named as
# MarvellousNum. Name of the function from main python file should be ListPrime().
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 10 34 2 5 8
# Output : 54 (13 + 5 + 7 +2 + 5)

import MarvellousNum as MN

def ListPrime(arr):
    brr=[]
    for i in range(len(arr)):
        if MN.ChkPrime(arr[i])==True:
            brr.append(arr[i])

    return brr

def AddPrime(arr):
    sum=0
    for i in range(len(arr)):
        sum=sum+arr[i]

    return sum

def main():
    arr=[]
    print("Enter number of elements : ")
    size=int(input())

    print("Enter elements : ")
    for i in range(size):
        no=int(input())
        arr.append(no)

    print("Entered data : ",arr)

    newdata=list(ListPrime(arr))
    print("Prime numbers : ",newdata)

    output=AddPrime(newdata)
    print("Addition of Prime numbers is : ",output)

if __name__=="__main__":
    main()