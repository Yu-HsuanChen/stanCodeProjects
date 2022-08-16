"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2, y=self.window.height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        self.drop = False

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.ball_start)

        # Draw bricks
        x = 0
        y = BRICK_OFFSET
        for i in range(brick_cols):
            self.brick = GRect(brick_width, brick_height)
            self.brick.filled = True
            if i < 2:
                self.brick.fill_color = 'red'
                self.brick.color = 'red'
            elif i < 4:
                self.brick.fill_color = 'orange'
                self.brick.color = 'orange'
            elif i < 6:
                self.brick.fill_color = 'yellow'
                self.brick.color = 'yellow'
            elif i < 8:
                self.brick.fill_color = 'green'
                self.brick.color = 'green'
            elif i < 10:
                self.brick.fill_color = 'blue'
                self.brick.color = 'blue'
            self.window.add(self.brick, x=x, y=y)
            for j in range(brick_rows):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if i < 2:
                    self.brick.fill_color = 'red'
                    self.brick.color = 'red'
                elif i < 4:
                    self.brick.fill_color = 'orange'
                    self.brick.color = 'orange'
                elif i < 6:
                    self.brick.fill_color = 'yellow'
                    self.brick.color = 'yellow'
                elif i < 8:
                    self.brick.fill_color = 'green'
                    self.brick.color = 'green'
                elif i < 10:
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'blue'
                x += brick_width + brick_spacing
                self.window.add(self.brick, x=x, y=y)
            y += brick_height + brick_spacing
            x = 0

    def paddle_move(self, mouse):
        if mouse.x < (0+self.paddle.width):
            self.paddle.x = 0
        elif mouse.x > (self.window.width-self.paddle.width):
            self.paddle.x = self.window.width-self.paddle.width
        else:
            self.paddle.x = mouse.x - self.paddle.width/2

    def set_ball_position(self):
        self.ball.x = (self.window.width-self.ball.width)/2
        self.ball.y = (self.window.height-self.ball.height)/2

    def set_ball_velocity(self):
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def handle_wall_collisions(self):
        if self.ball.x <= 0 or self.ball.x >= self.window.width-self.ball.width:
            self.__dx = -self.__dx
        if self.ball.y <= 0 or self.ball.y >= self.window.height-self.ball.height:
            self.__dy = -self.__dy

    def reset_ball(self):
        self.set_ball_position()
        self.set_ball_velocity()

    def move_ball(self):
        self.ball.move(self.__dx, self.__dy)

    def ball_start(self, mouse):
        self.drop = True

    def remove_brick(self):
        obj = self.window.get_object_at(self.ball.x, self.ball.y)
        obj1 = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y)
        obj2 = self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height)
        obj3 = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.height)
        if obj is self.paddle:
            self.__dy = -self.__dy
        elif obj1 is self.paddle:
            self.__dy = -self.__dy
        elif obj2 is self.paddle:
            self.__dy = -self.__dy
        elif obj3 is self.paddle:
            self.__dy = -self.__dy
        elif obj is not None and obj is not self.paddle:
            self.window.remove(obj)
            self.__dy = -self.__dy
        elif obj1 is not None and obj1 is not self.paddle:
            self.window.remove(obj)
            self.__dy = -self.__dy
        elif obj2 is not None and obj2 is not self.paddle:
            self.window.remove(obj)
            self.__dy = -self.__dy
        elif obj3 is not None and obj3 is not self.paddle:
            self.window.remove(obj)
            self.__dy = -self.__dy
