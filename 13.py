import curses
import time

from intcode import intcode_v3

with open('../13.txt') as f:
    i = [int(x) for x in f.read().split(',')]

arcade = intcode_v3(i)
count = 0
try:
    while True:
        next(arcade)
        next(arcade)
        t = next(arcade)
        if t == 2:
            count += 1
except StopIteration:
    pass
print(count)

i[0] = 2
arcade = intcode_v3(i)

score = 0

paddle_x = None
paddle_y = None
ball_x = None
ball_y = None
old_ball_x = None
old_ball_y = None

stdscr = curses.initscr()
old_cursor = curses.curs_set(False)

def update(x, y, t):
    global score
    global paddle_x
    global paddle_y
    global ball_x
    global ball_y
    global old_ball_x
    global old_ball_y
    if x == -1 and y == 0:
        score = t
        stdscr.addstr(0, 0, str(score))
    elif t == 0:
        stdscr.addstr(y+1, x, ' ') #empty
    elif t == 1:
        stdscr.addstr(y+1, x, '|') #wall
    elif t == 2:
        stdscr.addstr(y+1, x, 'X') #block
    elif t== 3:
        stdscr.addstr(y+1, x, 'T') #paddle
        paddle_x = x
        paddle_y = y
    elif t == 4:
        stdscr.addstr(y+1, x, 'o') #ball
        old_ball_x = ball_x
        old_ball_y = ball_y
        ball_x = x
        ball_y = y
    else:
        raise ValueError
    stdscr.refresh()

try:
    while True:
        x = next(arcade)
        if x is None:
            if old_ball_x is None:
                old_ball_x = ball_x - 1
                old_ball_y = ball_y - 1
            motion_x = ball_x - old_ball_x
            motion_y = ball_y - old_ball_y
            if motion_y > 0:
                steps = paddle_y - ball_y - 1
                target = ball_x + steps * motion_x
                #if steps == 0 and target == paddle_x and random.:
                    #target += motion_x
            else:
                target = ball_x
            if target > paddle_x:
                stick = 1
            elif target < paddle_x:
                stick = -1
            else:
                stick = 0
            #stick = int(input())
            time.sleep(0.05)
            x = arcade.send(stick)
        y = next(arcade)
        t = next(arcade)
        update(x, y, t)
except StopIteration:
    pass
curses.curs_set(old_cursor)
curses.endwin()
print(score)
