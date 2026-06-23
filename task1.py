import random

# List of 5 words
words = ["apple", "school", "computer", "garden", "house"]

word = random.choice(words)

guessed = ""
chances = 6

print("Welcome to Hangman Game!")

while chances > 0:
    display = ""

    # Show guessed letters and underscores
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check if word is completed
    if "_" not in display:
        print("Congratulations! You guessed the word.")
        break

    guess = input("Enter a letter: ")

    if guess in word:
        guessed += guess
        print("Correct Guess!")
    else:
        chances -= 1
        print("Wrong Guess!")
        print("Remaining Chances:", chances)

if chances == 0:
    print("\nGame Over!")
    print("The word was:", word)