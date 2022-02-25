
# Write a recursive program which display below pattern.
# Input : 5
# Output : * * * * *

def DisplayR(no):
    i=1
    if i<=no:
        print("*", end="  ")
        i=i+1
        DisplayR(no-1)

def main():
    num=int(input("Enter number : "))
    DisplayR(num)


if __name__=="__main__":
    main()
