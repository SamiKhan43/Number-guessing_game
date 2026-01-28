# Python Quiz Game 🐍

## Links
- Project URL: [Number-Guessing-Game](https://github.com/SamiKhan43/Number-guessing_game)
- inspiration: [Roadmap.sh](https://roadmap.sh/projects/number-guessing-game).


A fun and interactive command-line quiz game to test your Python programming knowledge!

## Description

This is a simple yet engaging Python quiz game that tests your understanding of Python fundamentals through multiple-choice questions. Each game session randomly selects 10 questions from a pool of 15, ensuring variety and replayability.

## Features

- **10 Random Questions**: Each game randomly selects 10 questions from a pool of 15
- **Multiple Choice Format**: Easy-to-answer format with numbered options
- **Instant Feedback**: Get immediate feedback on whether your answer is correct or wrong
- **Score Tracking**: See your total score at the end of each quiz
- **Time Tracking**: Find out how long it took you to complete the quiz
- **Replay Option**: Play multiple rounds without restarting the program
- **Input Validation**: Ensures only valid numeric inputs are accepted

## Topics Covered

The quiz covers fundamental Python concepts including:
- Basic syntax and keywords
- Data types (lists, tuples, sets, dictionaries)
- Operators and expressions
- Control flow (if, while, for)
- String operations
- Built-in functions
- Variable naming conventions

## Requirements

- Python 3.x

No external libraries are required - the game uses only Python's standard library.

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Run the game using Python

```bash
python quiz_game.py
```

## How to Play

1. Run the script
2. Press Enter to start the quiz
3. Read each question carefully
4. Type the number corresponding to your answer
5. Press Enter to submit
6. Receive instant feedback
7. Complete all 10 questions
8. View your final score and completion time
9. Choose whether to play again

## Example Gameplay

```
**********************************************************************
Welcome to the Python Quiz Game!
~ You will be asked 10 multiple-choice questions.
~ Type the number corresponding to your answer and press Enter.
~ Let's see how well you know Python!

**********************************************************************
Press Enter to start...

Q1: What keyword is used to print output in Python?
  1. echo
  2. printf
  3. print
  4. write
Your answer (number): 3
Correct!

...

You completed the quiz in 45.32 seconds.
Quiz Over! Your total score is: 8 out of 10
Do you want to play again? (yes/no):
```

## Code Structure

- `QuizGame` class: Main game controller
  - `__init__()`: Initializes the game and loads questions
  - `load_questions()`: Loads and randomizes quiz questions
  - `show_menu()`: Displays the welcome screen
  - `ask_question()`: Handles individual question logic
  - `play()`: Main game loop

## Customization

You can easily customize the game by:

- **Adding more questions**: Add new question dictionaries to the `quiz_questions` list in `load_questions()`
- **Changing question count**: Modify the number in `random.sample(quiz_questions, 10)` to select more or fewer questions
- **Adjusting difficulty**: Add more complex questions or modify existing ones

### Question Format

```python
{
    "question": "Your question here?",
    "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
    "answer": 2  # Index of correct answer (1-based)
}
```

## Future Enhancements

Potential improvements for future versions:
- Difficulty levels (Easy, Medium, Hard)
- Question categories
- High score tracking
- Leaderboard system
- Hints system
- Timer for each question
- GUI version using Tkinter

## Contributing

Feel free to fork this project and add your own improvements! Some ideas:
- Add more questions
- Implement new features
- Improve the user interface
- Add sound effects
- Create themed question sets

## License

This project is open source and available for educational purposes.

## Author

Created as an educational project to help Python learners test their knowledge.

---

