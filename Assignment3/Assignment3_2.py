
# .Write a program which accept N numbers from user and store it into List. Return Maximum
# number from that List.
# Input : Number of elements : 7
# Input Elements : 13 5 45 7 4 56 34
# Output : 56

def Max(list):
    i=0
    for i in range(len(list)):
        if list[0]<list[i]:
            list[0]=list[i]

    return list[0]

def main():
    arr=[]
    print("Enter the number of elements : ")
    size=int(input())

    for i in range(size):
        print("Enter element number : ",i+1)
        no=int(input())
        arr.append(no)

    print("Enter data : ",arr)

    ret=Max(arr)
    print("Maximum number from list is : ",ret)

if __name__=="__main__":
    main()