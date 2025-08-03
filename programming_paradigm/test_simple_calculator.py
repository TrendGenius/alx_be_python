#!/usr/bin/env python3
"""
Unit tests for the SimpleCalculator class.
"""
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Test cases for the SimpleCalculator class.
    """

    def setUp(self):
        """
        Set up the SimpleCalculator instance before each test method runs.
        This ensures each test starts with a fresh calculator object.
        """
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method with positive, negative, and zero inputs."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(100, -200), -100)
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)

    def test_subtraction(self):
        """Test the subtract method with various inputs."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(10, 10), 0)
        self.assertEqual(self.calc.subtract(100, -50), 150)
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)

    def test_multiplication(self):
        """Test the multiply method with various inputs, including zero."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(10, 0), 0)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)

    def test_division(self):
        """
        Test the divide method with various inputs, including the edge case
        of division by zero, which should return None as specified.
        """
        self.assertEqual(self.calc.divide(10, 5), 2.0)
        self.assertEqual(self.calc.divide(10, 4), 2.5)
        self.assertEqual(self.calc.divide(-10, 5), -2.0)
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        # Test the edge case of division by zero
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))