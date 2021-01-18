from random import randint


def easy_game():
    number = randint(0, 5)
    print('Computer chose a number in range of [0,5], go ahead and guess it.')
    player = int(input('Do you dare: '))
    if number == player:
        print('Wow You did it!!!')
    else:
        print("Sorry. Don't dare to try again")


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
print('Do you want to play easy mode in one turn or hard mode in several tries?')
choice = input('Type in Easy or Hard: ')
choice = choice.lower()
if choice == 'easy':
    easy_game()
elif choice == 'hard':
    hard_game()
