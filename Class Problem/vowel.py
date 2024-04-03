"""Write a userdefined function replace vowel(word) which removes 
all vowels ('a','e','i','o','u') in a word 
and returns the remaining letter in word"""

def replace_vowel(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ""

    for char in word:
        if char.lower() not in vowels:
            result += char

    return result
word = input("Enter Your Word:")
print(replace_vowel(word)) 