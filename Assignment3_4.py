
# Write a program which accept N numbers from user and store it into List. Accept one another
# number from user and return frequency of that number from List.
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 5 34 2 5 65
# Element to search : 5
# Output : 3

def Frequency(list,no):
    i=0
    icnt=0
    for i in range(len(list)):
        if list[i]==no:
            icnt=icnt+1

    return icnt

def main():
    arr=[]
    print("Enter the number of elements : ")
    size=int(input())

    for i in range(size):
        print("Enter element number : ",i+1)
        n=int(input())
        arr.append(n)

    print("Entered data : ",arr)

    value=int(input("Enter element to search : "))

    ret=Frequency(arr,value)
    print("Frequency of element : ",ret)

if __name__=="__main__":
    main()