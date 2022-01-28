import random
import os
# Ask the players to insert their names and assign them to a list
def playernames():
    names = []
    player1 = input("Player 1 please enter your name:")
    names.append(player1)
    player2 = input("Player 2 please enter your name:")
    names.append(player2)
    return names

def startingplayer(names):
    active_dict = dict()
    active_player = random.choice(names)
    print(f"{active_player} you randomly got selected to be the starting player. You play with the X token. Your opponent gets the O token")
    for item in names:
        if item == active_player:
            active_dict[item] = "X"
        else:
            active_dict[item] = "O"
    return active_player, active_dict

def change_active(names, player, dict):
    if names.index(player) == 0:
        player = names[1]
        token = dict[str(player)]
    else:
        player = names[0]
        token = dict[str(player)]
    return token, player

def win_cond():
    if row1[0] == row1[1] == row1[2] or row2[0] == row2[1] == row2[2] or row3[0] == row3[1] == row3[2]:
        print(f"{active_player} has won, congratz!")
    elif row1[0] == row2[0] == row3[0] or row1[1] == row2[1] == row3[1] or row1[2] == row2[2] == row3[2]:
        print(f"{active_player} has won, congratz!")
    elif row1[0] == row2[1] == row3[2] or row1[2] == row2[1] == row3[0]:
        print(f"{active_player} has won, congratz!")
    else:
        return False

def draw_cond(counter):
    if counter == 9:
        print("It's a draw - no one won.")
    else:
        return

def valid_input(x):
    if x not in validation_list:
        x = input("Your input is invalid. Please type in the number of an empty field:")
        valid_input(x)
    else:    
        validation_list.remove(x)
    return x, validation_list

def set_token(x, token):
    x = int(x)
    if x > 0 and x < 4:
        row1.pop(x-1)
        row1.insert(x-1,[f"{token}"])
    elif x > 3 and x < 7:
        row2.pop(x-4)
        row2.insert(x-4, [f"{token}"])
    elif x > 6 and x < 10:
        row3.pop(x-7)
        row3.insert(x-7, [f"{token}"])
    return row1, row2, row3

def restart(another):
    if another in ['Yes', 'YES', 'yes', 'YEs', 'yeS', 'YeS']:
        return 1
    elif another in ['no', 'No', 'NO', 'nO']:
        print("The game ends here!")
        clear_console()
        return 0
    else:
        another = input("The input was invalid. Please type, 'yes' or 'no': ")
        restart(another)

def clear_console():
    os.system("clear")

while True:

    row1 = [['1'], ['2'], ['3']]
    row2 = [['4'], ['5'], ['6']]
    row3 = [['7'], ['8'], ['9']]
    validation_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    counter = 0
    active_token = "X"
    names = playernames()
    active_player, active_dict = startingplayer(names)
    print('---------------------')
    print(row1)
    print(row2)
    print(row3)
    print('---------------------')
    while counter < 9:
        counter += 1
        choice = input(f"{active_player} please pick your field:")
        choice, validation_list = valid_input(choice)
        row1, row2, row3 = set_token(choice, active_token)
        print('---------------------')
        print(row1)
        print(row2)
        print(row3)
        print('---------------------')
        win = win_cond()
        if win == False:
            pass
        elif win != False:
            break
        active_token, active_player = change_active(names, active_player, active_dict)

        if counter == 9:
            print("It's a draw - no one won.")

    another = input("Do you want to play again? yes/no: ")
    if restart(another) == 1:
        pass
    else:
        break
