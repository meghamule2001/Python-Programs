
#  Write a program which accept one number and display below pattern.
# Input : 5
# Output :
#  * * * * *
#  * * * * *
#  * * * * *
#  * * * * *
#  * * * * *

def Display(no):
    for i in range(0,no,1):
        for j in range(0,no,1):
            print("*",end="  ")
        print("\r")

def main():
    num=int(input("Enter Number : "))
    ret=Display(num)

if __name__=="__main__":
    main()