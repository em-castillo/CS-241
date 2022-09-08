'''Week 06 - 07 Skeet Project'''
"""
File: skeet.py
Original Author: Br. Burton
Designed to be completed by others

This program implements an awesome version of skeet.
"""

# These are Global constants to use throughout the game


from abc import abstractmethod
import arcade
import math
import random
from arcade.color import BLACK, BLUE_BELL
from arcade.sprite_list.spatial_hash import check_for_collision
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

RIFLE_WIDTH = 100
RIFLE_HEIGHT = 20
RIFLE_COLOR = arcade.color.DARK_RED

BULLET_RADIUS = 3
BULLET_COLOR = arcade.color.BLACK_OLIVE
BULLET_SPEED = 10

TARGET_RADIUS = 20
TARGET_COLOR = arcade.color.CARROT_ORANGE
TARGET_SAFE_COLOR = arcade.color.AIR_FORCE_BLUE
TARGET_SAFE_HEIGHT = 20
TARGET_SAFE_WIDTH = 20


class Point:
    ''' Saves the location'''

    def __init__(self):
        self.x = 0.00  # float
        self.y = 0.00


class Velocity:
    ''' Saves the velocity of obsjects'''

    def __init__(self):
        self.dx = 0.00
        self.dy = 0.00


class FlyingObject:
    def __init__(self):
        '''This is a general flying object. Bullet or target'''
        self.center = Point()
        self.velocity = Velocity()
        self.radius = 0.00
        self.alive = True  # boolean
        self.color = None

    def draw(self):
        '''Draws a circle'''
        arcade.draw_circle_outline(
            self.center.x, self.center.y, self.radius, self.color)

    def advance(self):
        '''Changes the x and y position of the ball'''
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def is_off_screen(self, width, height):
        '''Verifies if flying object is off the screen'''
        if self.center.x > width or self.center.x < 0 or self.center.y > height or self.center.y < 0:
            return True
        else:
            return False


class Bullet(FlyingObject):
    '''Bullet class that inherits from FlyingObject'''

    def __init__(self):
        super().__init__()
        self.radius = BULLET_RADIUS
        self.color = BULLET_COLOR
        self.angle = 45
        # self.time = 0

    def draw(self):
        '''Draws the bullet'''
        arcade.draw_circle_filled(
            self.center.x, self.center.y, self.radius, self.color)

    # note: It doesn't need advance() because is already on FlyingObject class

    def fire(self, angle):
        '''Fires the bullet'''
        # Calculates velocity in x and y directions
        self.velocity.dx = math.cos(math.radians(angle)) * BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(angle)) * BULLET_SPEED
        # Makes bullet to be on top of the canon
        self.center.x = RIFLE_WIDTH * math.cos(math.radians(angle))
        self.center.y = RIFLE_WIDTH * math.sin(math.radians(angle))

    # note: It doesn't need is_off_screen() because is already on FlyingObject class


class Target(FlyingObject):
    '''Target class that inherits from FlyingObject - Standard target'''

    def __init__(self):
        super().__init__()
        self.center.x = random.uniform(SCREEN_WIDTH/10, SCREEN_HEIGHT)
        self.center.y = random.uniform(SCREEN_WIDTH/2, SCREEN_HEIGHT)
        self.velocity.dx = random.uniform(1, 5)
        self.velocity.dy = random.uniform(-2, 5)
        self.color = TARGET_COLOR
        self.radius = TARGET_RADIUS
        self.score = 0

    def draw(self):
        '''Draws a filled circle'''
        arcade.draw_circle_filled(
            self.center.x, self.center.y, self.radius, self.color)

    @abstractmethod
    def hit(self):
        '''Determines if target gets hit and its respective score. Plays sounds if gets hit.'''
        # Wins one point
        self.point = arcade.sound.load_sound("skeet_game/point.wav")
        arcade.sound.play_sound(self.point)
        # If target gets hit dies and point its earned
        self.score = 1
        self.alive = False
        return self.score


class StrongTarget(Target):
    '''Target class that inherits from Target - Strong target'''

    def __init__(self):
        super().__init__()
        self.velocity.dx = random.uniform(1, 3)
        self.velocity.dy = random.uniform(-2, 3)
        self.count = 0

    def draw(self):
        '''Draws a outline circle'''
        arcade.draw_circle_outline(
            self.center.x, self.center.y, self.radius, self.color)
        arcade.draw_text('3', start_x=self.center.x-5, start_y=self.center.y-5,
                         font_size=12, color=self.color)

    def hit(self):
        '''Determines if target gets hit and its respective score. Plays sounds if gets hit.'''
        # Wins stronger ponits
        self.extrapoints = arcade.sound.load_sound(
            "skeet_game/extrapoints.wav")
        arcade.sound.play_sound(self.extrapoints)
        # If target gets hit once or twice, one point its earned
        self.count += 1
        if self.count == 1 or self.count == 2:
            self.score = 1
            self.alive = True

        # If target gets hit dies and five points are earned
        elif self.count == 3:
            self.score = 5
            self.alive = False

        return self.score


