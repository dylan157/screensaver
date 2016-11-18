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
map_xy = 14
trail_len = 12
trail_text = "HELLO_WORLD_"

#boring variables 
screen = []
blank_icon = " "
player_xy = [0,0]
move = []
trail = []
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

def board_transport(move_choice):
    global player_xy #Player xy_location changer based on player_move() output and move logic (if xy != off-map or trail)
    global safety
    safety += 1
    if safety > 100:
        player_xy = [randint(0, len(screen)-1), randint(0, len(screen)-1)]
    chance = randint(0, map_xy)
    if chance == map_xy: player_moves()
    if move_choice[0] == 0:
        if move_choice[1] == 0 and (player_xy[0] - 1 >= 0) and (player_xy[1] - 1 >= 0):
            if screen[(player_xy[0] - 1)][(player_xy[1] - 1)] not in (trail_text):
                player_xy[0] -= 1
                player_xy[1] -= 1
            else:
                board_transport(player_moves())
        elif move_choice[1] == 1 and (player_xy[0] - 1 >= 0):
            if screen[(player_xy[0] - 1)][(player_xy[1])] not in (trail_text):
                player_xy[0] -= 1
            else:
                board_transport(player_moves())
        elif move_choice[1] == 2 and (player_xy[0] - 1 >= 0) and (player_xy[1] + 1 <= len(screen)-1):
            if screen[(player_xy[0] - 1)][(player_xy[1] + 1)] not in (trail_text):
                player_xy[0] -= 1
                player_xy[1] += 1
            else:
                board_transport(player_moves())
        else:
            board_transport(player_moves())

    elif move_choice[0] == 1:
        if move_choice[1] == 0 and (player_xy[1] - 1 >= 0):
            if screen[(player_xy[0])][(player_xy[1] - 1)] not in (trail_text):
                player_xy[1] -= 1
            else:
                board_transport(player_moves())
        elif move_choice[1] == 1 and (player_xy[1] + 1 <= len(screen)-1):
            if screen[(player_xy[0])][(player_xy[1] + 1)] not in (trail_text):
                player_xy[1] += 1
            else:
                board_transport(player_moves())
        else:
            board_transport(player_moves())

    elif move_choice[0] == 2:
        if move_choice[1] == 0 and (player_xy[0] + 1 <= len(screen)-1) and (player_xy[1] - 1 >= 0):
            if screen[(player_xy[0] + 1)][(player_xy[1] - 1)] not in (trail_text):
                player_xy[0] += 1
                player_xy[1] -= 1
            else:
                board_transport(player_moves())
        elif move_choice[1] == 1 and (player_xy[0] + 1 <= len(screen)-1):
            if screen[(player_xy[0] + 1)][(player_xy[1])] not in (trail_text):
                player_xy[0] += 1
            else:
                board_transport(player_moves())
        elif move_choice[1] == 2 and (player_xy[0] + 1 <= len(screen)-1) and (player_xy[1] + 1 <= len(screen)-1):
            if screen[(player_xy[0] + 1)][(player_xy[1] + 1)] not in (trail_text):
                player_xy[0] += 1
                player_xy[1] += 1
            else:
                board_transport(player_moves())
        else:
            board_transport(player_moves())

def draw():
    global count
    clear()
    screen[player_xy[0]][player_xy[1]] = trail_text[count%len(trail_text)-1]
    print_board(screen)
    trail.append(player_xy[:])
    if len(trail) > trail_len:
        screen[trail[0][0]][trail[0][1]] = blank_icon
        del(trail[0])
    time.sleep(0.066666666)
    count += 1
print "You can change trail text, trail length and map size by editing Config variables!"
time.sleep(2)
while True:
    safety = 0
    if move == None:
        board_transport(player_moves())
    else:
        board_transport(move)
    draw()

    

