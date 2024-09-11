import random

def ask_question(question, answer):
    user_answer = input(question + " ")
    return user_answer.lower() == answer.lower()

def main():
    questions = {
        #test commit! added a question about George Orwell :wq
        "Who is the author of 1984?": "george orwell",
        "What is the capital of France?": "paris",
        "What is 2 + 2?": "4",
        "What is the color of the sky?": "blue",
        "Who wrote 'To Kill a Mockingbird'?": "harper lee",
        "What is the largest planet in our solar system?": "jupiter"
    }

    score = 0
    question_list = list(questions.keys())
    random.shuffle(question_list)

    for question in question_list:
        if ask_question(question, questions[question]):
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    print(f"Your final score is {score} out of {len(questions)}")

if __name__ == "__main__":
    main()
