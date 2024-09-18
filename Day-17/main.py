from question_model import Question
from data import question_data

question_bank = []
for element in question_data:
    question_bank.append(Question(text = element['text'], answer = element['answer']))