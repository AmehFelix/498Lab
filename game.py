import random

def ask_question(question, answer):
    user_answer = input(question + " ")
    return user_answer.lower() == answer.lower()

def main():
    # Jason Soares - Change: Reworked questions to have point values based on perceived difficulty
    questions = {
        "What is the capital of France?": ("paris", 1),  
        "What is 2 + 2?": ("4", 1),  
        "What is the color of the sky?": ("blue", 1),  
        "Who wrote 'To Kill a Mockingbird'?": ("harper lee", 2),  
        "What is the largest planet in our solar system?": ("jupiter", 3)  
    }

    score = 0
    question_list = list(questions.keys())
    random.shuffle(question_list)

    for question in question_list:
        answer, points = questions[question]
        if ask_question(question, answer):
            print("Correct!")
            # Jason Soares - Change: Add points instead of static +1
            score += points
        else:
            print("Wrong!")

    print(f"Your final score is {score} out of {sum(points for _, points in questions.values())}")

if __name__ == "__main__":
    main()
