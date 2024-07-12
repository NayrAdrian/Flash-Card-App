from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# Load the data
data = pd.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")

current_card = {}
flip_timer = None


def next_card():
    global current_card, flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)

    # Select a random word from the list
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(front_image, image=card_front_img)
    # Schedule the flip to occur after 3 seconds
    flip_timer = window.after(3000, flip_cards)


def flip_cards():
    canvas.itemconfig(front_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# Initialize the window
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Initialize the canvas
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
front_image = canvas.create_image(400, 263, image=card_front_img)
back_image = canvas.create_image(400, 263, image=card_back_img)
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

# Start with the first card
next_card()

# Start the Tkinter event loop
window.mainloop()
