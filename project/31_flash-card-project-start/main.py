from tkinter import *
import random
import pandas as pd

## Color pallet
BACKGROUND_COLOR = "#B1DDC6"
BLACK = "#000000"
WHITE = "#ffffff"
# YELLOW = "#f1c232"

to_learn = {}
current_card = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    ## Reading data
    original_data = pd.read_csv("data/1000_french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    ## This is pair the French and English in dictinoary
    to_learn = data.to_dict(orient="records")

def french_card():
    global current_card, flip_timer, data
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_side, image=card_front)
    canvas.itemconfig(card_title, text="French", fill=BLACK)
    canvas.itemconfig(card_word, text=current_card["French"], fill=BLACK)
    flip_timer = window.after(3000, func=english_card)

def english_card():
    canvas.itemconfig(card_side, image=card_back)
    canvas.itemconfig(card_title, text="English", fill=WHITE)
    canvas.itemconfig(card_word, text=current_card["English"], fill=WHITE)

def is_known():
    to_learn.remove(current_card)
    df = pd.DataFrame.from_dict(to_learn)
    df.to_csv("./data/words_to_learn.csv", index=False)
    french_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(5000, func=english_card)

## Canvas
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
## if you want the image in centre you have divide the canvas width and height in half for create Image
card_side = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", fill=BLACK, font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", fill=BLACK, font=("Ariel", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

## Buttons
wrong_image = PhotoImage(file="./images/wrong.png")
wrong = Button(image=wrong_image, highlightthickness=0, command=french_card)
wrong.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
right = Button(image=right_image, highlightthickness=0, command=is_known)
right.grid(row=1, column=1)

french_card()


window.mainloop()