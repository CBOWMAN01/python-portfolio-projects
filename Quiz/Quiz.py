import json

# Load quiz questions from JSON
quiz_file = "quiz_questions.json"

# Sample questions if JSON doesn't exist
default_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. Berlin", "C. London", "D. Rome"],
        "answer": "A"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["A. 10", "B. 12", "C. 13", "D. 14"],
        "answer": "B"
    },
    {
        "question": "Which language is this program written in?",
        "options": ["A. Java", "B. C++", "C. Python", "D. Ruby"],
        "answer": "C"
    }
]

# Save default questions if file doesn't exist
try:
    with open(quiz_file, "r") as f:
        questions = json.load(f)
except FileNotFoundError:
    questions = default_questions
    with open(quiz_file, "w") as f:
        json.dump(questions, f, indent=4)

score = 0

print("=== Welcome to the Python Quiz Game! ===\n")

for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)
    answer = input("Enter your answer (A/B/C/D): ").upper()
    if answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! Correct answer: {q['answer']}\n")

print(f"Quiz complete! Your score: {score}/{len(questions)}")
