'''Week 07 Checkpoint B - Polymorphism'''
"""
File: check07b.py
Author: Br. Burton

Demonstrates abstract base classes.
"""

# TODO: Import anything you need for Abstract Base Classes / methods

# TODO: convert this to an ABC




from abc import ABC
from abc import abstractmethod
class Shape(ABC):
    def __init__(self):
        self.name = ""

    def display(self):
        print("{} - {:.2f}".format(self.name, self.get_area()))

    # TODO: Add an abstractmethod here called get_area
    # all classes that derive from the Shape class must implement the get_area method.
    @abstractmethod  # nothing inside function
    def get_area(self):
        pass


# TODO: Create a Circle class here that derives from Shape
class Circle(Shape):
    def __init__(self):
        super().__init__()  # super() adds to parent function
        self.name = 'Circle'
        self.radius = 0.0

    def get_area(self):
        # calculating area
        self.area = 3.14 * self.radius * self.radius
        return self.area


# TODO: Create a Rectangle class here that derives from Shape
class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        self.name = 'Rectangle'
        self.length = 0.0
        self.width = 0.0

    def get_area(self):
        # calculating area
        self.area = self.length * self.width
        return self.area


def main():

    # TODO: Declare your list of shapes here
    shapes = []

    command = ""

    while command != "q":
        command = input(
            "Please enter 'c' for circle, 'r' for rectangle or 'q' to quit: ")

        if command == "c":
            # TODO: Declare your Circle here, set its radius, and
            # add it to the list
            circle = Circle()
            circle.radius = float(input("Enter the radius: "))
            shapes.append(circle)

        elif command == "r":
            # TODO: Declare your Rectangle here, set its length
            # and width, and add it to the list
            rect = Rectangle()
            rect.length = float(input("Enter the length: "))
            rect.width = float(input("Enter the width: "))
            shapes.append(rect)

    # Done entering shapes, now lets print them all out:

    # TODO: Loop through each shape in the list, and call its display function
    for shape in shapes:
        shape.display()


if __name__ == "__main__":
    main()

# 1h 30 min
