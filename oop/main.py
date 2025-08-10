# main.py for Task 3

# Import the Calculator class from class_static_methods_demo.py
from class_static_methods_demo import Calculator

# This is the main function where our test code will run.
def main():
    # --- Using the static method ---
    # Static methods are called directly on the class name.
    # They do not require an object instance to be created.
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")
    # --- Using the class method ---
    # Class methods are also called directly on the class name.
    # They receive the class itself ('Calculator' in this case) as their first argument ('cls').
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

# This standard Python line makes sure main() runs when the script is executed directly.
if __name__ == "__main__":
    main()

