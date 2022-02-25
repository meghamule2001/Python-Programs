
# Design object oriented python application which accepts numbers from user and perform below operation
# Display all even numbers
# Calculate summation of all numbers
# Display all perfect numbers

class Numbers:

    def __init__(self,no=10):
        self.size=no
        self.arr=[]

    def __del__(self):
        print("Deallocating the memory of object")
        del self.arr

    def Accept(self):
        print("Please enter the elements : ")
        for i in range(self.size):
            print("Enter elements number ",i+1)
            self.arr.append(int(input()))

    def Display(self):
        print("Elements of list are :")
        for i in range(self.size):
            print(self.arr[i])

    def Summation(self):
        sum=0
        for i in range(self.size):
            sum=sum+self.arr[i]

        return sum

    def EvenDisplay(self):
        print("Even elements from array :")

        for i in range(self.size):
            if (self.arr[i]%2)==0:
                print(self.arr[i])

    def OddDisplay(self):
        print("Even elements from array :")

        for i in range(self.size):
            if (self.arr[i] % 2) == 0:
                print(self.arr[i])

    def PerfectDisplay(self):
        sum=0
        for i in range(self.size):
            for j in range(1,int(self.arr[i]/2)+1):
                if (self.arr[i]%j==0):
                    sum=sum+j
            if sum==self.arr[i]:
                print(self.arr[i])
            sum=0

    def PrimeDisplay(self):
        Flag=False
        for i in range(self.size):
            for j in range(2,int(self.arr[i]/2+1)):
                if(self.arr[i]%j)==0:
                    Flag=True
                    break
            if Flag==False:
                print(self.arr[i])
            Flag=False

def main():
    obj2=Numbers()  # jevha user input det nahi teva default input consider kel jat

    print("Enter number of elements : ")
    value=int(input())

    obj1=Numbers(value)
    print(obj1.size)

    obj1.Accept()
    obj1.Display()
    ret=obj1.Summation()
    print("Summation of all elements : ",ret)

    obj1.EvenDisplay()

    print("Perfect numbers are : ")
    obj1.PerfectDisplay()

    print("Primenumbers are : ")
    obj1.PrimeDisplay()

    del obj1

if __name__=="__main__":
    main()
