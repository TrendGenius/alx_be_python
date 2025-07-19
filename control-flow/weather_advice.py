# Task 0: Weather Recommendation Program
# Objective: Utilize conditional statements (if, elif, else) to provide clothing recommendations.

# --- Step 1: Prompt User for Weather Input ---
# The input() function asks the user a question and waits for them to type an answer.
# The answer is stored as text (a string) in the 'weather' variable.
weather = input("What's the weather like today? (sunny/rainy/cold): ")

# --- Step 2: Provide Clothing Recommendations based on input ---
# We use if, elif, and else to make decisions.
# The '==' checks if the text in 'weather' is EXACTLY equal to "sunny", "rainy", or "cold".

if weather == "sunny":
    # If the weather is sunny, print this recommendation.
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    # Else, if the weather is rainy, print this recommendation.
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    # Else, if the weather is cold, print this recommendation.
    print("Make sure to wear a warm coat and a scarf.")
else:
    # If none of the above conditions (sunny, rainy, cold) were true,
    # then the input was unexpected, so print this message.
    print("Sorry, I don't have recommendations for this weather.")