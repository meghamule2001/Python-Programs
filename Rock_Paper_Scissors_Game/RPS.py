
def main():
    print("________Rock Paper Scissor_________")
    print("Rules of Game : ")
    print("There are two players required to play this game.")
    print("\n1. If you choose Rock, you will win against Scissors but lose against Paper. "
          "\n2. If you choose Scissors, you will win against Paper but lose against Rock. "
          "\n3. If you choose Paper, you will win against Rock but lose against Scissors.")
    print("\nThere can be 3 to 5 rounds. The game ends when somebody gets 3 wins.")

    print("R : Rock\nP : Paper\nS : Scissor\n")

    Choice = ["R", "P","S"]

    iCnt1 =0
    iCnt2 = 0
    for i in range(1,4):
        print("Round : ",i)
        print("User1 : ")
        User1 = input()
        print("User2 : ")
        User2 = input()
        if(User1 == "R"):
            if(User2 == "S"):
                iCnt1 = iCnt1 + 1
                print("Count1 : {}".format(iCnt1))
        elif(User1 == "S"):
            if(User2 == "R"):
                iCnt2 = iCnt2 + 1
                print("Count2",iCnt2)
        elif(User1 == "S"):
            if(User2 == "P"):
                iCnt1 = iCnt1 + 1
                print("Count1",iCnt1)
        elif(User1 == "P"):
            if(User2 == "S"):
                iCnt2 = iCnt2 + 1
                print("Count2",iCnt2)
        elif(User1 == "P"):
            if(User2 == "R"):
                iCnt1 = iCnt1 + 1
                print("Count1",iCnt1)
        elif(User1 == "R"):
            if(User2 == "P"):
                iCnt2 = iCnt2 + 1
                print("Count2",iCnt2)
        else:
            pass
    print("Count1 is {} and Coount2 is {}".format(iCnt1,iCnt2))
    if(iCnt1 > iCnt2):
        print("User1 won the game!")
    elif(iCnt2 > iCnt1):
        print("User2 won the game!")
    elif(iCnt1 == iCnt2):
        print("Tie")
    else:
        pass

if __name__=="__main__":
    main()
