from tkinter import *


def button_clicked():
    my_label.config(text=text_input.get())


window = Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# label
my_label = Label(text="I Am a Label", font=("Arial", 25, "bold"))
my_label.config(text="New text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="Kill me")
new_button.grid(column=2, row=0)

# Input
text_input = Entry(width=10)
text_input.grid(column=3, row=2)


window.mainloop()
