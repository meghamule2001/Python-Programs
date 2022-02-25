
# Design python application which contains two threads named as thread1 and thread2.
# Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on
# screen. After execution of thread1 gets completed then schedule thread2.

###############################################################################################

import threading

def Thread1(iNo,kulup):
    kulup.acquire()
    print("Numbers in given range : ")
    for i in range(1,(iNo+1)):
        print(i)

    kulup.release()

def Thread2(iNo,kulup):
    kulup.acquire()
    print("Numbers in given range in reverse order : ")
    for i in range(1,(iNo+1)):
        print(i)

    kulup.release()

def main():
    print("Enter number : ")
    iValue = int(input())

    kulup = threading.Lock()
    t1 = threading.Thread(target = Thread1, args = (iValue,kulup,))
    t2 = threading.Thread(target = Thread2, args = (iValue,kulup,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__=="__main__":
    main()