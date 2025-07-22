# class car:

#     def __init__(self, color, engine):
#         self.color = color
#         self.engine = engine





# car1 = car("Black", "Honda")
# print(car1.color + " " + car1.engine)

class instaBot:

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.followings = 0

    def follow(self, user):
        user.followers += 1
        self.followings += 1

user1 = instaBot("001", "Jack")
user2 = instaBot("002", "Will")

user1.follow(user2)

print(user1.followers)
print(user1.followings)
print(user2.followers)
print(user2.followings)
        
        