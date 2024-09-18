class User:
    def __init__(self, username):
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1
aman = User("Aman Basoya")
nikhil = User("Nikhil Sharma")

aman.follow(nikhil)
print(aman.following)
print(nikhil.followers)