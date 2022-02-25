
# Design python application which creates two threads as evenlist and oddlist. Both the
# threads accept list of integers as parameter. Evenlist thread add all even elements
# from input list and display the addition. Oddlist thread add all odd elements from input
# list and display the addition.

########################################################################################################

import threading

def EvenList(arr, kulup):
    kulup.acquire()
    iSum = 0
    for i in range(len(arr)):
        if (arr[i]%2 == 0):
            iSum = iSum + arr[i]

    print("Addition of Even numbers of list : ",iSum)
    kulup.release()

def OddList(arr, kulup):
    kulup.acquire()
    iSum = 0
    for i in range(len(arr)):
        if (arr[i]%2 != 0):
            iSum = iSum + arr[i]

    print("Addition of Odd numbers of list : ",iSum)
    kulup.release()

def main():
    arr = []
    print("Enter number of elements : ")
    size = int(input())

    for i in range(size):
        print("Element number ",i+1)
        value = int(input())
        arr.append(value)

    print("Given List : ",arr)

    kulup = threading.Lock()

    t1 = threading.Thread(target = EvenList, args = (arr,kulup,))
    t2 = threading.Thread(target = OddList, args = (arr,kulup,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__=="__main__":
    main()