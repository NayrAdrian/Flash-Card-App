from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# Load the data
data = pd.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")


def next_card():
    # Select a random word from the list
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])


# Initialize the window
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Initialize the canvas
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

# Text elements on the canvas
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"), fill="black")

# Buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR,
                        borderwidth=0, command=next_card)
unknown_button.grid(row=1, column=0, pady=30)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR,
                      borderwidth=0, command=next_card)
known_button.grid(row=1, column=1, pady=30)

next_card()

window.mainloop()
