import random
number = random.randint(1,100)
while True:
    try:
        your_pick = int(input('Enter your guess: '))

        if your_pick < number:
                print("It's too low, try again")
        elif your_pick > number:
                print("It's too high, try again")
        else:
                print('Congratulations, You won!!!')
                break
    except ValueError:
        print('Please enter a valid number')



