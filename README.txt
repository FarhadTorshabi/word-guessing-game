🎮 Word Guessing Game (Python)

A console-based word guessing game developed while learning Python fundamentals, focusing on clean design, incremental refactoring, and version control best practices.

📌 Features

Three difficulty levels: Easy / Medium / Hard

Guess letters or the entire word

Limited hint system based on difficulty

Attempts decrease on wrong guesses and hint usage

Persistent scoreboard saved to a file

Clear game status handling (win / lose)

Designed step-by-step with meaningful commits

🕹️ How to Play

Run the game:

python guess-word.py


Choose a difficulty:

Easy → more attempts, more hints

Medium → balanced

Hard → fewer attempts, no hints

Enter:

A single letter (e.g. a)

Or the full word (e.g. python)

Or type hint (if available)

The game ends when:

All letters are revealed (Win)

Attempts reach zero (Loss)

💡 Hint System
Difficulty	Attempts	Hints
Easy	6	2
Medium	5	1
Hard	4	0

Using a hint:

Reveals one hidden letter

Costs 1 attempt

Hints cannot be used if:

No hints remain

No hidden letters remain

📊 Scoreboard

Wins and losses are saved to scoreboard.txt

Scores persist between game runs

Example file content:

wins=3
losses=2

🧠 Learning Goals Behind This Project

This project was intentionally built to practice:

Functions & dictionaries

Game state management

Input validation

Incremental refactoring

Bug fixing through reasoning

Git commits with meaningful history

Designing rules instead of patching bugs

🛠️ Future Improvements

Refactor using classes (OOP)

Add timer or streak bonuses

Improve UI (colors / formatting)

Add test cases

🤝 Note

This project was developed while learning Python, with guidance and explanations from ChatGPT.
The focus was not just making it work, but understanding why it works.