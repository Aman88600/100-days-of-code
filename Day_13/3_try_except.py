keep_going = True
while keep_going == True:
    try:
        age = int(input('Enter Your Age : '))
        keep_going = False
    except ValueError:
        print('Age Must be a number')
if age >= 18:
    print(f"You can Drive at age {age}")
else:
    print(f"You can't Drive at age {age}")