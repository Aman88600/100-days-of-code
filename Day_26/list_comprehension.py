# [new_item for item in list]

# numbers = [i for i in range(1,11)]
# new_numbers = [(number + 1) for number in numbers]
# print(new_numbers)

# numbers_2 = [num*2 for num in numbers]
# print(numbers_2)

names = ["Aman", "Nikhil", "Mukunds"]
short_names = [name for name in names if len(name) <= 4]
print(short_names)