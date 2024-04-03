def mad_libs():
    print("Welcome to Mad Libs! Let's create a funny story.")
    
    noun = input("Enter a noun: ")
    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")
    
    story = f"Once upon a time, there was a {adjective} {noun} who loved to {verb} {adverb}."
    
    print("\nHere's your Mad Libs story:\n")
    print(story)

if __name__ == "__main__":
    mad_libs()
