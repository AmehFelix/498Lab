import random

def ask_question(question, answer):
    user_answer = input(question + " ")
    return user_answer.lower() == answer.lower()

def main():
    questions = {
        "What is the capital of France?": "paris",
        "What is 2 + 2?": "4",
        "What is the color of the sky?": "blue",
        "Who wrote 'To Kill a Mockingbird'?": "harper lee",
        "What is the largest planet in our solar system?": "jupiter"
    }

    score = 0
    question_list = list(questions.keys())
    random.shuffle(question_list)

    # Jason Soares - Change: 5 points for right answer, subtract 2 points per wrong answer
    for question in question_list:
        if ask_question(question, questions[question]):
            print("Correct!")
            score += 5
        else:
            print("Wrong!")
            score -= 2

    print(f"Your final score is {score} out of {len(questions)}")

if __name__ == "__main__":
    main()