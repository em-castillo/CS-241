'''Week 08-10 Prove'''
"""
File: asteroids.py
Original Author: Br. Burton
Designed to be completed by others
This program implements the asteroids game.
"""

# These are Global constants to use throughout the game

from abc import ABC, abstractmethod
import arcade
import random
import math
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30

INITIAL_ROCK_COUNT = 5

BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2


class Point:
    ''' Saves the location'''

    def __init__(self):
        '''Initialize location axis'''
        self.x = 0.00
        self.y = 0.00


class Velocity:
    ''' Saves the velocity of objects'''

    def __init__(self):
        '''Initializes velocity according to axis'''
        self.dx = 0.00
        self.dy = 0.00


class FlyingObject(ABC):
    '''This is a general flying object. Bullets, asteroids, ship.'''

    def __init__(self, img):
        '''Initializes Flying Object characteristics'''
        self.center = Point()
        self.velocity = Velocity()
        self.radius = 0.00
        self.angle = 0.00
        self.speed = 0.00
        self.direction = 0.00
        self.alive = True
        self.img = img
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height

    def draw(self):
        '''Draws flying object'''
        arcade.draw_texture_rectangle(
            self.center.x, self.center.y, self.width, self.height, self.texture, self.angle, 255)  # 255 -> img can be seen

    def advance(self):
        '''Moves the flying object'''
        self.wrap()
        #  Changes the x and y position
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def is_alive(self):
        '''Checks is flying object is alive'''
        return self.alive

    def wrap(self):
        '''Return flying object to screen once gone'''
        # X axis
        if self.center.x > SCREEN_WIDTH:
            self.center.x -= SCREEN_WIDTH
        elif self.center.x < 0:
            self.center.x += SCREEN_WIDTH
        # Y axis
        elif self.center.y > SCREEN_HEIGHT:
            self.center.y -= SCREEN_HEIGHT
        elif self.center.y < 0:
            self.center.y += SCREEN_HEIGHT


class Ship(FlyingObject):
    """
    The ship is an object that moves according to keys pressed.
    """

    def __init__(self):
        '''Initializes ship characteristics'''
        super().__init__("asteroids_game/ship.png")
        self.center.x = (SCREEN_WIDTH / 2)
        self.center.y = (SCREEN_HEIGHT / 2)
        self.radius = SHIP_RADIUS
        self.angle = 1

    def left(self):
        '''Turns ship to the left'''
        self.angle += SHIP_TURN_AMOUNT

    def right(self):
        '''Turns ship to the right'''
        self.angle -= SHIP_TURN_AMOUNT

    def thrust(self):
        '''Makes ship move up'''
        self.velocity.dx -= math.sin(math.radians(self.angle)
                                     ) * SHIP_THRUST_AMOUNT
        self.velocity.dy += math.cos(math.radians(self.angle)
                                     ) * SHIP_THRUST_AMOUNT

    def down_thrust(self):
        '''Makes ship move down'''
        self.velocity.dx += math.sin(math.radians(self.angle)
                                     ) * SHIP_THRUST_AMOUNT
        self.velocity.dy -= math.cos(math.radians(self.angle)
                                     ) * SHIP_THRUST_AMOUNT

    def spin(self):
        '''Makes ship spin when is hit'''
        self.angle += 15


class Bullet(FlyingObject):
    '''Bullet class that inherits from FlyingObject'''

    def __init__(self, ship_angle, ship_x, ship_y, velocity_dx, velocity_dy):
        super().__init__("asteroids_game/laser.png")
        self.radius = BULLET_RADIUS
        self.life = BULLET_LIFE
        self.speed = BULLET_SPEED
        self.angle = ship_angle + 90  # rotates fire img
        self.center.x = ship_x
        self.center.y = ship_y
        # initial velocity
        self.velocity.dx = velocity_dx + self.speed
        self.velocity.dy = velocity_dy + self.speed
        # self.time = 0

    def fire(self):
        '''Fires bullets'''
        self.velocity.dx = math.cos(math.radians(self.angle)
                                    ) * self.speed
        self.velocity.dy = math.sin(math.radians(self.angle)
                                    ) * self.speed

    def advance(self):
        '''Checks if bullets moving die'''
        super().advance()
        self.life -= 1
        if (self.life <= 0):
            self.alive = False


