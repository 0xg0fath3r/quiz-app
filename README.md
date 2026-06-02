# Quiz App

Simple command-line quiz game written in Python.

## What It Does

- Presents 10 multiple-choice questions.
- Accepts answers from 1 to 4.
- Tracks the score and shows a final percentage.
- Displays a short performance message at the end.
- Lets you play again after each round.

## Project Files

- [main.py](main.py): application entry point and game loop.
- [questions.py](questions.py): quiz questions and answers.
- [quiz_logic.py](quiz_logic.py): quiz flow, scoring, and result helpers.
- [utils.py](utils.py): console display and input helpers.

## Requirements

- Python 3.8 or newer.

## Run The Quiz

From the project root, run:

```bash
python main.py
```

## How It Works

1. The welcome screen explains the rules.
2. Each question is shown with four numbered options.
3. Enter a choice from 1 to 4.
4. The app immediately tells you whether the answer was correct.
5. At the end, the app shows your score, percentage, and performance level.

## Customizing The Quiz

You can edit [questions.py](questions.py) to change the quiz content. Each question uses this structure:

```python
{
	"text": "Question text",
	"options": ["Option 1", "Option 2", "Option 3", "Option 4"],
	"correct_index": 0,
}
```

## Example

If you answer 8 out of 10 questions correctly, your score will be 80% and the app will show a performance message based on that result.