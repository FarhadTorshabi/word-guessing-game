import random

# -----------------------------
# Difficulty & Word Selection
# -----------------------------
def choose_difficulty():
    EASY_WORDS = ["cat", "dog", "sun", "book"]
    MEDIUM_WORDS = ["python", "planet", "flower"]
    HARD_WORDS = ["elephant", "computer", "mountain"]

    while True:
        level = input("Choose difficulty (easy / medium / hard): ").lower()

        if level == "easy":
            return random.choice(EASY_WORDS), 6
        elif level == "medium":
            return random.choice(MEDIUM_WORDS), 5
        elif level == "hard":
            return random.choice(HARD_WORDS), 4
        else:
            print("❌ Invalid choice. Try again.")


# -----------------------------
# Input Validation
# -----------------------------
def get_valid_guess(guessed_letters):
    while True:
        guess = input("Guess a letter or the whole word: ").lower()

        if not guess.isalpha():
            print("⚠️ Letters only.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that.")
            continue

        return guess


# -----------------------------
# Update Word Display
# -----------------------------
def update_display(word, display, guess):
    for i in range(len(word)):
        if word[i] == guess:
            display[i] = guess


# -----------------------------
# Play One Round
# -----------------------------
def play_round():
    word, attempts = choose_difficulty()
    guessed_letters = []
    display = ["_"] * len(word)

    print("\n🎯 New Game Started!")
    print("Word:", " ".join(display))

    while attempts > 0 and "_" in display:
        print("\nGuessed letters:", ", ".join(guessed_letters))
        print("Attempts left:", attempts)

        guess = get_valid_guess(guessed_letters)
        guessed_letters.append(guess)

        # Full word guess
        if len(guess) > 1:
            if guess == word:
                return True, word
            else:
                attempts -= 1
                print("❌ Wrong word!")
                continue

        # Single letter guess
        if guess in word:
            update_display(word, display, guess)
            print("✅ Correct!")
        else:
            attempts -= 1
            print("❌ Wrong letter!")

        print("Word:", " ".join(display))

    return "_" not in display, word


# -----------------------------
# Main Application Loop
# -----------------------------
def guess_word():
    wins = 0
    losses = 0

    print("🎮 Welcome to the Word Guessing Game!")

    while True:
        won, word = play_round()

        if won:
            wins += 1
            print("\n🎉 You won! The word was:", word)
        else:
            losses += 1
            print("\n💀 You lost! The word was:", word)

        print(f"\n📊 Score → Wins: {wins} | Losses: {losses}")

        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != "y":
            print("\nThanks for playing 👋")
            break


# -----------------------------
# Start the Game
# -----------------------------
guess_word()