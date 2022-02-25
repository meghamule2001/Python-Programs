
# Write a program which display first 10 even numbers on screen.
# Output : 2 4 6 8 10 12 14 16 18 20

def Print(num):
    for num in range(2,num*2+1):
        if num%2==0:
            print(num,end=" ")

def main():
    no=int(input("Enter number of elements wants to print : "))

    Print(no)

if __name__=="__main__":
    main()