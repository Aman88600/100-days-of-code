height = int(input('Enter Your Height in cm : '))
if height > 120:
    age = int(input('Enter Your Age : '))
    want_photo = input('Do you want a photo of you at roller coaster y/n:')
    if age < 12:
        print('That will be $5')
    elif age >= 12 and age <= 18:
        print('That will be $7')
    else:
        print('That\'ll be $12')
    if want_photo == 'y':
        print('That will be extra $3 for photo')
else:
    print('Can\'t ride')