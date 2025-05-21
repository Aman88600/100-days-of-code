keep_going = True
while keep_going == True:
    try:
        age = int(input('Enter Your Age : '))
        keep_going = False
    except ValueError:
        print('Age Must be a number')
if age >= 18:
    print("You can Drive")
else:
    print("You can't Drive")