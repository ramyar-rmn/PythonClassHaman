from random import randint


def easy_game():
    number = randint(0, 5)
    print('Computer chose a number in range of [0,5], go ahead and guess it.')
    player = int(input('Do you dare: '))
    if number == player:
        print('Wow You did it!!!')
    else:
        print("Sorry. Don't dare to try again")


def mid_game():
    global scores
    tries = 0
    number = randint(6, 16)
    print('Computer chose a number in range of [6,15], go ahead and guess it.')
    scoring = {1: 5, 2: 3, 3: 1}
    while tries <= 2:
        tries += 1
        player = int(input('Do you dare to guess: '))
        if number == player:
            print('Wow You did it!!!')
            scores += scoring[tries]
            print('You did it in:', tries, 'tries', 'and your average score is', scores/games)
            break
        elif number < player:
            print('You should guess a lower number')
        elif number > player:
            print('You should guess a greater number')
        if tries == 3:
            print("As I knew you lost this match",  'and your average score is', scores/games)


def hard_game():
    tries = 0
    number = randint(-100000, 100000)
    print('Computer chose a number in range of [-100000,100000], go ahead and guess it.')
    while True:
        tries += 1
        player = int(input('Do you dare to guess: '))
        if number == player:
            print('Wow You did it!!!')
            break
        elif number < player:
            print('You should guess a lower number')
        elif number > player:
            print('You should guess a greater number')
    print('You did it in:', tries, 'tries')


print('Welcome to guess the number game')
print('Do you want to play easy mode in one turn or mid mode with scoring or hard mode in several tries?')
choice = input('Type in Easy or Mid or Hard: ')
choice = choice.lower()
games = 0
scores = 0
while True:
    games += 1
    if choice == 'easy':
        easy_game()
    elif choice == 'mid':
        mid_game()
    elif choice == 'hard':
        hard_game()
    game_end = int(input('enter 1 for continue playing: '))
    if game_end != 1:
        break
