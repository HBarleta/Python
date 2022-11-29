class User():
    def __init__(self, firstName, lastName, email, age):
        self.first_name = firstName
        self.last_name = lastName
        self.email = email
        self. age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self

    def enroll(self):
        if(self.is_rewards_member == True):
            return print("Already a member")
        else: 
            self.is_rewards_member = True
            self.gold_card_points = 200
            return self
    
    def spend_points(self, amount):
        if(amount > self.gold_card_points):
            print('Not enough points')
            return self
        else:
            self.gold_card_points -= amount
            return self

user1 = User("Harold", "Barleta", "hbf20c@gmail.com", 34)
user1.display_info()
user1.enroll()
user1.display_info()
user1.enroll()
user1.spend_points(50).display_info()

user2 = User("John", "Cena", "Cantseeme23@yahoo.com", 30)
user2.enroll().display_info().spend_points(80)

user2.display_info()
user1.display_info()