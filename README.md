# My Python Practice 🐍

Hello! I'm Shardul, a first-year BTech CSE (IoT & Cyber Security) student at VIT Pune. This repository serves as a time capsule for my Python learning journey. It contains the foundational projects I built while getting comfortable with core programming concepts, and now, advanced Object-Oriented Programming (OOP) security tools.

## 📁 Projects

### 🛡️ 1. Interactive Security Scanner (`security_tool.py`)
An Object-Oriented Programming (OOP) based simulation of a penetration testing tool. This project demonstrates inheritance, method overriding, and user interaction.
*   **Features:**
    *   **Base Class (`Target`):** Handles core functions like scanning ports (simulated) and generating reports.
    *   **Inheritance (`WebTarget`):** Inherits from `Target` but adds unique web-specific methods like `check_sql_injection()`.
    *   **Inheritance (`DatabaseTarget`):** Inherits from `Target` but adds database-specific checks like `check_default_password()`.
    *   **Interactive Menu:** Uses a `while` loop and user input (`input()`) to allow the user to choose which type of target to scan.
*   **Concepts used:** Object-Oriented Programming (Classes, `__init__`, `self`), Inheritance (`super()`), Method Overriding, f-strings, `while` loops, conditionals.

### 🧮 2. Command-Line Calculator (`calculator.py` & `function_calculator.py`)
A robust calculator that handles user mistakes gracefully and is refactored into modular functions.
*   **Features:**
    *   Supports addition, subtraction, multiplication, division, modulo (`%`), and exponentiation (`**`).
    *   Runs continuously in a loop until the user types "quit".
    *   Prevents division by zero errors.
    *   Uses `try/except` blocks to prevent crashing if a user types a letter instead of a number.
    *   **Refactored:** Moved math logic into separate `def add()`, `def subtract()`, etc., functions for modularity.
*   **Concepts used:** Functions, `while` loops, `if/elif/else`, `try/except` error handling, floating-point arithmetic.

### 🎲 3. Word Guessing Game (`game2.py` / `guessgame.py`)
An interactive terminal game where the player has limited attempts to guess a randomly selected word.
*   **Features:**
    *   Randomly selects a word from a custom list (Linux/Unix/CyberSec themed).
    *   **Replayability:** Includes a "Play Again" loop.
    *   **Input Validation:** Prevents empty guesses and handles case-insensitivity.
    *   **Attempt Tracker:** Displays exactly how many tries you have left.
*   **Concepts used:** User-defined functions (`def`), `while` loops, boolean flags, `random` module, string methods (`.lower()`).

### 🔢 4. FizzBuzz Algorithm (`fizz.py`)
The classic programming interview question, optimized.
*   **Features:**
    *   Takes a maximum number from the user.
    *   Prints "Fizz" for multiples of 3, "Buzz" for multiples of 5, and "FizzBuzz" for multiples of both.
    *   Optimized to check multiples of 15 first to avoid redundant conditions.
*   **Concepts used:** `for` loops, modulo arithmetic (`%`), conditional logic.

## 🛠️ Technologies & Tools Used
*   **Language:** Python 3.14
*   **Editor:** VS Code
*   **Version Control:** Git & GitHub
*   **Networking Simulation:** Cisco Packet Tracer (100% Score in Final Exam)

## 🚀 How to Run
1. Ensure you have Python installed.
2. Clone this repository: `git clone <your-repo-url>`
3. Navigate to the folder and run any script:
   ```bash
   python security_tool.py
   python calculator.py
   python game2.py
   python fizz.py