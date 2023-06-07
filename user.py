
class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0


    def display_info(self):
        print(f"First Name: {self.first_name}\nLast Name: {self.last_name}\nEmail: {self.email}\nAge: {self.age} Rewards Member: {self.is_rewards_member}\nGold Card Points: {self.gold_card_points}")


    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200


    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount


todd = User("Todd", "Lee", "toddlee@gmail.com", "22")
todd.display_info()
todd.enroll()
todd.display_info()
todd.spend_points(50)
todd.display_info()
