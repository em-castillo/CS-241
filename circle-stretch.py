'''Week 06 Team Assignment stretch challenges'''

'''
Using HAS-A relationship approach.
Point as a member variable called center.Instead of inherit it.
'''


class Point:
    def __init__(self):
        self.x = 0.00
        self.y = 0.00

    def prompt_for_point(self):
        self.x = float(input('Enter x: '))
        self.y = float(input('Enter y: '))

    def display(self):
        print(f'({self.x}, {self.y})')


class Circle:
    def __init__(self):
        self.center = Point()
        self.radius = 0.00

    def prompt_for_circle(self):
        self.center.prompt_for_point()
        self.radius = float(input('Enter radius: '))

    def display(self):
        print('Center:')
        self.center.display()
        print(f'Radius: {self.radius}')


def main():
    circle = Circle()
    circle.prompt_for_circle()
    print()
    circle.display()


if __name__ == '__main__':
    main()
