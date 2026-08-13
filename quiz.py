#flashcard app
import json

#........FUNCTIONS........

def load_questions(filename):
    try:
        with open(filename, "r") as file:
            questions = json.load(file)
        return questions
    except FileNotFoundError:
        print("Error: the file", filename, "was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: the file", filename, "contains invalid JSON.")
        return []


def check_answer(user_answer, correct_answer):
    return user_answer.strip().lower() == correct_answer.strip().lower()


def ask_question(flashcard, question_number):
# Displays one question, gets the user's answer, and checks it
    print()
    print(f"Question: {question_number}. {flashcard["question"]}")
    user_answer = input("Your answer: ")
    is_correct = check_answer(user_answer, flashcard["answer"])
    return is_correct, user_answer


def run_quiz(questions):
    score = 0
    wrong_answers = []

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

    if not questions:
        print("No questions available. Exiting.")
        return
    score, wrong_answers = run_quiz(questions)

    # ----- RESULTS -----

    show_results(score, len(questions), wrong_answers)

main()