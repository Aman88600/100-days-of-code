height = int(input('Enter Your Height in cm : '))
if height > 120:
    age = int(input('Enter Your Age : '))
    if age < 12:
        print('That will be $5')
    elif age >= 12 and age <= 18:
        print('That will be $7')
    else:
        print('That\'ll be $12')
else:
    print('Can\'t ride')