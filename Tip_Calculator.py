# 1. Greet the user
print("Welcome to the tip calculator.")

# 2. Get the total Bill
total_bill = float(input("Enter the total bill $"))

# 3. What percentage of tip
tip_percentage = float(input("What percentage of tip would you like to give? 10, 12 or 15 : "))

# 4. Asking how many people are paying
number_of_people = float(input("How many people are splitting the Bill ? "))

# 5. Priting the result each person should pay
tip_percentage /= 100
tip_percentage += 1
each_person_should_pay = (total_bill / number_of_people) * tip_percentage


# 6. Round off the result to 2 decimal places
each_person_should_pay = round(each_person_should_pay, 2)
print(f"Each person should pay ${each_person_should_pay}\n")
input()