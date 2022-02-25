
#  Write a program which accept name from user and display length of its name.
# Input : Marvellous Output : 10

def CntLen(str):
    return len(str)

def main():
    name=input("Enter the name : ")
    iret=CntLen(name)
    print("Length of {} is : {}".format(name, int(iret)))

if __name__=="__main__":
    main()