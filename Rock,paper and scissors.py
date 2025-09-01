import random

computer_choice = ('r', 'p', 's')
emojis = {'r': '🪨', 'p': '📜', 's': '✂️'}
while True:
    your_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
    if your_choice not in computer_choice:
        print('Invalid Input.')
        continue

    choice = random.choice(computer_choice)

    print(f'You chose {emojis[your_choice]}')
    print(f'Computer chose {emojis[choice]}')

    if your_choice == choice:
        print('Game Tie.')

    elif (your_choice == 'r' and choice == 's') or (your_choice == 's' and choice == 'p') or (your_choice == 'p' and choice == 'r'):
        print('You Won!!')

    else:
        print('You loose')
