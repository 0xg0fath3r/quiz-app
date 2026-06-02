from questions import QUESTIONS
from quiz_logic import run_quiz, calculate_percentage, get_performance_level


def display_welcome():
    """Show welcome message"""
    print("=" * 50)
    print("        WELCOME TO THE QUIZ APP")
    print("=" * 50)
    print(f"You will answer {len(QUESTIONS)} questions")
    print("Each question has 4 options (1-4)")
    print("=" * 50)


def display_final_results(score, total):
    """Show final score and performance"""
    print("\n" + "=" * 50)
    print("           QUIZ COMPLETE!")
    print("=" * 50)
    print(f"Your score: {score} out of {total}")

    percentage = calculate_percentage(score, total)
    print(f"Percentage: {percentage:.1f}%")

    performance = get_performance_level(percentage)
    print(f"Performance: {performance}")
    print("=" * 50)


def ask_play_again():
    """Ask user if they want to play again"""
    while True:
        answer = input("\nDo you want to play again? (yes/no): ").lower()
        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            print("Please enter 'yes' or 'no'")


def main():
    """Main program flow with loop"""
    while True:
        display_welcome()

        # Run the quiz
        final_score = run_quiz(QUESTIONS)

        # Show results
        display_final_results(final_score, len(QUESTIONS))

        # Ask to play again
        if not ask_play_again():
            print("\nThanks for playing! Goodbye!")
            break


# This is the entry point
if __name__ == "__main__":
    main()
