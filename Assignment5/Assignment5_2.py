
# Write a recursive program which display below pattern.
# Input : 5
# Output : 1 2 3 4 5

def Display(no):
    if no>0:
        Display(no-1)
        print(no, end=" ")

def main():
    num=int(input("Enter number : "))
    Display(num)

if __name__=="__main__":
    main()