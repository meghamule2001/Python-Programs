# Sequential approach
def StartS():
    print("Jay Ganesh")
    print("Jay Ganesh")
    print("Jay Ganesh")
    print("Jay Ganesh")
    print("Jay Ganesh")

# Iterative approach
def StartI():
    iCnt=0
    while iCnt<5:
        print("Jay Ganesh")
        iCnt=iCnt+1

def StartDynamic(no,message="Jay Ganesh"):
    iCnt = 0
    while iCnt < no:
        print(message)
        print("Jay Ganesh")
        iCnt = iCnt + 1

def Display(no):
    print("Jay Ganesh"*no)

def main():
    print("Enter number of times you want to display message on screen")
    value=int(input())
    print("Enter the message")
    name=input()

    StartDynamic(value,name)
    StartDynamic(value)
    Display(value)

    print("Output by sequence")
    StartS()
    print("Output by Iteration")
    StartI()

if __name__=="__main__":
    main()