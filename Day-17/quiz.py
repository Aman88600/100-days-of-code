from questions import get_question

class Quiz:
    def __init__(self, score, questions_asked):
        self.score = score
        self.questions_asked = questions_asked
        
    def ask_question(self):
        question = get_question()
        if question:
            answer = (input(f"{question["question"]}. (True/False)(off to quit)").lower())
            if answer == 'off':
                exit(0)
            print(f"Correct answe was : {question["answer"]}")
            if answer.lower() == (str(question["answer"])).lower():
                self.score += 1
            self.questions_asked += 1
            print(f"Your Current Score is {self.score}/{self.questions_asked}")

quiz = Quiz(0, 0)
while True:
    quiz.ask_question()