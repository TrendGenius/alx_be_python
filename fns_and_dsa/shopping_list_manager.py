# Task 1: Shopping List Manager
# Objective: Utilize Python lists to create a simple shopping list manager.

def display_menu():
    """Displays the main menu options to the user."""
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Main function to run the shopping list manager."""
    shopping_list = [] # Initialize an empty list to store shopping items

    while True: # Loop continuously until the user chooses to exit
        display_menu() # Show the menu
        choice = input("Enter your choice: ").strip() # Get user's choice and remove any leading/trailing spaces

        if choice == '1':
            # --- Add Item functionality ---
            item = input("Enter the item to add: ").strip()
            if item: # Ensure the item name is not empty
                shopping_list.append(item) # Add the item to the list
                print(f"'{item}' added to the list.")
            else:
                print("Item name cannot be empty.")
        elif choice == '2':
            # --- Remove Item functionality ---
            if not shopping_list: # Check if the list is empty first
                print("The shopping list is already empty. Nothing to remove.")
                continue # Go back to the start of the loop
            
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list: # Check if the item exists in the list
                shopping_list.remove(item) # Remove the first occurrence of the item
                print(f"'{item}' removed from the list.")
            else:
                print(f"'{item}' not found in the list.")
        elif choice == '3':
            # --- View List functionality ---
            if not shopping_list: # Check if the list is empty
                print("Your shopping list is empty.")
            else:
                print("\n--- Your Shopping List ---")
                for i, item in enumerate(shopping_list, 1): # Loop through the list with numbers
                    print(f"{i}. {item}")
                print("--------------------------")
        elif choice == '4':
            # --- Exit functionality ---
            print("Goodbye!")
            break # Exit the while loop
        else:
            # --- Handle invalid choice ---
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main() # Call the main function when the script is executed