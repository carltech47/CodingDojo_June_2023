

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

# account_1 = BankAccount(.1,10000)
# account_2 = BankAccount(.5,50)

# account_1.deposit(1000).deposit(2000).deposit(8000).withdrawal(1500).display_account_info()
# account_2.deposit(100).deposit(100).withdrawal(100).withdrawal(200).withdrawal(200).withdrawal(2000).display_account_info()

# BankAccount.print_all_accounts()


"""
Create a User class with an __init__ method

Add a make_deposit method to the User class that calls on it's bank account's instance methods.

Add a make_withdrawal method to the User class that calls on it's bank account's instance methods.

Add a display_user_balance method to the User class that displays user's account balance

SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to

SENPAI BONUS: Add a transfer_money(self, amount, other_user) method to the user class that takes an amount and a different User instance, and transfers money from the user's account into another user's account.

"""

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, dep_amount):
        self.account.deposit(dep_amount)
        print(f"This is your account balance: {self.account.balance}")
        return self

# display_info(self) - Have this method print all of the users' details on separate lines.
# enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
# spend_points(self, amount) - have this method decrease the user's points by the amount specified.



#user_1 = User('Bob', 'Smith', 'bs@gmail.com', 41, False, 0)
# user_2 = User('Melissa', 'Wilson', 'mw@gmail.com', 37, False, 0)
# user_3 = User('Abby', 'Johnson', 'aj@gmail.com', 16, False, 0)
# user_4 = User('Lilly', 'Allen', 'la@gmail.com', 10, False, 0)


#user_1.display_info().enroll().spend_points(50)
# user_2.display_info().enroll().spend_points(80)
# user_3.display_info().enroll().spend_points(0)
# user_3.display_info().enroll().spend_points(0)

#user_1.make_deposit(2000)


