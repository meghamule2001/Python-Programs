
# Write a recursive program which display below pattern.
# Input : 5
# Output : 5 4 3 2 1

def DisplayR(no):
    i=1
    if i<=no:
        print(no, end=" ")
        DisplayR(no-1)

def main():
    num=int(input("Enter number : "))

    DisplayR(num)

if __name__=="__main__":
    main()