from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR)

frame = Frame(window, bg=BACKGROUND_COLOR)
frame.grid(row=0, column=0, padx=50, pady=50)

canvas = Canvas(frame, height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_img)  # Center the image
canvas.grid(row=0, column=0, columnspan=2)

# Adding text inside the canvas
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"), fill="black")
canvas.create_text(400, 263, text="Sample", font=("Arial", 60, "bold"), fill="black")

# Buttons
check_button = PhotoImage(file="images/right.png")
cross_button = PhotoImage(file="images/wrong.png")

wrong_button = Button(frame, image=cross_button, highlightthickness=0, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, borderwidth=0)
wrong_button.grid(row=1, column=0, pady=20)

right_button = Button(frame, image=check_button, highlightthickness=0, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, borderwidth=0)
right_button.grid(row=1, column=1, pady=20)

window.mainloop()
