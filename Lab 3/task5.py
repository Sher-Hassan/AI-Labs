from abc import ABC, abstractmethod
import math

class Shape():
    
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width

class Square(Shape):

    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2


class Cylinder(Shape):

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    
    def calculate_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

rect = Rectangle(5, 4)
square = Square(6)
circle = Circle(3)
cylinder = Cylinder(2, 10)

print(rect.calculate_area())
print(square.calculate_area())
print(circle.calculate_area())
print(cylinder.calculate_area())