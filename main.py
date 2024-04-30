from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
selected_word = {}

# read csv
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/English_word.csv")
dict_data = data.to_dict(orient="records")
key_list = list(dict_data[0].keys())


# ---------------------------- DISPLAY WORD ------------------------------- #
def display_word():
    global timer, selected_word
    window.after_cancel(timer)
    selected_word = random.choice(dict_data)
    key = key_list[0]
    word = selected_word[key]
    canvas.itemconfig(canvas_img, image=card_front_img)
    canvas.itemconfig(text_lang, text=key, fill="black")
    canvas.itemconfig(text_word, text=word, fill="black")
    timer = window.after(3000, flip_card)


def flip_card():
    key = key_list[1]
    word = selected_word[key]
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(text_lang, text=key, fill="white")
    canvas.itemconfig(text_word, text=word, fill="white")


def learned_card():
    dict_data.remove(selected_word)
    data = pandas.DataFrame(dict_data)
    data.to_csv("./data/words_to_learn.csv",index=False)
    display_word()


# ---------------------------- UI SETUP ------------------------------- #
# Display window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# setting image
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front_img)

text_lang = canvas.create_text(400, 150, text="title", fill="black", font=("Ariel", 40, "italic"))
text_word = canvas.create_text(400, 263, text="text", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# buttons
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, relief="flat", bg=BACKGROUND_COLOR, command=display_word)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, relief="flat", bg=BACKGROUND_COLOR, command=learned_card)
right_button.grid(column=1, row=1)

timer = window.after(3000, flip_card)
display_word()

window.mainloop()
