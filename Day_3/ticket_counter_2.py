height = int(input('Enter Your Height in cm : '))
# This is the total bill
bill = 0
if height > 120:
    age = int(input('Enter Your Age : '))
    want_photo = input('Do you want a photo of you at roller coaster y/n:')
    if age < 12:
        bill += 5
    elif age >= 12 and age <= 18:
        bill += 7
    elif age >= 45 and age <= 55:
        bill += 0
    else:
        bill += 12
    if want_photo == 'y':
        bill += 3
    print(f'Your Bill is {bill}')
else:
    print('Can\'t ride')