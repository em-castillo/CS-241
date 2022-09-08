'''Week 07 Checkpoint A - Polymorphism'''
"""
File: check07a.py

Starting template for your checkpoint assignment.
"""

# TODO: Create a base car class here


class Car:
    def __init__(self):
        self.name = 'Unknown model'

    def get_door_specs(self):
        return 'Unknown doors'


# TODO: Create a civic class here (individual name and specs)
class Civic(Car):
    # new variable name in constructor
    def __init__(self):
        self.name = 'Civic'

    # override get_door_specs() from Car class
    def get_door_specs(self):
        return '4 doors'


# TODO: Create an odyssey class here (individual name and specs)
class Odyssey(Car):
    def __init__(self):
        self.name = 'Odyssey'

    def get_door_specs(self):
        return '2 front doors, 2 sliding doors, 1 tail gate'


# TODO: Create a Ferrari class here  (individual name and specs)
class Ferrari(Car):
    def __init__(self):
        self.name = 'Ferrari'

    def get_door_specs(self):
        return '2 butterfly doors'


# TODO: Create your attach_doors function here
# It should accept any type of car and use its
# name and get_door_specs function to print out
# the necessary data.
# It should not be a member function of any class,
# but rather just a "regular" function.
def attach_doors(car):
    print(f'Attaching doors to {car.name} - {car.get_door_specs()}')


def main():
    # creating cars
    car1 = Civic()
    car2 = Odyssey()
    car3 = Ferrari()

    # prints cars info
    attach_doors(car1)
    attach_doors(car2)
    attach_doors(car3)


if __name__ == "__main__":
    main()

# reading: 15min
# assignment a: 2 hours
