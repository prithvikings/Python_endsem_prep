# Import the necessary libraries
import random

# Define a function to generate a random number
def generate_random_number():
    # Generate a random number between 1 and 99
    random_number = random.randint(1, 99)

    # Return the random number
    return random_number

# Define a function to take input from the user
def take_input():
    # Get the user's input
    input_text = input()

    # Return the user's input
    return input_text

# Define a function to check if the user's input is correct
def check_input(input_text, random_number):
    # Check if the user's input is a number
    if not input_text.isdigit():
        return False

    # Check if the user's input is within the range of 1 and 99
    if int(input_text) < 1 or int(input_text) > 99:
        return False

    # Check if the user's input is equal to the random number
    if int(input_text) == random_number:
        return True

    # Return False if the user's input is not correct
    return False

# Generate a random number
random_number = generate_random_number()

# Take input from the user
input_text = take_input()

# Check if the user's input is correct
is_correct = check_input(input_text, random_number)

# Print the result
if is_correct:
    print("You guessed the correct number!")
else:
    print("You guessed the wrong number.")