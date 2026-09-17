# My Python Practice 🐍

Hello! I'm Shardul, a first-year BTech CSE (IoT & Cyber Security) student at VIT Pune. 
This repository serves as a time capsule for my Python learning journey. It contains the foundational projects I built while getting comfortable with core programming concepts before and during my first semester.

## 📁 Projects

### 🧮 1. Command-Line Calculator (`calculator.py`)
A robust calculator that doesn't just do math—it handles user mistakes gracefully.
*   **Features:**
    *   Supports addition, subtraction, multiplication, division, modulo (`%`), and exponentiation (`**`).
    *   Runs continuously in a loop until the user types "quit".
    *   Prevents division by zero errors.
    *   Uses `try/except` blocks to prevent the program from crashing if a user types a letter instead of a number.
*   **Concepts used:** `while` loops, `if/elif/else`, `try/except` error handling, floating-point arithmetic.

### 🎲 2. Word Guessing Game (`guessgame.py`)
An interactive terminal game where the player has limited attempts to guess a randomly selected word.
*   **Features:**
    *   Randomly selects a word from a custom list (Linux/Unix/CyberSec themed).
    *   Gives the player only 3 attempts to guess correctly.
    *   Uses case-insensitive matching (e.g., "Linux" and "linux" count as the same).
*   **Concepts used:** `random` module, `while` loops, boolean flags (`out_of_guesses`), user input handling.

### 🔢 3. FizzBuzz Algorithm (`fizz.py`)
The classic programming interview question, optimized.
*   **Features:**
    *   Takes a maximum number from the user.
    *   Prints "Fizz" for multiples of 3, "Buzz" for multiples of 5, and "FizzBuzz" for multiples of both.
    *   Optimized to check multiples of 15 first to avoid redundant conditions.
*   **Concepts used:** `for` loops, modulo arithmetic (`%`), conditional logic.

### 🔤 4. Vowel and Consonant Counter (`pratice.py`)
A simple string analysis tool.
*   **Features:**
    *   Takes a name or sentence as input.
    *   Counts the number of vowels and consonants.
    *   Handles uppercase and lowercase letters seamlessly.
*   **Concepts used:** String iteration, `.lower()` method, `in` operator.

## 🛠️ Technologies & Tools Used
*   **Language:** Python 3.14
*   **Editor:** VS Code
*   **Version Control:** Git & GitHub

## 🚀 How to Run
1. Ensure you have Python installed.
2. Clone this repository: `git clone <your-repo-url>`
3. Navigate to the folder and run any script:
   bash
   python calculator.py
   python guessgame.py
   python fizz.py
   python pratice.py


🎯 Future Goals

As I progress through my degree, I plan to expand this repository with:

· Object-Oriented Programming (OOP) projects.
· Automation scripts using Bash and Python.
· Basic network scanning tools.
· Write-ups for PicoCTF challenges.

