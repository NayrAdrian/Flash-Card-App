from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)  # Center the image
canvas.grid(row=0, column=0, columnspan=2)

# Adding text inside the canvas
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"), fill="black")
canvas.create_text(400, 263, text="Sample", font=("Arial", 60, "bold"), fill="black")

# Buttons

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, activebackground=BACKGROUND_COLOR, borderwidth=0)
unknown_button.grid(row=1, column=0, pady=30)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, activebackground=BACKGROUND_COLOR, borderwidth=0)
known_button.grid(row=1, column=1, pady=30)

window.mainloop()

