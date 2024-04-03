import random

def choose_word():
    words = ["programming", "computer", "python", "developer", "web", "technology", "coding"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def main():
    print("Welcome to Hangman!")
    secret_word = choose_word()
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        print(display_word(secret_word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in secret_word:
            guessed_letters.append(guess)
            if "_" not in display_word(secret_word, guessed_letters):
                print("Congratulations! You've guessed the word:", secret_word)
                break
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

    if attempts == 0:
        print("Oops! You're out of attempts. The word was:", secret_word)

if __name__ == "__main__":
    main()
