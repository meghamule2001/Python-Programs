
# Design python application which creates two thread named as even and odd. Even
# thread will display first 10 even numbers and odd thread will display first 10 odd
# numbers.

###############################################################################################

import threading

def Even(kulup):
    kulup.acquire()
    print("Even numbers : ")
    arr = range(10)
    for i in arr:
        if (i%2 == 0):
            print(i)

    kulup.release()

def Odd(kulup):
    kulup.acquire()
    print("Odd number : ")
    arr = range(10)
    for i in arr:
        if (i%2 != 0):
            print(i)

    kulup.release()

def main():
    kulup = threading.Lock()

    t1 = threading.Thread(target = Even, args = (kulup,))
    t2 = threading.Thread(target = Odd, args = (kulup,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__=="__main__":
    main()
