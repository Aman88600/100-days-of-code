# This is the tip calculator
print("Welcome to the Tip Calculator!")
total_bill = float(input("What was the total Bill? $"))
tip_percentage = float(input("How much tip would you like to give? 10, 12, or 15? "))
tip = (tip_percentage/100) * total_bill
tip_plus_bill = total_bill + tip
number_of_people = int(input("How many people to split the bill? "))
per_person_bill = tip_plus_bill / number_of_people
print(f"Each person should pay: ${per_person_bill}")