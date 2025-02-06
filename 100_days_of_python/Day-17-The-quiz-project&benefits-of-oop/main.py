from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question = Question(text=item['question'],answer=item['correct_answer'])
    question_bank.append(question)

quiz = QuizBrain(question_bank)


#If quiz still has questions remaining: 
while quiz.still_has_questions():
    quiz.next_question()
print("You completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")