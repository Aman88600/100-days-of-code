class User:
    def __init__(self, username):
        self.username = username
        # Default attribute
        self.followers = 0
user_1 = User("Aman")
print(user_1.username, user_1.followers)