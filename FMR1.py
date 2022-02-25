
# Accept n numbers from user and filter out only even numbers from that N numbers.
# After that add 2 in every even number
# After that addition of 2 perform summation of that modified numbers.

# Input [1,3,2,4,6,5,4]

# After filter [2,4,6,4]
# after map [4,6,8,6]
# after reduce 24

# Start 60 61 39->51 18->21 12->16 21->24 51 52 53 54 26->30 54 55 56 57 32->37 57 58 61 End

def ChkEven(no):
    if no%2==0:
        return True
    else:
        return False

def Filter(arr):
    brr=[]
    for i in range(len(arr)):
        if ChkEven(arr[i])==True:
            brr.append(arr[i])

    return brr

def Map(arr):
    for i in range(len(arr)):
        arr[i]=arr[i]+2

    return arr

def Reduce(arr):
    sum=0
    for i in range(len(arr)):
        sum=sum+arr[i]

    return sum

def main():
    arr = []
    print("Enter number of elements")
    size=int(input())

    for i in range(size):
        print("Enter element number : ",i+1)
        no=int(input())
        arr.append(no)

    print("Entered data is : ",arr)

    newdata = Filter(arr)
    print("After Filtering data is : ",newdata)

    newdata1=Map(newdata)
    print("After map data is : ",newdata1)

    output=Reduce(newdata1)
    print("After reduce data is : ",output)

if __name__=="__main__":
    main()

