from utils import display_question, get_user_choice, show_result


def run_quiz(questions):
    """
    Main quiz engine.
    Returns: final score
    """
    score = 0
    total_questions = len(questions)

    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i} of {total_questions}")

        # Display the question
        display_question(question["text"], question["options"])

        # Get user's answer
        user_index = get_user_choice()

        # Check if correct
        is_correct = user_index == question["correct_index"]

        if is_correct:
            score += 1

        # Show feedback
        correct_answer = question["options"][question["correct_index"]]
        show_result(is_correct, correct_answer)

    return score


def calculate_percentage(score, total):
    """Convert score to percentage"""
    return (score / total) * 100


def get_performance_level(percentage):
    """Return performance rating based on percentage"""
    if percentage >= 90:
        return "Excellent!"
    elif percentage >= 70:
        return "Good job!"
    elif percentage >= 50:
        return "Not bad!"
    else:
        return "Keep practicing!"
