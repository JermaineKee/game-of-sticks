
# set player to 1
player = 1

# set the initial state
state = 20 #number of sticks
print("The number of sticks is now ",state)
while True:
    # get valid move

    print("Player ",player)
    while True:
        move = input("How many sticks do you want to pick up? ")
        if int(move) < 4:
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



print("Game is over.")
