"""
W05 Prove Assignment
File: pong.py
Original Author: Br. Burton
Designed to be completed by others
This program implements a simplistic version of the
classic Pong arcade game.
"""
import arcade
import random

# These are Global constants to use throughout the game
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
BALL_RADIUS = 10

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50
MOVE_AMOUNT = 5

SCORE_HIT = 1
SCORE_MISS = 5


class Point:
    ''' Saves the location'''

    def __init__(self):
        self.x = 0.00  # float
        self.y = 0.00


class Velocity:
    ''' Saves the velocity of obsjects'''

    def __init__(self):
        self.dx = 0.00  # float
        self.dy = 0.00


class Ball:
    ''' Saves the information about the ball'''

    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        # point class
        self.center.x = 50
        self.center.y = 50
        # velocity class
        self.velocity.dx = random.uniform(1, 2)
        self.velocity.dy = random.uniform(1, 3)

    def draw(self):
        # draws ball
        arcade.draw_circle_filled(
            self.center.x, self.center.y, BALL_RADIUS, arcade.color.WHITE)

    def advance(self):
        # increasing velocity according to axis
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def bounce_horizontal(self):
        # bouncing ball back horizontally once reached paddle
        self.velocity.dx = self.velocity.dx * -1

    def bounce_vertical(self):
        # bouncing ball back vertically
        self.velocity.dy = self.velocity.dy * -1

    def restart(self):
        # restarts ball location and speed randomly once lost
        self.center.x = random.uniform(0, 50)
        self.center.y = random.uniform(50, 250)
        self.velocity.dx = random.uniform(2, 5)
        self.velocity.dy = random.uniform(2, 5)


class Paddle:
    ''' Saves the information about the paddle'''

    def __init__(self):
        # paddle location
        # paddle height / 2 so it reaches edges of screen
        self.center = Point()
        self.center.x = SCREEN_WIDTH - 20
        self.center.y = PADDLE_HEIGHT / 2

    def draw(self):
        # draws paddle
        arcade.draw_rectangle_filled(
            self.center.x, self.center.y, PADDLE_WIDTH, PADDLE_HEIGHT, arcade.color.BLACK)

    def move_up(self):
        # moving paddle up (using left key) when reaches bottom of screen
        if (self.center.y > (PADDLE_HEIGHT / 2)):
            self.center.y -= MOVE_AMOUNT

    def move_down(self):
        # moving paddle down (using right key) when reaches top of screen
        if (self.center.y < (SCREEN_HEIGHT - PADDLE_HEIGHT/2)):
            self.center.y += MOVE_AMOUNT


class Pong(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Point
        Velocity
        Ball
        Paddle
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class,
    but should not have to if you don't want to.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)

        self.ball = Ball()
        self.paddle = Paddle()
        self.score = 0

        # These are used to see if the user is
        # holding down the arrow keys
        self.holding_left = False
        self.holding_right = False

        # loading background image
        self.background = arcade.load_texture('pong_game/ping-pong.jpeg')

        # background color
        # arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsiblity of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # drawing background image
        arcade.draw_texture_rectangle(
            200, 150, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        # draw each object
        self.ball.draw()
        self.paddle.draw()

        self.draw_score()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y,
                         font_size=12, color=arcade.color.WHITE)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """

        # Move the ball forward one element in time
        self.ball.advance()

        # Check to see if keys are being held, and then
        # take appropriate action
        self.check_keys()

        # check for ball at important places
        self.check_miss()
        self.check_hit()
        self.check_bounce()

    def check_hit(self):
        """
        Checks to see if the ball has hit the paddle
        and if so, calls its bounce method.
        :return:
        """
        too_close_x = (PADDLE_WIDTH / 2) + BALL_RADIUS
        too_close_y = (PADDLE_HEIGHT / 2) + BALL_RADIUS

        if (abs(self.ball.center.x - self.paddle.center.x) < too_close_x and
            abs(self.ball.center.y - self.paddle.center.y) < too_close_y and
                self.ball.velocity.dx > 0):
            # we are too close and moving right, this is a hit!
            self.ball.bounce_horizontal()
            self.score += SCORE_HIT

    def check_miss(self):
        """
        Checks to see if the ball went past the paddle
        and if so, restarts it.
        """
        if self.ball.center.x > SCREEN_WIDTH:
            # We missed!
            self.score -= SCORE_MISS
            self.ball.restart()

    def check_bounce(self):
        """
        Checks to see if the ball has hit the borders
        of the screen and if so, calls its bounce methods.
        """
        if self.ball.center.x < 0 and self.ball.velocity.dx < 0:
            self.ball.bounce_horizontal()

        if self.ball.center.y < 0 and self.ball.velocity.dy < 0:
            self.ball.bounce_vertical()

        if self.ball.center.y > SCREEN_HEIGHT and self.ball.velocity.dy > 0:
            self.ball.bounce_vertical()

    def check_keys(self):
        """
        Checks to see if the user is holding down an
        arrow key, and if so, takes appropriate action.
        """
        if self.holding_left:
            self.paddle.move_down()

        if self.holding_right:
            self.paddle.move_up()

    def on_key_press(self, key, key_modifiers):
        """
        Called when a key is pressed. Sets the state of
        holding an arrow key.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """
        if key == arcade.key.LEFT or key == arcade.key.DOWN:
            self.holding_left = True

        if key == arcade.key.RIGHT or key == arcade.key.UP:
            self.holding_right = True

    def on_key_release(self, key, key_modifiers):
        """
        Called when a key is released. Sets the state of
        the arrow key as being not held anymore.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """
        if key == arcade.key.LEFT or key == arcade.key.DOWN:
            self.holding_left = False

        if key == arcade.key.RIGHT or key == arcade.key.UP:
            self.holding_right = False


# Creates the game and starts it going
window = Pong(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
