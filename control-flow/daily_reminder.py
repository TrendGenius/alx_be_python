# Task 4: Personal Daily Reminder
# Objective: Create a simplified Python script that uses conditional statements,
#            Match Case, and loops to remind the user about a single, priority task.

# --- Step 1: Prompt for a Single Task ---
# Get the task description from the user.
task = input("Enter your task: ")

# Get the priority level from the user and convert it to lowercase for easier comparison.
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound and convert the answer to lowercase.
time_bound = input("Is it time-bound? (yes/no): ").lower()

# --- Step 2: Process the Task Based on Priority and Time Sensitivity ---
# Start building the reminder message.
reminder_message = f"Reminder: '{task}' is a {priority} priority task."

# Use a Match Case statement to react differently based on the task’s priority.
match priority:
    case "high":
        # Add specific text for high priority.
        reminder_message += " that requires immediate attention."
    case "medium":
        # Add specific text for medium priority.
        reminder_message += ". Try to complete it soon."
    case "low":
        # Add specific text for low priority.
        reminder_message += ". Consider completing it when you have free time."
    case _:
        # Default case for unexpected priority input.
        reminder_message = f"Reminder: '{task}' has an unrecognized priority. "

# --- Step 3: Modify the reminder if the task is time-bound ---
# Check if the user said "yes" to time-bound.
if time_bound == "yes":
    # If it's time-bound, add the specific phrase.
    # Note: We're being careful not to duplicate "that requires immediate attention"
    # if it's already added by a "high" priority.
    if "immediate attention" not in reminder_message: # Avoids double-adding for high priority
        reminder_message += " that requires immediate attention today!"
    else:
        reminder_message += " today!" # Just add "today!" if "immediate attention" is already there
elif time_bound == "no":
    # If not time-bound, and it's a low priority, adjust message for clarity
    if priority == "low" and "Consider completing it when you have free time." not in reminder_message:
        reminder_message += " Consider completing it when you have free time."
    elif "immediate attention" in reminder_message: # If it was high priority but not time-bound, remove "today!"
        reminder_message = reminder_message.replace(" today!", "") # Remove if it was added incorrectly
    # For medium priority and not time-bound, the default message is fine

# --- Step 4: Provide a Customized Reminder ---
print(reminder_message)