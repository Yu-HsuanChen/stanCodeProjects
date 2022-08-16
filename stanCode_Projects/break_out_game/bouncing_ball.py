"""
File: bouncing_ball
Name: Joanne Chen
-------------------------
TODO: Make a bouncing ball animation started by clicking the mouse.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
drops = False

window = GWindow(800, 500, title='bouncing_ball.py')


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global drops
    ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
    ball.filled = True
    window.add(ball)
    vy = 0
    # number of running the animation
    times = 0
    onmouseclicked(drop)
    while True:
        if drops:
            vy += GRAVITY
            ball.move(VX, vy)
            # if ball hit the floor
            if ball.y >= window.height:
                vy *= -REDUCE
            # if ball is out of window
            if ball.x >= window.width:
                ball.x = START_X
                ball.y = START_Y
                times += 1
                vy = 0
                drops = False
                if times == 3:
                    break
        # pause need to be at the end of the loop in case of infinite loop
        pause(DELAY)


def drop(mouse):
    global drops
    drops = True


if __name__ == "__main__":
    main()
