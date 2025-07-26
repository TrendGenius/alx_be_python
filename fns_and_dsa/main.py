# This is a temporary main.py for local testing.
# The checker will use its own version.
from arithmetic_operations import perform_operation

def main():
    print("Arithmetic Operations")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

        result = perform_operation(num1, num2, operation)
        print(f"Result: {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values for numbers.")

if __name__ == "__main__":
    main()