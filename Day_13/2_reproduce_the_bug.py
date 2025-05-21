from random import randint
dice_images = [i for i in range(1,7)]
dice_num = randint(0,5)
# dice_num = 6 # bug reproduction
print(dice_images[dice_num])