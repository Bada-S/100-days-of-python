from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    question_bank.append((q['text'], q['answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_question(question_bank):
    quiz.next_question()

print("You've completed the quiz")