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
	#added additional question below
	"In what year was this program last updated?": "2024"
    }

    score = 0
    question_list = list(questions.keys())
    #give the user the option of whether to shuffle questions
    if input("Shuffle questions (default: no)? ") == "yes":
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
