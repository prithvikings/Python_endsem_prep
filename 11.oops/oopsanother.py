"""write a program to reverse a string entered by the user using classes and object"""

"""
Minecraft Launcher is currently not available in your account. Make sure you are signed in to the Store and try again. Here’s the error code, in case you need it: 0x803F8001"""

class StringReverser:
    def __init__(self):
        self.original_string = ""

    def get_string(self):
        self.original_string = input("Enter a string: ")

    def reverse_string(self):
        return self.original_string[::-1]

# Creating an object of the StringReverser class
reverser = StringReverser()

# Getting input string from the user
reverser.get_string()

# Reversing the input string
reversed_string = reverser.reverse_string()

print("Reversed string:", reversed_string)

"""write a program to find wheater the string entered by the users is pallendrom or not"""
def is_palindrome(s):
    # Convert the string to lowercase and remove spaces
    s = s.lower().replace(" ", "")
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Get input from the user
user_input = input("Enter a string: ")

# Check if the input string is a palindrome
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome!")
else:
    print(f"'{user_input}' is not a palindrome.")
