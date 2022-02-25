
# Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which are even. Map function will calculate its square.
# Reduce will return addition of all that numbers.
# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204

import functools

def main():
    arr=[]
    print("Enter the number of elements : ")
    size=int(input())

    for i in range(size):
        print("Enter element number : ",i+1)
        value=int(input())
        arr.append(value)

    print("Entered data : ",arr)

    newdata=list(filter(lambda no:(no%2==0),arr))
    print("After filtering data : ",newdata)

    newdata1=list(map(lambda no:(no*no),newdata))
    print("After mapping data : ",newdata1)

    output=functools.reduce(lambda no1,no2:no1+no2,newdata1)
    print("After reducing data : ",output)

if __name__=="__main__":
    main()