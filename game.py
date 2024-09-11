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
    }

    lastQuestion = {"Would you like to play again? yes or other": "yes"}
    
    # While loop added in case user wants to play again
    wantToPlay = True
    while wantToPlay :
    
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
        # Change added which asks user if they want to play again. Yes will replay quiz, anything else will stop
        if ask_question("Would you like to play again?", "yes") :
            wantToPlay = True
        else :
            wantToPlay = False

if __name__ == "__main__":
    main()