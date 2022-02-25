
import functools

def main():
    arr = [] # mutable, ordered, indexed, duplicates, heterogeneous
    print("Enter number of elements")
    size =int(input())

    for i in range(size):
        print("Enter element number : ",i+1)
        no=int(input())
        arr.append(no)

    print("Entered data is : ", arr)
    print(functools.reduce(lambda a,b:a+b,list(map(lambda no:no+2,list(filter(lambda no:(no%2==0),arr))))))

if __name__=="__main__":
    main()