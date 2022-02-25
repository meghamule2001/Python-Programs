
# Design python application which creates two threads as evenfactor and oddfactor.
# Both the thread accept one parameter as integer. Evenfactor thread will display
# addition of even factors of given number and oddfactor will display addition of odd
# factors of given number. After execution of both the thread gets completed main
# thread should display message as “exit from main”.

#################################################################################################

import threading

def EvenFactor(iNo,kulup):
    kulup.acquire()
    iSum = 0
    for i in range(iNo):
        if (i%2 == 0):
            iSum = iSum + i

    print("Addition of even factors : ",iSum)
    kulup.release()

def OddFactor(iNo,kulup):
    kulup.acquire()
    iSum = 0
    for i in range(iNo):
        if (i%2 != 0):
            iSum = iSum + i

    print("Addition of Odd numbers : ",iSum)
    kulup.release()

def main():
    iValue = int(input("Enter number : "))

    kulup = threading.Lock()
    t1 = threading.Thread(target = EvenFactor, args = (iValue,kulup,))
    t2 = threading.Thread(target = OddFactor, args = (iValue,kulup,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main!")

if __name__=="__main__":
    main()