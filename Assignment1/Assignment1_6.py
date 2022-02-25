
# Write a program which accept number from user and check whether that number is positive or
# negative or zero.
# Input : 11 Output : Positive Number
# Input : -8 Output : Negative Number
# Input : 0 Output : Zero

def ChkNum(no):
    if no>=0:
        if no==0:
            print("Zero")
        else:
            print("{} is Positive Number".format(no))
    else:
        print("{} is Negative Number".format(no))


def main():
    n=int(input("Enter the number to be ckecked : "))
    ChkNum(n)

if __name__=="__main__":
    main()