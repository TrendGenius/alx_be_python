# main.py for Task 2

# Import the necessary classes from polymorphism_demo.py
# We also import 'math' because Circle uses math.pi
from polymorphism_demo import Shape, Rectangle, Circle
import math # Make sure math is imported if it's not already in polymorphism_demo.py (it is)

# This is the main function where our test code will run.
def main():
    # Create a list of different shape objects.
    # Even though they are different types (Rectangle, Circle),
    # they are treated polymorphically as 'Shape' objects because they all have an 'area()' method.
    shapes = [
        Rectangle(10, 5), # A Rectangle instance
        Circle(7)         # A Circle instance
    ]

    # Loop through each shape in the list.
    # The 'area()' method will be called, and Python will automatically
    # execute the correct 'area()' method based on the object's actual type.
    for shape in shapes:
        # shape.__class__.__name__ gets the name of the object's class (e.g., 'Rectangle' or 'Circle')
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

# This standard Python line makes sure main() runs when the script is executed.
if __name__ == "__main__":
    main()

