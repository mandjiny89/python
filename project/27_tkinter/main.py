from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

def button_clicked():
    print("Button clicked")
    new_text = float(entry.get())
    km = round(new_text * float(1.60934))
    my_label_3.config(text=km)

## Entry
entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(column=1, row=0)

## Label 1
my_label = Label(text="Miles", font=("Arial", 23, "bold"))
my_label.grid(column=2, row=0)

## Label 2
my_label_2 = Label(text="is equal to", font=("Arial", 23, "bold"))
my_label_2.grid(column=0, row=1)

## Label 3
my_label_3 = Label(text="0", font=("Arial", 23, "bold"))
my_label_3.grid(column=1, row=1)

## Label 4
my_label_4 = Label(text="Km", font=("Arial", 23, "bold"))
my_label_4.grid(column=2, row=1)

## Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()