
# Accept n numbers from user and filter out only even numbers from that N numbers.
# After that add 2 in every even number
# After that addition of 2 perform summation of that modified numbers.

# Input [1,3,2,4,6,5,4]

# After filter [2,4,6,4]
# after map [4,6,8,6]
# after reduce 24

import functools

def main():
    arr = []
    print("Enter number of elements")
    size =int(input())

    for i in range(size):
        print("Enter element number : ",i+1)
        no=int(input())
        arr.append(no)

    print("Entered data is : ",arr)
    # newdata=filter(function_name,Data)
    newdata=list(filter(lambda no:(no%2==0),arr))   #newdata = Filter(arr)
    print("After Filtering data is : ",newdata)

    newdata1=list(map(lambda no:no+2,newdata))  #newdata1 =Map(newdata)
    print("After map data is : ",newdata1)

    output = functools.reduce(lambda no1,no2:no1+no2,newdata1)   #output =Reduce(newdata1)
    print("After reduce data is : ",output)

if __name__=="__main__":
    main()

