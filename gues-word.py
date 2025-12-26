import random

def guess_word():
    words = ["python", "programming", "developer", "function", "variable"]

    while True:  # play-again loop
        secret_word = random.choice(words)
        attempts = 6
        guessed_letters = []

        while True:  # game loop
            display = ""
            for letter in secret_word:
                if letter in guessed_letters:
                    display += letter + " "
                else:
                    display += "_ "

            print(display)

            if "_" not in display:
                print("🎉 You guessed the word!")
                break

            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue

            if guess in guessed_letters:
                print("You already guessed that letter.")
                continue

            guessed_letters.append(guess)

            if guess not in secret_word:
                attempts -= 1
                if attempts == 0:
                    print(f"Sorry! Your attempts are over. The word was '{secret_word}'.")
                    break
                print(f"Wrong guess! Attempts left: {attempts}")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing 👋")
            break

guess_word()