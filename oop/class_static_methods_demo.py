# class_static_methods_demo.py
# This file demonstrates the use and differences between class methods and static methods.

class Calculator:
    """
    A simple Calculator class demonstrating a class method and a static method.
    It has a class-level attribute 'calculation_type'.
    """
    # --- Class Attribute ---
    # This attribute belongs to the class itself, not individual instances.
    # It's shared by all objects of the Calculator class.
    calculation_type = "Arithmetic Operations"

    # --- Static Method ---
    # Defined using the @staticmethod decorator.
    # It does NOT take 'self' (instance) or 'cls' (class) as its first argument.
    # It behaves like a regular function, but is logically grouped within the class.
    # It cannot access or modify instance-specific data or class-specific data directly (without explicit reference).
    @staticmethod
    def add(a, b):
        """
        A static method that returns the sum of two numbers.
        It doesn't need access to class or instance state.
        """
        return a + b

    # --- Class Method ---
    # Defined using the @classmethod decorator.
    # It takes the class itself (conventionally named 'cls') as its first argument.
    # It can access and modify class-level attributes using 'cls'.
    # It can also be used to create alternative constructors.
    @classmethod
    def multiply(cls, a, b):
        """
        A class method that returns the product of two numbers.
        It accesses a class-level attribute 'calculation_type' using 'cls'.
        """
        # Accessing the class attribute 'calculation_type' via the 'cls' parameter.
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

