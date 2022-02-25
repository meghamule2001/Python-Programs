
# Write a program which display 10 to 1 on screen.
# Output : 10 9 8 7 6 5 4 3 2 1


def DisplayF():
    print("Output of for loop")
    iCnt=0
    for iCnt in range(10,0,-1):
        print(iCnt)
    else:
        print("End of for loop")

def main():
    DisplayF()

if __name__=="__main__":
    main()
