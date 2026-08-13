# Flashcard Quiz App

A simple command-line flashcard/quiz application built in Python. Questions and answers are loaded from a JSON file, presented one at a time, and scored automatically — with a full results summary, including accuracy percentage and a review of any wrong answers.

## Features

- Loads quiz questions from a `questions.json` file
- Displays one question at a time, numbered (e.g. "Question 2 of 5")
- Case- and whitespace-insensitive answer checking (e.g. `"kigali"` and `"Kigali"` are treated as the same answer)
- Tracks score and wrong answers as the quiz progresses
- Calculates and displays a final accuracy percentage
- Reviews every wrong answer at the end, showing what you answered vs. the correct answer
- Handles a missing or invalid `questions.json` file gracefully instead of crashing

## Requirements

- Python 3.7 or later (no external libraries required — only the standard library)

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/cyubahiroprince18/flashcard-app.git
   cd flashcard-app
   ```

2. Make sure `questions.json` is present in the same folder as `quiz.py`. It should look like this:
   ```json
   [
       {
           "question": "What is the capital of Rwanda?",
           "answer": "Kigali"
       },
       {
           "question": "What is 2 + 2?",
           "answer": "4"
       }
   ]
   ```

## Usage

Run the app from inside the project folder:

```bash
python quiz.py
```

You'll be shown each question one at a time. Type your answer and press Enter. At the end of the quiz, you'll see your score, accuracy percentage, and a review of any questions you got wrong.

## Customizing the questions

Add, remove, or edit entries in `questions.json` — each flashcard just needs a `"question"` and an `"answer"` field. No code changes are required.

## Project structure

```
flashcard-app/
├── quiz.py           # Main program
├── questions.json    # Quiz content (questions and answers)
└── README.md
```

## How it works (brief overview)

- `load_questions()` — reads and parses `questions.json`
- `check_answer()` — compares the user's answer to the correct one
- `ask_question()` — displays a question and collects the user's answer
- `run_quiz()` — loops through all questions, tracking score and mistakes
- `show_results()` — prints the final score, accuracy, and wrong-answer review
- `main()` — ties everything together and runs the program

## License

Feel free to use, modify, and extend this project for personal or educational purposes.
