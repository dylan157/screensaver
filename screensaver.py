from random import randint
import time
from sys import platform
import os

#HELLO J

if platform == "linux" or platform == "linux2":
    clear = lambda: os.system('clear')
elif platform == "darwin":
    clear = lambda: os.system('clear')
elif platform == "win32":
    clear = lambda: os.system('cls')

#config variables. CHANGE US!
map_xy = 40 #40 max
trail_len = 0
trail_text = "#"
trail_speed = 0.001
trail_random = 20

#boring variables 
screen = []
blank_icon = " "
player_zero= [int(map_xy*0.5) , int(map_xy*0.5), ""]#left
player_list = [player_zero, [player_zero[0], player_zero[1]+2, ""], [player_zero[0]-1, player_zero[1]+1, ""], [player_zero[0]+1, player_zero[1]+1, ""]]
temp_player_list = []
move = []
trail_history = []
count = 0


for click in range(map_xy):
    screen.append([blank_icon] * map_xy)

def print_board(board):
    for row in board:
        for x in range(1):
            print " ".join(row)
print_board(screen)

def player_moves():
    global move # move generator
    move = []
    move.append(randint(0, 2))
    if move[0] != 1:
        move.append(randint(0, 2))
    else:
        move.append(randint(0, 1))
    return move
player_moves()

def board_transport(move_choice, who):
    #Player xy_location changer based on player_move() output and move logic (if xy != off-map or trail)
    global safety
    global blank_icon
    safety += 1
    if safety > 10:
        all = [randint(0, len(screen)-1), randint(0, len(screen)-1)]
        for PLAYER in player_list:
            PLAYER = all
    if move_choice[0] == 0:
        if move_choice[1] == 0 and (who[0] - 1 >= 0) and (who[1] - 1 >= 0):
            if screen[(who[0] - 1)][(who[1] - 1)] not in (trail_text):
                who[0] -= 1
                who[1] -= 1
            else:
                who[2] = "err"
        elif move_choice[1] == 1 and (who[0] - 1 >= 0):
            if screen[(who[0] - 1)][(who[1])] not in (trail_text):
                who[0] -= 1
            else:
                who[2] = "err"
        elif move_choice[1] == 2 and (who[0] - 1 >= 0) and (who[1] + 1 <= len(screen)-1):
            if screen[(who[0] - 1)][(who[1] + 1)] not in (trail_text):
                who[0] -= 1
                who[1] += 1
            else:
                who[2] = "err"
        else:
            who[2] = "err"

    elif move_choice[0] == 1:
        if move_choice[1] == 0 and (who[1] - 1 >= 0):
            if screen[(who[0])][(who[1] - 1)] not in (trail_text):
                who[1] -= 1
            else:
                who[2] = "err"
        elif move_choice[1] == 1 and (who[1] + 1 <= len(screen)-1):
            if screen[(who[0])][(who[1] + 1)] not in (trail_text):
                who[1] += 1
            else:
                who[2] = "err"
        else:
            who[2] = "err"

    elif move_choice[0] == 2:
        if move_choice[1] == 0 and (who[0] + 1 <= len(screen)-1) and (who[1] - 1 >= 0):
            if screen[(who[0] + 1)][(who[1] - 1)] not in (trail_text):
                who[0] += 1
                who[1] -= 1
            else:
                who[2] = "err"
        elif move_choice[1] == 1 and (who[0] + 1 <= len(screen)-1):
            if screen[(who[0] + 1)][(who[1])] not in (trail_text):
                who[0] += 1
            else:
                who[2] = "err"
        elif move_choice[1] == 2 and (who[0] + 1 <= len(screen)-1) and (who[1] + 1 <= len(screen)-1):
            if screen[(who[0] + 1)][(who[1] + 1)] not in (trail_text):
                who[0] += 1
                who[1] += 1
            else:
                who[2] = "err"
        else:
            who[2] = "err"

def draw():
    global count
    clear()
    chance, win = randint(0, trail_random), randint(0, trail_random)
    if chance == win: player_moves()
    for PLAYER in player_list:
        screen[PLAYER[0]][PLAYER[1]] = trail_text[count%len(trail_text)-1] # modulo <3
        trail_history.append(PLAYER[:])

    print_board(screen)
    for g in trail_history[:]:
        screen[g[0]][g[1]] = blank_icon
    for g in trail_history[:]:
        del(trail_history[0])




    time.sleep(trail_speed)
    count += 1
print "You can change trail text, trail length and map size by editing Config variables!"
time.sleep(2)
while True:
    safety = 0
    mover = True
    while mover:
        temp_player_list = []
        for player in player_list:
            temp_player_list.append(player[:])
        
        fail = False
        if move == None:
            board_transport(player_moves(), player_zero)
        else:
            for PLAYER in temp_player_list:
                board_transport(move, PLAYER)
        for players in temp_player_list:
            if players[2] != "":
                     fail = True
        if not fail:
            for indx in range(len(temp_player_list)):
                player_list[indx] = temp_player_list[indx]
            mover = False
        else:
            player_moves()


                


    draw()
    if count % 1000 == 0 and trail_speed != 0.157:
        trail_speed = float(raw_input("enter"))

    

