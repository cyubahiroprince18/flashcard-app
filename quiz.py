#flashcard app
import json

#........FUNCTIONS........

def load_questions(filename):

    """
    Opens a JSON file and loads its contents into a Python list of dictionaries.
    Handles the case where the file is missing or contains invalid JSON,
    so the program doesn't crash - it returns an empty list instead.
    """
    try:
        with open(filename, "r") as file:
            questions = json.load(file)
        return questions
    except FileNotFoundError:
        print("Error: the file", filename, "was not found.")
        return []  # Return an empty list (not None) so the rest of the program
                   # can safely treat this the same way as "a list with 0 items"
    except json.JSONDecodeError:
        # Happens if the file exists but its contents aren't valid JSON
        print("Error: the file", filename, "contains invalid JSON.")
        return []


def check_answer(user_answer, correct_answer):
    """
    Compares the user's answer to the correct answer.
    .strip() removes accidental leading/trailing spaces.
    .lower() makes the comparison case-insensitive (e.g. "kigali" == "Kigali").
    """
    return user_answer.strip().lower() == correct_answer.strip().lower()


def ask_question(flashcard, question_number):
    """
    Displays one flashcard's question, gets the user's typed answer,
    and checks whether it's correct.
    Returns both the result (True/False) AND what the user typed,
    since the caller (run_quiz) needs both pieces of information.
    """
    print()
    print(f"Question: {question_number}. {flashcard["question"]}")
    user_answer = input("Your answer: ")
    is_correct = check_answer(user_answer, flashcard["answer"])
    return is_correct, user_answer


def run_quiz(questions):
    """
    Runs the full quiz: loops through every flashcard, asks each one,
    and keeps track of the score and any wrong answers along the way.
    """
    score = 0
    wrong_answers = []

    # enumerate() gives us both the position (index) and the item (flashcard)
    # start=1 makes numbering human-friendly ("Question 1" instead of "Question 0")

    for index, flashcard in enumerate(questions, start=1):

        is_correct, user_answer = ask_question(flashcard, index)

        if is_correct:
            print("✓ Correct!")
            score += 1
        else:
            print("✗ Wrong!")
            print("Correct answer:", flashcard["answer"])
            print("Your answer:", user_answer)
            wrong_answers.append({
                "question": flashcard["question"],
                "your_answer": user_answer,
                "correct_answer": flashcard["answer"]
            })

    return score, wrong_answers

def show_results(score, total_questions, wrong_answers):
    """
    Prints the final results screen: accuracy percentage,
    plus a review of every question answered incorrectly.
    """
    print()
    print("================================")
    print("          QUIZ RESULTS")
    print("================================")

    if total_questions == 0:
        print("No questions were asked.")
    else:
        accuracy = (score / total_questions) * 100
        print(f"Total questions: {total_questions}")
        print(f"Correct answers: {score}")
        print(f"Wrong answers: {len(wrong_answers)}")
        print(f"Accuracy: {accuracy} %")

    if wrong_answers:
        print()
        print("Wrong Answers:")
        for i, mistake in enumerate(wrong_answers, start=1):
            print(f"{i}. {mistake["question"]}")
            print(f" Your answer: {mistake["your_answer"]}")
            print(f" Correct answer: {mistake["correct_answer"]}")

    print("================================")


# ----- DATA -----
def main():

    questions = load_questions("questions.json")

    # If loading failed (missing file / bad JSON), questions will be [] here.
    # We stop early instead of trying to run a quiz with zero questions.

    if not questions:
        print("No questions available. Exiting.")
        return
    score, wrong_answers = run_quiz(questions)

    # ----- RESULTS -----

    show_results(score, len(questions), wrong_answers)

main()