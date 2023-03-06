
class User:
    is_rewards_member = False
    gold_card_points = 0
    def __init__(self, first_name, last_name, email, age, member_status, gold_card_points):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.member_status = member_status

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Spend Points: {self.gold_card_points}")
        print("\n")
        return self

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


user_1.spend_points(50)
user_2.enroll()
user_2.spend_points(80)
user_1.display_info()
user_2.display_info()
user_3.display_info()
user_3.display_info()