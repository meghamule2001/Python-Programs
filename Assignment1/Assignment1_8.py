
# Write a program which accept number from user and print that number of “*” on screen.
# Input : 5 Output : * * * * *

def Print(num):
    for no in range(0,num,1):
        print("*",end=" ")

def main():
    no = int(input("Enter Number of stars to print : "))
    Print(no)

if __name__=="__main__":
    main()
