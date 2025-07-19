# Task 3: Drawing Patterns with Nested Loops
# Objective: Utilize while loops and nested for loops to draw a simple text-based pattern.

# --- Step 1: Prompt User for Pattern Size ---
# Get a positive whole number from the user for the size of the square.
size = int(input("Enter the size of the pattern: "))

# --- Step 2: Draw the Pattern using nested loops ---

# Initialize a counter for the outer loop (rows).
# This 'row_count' will go from 0 up to (size - 1).
row_count = 0

# Outer loop: Controls the number of rows.
# It continues as long as 'row_count' is less than 'size'.
while row_count < size:
    # Inner loop: Controls what is printed on each row (the columns).
    # It iterates 'size' number of times to print 'size' asterisks.
    for _ in range(size): # Using '_' as variable name because we don't need its value
        # Print an asterisk. 'end=""' prevents moving to the next line after each asterisk.
        print("*", end="")
    
    # After the inner loop finishes (one row is complete),
    # print an empty line to move to the next row.
    print()
    
    # Increment the row counter so the while loop eventually stops.
    row_count += 1 # This is a shorthand for row_count = row_count + 1