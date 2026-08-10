import random

WORDS = ["python", "hangman", "internship", "coding", "developer"]
MAX_WRONG_GUESSES = 6

def choose_word():
    return random.choice(WORDS)

def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def play_hangman():
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0
    print("Welcome to Hangman!")
    print(f"You have {MAX_WRONG_GUESSES} wrong guesses allowed.\n")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print("word:", display_word(word, guessed_letters))
        print(f"Wrong guesses left: {MAX_WRONG_GUESSES - wrong_guesses}")
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct guess!\n")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                return
        else:
            wrong_guesses += 1
            print(f"Wrong guess! ({wrong_guesses}/{MAX_WRONG_GUESSES})\n")

    print(f"Game over! The word was: {word}")

play_hangman()