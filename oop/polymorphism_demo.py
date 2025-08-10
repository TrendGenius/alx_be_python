# polymorphism_demo.py
# This file defines classes to demonstrate polymorphism and method overriding.

import math # We need this to use math.pi for circle area calculation

# --- Base Class: Shape ---
# This is our general blueprint for any shape.
# It defines an 'area' method that subclasses MUST override.
class Shape:
    """
    Base class for geometric shapes.
    It includes an 'area' method that must be implemented by derived classes.
    """
    def area(self):
        """
        Placeholder method for calculating the area of a shape.
        Raises NotImplementedError to ensure derived classes override it.
        """
        raise NotImplementedError("Subclass must implement abstract method 'area'")

# --- Derived Class (Inheritance & Overriding): Rectangle ---
# Rectangle is a 'Shape' and will provide its own way to calculate 'area'.
class Rectangle(Shape):
    """
    Represents a rectangle, inheriting from Shape.
    Overrides the 'area' method to calculate the rectangle's area.
    """
    def __init__(self, length, width):
        """
        Initializes a new Rectangle instance.

        Args:
            length (float or int): The length of the rectangle.
            width (float or int): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Calculates and returns the area of the rectangle (length * width).
        This method *overrides* the area method from the Shape base class.
        """
        return self.length * self.width

# --- Derived Class (Inheritance & Overriding): Circle ---
# Circle is also a 'Shape' and will provide its own way to calculate 'area'.
class Circle(Shape):
    """
    Represents a circle, inheriting from Shape.
    Overrides the 'area' method to calculate the circle's area.
    """
    def __init__(self, radius):
        """
        Initializes a new Circle instance.

        Args:
            radius (float or int): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle (pi * radius^2).
        This method *overrides* the area method from the Shape base class.
        """
        return math.pi * (self.radius ** 2)

