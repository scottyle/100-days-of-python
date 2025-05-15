from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#Empty list to initialize question bank 
question_bank = [] 

#Loop over question_data 
for i in question_data: 
    questions = Question(text = i["text"],answer = i["answer"])
    question_bank.append(questions)


quiz = QuizBrain(question_bank)

while not quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(quiz.questions_list)}")