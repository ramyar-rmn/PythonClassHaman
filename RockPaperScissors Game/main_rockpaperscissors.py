import random
print('Choose your weapon:')
print('1. Rock')
print('2. Paper')
print('3. Scissor')
player = input('Make your choice (1,2,3) or 0 to quit: ')
if player not in ('0', '1', '2', '3'):
    print('Wrong choice')
while player in ('1', '2', '3'):
    player = int(player)
    computer = int(random.random()*3+1)
    weapon = ['Rock', 'Paper', 'Scissor']
    print('Computer chose', weapon[computer-1])
    if player == computer:
        print('Draw')
    elif player == 1:
        if computer == 2:
            print('You lost')
        else:
            print('You won')
    elif player == 2:
        if computer == 3:
            print('You lost')
        else:
            print('You won')
    elif player == 3:
        if computer == 1:
            print('You lost')
        else:
            print('You won')
    print('Another turn?')
    player = input('Make your choice (1,2,3) or 0 to quit: ')
