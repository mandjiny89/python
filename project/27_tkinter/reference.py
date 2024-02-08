from tkinter import *

window = Tk()
window.title("My First GUI Programming")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

def button_clicked():
    print("Button clicked")
    new_text = text_input.get()
    # my_label.config(text=text.get())
    my_label.config(text=new_text)

## Label
my_label = Label(text="I am a Label", font=("Arial", 23, "bold"))
my_label.grid(column=0, row=0)

## Entry
text_input = Entry(width=10)
text_input.grid(column=3, row=3)

## Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

## Button 2
button_2= Button(text="New Button")
button_2.grid(column=2, row=0)

window.mainloop()