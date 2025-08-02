#!/usr/bin/env python3
# File: test_simple_calculator.py

# Import the built-in unittest module for creating tests.
import unittest
# Import our SimpleCalculator class from the file simple_calculator.py.
from simple_calculator import SimpleCalculator

# We create a new class that will contain our tests.
# It must inherit from unittest.TestCase.
class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """
        Set up the SimpleCalculator instance before each test method runs.
        This is a best practice to ensure each test starts with a fresh object.
        """
        self.calc = SimpleCalculator()

    # --- Test methods for the 'add' function ---
    def test_addition(self):
        """
        Tests the add method with various inputs.
        """
        # Test with positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 20), 30)

        # Test with negative numbers
        self.assertEqual(self.calc.add(-5, -5), -10)
        self.assertEqual(self.calc.add(-10, 5), -5)

        # Test with zero
        self.assertEqual(self.calc.add(0, 7), 7)
        self.assertEqual(self.calc.add(7, 0), 7)

        # Test with floating-point numbers
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)

    # --- Test methods for the 'subtract' function ---
    def test_subtraction(self):
        """
        Tests the subtract method with various inputs.
        """
        # Test with positive numbers
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(20, 10), 10)

        # Test with negative numbers
        self.assertEqual(self.calc.subtract(-5, -2), -3)
        self.assertEqual(self.calc.subtract(5, -2), 7)

        # Test with zero
        self.assertEqual(self.calc.subtract(10, 0), 10)
        self.assertEqual(self.calc.subtract(0, 5), -5)

        # Test with floating-point numbers
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)

    # --- Test methods for the 'multiply' function ---
    def test_multiplication(self):
        """
        Tests the multiply method with various inputs.
        """
        # Test with positive numbers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(5, 10), 50)

        # Test with negative numbers
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertEqual(self.calc.multiply(-3, -4), 12)

        # Test with zero
        self.assertEqual(self.calc.multiply(10, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)

        # Test with floating-point numbers
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)

    # --- Test methods for the 'divide' function ---
    def test_division(self):
        """
        Tests the divide method, including the edge case of division by zero.
        """
        # Test with normal division
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(10, 4), 2.5)

        # Test with negative numbers
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -5), -2)

        # Test with floating-point numbers
        self.assertEqual(self.calc.divide(5, 2), 2.5)

        # Test the edge case of division by zero.
        # The SimpleCalculator class is designed to return None for this case.
        self.assertIsNone(self.calc.divide(10, 0))

# The code inside this block will run when you execute the script from the command line.
if __name__ == "__main__":
    unittest.main()