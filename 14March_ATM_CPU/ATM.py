
Amount = 1000

def ATM(func):
    func()

def Deposit():
    value = int(input("Enter amount to deposit : "))
    global Amount
    Amount = Amount + value
    print("Deposit successful - Balance : ",Amount)

def Withdraw():
    value = int(input("Enter the amount to withdraw : "))
    global Amount
    if value > Amount:
        print("There is no sufficient amount!!")
    else:
        Amount = Amount - value
        print("Withdraw successful - Balance : ",Amount)

def main():
    print("Inside main")
    ATM(Deposit)
    ATM(Withdraw)


if __name__=="__main__":
    main()
