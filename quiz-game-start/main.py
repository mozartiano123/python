from question_model import Question
from data import *
from quiz_brain import QuizBrain
from ui import *

NUMBER_OF_QUESTIONS = 10
TYPE_OF_QUESTIONS = "boolean"

questionnaire = Questionnaire(NUMBER_OF_QUESTIONS, TYPE_OF_QUESTIONS)
question_bank = []

for line in questionnaire.question_data:
        question = line["question"]
        answer = line["correct_answer"]
        question_bank.append(Question(q_text=question,q_answer=answer))

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

# print(f"You've completed the quiz. \n Your final score is {quiz.current_score}/{quiz.question_number}.")