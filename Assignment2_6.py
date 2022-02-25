
# Write a program which accept one number and display below pattern.
# Input : 5
# Output :
#  * * * * *
#  * * * *
#  * * *
#  * *
#  *

def Display(no):
    for i in range(no+1,0,-1):
        for j in range(0,i-1):
            print("*",end=" ")
        print("\r")

def main():
    num=int(input("Enter number : "))
    Display(num)

if __name__=="__main__":
    main()