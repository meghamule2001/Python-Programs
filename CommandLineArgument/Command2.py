
import sys

def Addition(no1,no2):
    return no1+no2

def main():
    ret = Addition(int(sys.argv[1]),int(sys.argv[2]))
    print("Addition of {} and {} is {} ".format(sys.argv[1],sys.argv[2],ret))

# Python Command.py 11 21 51 -> arguments : 4

if __name__=="__main__":
    main()

# python3 Command2.py 11 21