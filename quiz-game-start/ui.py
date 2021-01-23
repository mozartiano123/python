from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR="#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        #Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        #Images
        self.true_img = PhotoImage(file="./images/true.png")
        self.false_img = PhotoImage(file="./images/false.png")

        #Canvas
        self.canvas = Canvas(
            width=300,
            height=250,
            bg="white",
            highlightthickness=0
            )
        self.c_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question Text",
            font=("Arial",14,"italic")
            )
        self.canvas.grid(column=0,row=1, columnspan=2, pady=50)

        #Buttons
        self.true_bt = Button(
            image=self.true_img,
            bg=THEME_COLOR,
            highlightthickness=0,
            command = self.respond_true
            )
        self.true_bt.grid(column=0,row=2, pady=20, padx=20)
        self.false_bt = Button(
            image = self.false_img,
            bg = THEME_COLOR,
            highlightthickness = 0,
            command = self.respond_false
            )
        self.false_bt.grid(column=1,row=2, padx=20)

        #Label
        self.score_lbl = Label(
            text=f"Score: {self.quiz.current_score}",
            fg="white",bg=THEME_COLOR,
            font=("Arial",10)
            )
        self.score_lbl.grid(column=1,row=0, padx=20)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.c_text,text=q_text)
        else:
            q_text = f"GAME OVER. \n" \
                     f"You scored {self.quiz.current_score} " \
                     f"out of {len(self.quiz.question_list)} "
            self.canvas.itemconfig(self.c_text,text=q_text)
            self.true_bt.config(state="disabled")
            self.false_bt.config(state="disabled")

    def respond_true(self):
        q_number = self.quiz.question_number-1
        q_answer = self.quiz.question_list[q_number].answer
        is_right = self.quiz.check_answer("True", q_answer)
        user_score = self.quiz.current_score
        self.score_lbl.config(text=f"Score: {user_score}")
        self.give_feedback(is_right)

    def respond_false(self):
        q_number = self.quiz.question_number-1
        q_answer = self.quiz.question_list[q_number].answer
        is_right = self.quiz.check_answer("False", q_answer)
        user_score = self.quiz.current_score
        self.score_lbl.config(text=f"Score: {user_score}")
        self.give_feedback(is_right)


    def give_feedback(self, result):
        if result:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)