class Asteroid(FlyingObject):
    '''Asteroid class that inherits from FlyingObject'''

    def __init__(self, img):
        '''Initializes general asteroid characteristics'''
        super().__init__(img)
        self.radius = 0.00

    @abstractmethod
    def break_apart(self, asteroids):
        '''Determines when asteroid breaks apart into smaller ones.'''
        self.alive = False


class Large_asteroid(Asteroid):
    '''Large asteroid class that inherits from Asteroid '''

    def __init__(self):
        '''Initializes large asteroid characteristics'''
        super().__init__("asteroids_game/large-rock.png")
        self.center.x = random.randint(1, 50)  # starts at the bottom left
        self.center.y = random.randint(1, 150)
        self.direction = random.randint(1, 50)
        self.velocity.dx = math.cos(
            math.radians(self.direction)) * BIG_ROCK_SPEED
        self.velocity.dy = math.sin(
            math.radians(self.direction)) * BIG_ROCK_SPEED
        self.radius = BIG_ROCK_RADIUS
        self.speed = BIG_ROCK_SPEED  # self.speed didn't moved the rocks

    def advance(self):
        '''Makes asteroid spin while moving'''
        super().advance()
        self.angle += BIG_ROCK_SPIN

    def break_apart(self, asteroids):
        '''Determines when large asteroid breaks into smaller asteroids'''
        # medium asteroid one
        med_one = Medium_asteroid()
        med_one.center.x = self.center.x
        med_one.center.y = self.center.y
        med_one.velocity.dy = self.velocity.dy + 2  # goes 2 faster
        med_one.velocity.dx = self.velocity.dx + 2

        # medium asteroid two
        med_two = Medium_asteroid()
        med_two.center.x = self.center.x
        med_two.center.y = self.center.y
        med_two.velocity.dy = self.velocity.dy - 2  # goes 2 slower
        med_one.velocity.dx = self.velocity.dx - 2

        # small asteroid
        small = Small_asteroid()
        small.center.x = self.center.x
        small.center.y = self.center.y
        small.velocity.dy = self.velocity.dy + 5  # goes 5 faster
        small.velocity.dx = self.velocity.dx + 5

        # adds to list
        asteroids.append(med_one)
        asteroids.append(med_two)
        asteroids.append(small)

        # larger asteroid is not alive because it broke apart and play sound
        self.alive = False
        self.break_rock = arcade.sound.load_sound(
            "asteroids_game/break_apart.wav")
        arcade.sound.play_sound(self.break_rock)


class Medium_asteroid(Asteroid):
    '''Medium asteroid class that inherits from Asteroid '''

    def __init__(self):
        '''Initializes medium asteroid characteristics'''
        super().__init__("asteroids_game/medium-rock.png")
        self.radius = MEDIUM_ROCK_RADIUS

    def advance(self):
        '''Makes asteroid spin while moving'''
        super().advance()
        self.angle += MEDIUM_ROCK_SPIN

    def break_apart(self, asteroids):
        '''Determines when medium asteroid breaks into two small asteroids'''
        # small asteroid one
        small_one = Small_asteroid()
        small_one.center.x = self.center.x
        small_one.center.y = self.center.y
        small_one.velocity.dy = self.velocity.dy + 1.5
        small_one.velocity.dx = self.velocity.dx + 1.5

        # small asteroid two
        small_two = Small_asteroid()
        small_two.center.x = self.center.x
        small_two.center.y = self.center.y
        small_two.velocity.dy = self.velocity.dy - 1.5
        small_one.velocity.dx = self.velocity.dx - 1.5

        asteroids.append(small_one)
        asteroids.append(small_two)
        self.alive = False
        self.break_rock = arcade.sound.load_sound(
            "asteroids_game/break_apart.wav")
        arcade.sound.play_sound(self.break_rock)


