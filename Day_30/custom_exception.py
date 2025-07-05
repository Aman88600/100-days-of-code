height = float(input("Enter Your Height : "))
weight = float(input("Enter Your Weight : "))

if height > 3:
    raise ValueError("Human height is not more than 3 meters")

bmi = weight / height ** 2
print(bmi)