
class Demo:

    def __init__(self,i):
        print("Inside Constructor")
        self.no=i

    def Even(self):
        return (self.no%2==0)

    def Odd(self):
        return (self.no%2!=0)

    def Perfect(self):
        pass


    def Prime(self):
        if self.no>1:
            for i in range(2,self.no):
                if self.no%2==0:
                    return False
                else:
                    return True
        else:
            return False





def main():
    arr=[]
    num=int(input("Enter number of elements : "))
    size=int(input())

    for i in range(size):
        print("Element number : ",i+1)
        value=int(input())
        arr.append(value)

    print("Entered numbers : ",arr)

    obj1=Demo(arr)

    ret=list(obj1.Even(arr))
    print("Even numbers : ",ret)

    ret=list(obj1.Odd(arr))
    print("Even numbers : ",ret)


    ret=list(obj1.Perfect(arr))
    print("Even numbers : ",ret)


    ret=list(obj1.Prime(arr))
    print("Even numbers : ",ret)

if __name__=="__main__":
    main()
