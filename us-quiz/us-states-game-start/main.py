from turtle import Turtle, Screen
import pandas
from map import Map
from scoreboard import ScoreBoard

screen = Screen()
turtle = Turtle()
scoreboard = ScoreBoard()
screen.title("U.S. States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# screen.onscreenclick(get_mouse_click_coor)
# screen.mainloop()

def compare_answer(user_answer):
    pass

df = pandas.read_csv("50_states.csv")
all_states = df.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    screen.update()
    answer_state = screen.textinput(title = "Guess the State",
                                    prompt = "What's the next state's name?").title()
    if answer_state == "Exit":
        for state in guessed_state:
            all_states.remove(state)
        new_df = pandas.DataFrame(all_states)
        new_df.to_csv("Missing.csv")
        break

    df2 = df.loc[df.state == answer_state]
    if not df2.empty:
        if answer_state not in guessed_state:
            guessed_state.append(answer_state)
            x_cor = df2["x"]
            y_cor = df2["y"]
            print(df2)
            map = Map(int(x_cor), int(y_cor), answer_state)
            scoreboard.increase_score()

screen.exitonclick()
