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
        "What is the largest planet in our solar system?": "jupiter",
        #Added a new question
        "What planet are we on?": "earth"
    }

    score = 0
    question_list = list(questions.keys())
    random.shuffle(question_list)

    for question in question_list:
        if ask_question(question, questions[question]):
            #Changed correct answer print statement
            print("Correct answer!!")
            score += 1
        else:
            #Changed wrong answer print statement
            print("Wrong answer!!")

    print(f"Your final score is {score} out of {len(questions)}")

if __name__ == "__main__":
    main()