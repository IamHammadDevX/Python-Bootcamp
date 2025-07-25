from tkinter import *

window = Tk()
window.title("Graphical User Interface")
window.minsize(width=500, height=300)

# label
my_label = Label(text="First label goes here", font=("Arial", 24, "bold"))
my_label.config(text="Text changed")
# my_label.pack()
my_label.grid(column=0, row=0)

def btn_clicked():
    new_input = input.get()
    my_label.config(text=new_input)


btn = Button(text="Click me", command=btn_clicked)
# btn.pack()
btn.grid(column=1, row=1)

input = Entry()
# input.pack()
input.grid(column=2, row=2)


# Keep the window on screen
window.mainloop()