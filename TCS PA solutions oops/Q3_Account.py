class Account:
    def __init__(self, Acno, Acname, AcBalance):
        self.account_no = Acno
        self.account_name = Acname
        self.account_balance = AcBalance

    def depositAmnt(self, Amtdeposited):
        self.account_balance += Amtdeposited
        return(self.account_balance)

    def withdrawAmnt(self, Amtwithdrawn):
        if((self.account_balance-Amtwithdrawn) >= 1000):
            self.account_balance -= Amtwithdrawn
            return(1)
        else:
            return(0)


if __name__ == "__main__":
    accountno = int(input())
    accountname = input()
    accountbalance = int(input())
    Amountdeposited = int(input())
    AmountWithDrawn = int(input())
    acct = Account(accountno, accountname, accountbalance)
    print(acct.depositAmnt(Amountdeposited))
    #print("Balance after deposit:", acct.account_balance)
    res = acct.withdrawAmnt(AmountWithDrawn)
    if(res == 1):
        print("Balance after withdrawl of amount:", acct.acct.account_balance)
    else:
        print("Insufficient balance for withdrawl")
