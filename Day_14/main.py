from game_data import instagram_celebrities
from logo import higher_lower_logo, vs
from random import randint

print(higher_lower_logo)

keep_going = True
num1 = randint(0, len(instagram_celebrities) - 1)
num2 = num1
while num2 == num1:
    num2 = randint(0, len(instagram_celebrities) - 1)

while keep_going:
    print(f"Compare A:, {instagram_celebrities[num1]["name"]}, {instagram_celebrities[num1]["description"]}, from {instagram_celebrities[num1]["country"]}")
    print(vs)
    print(f"Against B:, {instagram_celebrities[num2]["name"]}, {instagram_celebrities[num2]["description"]}, from {instagram_celebrities[num2]["country"]}")
    user_ans = input("Who has more followers A or B : ")
    if (instagram_celebrities[num1]["follower_count"] > instagram_celebrities[num2]["follower_count"]) and user_ans == "A":
        keep_going = True
        num2 = randint(0, len(instagram_celebrities) - 1)
        while num2 == num1:
            num2 = randint(0, len(instagram_celebrities) - 1)
    elif (instagram_celebrities[num1]["follower_count"] < instagram_celebrities[num2]["follower_count"]) and user_ans == "B":
        num1 = randint(0, len(instagram_celebrities) - 1)
        while num1 == num2:
            num1 = randint(0, len(instagram_celebrities) - 1)
        keep_going = True
    else:
        keep_going = False
# for i in instagram_celebrities:
#     print(i)


