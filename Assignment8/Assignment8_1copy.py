
# Design python application which creates two thread named as even and odd. Even
# thread will display first 10 even numbers and odd thread will display first 10 odd
# numbers.

import threading

def Even(iNo):
    print("Even numbers : ")
    for i in range(iNo):
        if (i%2 == 0):
            print(i)

def Odd(iNo):
    print("Odd number : ")
    for i in range(iNo):
        if (i%2 != 0):
            print(i)

def main():
    print("Inside main")
    iValue = int(input("Enter number : "))

    t1 = threading.Thread(target = Even, args = (iValue,))
    t2 = threading.Thread(target = Odd, args = (iValue,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End of main")

if __name__=="__main__":
    main()