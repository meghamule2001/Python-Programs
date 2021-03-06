import os
import time
import multiprocessing

def Square(no):
    return no*no
###############################################################

def ParallelProcessing():
    start = time.time()
    print("Parallel Processing")
    arr = range(1000)

    pobj = multiprocessing.Pool()

    ret = pobj.map(Square,arr)

    end = time.time()
    print("Time required for Parallel processing : ", end - start)

###############################################################
def SerialProcessing():
    start = time.time()
    print("Serial Processing")
    arr = range(1000)
    ret = []

    for i in arr:
        ret.append(Square(i))

    # print("Result of serial processing is : ",ret)
    end = time.time()
    print("Time required for serial processing : ",end-start)
###################################################################
def main():
    print("Inside main")
    ParallelProcessing()
    SerialProcessing()

if __name__=="__main__":
    main()