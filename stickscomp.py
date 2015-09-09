import random

while True:
    game_type = input("Play a Human (h) or computer (cpu)?")
    if game_type == "cpu" or game_type == "h":
        break
    else:
        print("Please enter 'cpu' or 'h' in order to play")

if game_type == "cpu":
    cpu = random.randint(1, 3)
# set player to 1
player = 1
cpu = 1

# set the initial state
state = 20 #number of sticks
print("The number of sticks is now ",state)
while True:
    # get valid move

    print("Player ",player)
    while True:
        move = input("How many sticks do you want to pick up? ")
        if int(move) < 4 and int(move) < state:
            break
        else:
            print("Illegal Move")
    # update the state
    state = state - int(move)
    # show the state
    print("The number of sticks is now ",state)
    # check win status - win, lose
    if state == 1:
        print("Player ",player, " wins!")
        break

    #switch players 2->1, 1->2
    if player == 1:
        player = 2

    else:
        player = 1

    if cpu == 1:
        player = 1
    else:
        cpu = 1



print("Game is over.")
