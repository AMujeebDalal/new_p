from tkinter import *


def calculate():
    miles = float(miles_input.get())
    km = round(1 / 1.6093 * miles, 3)
    km_result.config(text=km)

window = Tk()
window.title("Miles-Km Converter")
window.minsize(width=200, height=150)
window.config(padx=20, pady=30)

is_equal = Label(text="is equal to", font=("Arial", 10, "bold"))
is_equal.grid(column=0, row=2)
is_equal.config(padx=20, pady=20)

# Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 10, "bold"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=20, pady=20)


km_result = Label(text="0", width=10, font=("Arial", 10, "bold"))
km_result.grid(column=1, row=2)
km_result.config(padx=20, pady=20)

km_label = Label(text="Km", font=("Arial", 10, "bold"))
km_label.grid(column=2, row=2)
km_label.config(padx=20, pady=20)

# Button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=4)

window.mainloop()
