"""
    Calculate the area of different shapes using OOP

    You have given a Shape class and subclasses Circle  and Square. The parent class (Shape) has a area() method.

    Now, Write a OOP code to calculate the area of each shapes (each subclass must write its own implementation of area() method to calculates its area).

"""

import math


class Shape:
    def area(self):
        raise NotImplementedError("Area method must be implemented by subclasses")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pi * (self.radius ** 2)
        return area


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        area = self.side ** 2
        return area

# Example of polymorphism
shapes = [Circle(5), Square(7), Circle(3)]

for shape in shapes:
    print(f'{shape.area():.2f}')  # Output: 78.53975, 49, 28.27431

