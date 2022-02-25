
# Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which greater than or equal to 70 and less than or equal to
# 90. Map function will increase each number by 10. Reduce will return product of all that
# numbers.
# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70]
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000

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

    newdata=list(filter(lambda no:(no>=70 and no<=90),arr))
    print("After filtering data : ",newdata)

    newdata1=list(map(lambda no:no+10,newdata))
    print("After maping data : ",newdata1)

    output=functools.reduce(lambda no1,no2:no1*no2,newdata1)
    print("After reducing data : ",output)


if __name__=="__main__":
    main()