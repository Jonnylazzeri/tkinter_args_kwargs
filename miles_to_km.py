from tkinter import *


def button_clicked():
    miles = int(text_input.get())
    measure_label.config(text=round(miles * 1.60934, 2))


window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=200, height=100)
window.config()

text_input = Entry(width=10)
text_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

measure_label = Label(text=0)
measure_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calc_btn = Button(text="Calculate", command=button_clicked)
calc_btn.grid(column=1,row=2)


window.mainloop()
