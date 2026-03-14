# 5) Create a basic quiz game that:
# •	1)Contains a list of 5–10 questions stored in a dictionary (or list of dictionaries [{}, {}] ).
# •	2)Ask the user each question and records their answers.
# •	3)At the end, displays:
# o	4)The user's score (e.g., 7/10)
# o	5)Correct answers for any questions they got wrong


basic_quiz = [
    {"question": "What is the name of the longest river in the world?", "answer": "nile"},
    {"question": "Name the largest planet in our solar system:", "answer": "jupiter"},
    {"question": "What is the name of the capital city of Brazil?", "answer": "brasilia"},
    {"question": "Which continent is the Sahara Desert located in?", "answer": "africa"},
    {"question": "How many days are in a week?", "answer": "7"},
    {"question": "Which organ in the human body pumps blood?", "answer": "heart"},
]

score = 0
wrong_answers = []

for quiz in basic_quiz:
    user_answer = input(quiz["question"] + " ").strip().lower()
    
    if user_answer == quiz["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        wrong_answers.append(quiz)

print("\n--- Quiz Finished ---")

print(f"Your final score is {score}/{len(basic_quiz)}!")

if wrong_answers:
    print("\nHere are the correct answers for the ones you missed:")
    for item in wrong_answers:
        print(f"Question: {item['question']}")
        print(f"Correct Answer: {item['answer']}\n")
