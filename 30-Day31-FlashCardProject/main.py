from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
random_word = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
    


def next_card():
    global random_word, flip_timer
    random_word = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=random_word["French"], fill="black")
    canvas.itemconfig(card_bgc, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=random_word["English"], fill="white")
    canvas.itemconfig(card_bgc, image=card_back_img)

def is_known():
    to_learn.remove(random_word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_bgc = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


# buttons
cross_img = PhotoImage(file="images/wrong.png")
unknow_btn = Button(image=cross_img, highlightthickness=0, command=next_card)
unknow_btn.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
check_btn = Button(image=check_img, highlightthickness=0, command=is_known)
check_btn.grid(row=1, column=1)

next_card()

window.mainloop()