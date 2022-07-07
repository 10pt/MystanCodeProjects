"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

Classic pinball game
bricks get crashed when hit by ball.
The goal is to get rid of all bricks.
Players got three lives to lose.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Height of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle_width = paddle_width
        self.window.add(self.paddle, x=(self.window_width - paddle_width) / 2,
                        y=self.window_height - paddle_offset)
        # Center a filled ball in the graphical window
        self.ball_radius = ball_radius
        self.ball = GOval(self.ball_radius * 2, self.ball_radius * 2)
        self.ball.filled = True

        self.__dx = 0
        self.__dy = 0

        self.window.add(self.ball, x=self.window_width / 2 - ball_radius,
                        y=self.window_height / 2 - ball_radius)
        # Default initial velocity for the ball
        self.reset_ball()

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.ball_go)

        self.set_ball_position()
        self.window.add(self.ball)

        # Draw bricks
        brick_start_width = 0
        brick_start_height = brick_offset
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if i % 10 == 0 or i % 10 == 1:
                    self.brick.fill_color = 'red'
                    self.brick.color = 'red'
                if i % 10 == 2 or i % 10 == 3:
                    self.brick.fill_color = 'orange'
                    self.brick.color = 'orange'
                if i % 10 == 4 or i % 10 == 5:
                    self.brick.fill_color = 'yellow'
                    self.brick.color = 'yellow'
                if i % 10 == 6 or i % 10 == 7:
                    self.brick.fill_color = 'green'
                    self.brick.color = 'green'
                if i % 10 == 8 or i % 10 == 9:
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'blue'
                self.window.add(self.brick, brick_start_width, brick_start_height)
                brick_start_width += brick_width
                brick_start_width += brick_spacing
            brick_start_width = 0
            brick_start_height += brick_height
            brick_start_height += brick_spacing

    def ball_go(self, mouse):
        if self.__dx == 0 or self.__dy == 0:
            self.set_ball_velocity()
            self.ball.move(self.__dx, self.__dy)

    def ball_move(self):
        self.ball.move(self.__dx, self.__dy)

    def paddle_move(self, mouse):   # Make paddle move with mouse
        self.paddle.x = mouse.x - self.paddle_width / 2
        if mouse.x < 0:
            self.paddle.x = 0
        elif mouse.x > self.window_width:
            self.paddle.x = self.window_width - self.paddle_width

    def set_ball_velocity(self):    # Make velocity random
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def set_ball_position(self):    # Place ball in the middle
        self.ball.x = self.window_width / 2 - self.ball_radius
        self.ball.y = self.window_height / 2 - self.ball_radius

    def reset_ball(self):
        self.set_ball_position()
        while self.ball_dropped():
            self.set_ball_position()
        self.to_zero()
        self.window.add(self.ball)

    def to_zero(self):
        self.__dx = 0
        self.__dy = 0

    def bouncing_ball(self):      # Make ball bounce when hitting walls
        if self.ball.x <= 0 or self.ball.x + self.ball_radius >= self.window.width:
            self.__dx = - self.__dx
        if self.ball.y <= 0:
            self.__dy = - self.__dy
        if self.ball.y + self.ball_radius >= self.window.height:
            self.reset_ball()

    def ball_dropped(self):     # Detect when ball dropped
        ball_lost = (self.window_height - self.ball_radius * 2) <= self.ball.y <= self.window_height
        return ball_lost

    def collision_check(self):  # Differ different collisions
        switch = 0
        for i in range(0, 2):
            for j in range(0, 2):
                touch = self.window.get_object_at(self.ball.x + i * (self.ball_radius * 2),
                                                  self.ball.y + j * (self.ball_radius * 2))
                if touch is self.paddle:
                    # if touch is self.paddle
                    if self.__dy > 0:   # modify
                        self.__dy = - self.__dy
                if touch is not None and touch is not self.paddle:
                    # if touch is self.brick
                    self.window.remove(touch)
                    self.__dy = - self.__dy
                    switch = 1
                    return


