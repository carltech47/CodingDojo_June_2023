
class BankAccount:
    accounts = []
    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, dep_amount):
        self.balance += dep_amount
        return self

    def withdrawal(self, withdrawal_amount):
        if (self.balance - withdrawal_amount) >=0:
            self.balance -= withdrawal_amount
        else: 
            print(f"Insufficient Funds: Charging a $5 Fee")
            self.balance -= 5
            return self
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        print("\n")
        return self

    def yield_interest(self):
        amount = 0.1
        total_interest = (self.balance * amount )
        if self.balance > 0:
            sum_total = (self.balance + total_interest)
        print(sum_total)
        print("\n")
        return

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

account_1 = BankAccount(.1,10000)
account_2 = BankAccount(.5,50)

account_1.deposit(1000).deposit(2000).deposit(8000).withdrawal(1500).display_account_info()
account_2.deposit(100).deposit(100).withdrawal(100).withdrawal(200).withdrawal(200).withdrawal(2000).display_account_info()

BankAccount.print_all_accounts()