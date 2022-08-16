"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    global NUM_LIVES
    graphics = BreakoutGraphics()

    # Add the animation loop here!
    graphics.reset_ball()

    while True:
        if graphics.drop:
            graphics.move_ball()
            graphics.remove_brick()
            graphics.handle_wall_collisions()
            if graphics.ball.y > graphics.window.height - graphics.ball.height:
                NUM_LIVES -= 1
                if NUM_LIVES > 0:
                    graphics.drop = False
                    graphics.reset_ball()
                else:
                    graphics.reset_ball()
                    break
            if graphics.brick is None:
                graphics.reset_ball()
                break
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
