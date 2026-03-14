# 5) Create a basic quiz game that:
# •	1)Contains a list of 5–10 questions stored in a dictionary (or list of dictionaries [{}, {}] ).
# •	2)Ask the user each question and records their answers.
# •	3)At the end, displays:
# o	4)The user's score (e.g., 7/10)
# o	5)Correct answers for any questions they got wrong


basic_quiz = [
        {
        "question": "What is the name of the longest revir in the world?",
        "answer": "nile"
        },
        {
        "question": "Name the largest plant in our solar system",
        "answer": "jupyter"
        },
        {
        "question": "What is the name of capital city of Brazil?",
        "answer": "rio"
        },
        {
        "question": "Which continent is the Sahara Desert located in?",
        "answer": "africa"
        },

        {
        "question": "How many days are in a week?",
        "answer": "7"
        },
        {
        "question": "Which organ in the human body pumps blood?",
        "answer": "heart"
        },
]
score = 0
wrong_answer= []
for quiz in basic_quiz:
    question = quiz["question"]
    user_answer = input(question)
    correct_answer = quiz["answer"]
    if correct_answer == user_answer.lower():
        print("correct!")
        score = score + 1
    else:
        print("wrong!")
        wrong_answer.append(quiz)
print("Done!")
print(f"Your final score is {score}/6 !")
for incorrect in wrong_answer:
    print(incorrect["question"], ": answer is ",incorrect["answer"])


    
  
