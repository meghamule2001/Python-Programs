
#  Write a program which contains one function named as Add() which accepts two numbers
# from user and return addition of that two numbers.
# Input : 11 5 Output : 16

def Add(a, b):
    sum =a+b
    return sum

def main():
    no1=int(input("Enter first number : "))
    no2=int(input("Enter second number : "))

    res=Add(no1,no2)
    print("Addition of {} and {} is {}".format(no1,no2,res))

if __name__=="__main__":
    main()