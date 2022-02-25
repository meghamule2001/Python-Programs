
# Write a program which accept N numbers from user and store it into List. Return addition of all
# elements from that List.
# Input : Number of elements : 6
# Input Elements : 13 5 45 7 4 56
# Output : 130

def Addition(list):
    i=0
    sum=0
    for i in range(len(list)):
        sum=sum+list[i]

    return sum

def main():
    arr=[]
    print("Enter Number of elements : ")
    size=int(input())

    for i in range(size):
        print("Enter element number : ",i+1)
        n=int(input())
        arr.append(n)

    print("Entered data is : ",arr)

    ret=Addition(arr)
    print("Addition of elements is : ",ret)

if __name__=="__main__":
    main()
