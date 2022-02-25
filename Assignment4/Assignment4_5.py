
# Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
# return Maximum number from that numbers. (You can also use normal functions instead of
# lambda functions).
# Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# Output of reduce = 62


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

    newdata=list(filter(lambda no:all(no%i!=0 for i in range(2,int(no**0.5)+1)),arr))
    print("After filtering data : ",newdata)

    newdata1=list(map(lambda no:(no*2),newdata))
    print("After mapping data : ",newdata1)

    output=functools.reduce(lambda no1,no2:(no1 if no1>no2 else no2),newdata1)
    print("After reducing data : ",output)

if __name__=="__main__":
    main()