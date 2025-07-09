def police_check(age:int) -> bool:
    if age >= 18:
        is_eligible = True
    else:
        is_eligible = False
    return is_eligible


if police_check(age=22):
    print("Alright You can Go!")
else:
    print("Stop right there!")