# Task 2: Explore `datetime` Module
# Objective: Familiarize with Python's datetime module for date and time operations.

# Import necessary classes from the datetime module
from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    """
    # Get the current date and time
    current_date = datetime.now()
    
    # Format the current date and time into a readable string
    # %Y: Year with century (e.g., 2024)
    # %m: Month as a zero-padded decimal number (e.g., 03)
    # %d: Day of the month as a zero-padded decimal number (e.g., 25)
    # %H: Hour (24-hour clock) as a zero-padded decimal number (e.g., 15)
    # %M: Minute as a zero-padded decimal number (e.g., 30)
    # %S: Second as a zero-padded decimal number (e.g., 45)
    formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Current date and time: {formatted_current_date}")

def calculate_future_date():
    """
    Prompts the user for a number of days, calculates a future date,
    and prints it in 'YYYY-MM-DD' format.
    """
    try:
        # Prompt the user to enter a number of days
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        
        # Get the current date (we only need the date part for future calculation)
        current_date = datetime.now()
        
        # Calculate the future date by adding the timedelta object
        # timedelta(days=...) creates a duration object
        future_date = current_date + timedelta(days=days_to_add)
        
        # Format the future date into 'YYYY-MM-DD' string
        # %Y: Year, %m: Month, %d: Day
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        
        print(f"Future date: {formatted_future_date}")
    except ValueError:
        # Handle cases where the user input is not a valid integer
        print("Invalid input. Please enter a whole number for days.")

def main():
    """
    Main function to run the datetime exploration tasks.
    """
    display_current_datetime() # Call the function to display current date/time
    calculate_future_date()    # Call the function to calculate and display future date

if __name__ == "__main__":
    main() # Ensure main() is called only when the script is executed directly
