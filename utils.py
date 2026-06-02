def display_question(question_text, options):
    """Display a question and its options"""
    print(f"\n{question_text}")
    print("-" * 40)

    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    print("-" * 40)


def get_user_choice():
    """Get and validate user input (1-4)"""
    while True:
        try:
            choice = int(input("Your choice (1-4): "))
            if 1 <= choice <= 4:
                return choice - 1  # Convert to 0-based index
            else:
                print("Please enter a number between 1 and 4")
        except ValueError:
            print("Please enter a valid number")


def show_result(is_correct, correct_answer):
    """Show feedback for an answer"""
    if is_correct:
        print("✓ Correct!")
    else:
        print(f"✗ Wrong! The correct answer was: {correct_answer}")