class Small_asteroid(Asteroid):
    '''Small asteroid class that inherits from Asteroid '''

    def __init__(self):
        '''Initializes small asteroid characteristics'''
        super().__init__("asteroids_game/small-rock.png")
        self.radius = SMALL_ROCK_RADIUS

    def advance(self):
        '''Makes asteroid spin while moving'''
        super().advance()
        self.angle += SMALL_ROCK_SPIN

    def break_apart(self, asteroids):
        '''Determines when an asteroid breaks apart'''
        self.alive = False
        self.break_rock = arcade.sound.load_sound(
            "asteroids_game/break_apart.wav")
        arcade.sound.play_sound(self.break_rock)


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        # arcade.set_background_color(arcade.color.SMOKY_BLACK)
        self.background = arcade.load_texture('asteroids_game/universe.jpeg')

        self.held_keys = set()

        # TODO: declare anything here you need the game class to track

        self.asteroids = []  # this list has all size asteroids

        for i in range(INITIAL_ROCK_COUNT):
            large_asteroid = Large_asteroid()
            self.asteroids.append(large_asteroid)

        self.ship = Ship()
        self.bullets = []

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # drawing background image
        arcade.draw_texture_rectangle(
            400, 300, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        # TODO: draw each object
        for asteroid in self.asteroids:
            asteroid.draw()

        self.ship.draw()

        for bullet in self.bullets:
            bullet.draw()

    def remove_deadObjects(self):
        '''Removes not alive flying objects'''
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for asteroid in self.asteroids:
            if not asteroid.alive:
                self.asteroids.remove(asteroid)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()

        # TODO: Tell everything to advance or move forward one step in time
        # Tells objects to advance

        for asteroid in self.asteroids:
            asteroid.advance()

        for bullet in self.bullets:
            bullet.advance()

        self.remove_deadObjects()

        self.ship.advance()

        # TODO: Check for collisions
        self.check_collisions()

    def game_over(self):
        '''Plays game over song when all asteroids are destroyed'''
        if len(self.asteroids) == 1:
            self.win = arcade.sound.load_sound(
                "asteroids_game/win.wav")
            arcade.sound.play_sound(self.win)
            # print('You won! Game over')

    def check_collisions(self):
        """
        Checks to see if bullets have hit asteroids.
        Removes dead items.
        :return:
        """
        # bullet and asteroid collision
        for bullet in self.bullets:
            for asteroid in self.asteroids:
                if bullet.alive and asteroid.alive:
                    # distance between bullets and astroids.
                    # abs -> absolute value
                    distance_x = abs(asteroid.center.x - bullet.center.x)
                    distance_y = abs(asteroid.center.y - bullet.center.y)
                    max_distance = asteroid.radius + bullet.radius
                    if distance_x < max_distance and distance_y < max_distance:
                        # collision happens
                        # print('Asteroid and bullets collision!')
                        asteroid.break_apart(self.asteroids)
                        bullet.alive = False
                        asteroid.alive = False
                        self.game_over()

        # ship and asteroids collision
        for asteroid in self.asteroids:
            if self.ship.alive and asteroid.alive:
                # distance between bullets and astroids.
                # abs -> absolute value
                distance_x = abs(asteroid.center.x - self.ship.center.x)
                distance_y = abs(asteroid.center.y - self.ship.center.y)
                max_distance = asteroid.radius + self.ship.radius
                if distance_x < max_distance and distance_y < max_distance:
                    # collision happens
                    # print('Asteroid and ship collision!')
                    # self.ship.alive = False
                    self.ship.spin()

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            self.ship.left()

        if arcade.key.RIGHT in self.held_keys:
            self.ship.right()

        if arcade.key.UP in self.held_keys:
            self.ship.thrust()

        if arcade.key.DOWN in self.held_keys:
            self.ship.down_thrust()

        # Machine gun mode...
        # if arcade.key.SPACE in self.held_keys:
        #    pass

    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                # TODO: Fire the bullet here!
                # parameters from bullet class. self.ship from Game init()
                bullet = Bullet(self.ship.angle,
                                self.ship.center.x, self.ship.center.y, self.ship.velocity.dx, self.ship.velocity.dy)
                self.bullets.append(bullet)
                bullet.fire()

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
