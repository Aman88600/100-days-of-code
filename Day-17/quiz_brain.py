from main import question_bank

score = 0
for i, question in enumerate(question_bank):
    user_answer = input(f"Q{i + 1}: {question.text}(True/False)?: ")
    if user_answer.capitalize() == (question.answer):
        print("You got it right.")
        print(f"The Correct answer was {question.answer}")
        score += 1
        print(f"Your current score is: {score}/{i+1}.")
    else:
        print("That's wrong.")
        print(f"The Correct answer was {question.answer}")
        print(f"Your current score is: {score}/{i+1}.")