class SafeTarget(Target):
    '''Target class that inherits from Target - Safe target'''

    def __init__(self):
        super().__init__()
        self.color = TARGET_SAFE_COLOR

    def draw(self):
        '''Draws a aquare'''
        arcade.draw_rectangle_filled(
            self.center.x, self.center.y, TARGET_SAFE_WIDTH, TARGET_SAFE_HEIGHT, self.color)

    def hit(self):
        '''Determines if target gets hit and its respective score. Plays sounds if gets hit.'''
        # Looses -10 points
        self.lost = arcade.sound.load_sound("skeet_game/lost.wav")
        arcade.sound.play_sound(self.lost)
        # If target gets hit dies and point its earned
        self.score = -10
        return self.score


class Rifle:
    """
    The rifle is a rectangle that tracks the mouse.
    """

    def __init__(self):
        self.center = Point()
        self.center.x = 0
        self.center.y = 0
        self.radius = 10
        self.angle = 45

    def draw(self):
        '''Draws rectangle as rifle'''
        arcade.draw_rectangle_filled(
            self.center.x, self.center.y, RIFLE_WIDTH, RIFLE_HEIGHT, RIFLE_COLOR, 360 - self.angle)


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Rifle
        Target (and it's sub-classes)
        Point
        Velocity
        Bullet

    This class will then call the appropriate functions of
    each of the above classes.

    You are welcome to modify anything in this class, but mostly
    you shouldn't have to. There are a few sections that you
    must add code to.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)

        self.rifle = Rifle()
        self.score = 0

        self.bullets = []  # list of bullet classes

        # TODO: Create a list for your targets (similar to the above bullets)
        self.targets = []  # list of target classes

        # loading background image
        self.background = arcade.load_texture('skeet_game/sky.jpeg')
        # arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # drawing background image
        arcade.draw_texture_rectangle(
            300, 250, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        # draw each object
        self.rifle.draw()

        for bullet in self.bullets:
            bullet.draw()

        # TODO: iterate through your targets and draw them...
        for target in self.targets:
            target.draw()

        self.draw_score()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y,
                         font_size=12, color=arcade.color.BLUE_SAPPHIRE)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_collisions()
        self.check_off_screen()

        # decide if we should start a target
        if random.randint(1, 50) == 1:
            self.create_target()

        for bullet in self.bullets:
            bullet.advance()

        # TODO: Iterate through your targets and tell them to advance
        for target in self.targets:
            target.advance()

    def create_target(self):
        """
        Creates a new target of a random type and adds it to the list.
        :return:
        """

        # TODO: Decide what type of target to create and append it to the list

        # creates library
        target_library = [Target(), StrongTarget(), SafeTarget()]
        # chooses target randomly
        choose_target = random.choice(target_library)
        # appends to the list
        self.targets.append(choose_target)

    def check_collisions(self):
        """
        Checks to see if bullets have hit targets.
        Updates scores and removes dead items.
        :return:
        """

        # NOTE: This assumes you named your targets list "targets"

        for bullet in self.bullets:
            for target in self.targets:

                # Make sure they are both alive before checking for a collision
                if bullet.alive and target.alive:
                    too_close = bullet.radius + target.radius

                    if (abs(bullet.center.x - target.center.x) < too_close and
                            abs(bullet.center.y - target.center.y) < too_close):
                        # its a hit!
                        bullet.alive = False
                        target.alive = False
                        self.score += target.hit()

                        # We will wait to remove the dead objects until after we
                        # finish going through the list

        # Now, check for anything that is dead, and remove it
        self.cleanup_zombies()

    def cleanup_zombies(self):
        """
        Removes any dead bullets or targets from the list.
        :return:
        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for target in self.targets:
            if not target.alive:
                self.targets.remove(target)

        # for strong_target in self.strong_targets:
        #     if not strong_target.alive:
        #         self.strong_targets.remove(strong_target)

        # for safe_target in self.safe_targets:
        #     if not safe_target.alive:
        #         self.safe_targets.remove(safe_target)

    def check_off_screen(self):
        """
        Checks to see if bullets or targets have left the screen
        and if so, removes them from their lists.
        :return:
        """
        for bullet in self.bullets:
            if bullet.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.bullets.remove(bullet)

        for target in self.targets:
            if target.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.targets.remove(target)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        # set the rifle angle in degrees
        self.rifle.angle = self._get_angle_degrees(x, y)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # Fire!
        angle = self._get_angle_degrees(x, y)

        bullet = Bullet()
        bullet.fire(angle)

        self.bullets.append(bullet)

    def _get_angle_degrees(self, x, y):
        """
        Gets the value of an angle (in degrees) defined
        by the provided x and y.

        Note: This could be a static method, but we haven't
        discussed them yet...
        """
        # get the angle in radians
        angle_radians = math.atan2(y, x)

        # convert to degrees
        angle_degrees = math.degrees(angle_radians)

        return angle_degrees


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
