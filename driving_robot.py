'''Week 03 Prove Assignment'''

'''Class that models robot's actions to move around in an enviroment'''


class Robot():

    # Initialize variables
    def __init__(self):
        self.x_coordinate = 10
        self.y_coordinate = 10
        self.fuel = 100

    # Robot turns left if it has fuel
    def robot_left(self):
        self.checking_fuel()
        self.x_coordinate == self.x_coordinate

        if self.fuel >= 1:
            self.fuel -= 5
            self.x_coordinate -= 1
        return

    # Robot turns right if it has fuel
    def robot_right(self):
        self.checking_fuel()
        self.x_coordinate == self.x_coordinate

        if self.fuel >= 1:
            self.fuel -= 5
            self.x_coordinate += 1
        return

    # Robot moves down if it has fuel
    def robot_down(self):
        self.checking_fuel()
        self.y_coordinate == self.y_coordinate

        if self.fuel >= 1:
            self.fuel -= 5
            self.y_coordinate += 1
        return

    # Robot moves up if it has fuel
    def robot_up(self):
        self.checking_fuel()
        self.y_coordinate == self.y_coordinate

        if self.fuel >= 1:
            self.fuel -= 5
            self.y_coordinate -= 1
        return

    # Display robot's status
    def display_status(self):
        print(f'({self.x_coordinate}, {self.y_coordinate}) - Fuel: {self.fuel}')

    # Firing laser if it has fuel
    def laser(self):
        if self.fuel < 15:
            print('Insufficient fuel to perform action')

        else:
            print('Pew! Pew!')
            self.fuel -= 15

        return

    # Checking for fuel left
    def checking_fuel(self):
        if self.fuel < 1:
            print('Insufficient fuel to perform action')


'''Main function - constructing what is defined in the Robot class according to input'''


def main():

    play_robot = Robot()  # Creating object
    command = ''

    # Calling member functions according to command entered
    while command != 'quit':
        command = input('Enter command: ')
        if command == 'left':
            play_robot.robot_left()
        elif command == 'right':
            play_robot.robot_right()
        elif command == 'down':
            play_robot.robot_down()
        elif command == 'up':
            play_robot.robot_up()
        elif command == 'status':
            play_robot.display_status()
        elif command == 'fire':
            play_robot.laser()
        elif command == 'quit':
            print('Goodbye.')


''' If this is the main program being run, call our main function above'''
if __name__ == "__main__":
    main()
