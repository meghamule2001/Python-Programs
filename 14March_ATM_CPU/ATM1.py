# Syanchronization
import threading        # os module is internally imported in threading module

Amount = 1000

def ATM(func, kulup):
    func(kulup)                 # t1 -> Deposit(kulup)      # t2 -> Withdraw(kulup)

def Deposit(kulup):
    kulup.acquire()
    value = int(input("Enter amount to deposit : "))
    global Amount
    Amount = Amount + value
    print("Deposit successful - Balance : ",Amount)
    kulup.release()

def Withdraw(kulup):
    kulup.acquire()
    value = int(input("Enter the amount to withdraw : "))
    global Amount
    if value > Amount:
        print("There is no sufficient amount!!")
    else:
        Amount = Amount - value
        print("Withdraw successful - Balance : ",Amount)
    kulup.release()

#   Start 45 46 29 32 34 6 7
def main():
    print("Inside main")

    kulup = threading.Lock()

    t1 = threading.Thread(target = ATM, args = (Deposit, kulup,))   # ATM(Deposit, kulup)
    t2 = threading.Thread(target = ATM, args = (Withdraw, kulup,))  # ATM(Deposit, kulup)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("ATM application closed")

if __name__=="__main__":
    main()