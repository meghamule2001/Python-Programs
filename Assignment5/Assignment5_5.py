
# Write a recursive program which accept number from user and return its
# factorial.
# Input : 5
#
# Output : 120

def Display(no):
    if no==0:
        return 1
    else:
        return (no*Display(no-1))

def main():
    num=int(input("Enter number : "))

    ret=Display(num)
    print("Factorial of {} is : {}".format(num,ret))

if __name__=="__main__":
    main()