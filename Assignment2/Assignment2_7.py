
#  Write a program which accept one number and display below pattern.
# Input : 5
# Output :
#  1 2 3 4 5
#  1 2 3 4 5
#  1 2 3 4 5
#  1 2 3 4 5
#  1 2 3 4 5

def Display(no):
    for i in range(1,no+1,1):
        for j in range(1,no+1,1):
            print(j,end="  ")
        print("")

def main():
    num=int(input("Enter Number : "))
    Display(num)

if __name__=="__main__":
    main()