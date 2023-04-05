from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question_text = item['question']
    question_answer = item['correct_answer']
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)
print(question_bank[0].question)


quiz = QuizBrain(question_bank)

while quiz.still_have_questions():
    quiz.next_question()
else:
    print(f"You've completed the quiz \nYour final score was: {quiz.score}/{quiz.question_number}")




