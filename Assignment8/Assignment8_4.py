
# Design python application which creates three threads as small, capital, digits. All the
# threads accepts string as parameter. Small thread display number of small characters,
# capital thread display number of capital characters and digits thread display number of
# digits. Display id and name of each thread.

#######################################################################################################

import os
import threading

def Small(str, kulup):
    kulup.acquire()
    print("\nPID of thread Small is : ",os.getpid())
    print("PID of parent process of thread Small is : ",os.getppid())

    iCnt = 0
    for i in range(len(str)):
        if ((str[i] > 'a') and (str[i] < 'z')):
            iCnt = iCnt + 1

    print("Number of small characters in given string : ",iCnt)
    kulup.release()

def Capital(str, kulup):
    kulup.acquire()
    print("\nPID of thread Capital is : ",os.getpid())
    print("PID of parent process of thread Capital is : ",os.getppid())

    iCnt = 0
    for i in range(len(str)):
        if ((str[i] > 'A') and (str[i] < 'Z')):
            iCnt = iCnt + 1

    print("Number of capital characters in given string : ",iCnt)
    kulup.release()

def Digits(str, kulup):
    kulup.acquire()
    print("\nPID of thread Digits is : ",os.getpid())
    print("PID of parent process of thread Digits is : ",os.getppid())

    iCnt = 0
    for i in range(len(str)):
        if ((str[i] >= '0') and (str[i] <= '9')):
            iCnt = iCnt + 1

    print("Number of digits in given string : ",iCnt)
    kulup.release()

def main():
    print("PID of main process is : ",os.getpid())
    print("PID of parent process of main is : ",os.getppid())
    print("Enter string : ")
    sValue = input()

    kulup = threading.Lock()

    t1 = threading.Thread(target = Small, args = (sValue,kulup,))
    t2 = threading.Thread(target = Capital, args = (sValue,kulup,))
    t3 = threading.Thread(target = Digits, args = (sValue,kulup,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__=="__main__":
    main()