import os
import time

def Square(no):
    return no*no

def SerialProcessing():
    start = time.time()
    print("Serial Processing")
    arr = range(100000)
    ret = []

    for i in arr:
        ret.append(Square(i))

    # print("Result of serial processing is : ",ret)
    end = time.time()
    print("Time required for serial processing : ",end-start)

def main():
    print("Inside main")
    SerialProcessing()

if __name__=="__main__":
    main()