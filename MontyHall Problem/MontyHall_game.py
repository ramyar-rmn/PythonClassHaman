import random

doors = [0, 0, 0]
doors[random.randint(0, 2)] = 1
a = int(input('Which door? 1,2 or 3? '))
while True:
    i = random.randint(1, 3)
    if a != i:
        if doors[i-1] == 0:
            print('Door #'+str(i)+' is one the goats')
            break
for c in range(1, 4):
    if c not in (a, i):
        print('Do you wish to change your decision to door #'+str(c)+' Or you will keep door #'+str(a)+' ?')
        i = int(input('Which one is your preferred? '+str(a)+' OR '+str(c)+' ?'))
        break
if doors[i-1] == 1:
    print('WOW You WIN!')
else:
    print('You win the goat')
