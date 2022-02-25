
# Write a program which contains one lambda function which accepts one parameter and return
# power of two.
# Input : 4 Output : 16
# Input : 6 Output : 64

power=lambda no:no*no

def main():
    value=int(input("Enter number : "))
    iret=power(value)
    print("Square of {} is : {}".format(value,iret))

if __name__=="__main__":
    main()