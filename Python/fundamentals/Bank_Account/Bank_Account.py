
class BankAccount:
    accounts = []
    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance
        BankAccount.accounts.append(self)
        
    def deposit(self, dep_amount):
        self.balance += dep_amount
        return self
    
    #
# yield_interest(self) - 
# increases the account balance by the current balance * the interest rate (as long as the balance is positive)
#
    def yield_interest(self): ### This is my new "yield_interest" method. Signed by Torrey - 3/19/2023 ###
        total_interest = (self.balance * self.interest_rate )
        if self.balance > 0:
            print("You have a positive balance in your bank account, and interest is being calculated.")
            print("One moment please....")
            sum_total = (self.balance + total_interest)
            print(sum_total)
            print("\n")
        else: 
            self.balance < 0
            print("There are insufficient funds to calculate any interest rate accruel.")
            print("Please contact your local branch for assistance.")
            print("\n")
            

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


        
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            print(account)
            print("\n")
        return account
    
    @classmethod
    def all_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.accounts:
            sum += account.balance
        return sum
            
account_1 = BankAccount(.1,10000)
account_2 = BankAccount(.5,5000)
account_3 = BankAccount(2.5,100000)

account_1.deposit(1000).deposit(2000).deposit(8000).withdrawal(1500).display_account_info().yield_interest()
account_2.deposit(100).deposit(100).withdrawal(100).withdrawal(200).withdrawal(200).withdrawal(2000).display_account_info().yield_interest()
account_3.deposit(200000).deposit(300000).withdrawal(115000).display_account_info().yield_interest()


BankAccount.print_all_accounts()
BankAccount.all_balances()

#account_info = BankAccount.accounts

print(account_1.balance)