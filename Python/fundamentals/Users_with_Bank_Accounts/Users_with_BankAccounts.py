

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


class User:
    is_rewards_member = False
    gold_card_points = 0
    def __init__(self, first_name, last_name, email, age, member_status, gold_card_points):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.member_status = member_status
        self.account = BankAccount(0.02, 125)

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Spend Points: {self.gold_card_points}")
        print("\n")
        return self

    def make_deposit(self, amount):
        self.accounts.deposit = 5555
        print(self.account.deposit)
        print("This is your account balance: ")


    def enroll(self):
        self.member_status = True
        print(self.member_status)
        self.gold_card_points = 200
        print(self.gold_card_points)
        print(f"\n")
        return self
    
    def spend_points(self, amount):
        print(self.gold_card_points-amount)
        print(f"\n")
        return self

# display_info(self) - Have this method print all of the users' details on separate lines.
# enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
# spend_points(self, amount) - have this method decrease the user's points by the amount specified.



user_1 = User('Bob', 'Smith', 'bs@gmail.com', 41, False, 0)
user_2 = User('Melissa', 'Wilson', 'mw@gmail.com', 37, False, 0)
user_3 = User('Abby', 'Johnson', 'aj@gmail.com', 16, False, 0)
user_4 = User('Lilly', 'Allen', 'la@gmail.com', 10, False, 0)


user_1.display_info().enroll().spend_points(50)
user_2.display_info().enroll().spend_points(80)
user_3.display_info().enroll().spend_points(0)
user_3.display_info().enroll().spend_points(0)