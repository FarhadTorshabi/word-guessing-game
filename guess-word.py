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
# Reset Game State
# -----------------------------
def reset_round_state(game_state):
    game_state["guessed_letters"] = []
    game_state["status"] = "playing"

# -----------------------------
# Apply Guess
# -----------------------------
def apply_guess(game_state, guess):
    if guess in game_state["secret_word"]:
        return True
    else:
        game_state["attempts_left"] -= 1
        return False

# -----------------------------
# Update Game Status
# -----------------------------
def update_game_status(game_state, display):
    if "_" not in display:
        game_state["status"] = "won"
    elif game_state["attempts_left"] == 0:
        game_state["status"] = "lost"

# -----------------------------
# User Requests a Hint
# -----------------------------
def get_hint_letter(secret_word, guessed_letters):
    hidden_letters = list()
    
    for letter in secret_word:
        if letter not in guessed_letters:
            hidden_letters.append(letter)
    
    if not hidden_letters:
        return None
    
    return random.choice(hidden_letters)

# -----------------------------
# Play One Round
# -----------------------------
def play_round(game_state):

    reset_round_state(game_state)

    game_state["secret_word"], game_state["attempts_left"] = choose_difficulty()
    
    display = ["_"] * len(game_state["secret_word"])

    print("\n🎯 New Game Started!")
    print("Word:", " ".join(display))

    while game_state["status"] == "playing":
        if game_state["guessed_letters"]:
            print("\nGuessed letters:", ", ".join(game_state["guessed_letters"]))
        else:
            print("\nGuessed letters: none")
        
        print("Attempts left:", game_state["attempts_left"])

        guess = get_valid_guess(game_state["guessed_letters"])
        
        # Hint request
        if guess == "hint":
            hint_letter = get_hint_letter(game_state["secret_word"], game_state["guessed_letters"])
            if hint_letter is None:
                print("ℹ️ No hints available.")
                continue
            
            game_state["guessed_letters"].append(hint_letter)
            update_display(game_state["secret_word"], display, hint_letter)
            game_state["attempts_left"] -= 1

            print(f"💡 Hint used! Letter revealed: {hint_letter}")
            print("Word:", " ".join(display))

            # ✅ FIX: check for win immediately
            if "_" not in display:
                game_state["status"] = "won"
                break
            
            continue

        game_state["guessed_letters"].append(guess)

        # Full word guess
        if len(guess) > 1:
            if guess == game_state["secret_word"]:
                return True, game_state["secret_word"]
            else:
                game_state["attempts_left"] -= 1
                print("❌ Wrong word!")
                continue

        # Single letter guess
        if apply_guess(game_state, guess):
             update_display(game_state["secret_word"], display, guess)
             print("✅ Correct!")
        else:
            print("❌ Wrong letter!")

        print("Word:", " ".join(display))

        update_game_status(game_state, display)

# -----------------------------
# Main Application Loop
# -----------------------------
def guess_word():

    game_state = {
        "secret_word": "python",
        "guessed_letters": [],
        "attempts_left": 5,
        "status": "playing"
    }
    wins = 0
    losses = 0

    print("🎮 Welcome to the Word Guessing Game!")
    print("Guess letters one by one, or try to guess the whole word.")
    print("Be careful — wrong guesses cost attempts!\n")

    while True:
        play_round(game_state)

        if game_state["status"] == "won":
            wins += 1
            print(f"\n🎉 You won! The word was '{game_state['secret_word']}'.")
        elif game_state["status"] == "lost":
            losses += 1
            print(f"\n💀 You lost. The word was '{game_state['secret_word']}'.")

        print(f"\n📊 Score → Wins: {wins} | Losses: {losses}")

        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != "y":
            print("\nThanks for playing 👋")
            break


# -----------------------------
# Start the Game
# -----------------------------
guess_word()