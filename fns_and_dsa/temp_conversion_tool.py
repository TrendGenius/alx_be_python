# Task 3: Temperature Conversion Tool
# Objective: Convert temperatures between Celsius and Fahrenheit using global variables.

# Define Global Conversion Factors
# These variables are defined at the top level, making them accessible
# from anywhere within this script. They act as constants for conversion.
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature converted to Celsius.
    """
    # Use the global conversion factor
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature converted to Fahrenheit.
    """
    # Use the global conversion factor
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    """
    Main function to handle user interaction for temperature conversion.
    Prompts for temperature and unit, performs conversion, and displays result.
    Includes input validation.
    """
    print("Temperature Conversion Tool")

    try:
        # Prompt user for temperature and attempt to convert to float
        temperature_input = input("Enter the temperature to convert: ")
        temperature_value = float(temperature_input)
    except ValueError:
        # If conversion to float fails, raise a specific error as required
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Prompt user for the unit and clean the input
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'F':
        # If input is Fahrenheit, convert to Celsius
        converted_temp = convert_to_celsius(temperature_value)
        print(f"{temperature_value}°F is {converted_temp}°C")
    elif unit == 'C':
        # If input is Celsius, convert to Fahrenheit
        converted_temp = convert_to_fahrenheit(temperature_value)
        print(f"{temperature_value}°C is {converted_temp}°F")
    else:
        # Handle invalid unit input
        print("Invalid unit. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    # Call the main function when the script is executed directly
    main()
