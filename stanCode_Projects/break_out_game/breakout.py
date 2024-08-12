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

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 20         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    while True:
        pause(FRAME_RATE)
        if graphics.ball_dropped():
            lives -= 1
            if lives > 0:
                graphics.reset_ball()
            else:
                break
        graphics.ball_move()

        graphics.bouncing_ball()
        graphics.collision_check()
    # Add the animation loop here!


if __name__ == '__main__':
    main()
