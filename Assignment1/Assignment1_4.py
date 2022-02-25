
# Write a program which display 5 times Marvellous on screen.
# Output : Marvellous
#  Marvellous
#  Marvellous
#  Marvellous
#  Marvellous

def Display(no):
    for no in range(0,no,1):
        print("Marvllous")

def main():
    i=int(input("Enter number of iterations : "))
    Display(i)

if __name__=="__main__":
    main()