from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    Abstract Base Class for shapes.
    Defines the blueprint for all shape classes by enforcing implementation
    of the `area` and `perimeter` methods in subclasses.
    """

    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the shape.
        Must be implemented by subclasses.
        """
        pass


class Circle(Shape):
    """
    A class representing a circle, inheriting from the Shape abstract base class.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius):
        """
        Initialize a Circle instance with a given radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return round(pi * self.radius ** 2, 2)

    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return round(2 * pi * self.radius, 2)


class Rectangle(Shape):
    """
    A class representing a rectangle, inheriting from the Shape abstract base class.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with a given width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return round(self.width * self.height, 2)

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return round(2 * (self.width + self.height), 2)


def describe_shape(shape):
    """
    Polymorphic function that works with any subclass of Shape.
    Prints the area and perimeter of the given shape.

    Args:
        shape (Shape): An instance of a subclass of Shape.
    """
    # Print the calculated area and perimeter of the shape
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


# Usage example
# Creating a list of different shapes
shapes = [Circle(3), Rectangle(4, 5)]

# Loop through each shape, display its type, and describe it
for shape in shapes:
    # Display the type of the shape (Circle or Rectangle)
    print(f"Shape: {type(shape).__name__}")
    # Call describe_shape to show polymorphic behavior
    describe_shape(shape)
    print()                                 # Print a blank line for better readability
