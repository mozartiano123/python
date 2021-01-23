from tkinter import *
from pandas import *
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
new_word = []
csv_file=""
empty_dict = {}

def save_to_csv():
    df_words = DataFrame(all_words)
    df_words.to_csv("./data/words_to_learn.csv", index=False)

def got_right():
    all_words.remove(new_word)
    save_to_csv()
    get_new_word()

def got_wrong():
    get_new_word()

def get_new_word():
    #first thing is to stop the timer that flips the cards as soon as the button is hit.
    global flip_timer
    window.after_cancel(flip_timer)

    #get the word from dictionary
    global new_word
    new_word = choice(all_words)
    keys = list(new_word.keys())
    orig_lang = keys[0]
    new_guess_word = new_word[orig_lang]

    #changes the layout
    canvas.itemconfig(canvas_img, image=card_front_img)
    canvas.itemconfig(canvas_word, text=new_guess_word, fill="black")
    canvas.itemconfig(canvas_lang, text=orig_lang, fill="black")

    #creates a new timer so the card flips after 3 seconds without interaction.
    flip_timer = window.after(3000,flip_card, new_word)

def flip_card(word):
    #gets word from dictionary
    keys = list(word.keys())
    trans_lang = keys[1]
    translated_word = word[trans_lang]

    #changes the layout
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(canvas_lang, text=trans_lang, fill="white")
    canvas.itemconfig(canvas_word, text=translated_word, fill="white")


#Load csv as pandas df and convert the columns into 2 time series and then to a list, to navigate through.
try:
    with open("./data/words_to_learn.csv") as data_file:
        data_file.read()
except FileNotFoundError:
    csv_file = "./data/french_words.csv"
else:
    csv_file = "./data/words_to_learn.csv"
finally:
    print(csv_file)
    df_words = read_csv(csv_file)
    #all_words = [(word.French, word.English) for index, word in df_words.iterrows()]
    all_words = df_words.to_dict(orient="records")


window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,flip_card, empty_dict)


#Images
card_back_img = PhotoImage(file="./images/card_back.png")
card_front_img = PhotoImage(file="./images/card_front.png")
right_img = PhotoImage(file="./images/right.png")
wrong_img =  PhotoImage(file="./images/wrong.png")

#Canvas
canvas = Canvas(width=800,height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_img = canvas.create_image(400,263,image=card_front_img)
canvas_lang = canvas.create_text(400,150,text="Title", font=("Ariel",40,"italic"))
canvas_word = canvas.create_text(400,263,text="word", font=("Ariel",60,"bold"))
canvas.grid(column=0,row=0, columnspan=2)

#Buttons
right_bt = Button(image=right_img, command=got_right, highlightthickness=0)
# right_bt = Button(image=right_img, command=get_new_word, highlightthickness=0)
right_bt.grid(column=0,row=1)

wrong_bt = Button(image=wrong_img, command=got_wrong, highlightthickness=0)
# wrong_bt = Button(image=wrong_img, command=get_new_word, highlightthickness=0)
wrong_bt.grid(column=1,row=1)

get_new_word()

window.mainloop()