'''Week 06 Team Assignment'''

'''
This program demonstrates inheritance to define a circle
that inherits from a point.
IS-A
'''


class Point:
    """
    A Point has an x and y coordinate.
    """

    def __init__(self):
        self.x = 0.00
        self.y = 0.00

    def prompt_for_point(self):
        self.x = float(input('Enter x: '))
        self.y = float(input('Enter y: '))

    def display(self):
        print(f'({self.x}, {self.y})')


class Circle(Point):
    """
    A Circle has an x and y, plus a radius.
    """

    def __init__(self):
        super().__init__()
        self.radius = 0.00

    def prompt_for_circle(self):
        self.prompt_for_point()  # call the point method
        self.radius = float(input('Enter radius: '))

    def display(self):
        print('Center:')
        Point.display(self)  # super().display() # call the point method
        print(f'Radius: {self.radius}')


def main():
    circle = Circle()
    circle.prompt_for_circle()
    print()
    circle.display()


if __name__ == '__main__':
    main()
