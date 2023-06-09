# Create a file with the User class, including the __init__ with all the attributes, parameters and default values.

class User:
    def __init__(self, first_name, last_name, email, age, is_rewards_member, gold_card_points):
        self.first_name = "John"
        self.last_name = "Doe"
        self.email = "tugrp@example.com"
        self.age = 35
        self.is_rewards_member = False
        self.gold_card_points = 0

# Add the display_info(self) method to the User class
    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Is Rewards Member: {self.is_rewardss_member}")
        print(f"Gold Card Points: {self.gold_cars_points}")

# In the outer scope, create a user instance and call the display_info method to test.
user = User()
user.display_info()

# Add the enroll method to the User class, implement and test by calling the method on the user in the outer scope.
def enroll(self):
    self.is_rewards_member = True

# Make 2 more instances of the User class.
    user1 = User()
    user2 = User()

# Implement the spend_points(self, amount) method
    def spend_points(self, amount):
        if self.gold_card_points - amount <0:
            print("Not enough points")

# Have the first user spend 50 points
        user1.spending_points(50)
        
        

# Have the second user enroll.
        

# Have the second user spend 80 points
        user2.spending_points(80)

# Call the display method on all the users.
        user1.diplay_info()
        user2.display_info()

# BONUS: Implement the logic for testing if already a member and try to re-enroll the first user.abs


# BONUS: Implement the logic to prevent over-spending and call the spend_points method with 40 points on the 3rd user.