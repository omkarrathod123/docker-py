from random import randint

min_number = int(input('please enter min: '))
max_number = int(input('please enter max: '))

if (max_number < min_number):
    print('Invalid input - Error')
else:
    rad_number = randint(min_number,max_number)
    print(rad_number)