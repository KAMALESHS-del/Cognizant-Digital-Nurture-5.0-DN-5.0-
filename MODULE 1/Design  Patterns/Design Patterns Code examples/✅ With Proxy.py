class BankAccount:

    def withdraw(self):
        print("Money Withdrawn")


class ATMProxy:

    def __init__(self):
        self.account = BankAccount()
        

    def withdraw(self,pin):
        print("Checking PIN...")
        if pin==2006:
            print("account valid")

        self.account.withdraw()


atm = ATMProxy()

atm.withdraw(2006)