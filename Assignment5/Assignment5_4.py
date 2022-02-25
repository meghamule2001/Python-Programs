
# Write a recursive program which accept number from user and return
# summation of its digits.
# Input : 879
# Output : 24

def Display(no):
    if no==0:
        return 0
    return (no%10)+Display(int(no/10))

def main():
    num=int(input("Enter number : "))

    ret=Display(num)
    print("Addition is : ",ret)

if __name__=="__main__":
    main()