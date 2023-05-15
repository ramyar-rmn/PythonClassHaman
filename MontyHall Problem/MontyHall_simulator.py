import random
wonC = 0
wonK = 0
turns = int(input('How many turns? '))
for counter in range(0, turns):
    doors = [0, 0, 0]
    doors[random.randint(0, 2)] = 1
    a = random.randint(1, 3)
    while True:
        i = random.randint(1, 3)
        if a != i:
            if doors[i-1] == 0:
                break
    for c in range(1, 4):
        if c not in (a, i):
            break
    if doors[c-1] == 1:
        wonC += 1
    if doors[a-1] == 1:
        wonK += 1
print('The winning probability for changing the door was: ', wonC/turns)
print('The winning probability for keeping the door was: ', wonK/turns)
