
# Write a program which contains one class named as BankAccount.
# BankAccount class contains two instance variables as Name & Amount.
# That class contains one class variable as ROI which is initialise to 10.5.
# Inside init method initialise all name and amount variables by accepting the values from user.
# There are Four instance methods inside class as Display(), Deposit(), Withdraw(),
# CalculateIntrest().
# Deposit() method will accept the amount from user and add that value in class instance variable
# Amount.
# Withdraw() method will accept amount to be withdrawn from user and subtract that amount
# from class instance variable Amount.
# CalculateIntrest() method calculate the interest based on Amount by considering rate of interest
# which is Class variable as ROI.
# And Display() method will display value of all the instance variables as Name and Amount.
# After designing the above class call all instance methods by creating multiple objects.

class BankAccount:
    ROI = 10.5
    def __init__(self,i,j):
        self.Name = i
        self.Amount = j

    def Display(self):
        print("Name : ",self.Name)
        print("Amount : ",self.Amount)

    def Deposit(self):
        print("\nEnter the amount to deposit : ")
        dAmount = float(input())
        self.Amount = self.Amount + dAmount
        return (self.Amount)

    def Withdraw(self):
        print("\nEnter the amount to withdraw : ")
        wAmount = float(input())

        if self.Amount >= wAmount:
            self.Amount = self.Amount - wAmount
            return (self.Amount)
        else:
            print("Insufficient Amount!")

    def CalculateInterest(self):
        RI = (self.Amount * BankAccount.ROI) // 100
        return (RI)

def main():
    print("Enter your name : ")
    cValue = input()

    print("Enter amount : ")
    fValue = float(input())

    obj = BankAccount(cValue, fValue)

    print("\nAccount holders current details : ")
    obj.Display()

    fRet = obj.Deposit()
    print("Amount present after deposite : ",fRet)

    fRet = obj.Withdraw()
    print("Amount present after Withdrawal : ",fRet)

    fRet = obj.CalculateInterest()
    print("\nInterest on present amount : ",fRet)

if __name__=="__main__":
    main()